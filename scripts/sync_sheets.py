import os
import glob
import re
from datetime import date
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

# ── Auth ─────────────────────────────────────────────────────────────────────
creds = Credentials(
    token=None,
    refresh_token=os.getenv("YOUTUBE_REFRESH_TOKEN"),
    token_uri="https://oauth2.googleapis.com/token",
    client_id=os.getenv("YOUTUBE_CLIENT_ID"),
    client_secret=os.getenv("YOUTUBE_CLIENT_SECRET"),
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/youtube.readonly",
        "https://www.googleapis.com/auth/yt-analytics.readonly"
    ]
)
creds.refresh(Request())

youtube   = build("youtube",           "v3", credentials=creds)
sheets    = build("sheets",            "v4", credentials=creds)
analytics = build("youtubeAnalytics",  "v2", credentials=creds)
SHEETS_ID = os.getenv("GOOGLE_SHEETS_ID")
TODAY     = str(date.today())

COLOR_MAP = {
    "Trend Analizi":  "#414ecf",
    "Tutorial":       "#f0eee9",
    "Kariyer / POV":  "#d2c7ff",
    "Girişim / Para": "#f4b5de",
}

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("AXONODEAI — Sheets Sync Başlıyor")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# ── Helpers ───────────────────────────────────────────────────────────────────
def get_existing_keys(tab):
    resp = sheets.spreadsheets().values().get(
        spreadsheetId=SHEETS_ID,
        range=f"{tab}!A:A"
    ).execute()
    return [r[0] if r else "" for r in resp.get("values", [])]


def upsert_row(tab, end_col, row_data, existing_keys):
    key = row_data[0]
    if key in existing_keys:
        idx = existing_keys.index(key) + 1
        sheets.spreadsheets().values().update(
            spreadsheetId=SHEETS_ID,
            range=f"{tab}!A{idx}:{end_col}{idx}",
            valueInputOption="USER_ENTERED",
            body={"values": [row_data]}
        ).execute()
        return "güncellendi"
    else:
        sheets.spreadsheets().values().append(
            spreadsheetId=SHEETS_ID,
            range=f"{tab}!A2",
            valueInputOption="USER_ENTERED",
            body={"values": [row_data]}
        ).execute()
        return "eklendi"


def ensure_tab_with_header(tab_name, headers):
    """Create tab if missing and write header row. Returns True if tab already existed."""
    spreadsheet = sheets.spreadsheets().get(spreadsheetId=SHEETS_ID).execute()
    existing = [s["properties"]["title"] for s in spreadsheet["sheets"]]
    just_created = False
    if tab_name not in existing:
        sheets.spreadsheets().batchUpdate(
            spreadsheetId=SHEETS_ID,
            body={"requests": [{"addSheet": {"properties": {"title": tab_name}}}]}
        ).execute()
        just_created = True
        print(f"  ✓ Tab oluşturuldu: {tab_name}")
    # Always write/refresh header
    col_end = chr(ord("A") + len(headers) - 1)
    sheets.spreadsheets().values().update(
        spreadsheetId=SHEETS_ID,
        range=f"{tab_name}!A1:{col_end}1",
        valueInputOption="USER_ENTERED",
        body={"values": [headers]}
    ).execute()
    return not just_created


# ── Parse content-calendar.md ─────────────────────────────────────────────────
def parse_content_calendar():
    rows = []
    with open("knowledge/content-calendar.md", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line.startswith("| VID-"):
                continue
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) < 5:
                continue
            tip  = parts[1]
            seri = parts[5] if len(parts) > 5 else ""
            rows.append({
                "vid_key": parts[0],
                "tip":     tip,
                "baslik":  parts[2],
                "tarih":   parts[3],
                "durum":   parts[4],
                "seri":    seri if seri not in ("—", "-", "") else "",
                "renk":    COLOR_MAP.get(tip, ""),
            })
    return rows


# ── 1. Kanal verisi ───────────────────────────────────────────────────────────
channel = youtube.channels().list(
    part="snippet,statistics",
    id=os.getenv("YOUTUBE_CHANNEL_ID")
).execute()
ch = channel["items"][0]
print(f"✓ Kanal: {ch['snippet']['title']}")
print(f"  Abone: {ch['statistics'].get('subscriberCount')} | "
      f"İzlenme: {ch['statistics'].get('viewCount')}")

all_vids = parse_content_calendar()

# ── 2. İçerik Takvimi — tüm VID'ler (URL'siz dahil) ─────────────────────────
print("\n— İçerik Takvimi —")
ensure_tab_with_header("Icerik Takvimi", [
    "VID Key", "Video Tipi", "Renk Kodu", "Başlık",
    "Yayın Tarihi", "Durum", "Analytics Link",
    "IG Post", "IG Haftası", "Notlar"
])
existing_takvim = get_existing_keys("Icerik Takvimi")

for v in all_vids:
    row = [
        v["vid_key"], v["tip"], v["renk"], v["baslik"],
        v["tarih"], v["durum"],
        "", "", "",    # Analytics Link, IG Post, IG Haftası
        v["seri"],     # Notlar — seri bilgisi
    ]
    result = upsert_row("Icerik Takvimi", "J", row, existing_takvim)
    if v["vid_key"] not in existing_takvim:
        existing_takvim.append(v["vid_key"])
    print(f"  {v['vid_key']} ({v['durum']}) — {result}")

print(f"✓ İçerik Takvimi: {len(all_vids)} video")

# ── 3. Öneriler — tüm planlı ve önerilen videolar ────────────────────────────
print("\n— Öneriler —")
ensure_tab_with_header("Oneriler", [
    "VID Key", "Video Tipi", "Başlık",
    "Önerilen Tarih", "Durum", "Seri",
    "Thumbnail Rengi", "Notlar"
])

# Full refresh — her sync'te tüm öneri listesi yeniden yazılır
sheets.spreadsheets().values().clear(
    spreadsheetId=SHEETS_ID,
    range="Oneriler!A2:H1000"
).execute()

oneriler_rows = [
    [v["vid_key"], v["tip"], v["baslik"], v["tarih"],
     v["durum"], v["seri"], v["renk"], ""]
    for v in all_vids
]
sheets.spreadsheets().values().append(
    spreadsheetId=SHEETS_ID,
    range="Oneriler!A2",
    valueInputOption="USER_ENTERED",
    body={"values": oneriler_rows}
).execute()
print(f"✓ Öneriler: {len(oneriler_rows)} video")

# ── 4. Viral Patterns — viral-mechanism-library.md içeriği ───────────────────
print("\n— Viral Patterns —")
ensure_tab_with_header("Viral Patterns", [
    "VPT Key", "Video URL", "Kanal", "Başlık",
    "İzlenme", "Yayın Tarihi", "Hook Tipi",
    "Başlık Formülü", "Thumbnail Özelliği",
    "En Güçlü Özellik", "Kullanılabilir mi", "Analiz Tarihi"
])
existing_vpt = get_existing_keys("Viral Patterns")

vpt_rows = [
    ["VPT-001",
     "https://www.youtube.com/watch?v=VxZ5nd0-lug",
     "Mert Durmazer | Digital Academy",
     "Yeni Yapay Zeka Meslekleri: 120K€, Kod Yok, Diploma Yok (2026 Patlayacak!)",
     "50.000+", "2025-12-22", "Veri / Şok", "Formül 3+1 Hibrit",
     "Yüz var, yüksek kontrast, para rakamı",
     "Başlıkta somut para rakamı CTR artırıyor", "Evet", "2026-05-09"],
    ["VPT-002",
     "https://www.youtube.com/watch?v=sRG8Pa5IQTo",
     "Erhan Meydan",
     "2025'te Hayatımızı Değiştirecek AI Agents Nedir?",
     "50.000+", "2025-01-18", "İddia", "Formül 1",
     "Yüz var, yüksek kontrast",
     "Yıl + etki iddiası kombinasyonu", "Kısmen", "2026-05-09"],
    ["VPT-003",
     "https://www.youtube.com/watch?v=QNp0YCZDjc4",
     "Türkçe AI kariyer kanalı",
     "IT ve AI Sektöründe Yükselen ve Yok Olan Meslekler",
     "50.000+", "2025-10-01", "Kontrast", "Formül 1",
     "Yüz var, kontrast çifti",
     "Kontrast çifti tekniği (Yükselen/Yok Olan)", "Evet", "2026-05-09"],
    ["VPT-002b",
     "",
     "İngilizce LangChain / CrewAI tutorial kanalları",
     "Tutorial — Vadi Hook örnekleri (LangChain, CrewAI vb.)",
     "100.000+", "2024-2025", "Vadi Hook", "Tutorial Formülü",
     "Ekran kaydı + yüz",
     "İlk 30 sn somut çıktı vaadi retention'ı %45-55'e taşıyor",
     "Evet", "2026-05-09"],
    ["VPT-005",
     "",
     "Alphamatch AI, DevTo, Analytics Vidhya (web araştırması)",
     "Canlı istatistik + sektör baskısı pattern",
     "—", "2026", "Veri + FOMO", "Formül Hibrit",
     "—",
     "Spesifik sektör istatistiği güvenilirlik + FOMO üretiyor",
     "Evet", "2026-05-10"],
    ["VPT-006",
     "",
     "VID-001 retention verisi + İngilizce tutorial kanallar",
     "Vadi Hook + Retention bağlantısı (VID-001 negatif kanıt)",
     "—", "2026", "Vadi Hook", "Tutorial / Trend Formülü",
     "—",
     "Vadi hook olmadan Türkçe teknik video retention %20'de kalıyor",
     "Evet", "2026-05-10"],
]

for row in vpt_rows:
    result = upsert_row("Viral Patterns", "L", row, existing_vpt)
    if row[0] not in existing_vpt:
        existing_vpt.append(row[0])
    print(f"  {row[0]} — {result}")

print(f"✓ Viral Patterns: {len(vpt_rows)} pattern")

# ── 5. YouTube Analytics — yayında videolar ───────────────────────────────────
print("\n— YouTube Analytics —")

videos_response = youtube.search().list(
    part="snippet",
    channelId=os.getenv("YOUTUBE_CHANNEL_ID"),
    type="video",
    order="date",
    maxResults=50
).execute()
video_ids = [item["id"]["videoId"] for item in videos_response.get("items", [])]

if not video_ids:
    print("  ✗ Yayında video bulunamadı")
else:
    video_details = youtube.videos().list(
        part="snippet,statistics,contentDetails",
        id=",".join(video_ids)
    ).execute()

    def get_analytics(video_id, start_date):
        try:
            r1 = analytics.reports().query(
                ids="channel==MINE",
                startDate=start_date,
                endDate="2026-12-31",
                metrics="views,estimatedMinutesWatched,averageViewPercentage,subscribersGained",
                dimensions="video",
                filters=f"video=={video_id}"
            ).execute()
            r2 = analytics.reports().query(
                ids="channel==MINE",
                startDate=start_date,
                endDate="2026-12-31",
                metrics="cardImpressions,cardClickRate",
                dimensions="video",
                filters=f"video=={video_id}"
            ).execute()
            r3 = analytics.reports().query(
                ids="channel==MINE",
                startDate=start_date,
                endDate="2026-12-31",
                metrics="views",
                dimensions="insightTrafficSourceType",
                filters=f"video=={video_id}",
                sort="-views"
            ).execute()
            result = {"views": 0, "watch_minutes": 0, "retention": 0, "subs": 0,
                      "impressions": 0, "ctr": 0, "oneri": 0, "arama": 0}
            if r1.get("rows"):
                r = r1["rows"][0]
                result.update({"views": r[1], "watch_minutes": round(r[2], 1),
                               "retention": round(r[3], 1), "subs": r[4]})
            if r2.get("rows"):
                r = r2["rows"][0]
                result.update({"impressions": r[1], "ctr": round(float(r[2]) * 100, 2)})
            for r in r3.get("rows", []):
                if r[0] == "SUGGESTED_VIDEO": result["oneri"] = r[1]
                elif r[0] == "YT_SEARCH":     result["arama"] = r[1]
            return result
        except Exception as e:
            print(f"  Analytics hatası ({video_id}): {e}")
            return None

    # VID key map — my-videos + pipeline klasörlerinden
    vid_key_map = {}
    for filepath in (glob.glob("knowledge/my-videos/VID-*.md")
                     + glob.glob("knowledge/pipeline/VID-*.md")):
        vid_key = os.path.basename(filepath).replace(".md", "")
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        match = re.search(r"\*\*video_id:\*\*\s*([A-Za-z0-9_-]{11})", content)
        if match:
            vid_key_map[match.group(1)] = vid_key
    print(f"  VID map: {vid_key_map}")

    existing_analytics = get_existing_keys("YouTube Analytics")

    for item in video_details.get("items", []):
        vid_id  = item["id"]
        stats   = item["statistics"]
        snippet = item["snippet"]
        vid_key = vid_key_map.get(vid_id, f"VID-{vid_id[:6]}")
        yayin   = snippet["publishedAt"][:10]
        print(f"\n  {vid_key} — {snippet['title'][:50]}")

        izlenme = stats.get("viewCount",   "0")
        begeni  = stats.get("likeCount",   "0")
        yorum   = stats.get("commentCount","0")
        an = get_analytics(vid_id, yayin)

        if an:
            retention = f"{an['retention']}%" if an["retention"] else "Birikme devam ediyor"
            ctr       = f"{an['ctr']}%"       if an["ctr"]       else "Birikme devam ediyor"
            watch     = an["watch_minutes"]
            subs      = an["subs"]
            oneri_pct = round(an["oneri"] / max(an["views"], 1) * 100, 1) if an["views"] else 0
            arama_pct = round(an["arama"] / max(an["views"], 1) * 100, 1) if an["views"] else 0
        else:
            retention = ctr = "Birikme devam ediyor"
            watch = subs = oneri_pct = arama_pct = ""

        vid_type = next((v["tip"] for v in all_vids if v["vid_key"] == vid_key), "")

        row_data = [
            vid_key, "",
            snippet["title"], yayin, vid_type,
            izlenme, "", "",
            retention, ctr, watch,
            f"{oneri_pct}%" if oneri_pct else "",
            f"{arama_pct}%" if arama_pct else "",
            begeni, yorum, subs,
            TODAY
        ]
        result = upsert_row("YouTube Analytics", "Q", row_data, existing_analytics)
        if vid_key not in existing_analytics:
            existing_analytics.append(vid_key)
        print(f"  ✓ {result}")
        print(f"    İzlenme: {izlenme} | Beğeni: {begeni} | Yorum: {yorum}")
        print(f"    Retention: {retention} | CTR: {ctr}")

print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("✓ Sheets sync tamamlandı")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
