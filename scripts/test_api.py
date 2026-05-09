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
print("✓ OAuth token geçerli")

# Test 1 — YouTube Data API
youtube = build("youtube", "v3", credentials=creds)
channel = youtube.channels().list(
    part="snippet,statistics",
    id=os.getenv("YOUTUBE_CHANNEL_ID")
).execute()

if channel["items"]:
    ch = channel["items"][0]
    print(f"✓ YouTube Data API bağlandı")
    print(f"  Kanal: {ch['snippet']['title']}")
    print(f"  Abone: {ch['statistics'].get('subscriberCount', 'gizli')}")
    print(f"  Toplam video: {ch['statistics'].get('videoCount', '?')}")
    print(f"  Toplam izlenme: {ch['statistics'].get('viewCount', '?')}")
else:
    print("✗ Kanal bulunamadı — CHANNEL_ID kontrol et")

# Test 2 — Video listesi
videos = youtube.search().list(
    part="snippet",
    channelId=os.getenv("YOUTUBE_CHANNEL_ID"),
    type="video",
    order="date",
    maxResults=5
).execute()

print(f"\n✓ Son videolar:")
for item in videos.get("items", []):
    print(f"  - {item['snippet']['title']}")
    print(f"    ID: {item['id']['videoId']}")

# Test 3 — Analytics API
# Test 3 — Analytics API
try:
    analytics = build("youtubeAnalytics", "v2", credentials=creds)
    
    # Önce kanal geneli metrikler (dimensions olmadan)
    report = analytics.reports().query(
        ids="channel==MINE",
        startDate="2026-05-01",
        endDate="2026-05-09",
        metrics="views,estimatedMinutesWatched,subscribersGained"
    ).execute()

    print(f"\n✓ YouTube Analytics API bağlandı")
    print(f"  Kanal geneli (1-9 Mayıs):")
    if report.get("rows"):
        row = report["rows"][0]
        print(f"  İzlenme: {row[0]}")
        print(f"  İzlenme süresi (dk): {row[1]}")
        print(f"  Yeni abone: {row[2]}")
    else:
        print("  Veri yok")

    # Video bazlı CTR ve izlenme
    report2 = analytics.reports().query(
        ids="channel==MINE",
        startDate="2026-05-01",
        endDate="2026-05-09",
        metrics="views,estimatedMinutesWatched,averageViewPercentage,subscribersGained",
        dimensions="video",
        sort="-views",
        maxResults=5
    ).execute()

    print(f"\n  Video bazlı:")
    if report2.get("rows"):
        for row in report2["rows"]:
            print(f"  Video ID: {row[0]}")
            print(f"  İzlenme: {row[1]}")
            print(f"  İzlenme süresi (dk): {row[2]}")
            print(f"  Retention: {row[3]}%")
            print(f"  Yeni abone: {row[4]}")
    else:
        print("  Video bazlı veri henüz yok")

    # Traffic source
    report3 = analytics.reports().query(
        ids="channel==MINE",
        startDate="2026-05-01",
        endDate="2026-05-09",
        metrics="views",
        dimensions="insightTrafficSourceType",
        sort="-views"
    ).execute()

    print(f"\n  Trafik kaynakları:")
    if report3.get("rows"):
        for row in report3["rows"]:
            print(f"  {row[0]}: {row[1]} izlenme")
    else:
        print("  Trafik verisi henüz yok")

except Exception as e:
    print(f"\n✗ Analytics API hatası: {e}")