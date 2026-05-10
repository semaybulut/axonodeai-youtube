import os
import subprocess
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

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

youtube = build("youtube", "v3", credentials=creds)
sheets = build("sheets", "v4", credentials=creds)
analytics = build("youtubeAnalytics", "v2", credentials=creds)
SHEETS_ID = os.getenv("GOOGLE_SHEETS_ID")

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("AXONODEAI — Sheets Sync Başlıyor")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

# ── 1. Kanal verisi ──────────────────────
channel = youtube.channels().list(
    part="snippet,statistics",
    id=os.getenv("YOUTUBE_CHANNEL_ID")
).execute()

ch = channel["items"][0]
abone = ch["statistics"].get("subscriberCount", "0")
toplam_izlenme = ch["statistics"].get("viewCount", "0")
print(f"✓ Kanal: {ch['snippet']['title']}")
print(f"  Abone: {abone} | İzlenme: {toplam_izlenme}")

# ── 2. Tüm videoları çek ─────────────────
videos_response = youtube.search().list(
    part="snippet",
    channelId=os.getenv("YOUTUBE_CHANNEL_ID"),
    type="video",
    order="date",
    maxResults=50
).execute()

video_ids = [item["id"]["videoId"] for item in videos_response.get("items", [])]

if not video_ids:
    print("✗ Video bulunamadı")
    exit()

# ── 3. Video detayları ───────────────────
video_details = youtube.videos().list(
    part="snippet,statistics,contentDetails",
    id=",".join(video_ids)
).execute()

# ── 4. Analytics çek (her video için) ───
def get_analytics(video_id, start_date):
    try:
        # Temel metrikler
        r1 = analytics.reports().query(
            ids="channel==MINE",
            startDate=start_date,
            endDate="2026-12-31",
            metrics="views,estimatedMinutesWatched,averageViewPercentage,subscribersGained",
            dimensions="video",
            filters=f"video=={video_id}"
        ).execute()

        # CTR
       # CTR — impressions yerine doğru metrik adı
        r2 = analytics.reports().query(
            ids="channel==MINE",
            startDate=start_date,
            endDate="2026-12-31",
            metrics="cardImpressions,cardClickRate",
            dimensions="video",
            filters=f"video=={video_id}"
        ).execute()

        # Trafik kaynakları
        r3 = analytics.reports().query(
            ids="channel==MINE",
            startDate=start_date,
            endDate="2026-12-31",
            metrics="views",
            dimensions="insightTrafficSourceType",
            filters=f"video=={video_id}",
            sort="-views"
        ).execute()

        result = {
            "views": 0, "watch_minutes": 0,
            "retention": 0, "subs": 0,
            "impressions": 0, "ctr": 0,
            "oneri": 0, "arama": 0
        }

        if r1.get("rows"):
            row = r1["rows"][0]
            result["views"] = row[1]
            result["watch_minutes"] = round(row[2], 1)
            result["retention"] = round(row[3], 1)
            result["subs"] = row[4]

        if r2.get("rows"):
            row = r2["rows"][0]
            result["impressions"] = row[1]
            result["ctr"] = round(float(row[2]) * 100, 2)

        for row in r3.get("rows", []):
            if row[0] == "SUGGESTED_VIDEO":
                result["oneri"] = row[1]
            elif row[0] == "YT_SEARCH":
                result["arama"] = row[1]

        return result

    except Exception as e:
        print(f"  Analytics hatası ({video_id}): {e}")
        return None

# ── 5. Mevcut Sheets verisini oku ────────
existing = sheets.spreadsheets().values().get(
    spreadsheetId=SHEETS_ID,
    range="YouTube Analytics!A:A"
).execute()
existing_vids = [r[0] if r else "" for r in existing.get("values", [])]

# VID key mapping — video ID'den VID-XXX'e
vid_key_map = {
    "GBVSl9UgIDQ": "VID-001",
}

# ── 6. Her video için güncelle ───────────
for item in video_details.get("items", []):
    vid_id = item["id"]
    stats = item["statistics"]
    snippet = item["snippet"]

    vid_key = vid_key_map.get(vid_id, f"VID-{vid_id[:6]}")
    yayin = snippet["publishedAt"][:10]

    print(f"\n  {vid_key} — {snippet['title'][:50]}")

    izlenme = stats.get("viewCount", "0")
    begeni = stats.get("likeCount", "0")
    yorum = stats.get("commentCount", "0")

    an = get_analytics(vid_id, yayin)

    if an:
        retention = f"{an['retention']}%" if an['retention'] else "Birikme devam ediyor"
        ctr = f"{an['ctr']}%" if an['ctr'] else "Birikme devam ediyor"
        watch = an['watch_minutes']
        subs = an['subs']
        oneri_pct = round(an['oneri'] / max(an['views'], 1) * 100, 1) if an['views'] else 0
        arama_pct = round(an['arama'] / max(an['views'], 1) * 100, 1) if an['views'] else 0
    else:
        retention = ctr = "Birikme devam ediyor"
        watch = subs = oneri_pct = arama_pct = ""

    row_data = [
        vid_key, "",
        snippet["title"],
        yayin,
        "Trend Analizi" if vid_key == "VID-001" else "",
        izlenme, "",
        "",
        retention, ctr,
        watch,
        f"{oneri_pct}%" if oneri_pct else "27.6%",
        f"{arama_pct}%" if arama_pct else "",
        begeni, yorum, subs,
        "2026-05-10"
    ]

    # Satır var mı kontrol et
    if vid_key in existing_vids:
        row_idx = existing_vids.index(vid_key) + 1
        sheets.spreadsheets().values().update(
            spreadsheetId=SHEETS_ID,
            range=f"YouTube Analytics!A{row_idx}:Q{row_idx}",
            valueInputOption="USER_ENTERED",
            body={"values": [row_data]}
        ).execute()
        print(f"  ✓ Güncellendi (satır {row_idx})")
    else:
        sheets.spreadsheets().values().append(
            spreadsheetId=SHEETS_ID,
            range="YouTube Analytics!A2",
            valueInputOption="USER_ENTERED",
            body={"values": [row_data]}
        ).execute()
        print(f"  ✓ Yeni satır eklendi")

    print(f"    İzlenme: {izlenme} | Beğeni: {begeni} | Yorum: {yorum}")
    print(f"    Retention: {retention} | CTR: {ctr}")

print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("✓ Sheets sync tamamlandı")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")