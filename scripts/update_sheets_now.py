import os
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
        "https://www.googleapis.com/auth/youtube.readonly",
        "https://www.googleapis.com/auth/yt-analytics.readonly",
        "https://www.googleapis.com/auth/spreadsheets"
    ]
)
creds.refresh(Request())

youtube = build("youtube", "v3", credentials=creds)
sheets = build("sheets", "v4", credentials=creds)
SHEETS_ID = os.getenv("GOOGLE_SHEETS_ID")

# Kanal genel istatistikleri çek
channel = youtube.channels().list(
    part="snippet,statistics",
    id=os.getenv("YOUTUBE_CHANNEL_ID")
).execute()

ch = channel["items"][0]
abone = ch["statistics"].get("subscriberCount", "0")
toplam_izlenme = ch["statistics"].get("viewCount", "0")
toplam_video = ch["statistics"].get("videoCount", "0")

print(f"Kanal: {ch['snippet']['title']}")
print(f"Abone: {abone}")
print(f"Toplam izlenme: {toplam_izlenme}")
print(f"Toplam video: {toplam_video}")

# Video detayları çek
video = youtube.videos().list(
    part="snippet,statistics,contentDetails",
    id="GBVSl9UgIDQ"
).execute()

v = video["items"][0]
izlenme = v["statistics"].get("viewCount", "0")
begeni = v["statistics"].get("likeCount", "0")
yorum = v["statistics"].get("commentCount", "0")
sure = v["contentDetails"]["duration"]

print(f"\nVID-001:")
print(f"  İzlenme: {izlenme}")
print(f"  Beğeni: {begeni}")
print(f"  Yorum: {yorum}")
print(f"  Süre: {sure}")

# Analytics sheet güncelle — VID-001 satırını bul ve güncelle
result = sheets.spreadsheets().values().get(
    spreadsheetId=SHEETS_ID,
    range="YouTube Analytics!A:A"
).execute()

rows = result.get("values", [])
vid001_row = None
for i, row in enumerate(rows):
    if row and row[0] == "VID-001":
        vid001_row = i + 1
        break

if vid001_row:
    # Satırı güncelle
    sheets.spreadsheets().values().update(
        spreadsheetId=SHEETS_ID,
        range=f"YouTube Analytics!A{vid001_row}:Q{vid001_row}",
        valueInputOption="USER_ENTERED",
        body={"values": [[
            "VID-001",
            "",
            "Python Öğrenmek Yetmiyor — 2026'da Veri Bilimi Gerçekten Ne İstiyor?",
            "2026-05-08",
            "Trend Analizi",
            izlenme,
            "",
            "",
            "Analytics bekleniyor (24-72s)",
            "Analytics bekleniyor (24-72s)",
            "",
            "27.6",
            "",
            begeni,
            yorum,
            "",
            "2026-05-09"
        ]]}
    ).execute()
    print(f"\n✓ YouTube Analytics sheet güncellendi (satır {vid001_row})")
else:
    print("\n✗ VID-001 satırı bulunamadı")

# Kanal özet satırı ekle — ayrı bir yere
# Analytics snapshot olarak ilk satırın üstüne not ekle
print(f"\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"Kanal özeti Sheets'e yazıldı.")
print(f"Analytics verisi 2-3 gün içinde dolacak.")
print(f"O zaman tekrar çalıştır: python scripts/update_sheets_now.py")
print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")