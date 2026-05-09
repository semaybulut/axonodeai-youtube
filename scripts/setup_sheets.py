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
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/youtube.readonly",
        "https://www.googleapis.com/auth/yt-analytics.readonly"
    ]
)
creds.refresh(Request())

service = build("sheets", "v4", credentials=creds)
SHEETS_ID = os.getenv("GOOGLE_SHEETS_ID")

# Mevcut tab adlarını kontrol et
spreadsheet = service.spreadsheets().get(spreadsheetId=SHEETS_ID).execute()
existing_tabs = [s["properties"]["title"] for s in spreadsheet["sheets"]]
print(f"Mevcut tablar: {existing_tabs}")

# Gerekli tablar
required_tabs = ["Icerik Takvimi", "YouTube Analytics", "Viral Patterns"]

# Eksik tabları ekle
add_requests = []
for tab in required_tabs:
    if tab not in existing_tabs:
        add_requests.append({
            "addSheet": {"properties": {"title": tab}}
        })

if add_requests:
    service.spreadsheets().batchUpdate(
        spreadsheetId=SHEETS_ID,
        body={"requests": add_requests}
    ).execute()
    print(f"✓ Yeni tablar eklendi: {[r['addSheet']['properties']['title'] for r in add_requests]}")
else:
    print("✓ Tüm tablar zaten mevcut")

# Başlık satırlarını yaz (üzerine yaz)
headers = {
    "Icerik Takvimi!A1:J1": [[
        "VID Key", "Video Tipi", "Renk Kodu", "Başlık",
        "Yayın Tarihi", "Durum", "Analytics Link",
        "IG Post", "IG Haftası", "Notlar"
    ]],
    "YouTube Analytics!A1:Q1": [[
        "VID Key", "Takvim Link", "Başlık", "Yayın Tarihi",
        "Video Tipi", "İzlenme", "Benzersiz İzleyici",
        "Ort. İzlenme Süresi", "Retention", "CTR",
        "Toplam İzlenme Dk", "Öneri Trafiği", "Arama Trafiği",
        "Beğeni", "Yorum", "Abone Artışı", "Son Güncelleme"
    ]],
    "Viral Patterns!A1:L1": [[
        "VPT Key", "Video URL", "Kanal", "Başlık",
        "İzlenme", "Yayın Tarihi", "Hook Tipi",
        "Başlık Formülü", "Thumbnail Özelliği",
        "En Güçlü Özellik", "Kullanılabilir mi", "Analiz Tarihi"
    ]]
}

for range_, values in headers.items():
    service.spreadsheets().values().update(
        spreadsheetId=SHEETS_ID,
        range=range_,
        valueInputOption="USER_ENTERED",
        body={"values": values}
    ).execute()
    print(f"✓ {range_} başlıkları yazıldı")

# Verileri yaz
takvim_rows = [
    ["VID-001", "Trend Analizi", "#414ecf",
     "Python Öğrenmek Yetmiyor — 2026'da Veri Bilimi Gerçekten Ne İstiyor?",
     "2026-05-08", "Yayında", "", "", "", ""],
    ["VID-002", "Tutorial", "#f0eee9",
     "AI Agent Sistemleri: Veri Biliminde Nasıl Kullanılır?",
     "2026-05-14", "Planlandı", "", "", "", "Verilen söz"],
    ["VID-003", "Kariyer / POV", "#d2c7ff",
     "Sağlıktan Veri Bilimine — Kimse Söylemedi Bunları",
     "2026-05-21", "Fikir", "", "", "", ""],
    ["VID-004", "Trend Analizi", "#414ecf",
     "%57 Şirket AI Agent Kullanıyor — Sen Ne Yapıyorsun?",
     "2026-05-28", "Fikir", "", "", "", ""],
]

analytics_rows = [
    ["VID-001", "",
     "Python Öğrenmek Yetmiyor — 2026'da Veri Bilimi Gerçekten Ne İstiyor?",
     "2026-05-08", "Trend Analizi",
     "", "", "", "", "", "", "27.6", "", "", "", "", "2026-05-09"],
]

viral_rows = [
    ["VPT-001", "https://www.youtube.com/watch?v=VxZ5nd0-lug",
     "Mert Durmazer | Digital Academy",
     "Yeni Yapay Zeka Meslekleri: 120K€, Kod Yok, Diploma Yok (2026 Patlayacak!)",
     "50000+", "2025-12-22", "Veri/Şok", "Formül 3+1 Hibrit",
     "Yüz var, yüksek kontrast, para rakamı",
     "Somut para rakamı ile dikkat çekme", "Evet", "2026-05-09"],
    ["VPT-002", "https://www.youtube.com/watch?v=sRG8Pa5IQTo",
     "Erhan Meydan",
     "2025'te Hayatımızı Değiştirecek AI Agents Nedir?",
     "50000+", "2025-01-18", "İddia", "Formül 1",
     "Yüz var, yüksek kontrast",
     "Yıl + etki iddiası kombinasyonu", "Kısmen", "2026-05-09"],
    ["VPT-003", "https://www.youtube.com/watch?v=QNp0YCZDjc4",
     "Türkçe AI kariyer kanalı",
     "IT ve AI Sektöründe Yükselen ve Yok Olan Meslekler",
     "50000+", "2025-10-01", "Kontrast", "Formül 1",
     "Yüz var, kontrast çifti",
     "Kontrast çifti tekniği (Yükselen/Yok Olan)", "Evet", "2026-05-09"],
]

# Mevcut veri varsa temizle, sonra yaz
for tab in ["Icerik Takvimi", "YouTube Analytics", "Viral Patterns"]:
    service.spreadsheets().values().clear(
        spreadsheetId=SHEETS_ID,
        range=f"{tab}!A2:Z1000"
    ).execute()

service.spreadsheets().values().append(
    spreadsheetId=SHEETS_ID,
    range="Icerik Takvimi!A2",
    valueInputOption="USER_ENTERED",
    body={"values": takvim_rows}
).execute()
print("✓ İçerik Takvimi dolduruldu")

service.spreadsheets().values().append(
    spreadsheetId=SHEETS_ID,
    range="YouTube Analytics!A2",
    valueInputOption="USER_ENTERED",
    body={"values": analytics_rows}
).execute()
print("✓ YouTube Analytics dolduruldu")

service.spreadsheets().values().append(
    spreadsheetId=SHEETS_ID,
    range="Viral Patterns!A2",
    valueInputOption="USER_ENTERED",
    body={"values": viral_rows}
).execute()
print("✓ Viral Patterns dolduruldu")

print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("✓ Google Sheets kurulumu tamamlandı")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")