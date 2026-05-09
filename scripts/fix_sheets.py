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
sheets = build("sheets", "v4", credentials=creds)
SHEETS_ID = os.getenv("GOOGLE_SHEETS_ID")

# Mevcut sheet ID'lerini al
spreadsheet = sheets.spreadsheets().get(spreadsheetId=SHEETS_ID).execute()
sheet_map = {s["properties"]["title"]: s["properties"]["sheetId"] 
             for s in spreadsheet["sheets"]}
print(f"Mevcut tablar: {list(sheet_map.keys())}")

# ── 1. Öneriler tab'ı ekle ──────────────────────────────────────
if "Oneriler" not in sheet_map:
    sheets.spreadsheets().batchUpdate(
        spreadsheetId=SHEETS_ID,
        body={"requests": [{"addSheet": {"properties": {"title": "Oneriler"}}}]}
    ).execute()
    spreadsheet = sheets.spreadsheets().get(spreadsheetId=SHEETS_ID).execute()
    sheet_map = {s["properties"]["title"]: s["properties"]["sheetId"] 
                 for s in spreadsheet["sheets"]}
    print("✓ Oneriler tab'ı eklendi")

# ── 2. İçerik Takvimi — başlık satırına YouTube URL ekle ────────
sheets.spreadsheets().values().update(
    spreadsheetId=SHEETS_ID,
    range="Icerik Takvimi!A1:K1",
    valueInputOption="USER_ENTERED",
    body={"values": [[
        "VID Key", "Video Tipi", "Renk Kodu", "Başlık",
        "YouTube URL", "Yayın Tarihi", "Durum",
        "Analytics Link", "IG Post", "IG Haftası", "Notlar"
    ]]}
).execute()
print("✓ İçerik Takvimi başlık güncellendi")

# ── 3. İçerik Takvimi — veri satırlarını temizle ve yeniden yaz ─
sheets.spreadsheets().values().clear(
    spreadsheetId=SHEETS_ID, range="Icerik Takvimi!A2:K1000"
).execute()

takvim_rows = [
    ["VID-001", "Trend Analizi", "#414ecf",
     "Python Öğrenmek Yetmiyor — 2026'da Veri Bilimi Gerçekten Ne İstiyor?",
     "https://youtu.be/GBVSl9UgIDQ",
     "2026-05-08", "✅ Yayında",
     '=HYPERLINK("#\'YouTube Analytics\'!A"&MATCH(A2,\'YouTube Analytics\'!A:A,0),A2)',
     "", "", ""],
    ["VID-002", "Tutorial", "#f0eee9",
     "AI Agent Sistemleri: Veri Biliminde Nasıl Kullanılır?",
     "", "2026-05-14", "📋 Planlandı",
     '=HYPERLINK("#\'YouTube Analytics\'!A"&MATCH(A3,\'YouTube Analytics\'!A:A,0),A3)',
     "", "", "Verilen söz"],
    ["VID-003", "Kariyer / POV", "#d2c7ff",
     "Sağlıktan Veri Bilimine — Kimse Söylemedi Bunları",
     "", "2026-05-21", "💡 Fikir",
     '=HYPERLINK("#\'YouTube Analytics\'!A"&MATCH(A4,\'YouTube Analytics\'!A:A,0),A4)',
     "", "", ""],
    ["VID-004", "Trend Analizi", "#414ecf",
     "%57 Şirket AI Agent Kullanıyor — Sen Ne Yapıyorsun?",
     "", "2026-05-28", "💡 Fikir",
     '=HYPERLINK("#\'YouTube Analytics\'!A"&MATCH(A5,\'YouTube Analytics\'!A:A,0),A5)',
     "", "", ""],
]

sheets.spreadsheets().values().append(
    spreadsheetId=SHEETS_ID,
    range="Icerik Takvimi!A2",
    valueInputOption="USER_ENTERED",
    body={"values": takvim_rows}
).execute()
print("✓ İçerik Takvimi veri güncellendi")

# ── 4. Renklendirme ─────────────────────────────────────────────
takvim_id = sheet_map["Icerik Takvimi"]
analytics_id = sheet_map["YouTube Analytics"]

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16)/255 for i in (0, 2, 4))
    return {"red": r, "green": g, "blue": b}

format_requests = [
    # ── Başlık satırı koyu — İçerik Takvimi ──
    {
        "repeatCell": {
            "range": {"sheetId": takvim_id, "startRowIndex": 0, "endRowIndex": 1,
                      "startColumnIndex": 0, "endColumnIndex": 11},
            "cell": {"userEnteredFormat": {
                "backgroundColor": hex_to_rgb("1a1a2e"),
                "textFormat": {"foregroundColor": {"red":1,"green":1,"blue":1},
                               "bold": True, "fontSize": 10},
                "horizontalAlignment": "CENTER"
            }},
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment)"
        }
    },
    # ── Başlık satırı koyu — Analytics ──
    {
        "repeatCell": {
            "range": {"sheetId": analytics_id, "startRowIndex": 0, "endRowIndex": 1,
                      "startColumnIndex": 0, "endColumnIndex": 17},
            "cell": {"userEnteredFormat": {
                "backgroundColor": hex_to_rgb("1a1a2e"),
                "textFormat": {"foregroundColor": {"red":1,"green":1,"blue":1},
                               "bold": True, "fontSize": 10},
                "horizontalAlignment": "CENTER"
            }},
            "fields": "userEnteredFormat(backgroundColor,textFormat,horizontalAlignment)"
        }
    },
    # ── Veri satırları beyaz ──
    {
        "repeatCell": {
            "range": {"sheetId": takvim_id, "startRowIndex": 1, "endRowIndex": 100,
                      "startColumnIndex": 0, "endColumnIndex": 11},
            "cell": {"userEnteredFormat": {
                "backgroundColor": {"red":1,"green":1,"blue":1}
            }},
            "fields": "userEnteredFormat(backgroundColor)"
        }
    },
    # ── Sütun genişlikleri ──
    {"updateDimensionProperties": {
        "range": {"sheetId": takvim_id, "dimension": "COLUMNS",
                  "startIndex": 3, "endIndex": 4},
        "properties": {"pixelSize": 350}, "fields": "pixelSize"
    }},
    {"updateDimensionProperties": {
        "range": {"sheetId": takvim_id, "dimension": "COLUMNS",
                  "startIndex": 4, "endIndex": 5},
        "properties": {"pixelSize": 220}, "fields": "pixelSize"
    }},

    # ══════════════════════════════════════════
    # DURUM SÜTUNU (G = index 6) — Conditional Formatting
    # ✅ Yayında → yeşil
    # ══════════════════════════════════════════
    {
        "addConditionalFormatRule": {
            "rule": {
                "ranges": [{"sheetId": takvim_id, "startRowIndex": 1, "endRowIndex": 100,
                            "startColumnIndex": 6, "endColumnIndex": 7}],
                "booleanRule": {
                    "condition": {"type": "TEXT_CONTAINS", "values": [{"userEnteredValue": "Yayında"}]},
                    "format": {"backgroundColor": hex_to_rgb("90e0a0"),
                               "textFormat": {"bold": True}}
                }
            },
            "index": 0
        }
    },
    # 📋 Planlandı / Hazırlık → somon/turuncu
    {
        "addConditionalFormatRule": {
            "rule": {
                "ranges": [{"sheetId": takvim_id, "startRowIndex": 1, "endRowIndex": 100,
                            "startColumnIndex": 6, "endColumnIndex": 7}],
                "booleanRule": {
                    "condition": {"type": "TEXT_CONTAINS", "values": [{"userEnteredValue": "Planlandı"}]},
                    "format": {"backgroundColor": hex_to_rgb("ffb347"),
                               "textFormat": {"bold": True}}
                }
            },
            "index": 1
        }
    },
    # 🎬 Çekimde → somon
    {
        "addConditionalFormatRule": {
            "rule": {
                "ranges": [{"sheetId": takvim_id, "startRowIndex": 1, "endRowIndex": 100,
                            "startColumnIndex": 6, "endColumnIndex": 7}],
                "booleanRule": {
                    "condition": {"type": "TEXT_CONTAINS", "values": [{"userEnteredValue": "Çekimde"}]},
                    "format": {"backgroundColor": hex_to_rgb("ffa07a"),
                               "textFormat": {"bold": True}}
                }
            },
            "index": 2
        }
    },
    # ✂️ Post → açık turuncu
    {
        "addConditionalFormatRule": {
            "rule": {
                "ranges": [{"sheetId": takvim_id, "startRowIndex": 1, "endRowIndex": 100,
                            "startColumnIndex": 6, "endColumnIndex": 7}],
                "booleanRule": {
                    "condition": {"type": "TEXT_CONTAINS", "values": [{"userEnteredValue": "Post"}]},
                    "format": {"backgroundColor": hex_to_rgb("ffcc99"),
                               "textFormat": {"bold": True}}
                }
            },
            "index": 3
        }
    },
    # 💡 Fikir → lila
    {
        "addConditionalFormatRule": {
            "rule": {
                "ranges": [{"sheetId": takvim_id, "startRowIndex": 1, "endRowIndex": 100,
                            "startColumnIndex": 6, "endColumnIndex": 7}],
                "booleanRule": {
                    "condition": {"type": "TEXT_CONTAINS", "values": [{"userEnteredValue": "Fikir"}]},
                    "format": {"backgroundColor": hex_to_rgb("d2c7ff"),
                               "textFormat": {"bold": True}}
                }
            },
            "index": 4
        }
    },

    # ══════════════════════════════════════════
    # VİDEO TİPİ SÜTUNU (B = index 1) — Conditional Formatting
    # ══════════════════════════════════════════
    # Trend Analizi → mor
    {
        "addConditionalFormatRule": {
            "rule": {
                "ranges": [{"sheetId": takvim_id, "startRowIndex": 1, "endRowIndex": 100,
                            "startColumnIndex": 1, "endColumnIndex": 2}],
                "booleanRule": {
                    "condition": {"type": "TEXT_CONTAINS", "values": [{"userEnteredValue": "Trend"}]},
                    "format": {"backgroundColor": hex_to_rgb("9b5de5"),
                               "textFormat": {"foregroundColor": {"red":1,"green":1,"blue":1},
                                              "bold": True}}
                }
            },
            "index": 5
        }
    },
    # Tutorial → mavi
    {
        "addConditionalFormatRule": {
            "rule": {
                "ranges": [{"sheetId": takvim_id, "startRowIndex": 1, "endRowIndex": 100,
                            "startColumnIndex": 1, "endColumnIndex": 2}],
                "booleanRule": {
                    "condition": {"type": "TEXT_CONTAINS", "values": [{"userEnteredValue": "Tutorial"}]},
                    "format": {"backgroundColor": hex_to_rgb("414ecf"),
                               "textFormat": {"foregroundColor": {"red":1,"green":1,"blue":1},
                                              "bold": True}}
                }
            },
            "index": 6
        }
    },
    # Kariyer / POV → pembe
    {
        "addConditionalFormatRule": {
            "rule": {
                "ranges": [{"sheetId": takvim_id, "startRowIndex": 1, "endRowIndex": 100,
                            "startColumnIndex": 1, "endColumnIndex": 2}],
                "booleanRule": {
                    "condition": {"type": "TEXT_CONTAINS", "values": [{"userEnteredValue": "Kariyer"}]},
                    "format": {"backgroundColor": hex_to_rgb("f4b5de"),
                               "textFormat": {"bold": True}}
                }
            },
            "index": 7
        }
    },
    # Girişim / Para → sarı-yeşil
    {
        "addConditionalFormatRule": {
            "rule": {
                "ranges": [{"sheetId": takvim_id, "startRowIndex": 1, "endRowIndex": 100,
                            "startColumnIndex": 1, "endColumnIndex": 2}],
                "booleanRule": {
                    "condition": {"type": "TEXT_CONTAINS", "values": [{"userEnteredValue": "Girişim"}]},
                    "format": {"backgroundColor": hex_to_rgb("cedd82"),
                               "textFormat": {"bold": True}}
                }
            },
            "index": 8
        }
    },
    # Vlog → açık turuncu
    {
        "addConditionalFormatRule": {
            "rule": {
                "ranges": [{"sheetId": takvim_id, "startRowIndex": 1, "endRowIndex": 100,
                            "startColumnIndex": 1, "endColumnIndex": 2}],
                "booleanRule": {
                    "condition": {"type": "TEXT_CONTAINS", "values": [{"userEnteredValue": "Vlog"}]},
                    "format": {"backgroundColor": hex_to_rgb("ffb347"),
                               "textFormat": {"bold": True}}
                }
            },
            "index": 9
        }
    },
]

sheets.spreadsheets().batchUpdate(
    spreadsheetId=SHEETS_ID,
    body={"requests": format_requests}
).execute()
print("✓ Renkler uygulandı")

# ── 5. Öneriler tab'ına son /youtube çıktısını yaz ───────────────
oneriler_id = sheet_map["Oneriler"]

sheets.spreadsheets().values().clear(
    spreadsheetId=SHEETS_ID, range="Oneriler!A1:Z1000"
).execute()

oneriler_data = [
    ["AXONODEAI /youtube ÖNERİLER — 2026-05-09"],
    [""],
    ["VID-002 — TUTORIAL (Verilen Söz)"],
    ["Başlık (Ana)", "AI Agent Sistemleri: Veri Biliminde Nasıl Kullanılır?"],
    ["Başlık (Alt 1)", "Veri Bilimciler İçin AI Agent Rehberi — 2026"],
    ["Başlık (Alt 2)", "AI Agent ile Veri Analizi — Adım Adım 2026"],
    ["Thumbnail arka plan", "#f0eee9"],
    ["Thumbnail metin rengi", "#f94144"],
    ["Thumbnail metni", "AI AGENT KURULUM"],
    ["İfade", "Merak"],
    ["Hook tipi", "Vadi"],
    ["Hook taslağı", "Geçen hafta söz verdim — AI agent anlatacağım. İşte buradayım. Bu videonun sonunda LangChain kullanarak kendi veri analizi ajanını kurmuş olacaksın."],
    ["Taglar", "veri bilimi, yapay zeka, yapay zeka kariyer, AI, artificial intelligence, data science, kariyer gelisimi, axonodeai, AI literacy, yapay zeka 2026, AI agent, veri bilimi araclari, machine learning, LangChain, CrewAI"],
    ["Hedef yayın", "2026-05-14"],
    [""],
    ["VID-003 — KARİYER / POV"],
    ["Başlık (Ana)", "Sağlıktan Veri Bilimine — Kimse Söylemedi Bunları"],
    ["Başlık (Alt 1)", "AI Çağında Kariyer Değiştirmek: Gerçekten Ne Gerekiyor?"],
    ["Başlık (Alt 2)", "Veri Bilimine Geçişin Gerçeği — AI Çağında Kariyer"],
    ["Thumbnail arka plan", "#d2c7ff"],
    ["Thumbnail metin rengi", "#31241f"],
    ["Thumbnail metni", "KİMSE SÖYLEMEDİ"],
    ["İfade", "Ciddiyet"],
    ["Hook tipi", "Hikaye"],
    ["Hook taslağı", "3 yıl önce hemşirelikteyken veri bilimi yapacağımı düşünmezdim. Bugün yapıyorum. Bu geçişte bana kimsenin söylemediği 3 şey var."],
    ["Taglar", "veri bilimi, yapay zeka, yapay zeka kariyer, AI, artificial intelligence, data science, kariyer gelisimi, axonodeai, AI literacy, yapay zeka 2026, kariyer degisikligi, veri bilimi nasil ogrenilir, AI ile kariyer, yapay zeka ile para kazanma, AI nasil ogrenilir"],
    ["Hedef yayın", "2026-05-21"],
    [""],
    ["VID-004 — TREND ANALİZİ"],
    ["Başlık (Ana)", "%57 Şirket AI Agent Kullanıyor — Sen Ne Yapıyorsun?"],
    ["Başlık (Alt 1)", "AI Araçları 2026: Veri Bilimciler Bunları Bilmeli"],
    ["Başlık (Alt 2)", "Agentic AI Çağında Veri Bilimi Nereye Gidiyor?"],
    ["Thumbnail arka plan", "#414ecf"],
    ["Thumbnail metin rengi", "#d9f103"],
    ["Thumbnail metni", "%57 KULLANIYOR"],
    ["İfade", "Şaşkınlık"],
    ["Hook tipi", "Veri / Şok"],
    ["Hook taslağı", "Yüzde 57. 2026 itibarıyla şirketlerin yarısından fazlası AI agent kullanıyor. Peki bu biz veri bilimciler için ne anlama geliyor?"],
    ["Taglar", "veri bilimi, yapay zeka, yapay zeka kariyer, AI, artificial intelligence, data science, kariyer gelisimi, axonodeai, AI literacy, yapay zeka 2026, AI trendleri, yapay zeka egitimi, is dunyasinin gelecegi, AI agent, yapay zeka araclari"],
    ["Hedef yayın", "2026-05-28"],
    [""],
    ["VİRAL PATTERN'LER (Bu Çalışma)"],
    ["Sayı/Para Motivasyonu", "Somut rakam başlıkta — yüksek CTR. Girişim/Para videosunda kullan."],
    ["Yıl + Etki İddiası", "'2026'da Hayatımızı Değiştirecek' tarzı — güncellik + önem sinyali."],
    ["Kontrast Çifti", "'Yükselen / Yok Olan' tarzı — merak + FOMO. VID-004 sonrası dene."],
    ["Vadi Hook", "'Bu videonun sonunda X yapmış olacaksın' — yüksek retention. VID-002'de uygula."],
    ["ÖNEMLİ GAP", "Türkçe AI Agent pratik tutorial boşluğu — açıklama var, kurulum yok. VID-002 bunu doldurabilir."],
]

sheets.spreadsheets().values().update(
    spreadsheetId=SHEETS_ID,
    range="Oneriler!A1",
    valueInputOption="USER_ENTERED",
    body={"values": oneriler_data}
).execute()

# Öneriler tab başlık formatı
oneriler_sheet_id = sheet_map["Oneriler"]
sheets.spreadsheets().batchUpdate(
    spreadsheetId=SHEETS_ID,
    body={"requests": [
        {
            "repeatCell": {
                "range": {"sheetId": oneriler_sheet_id,
                          "startRowIndex": 0, "endRowIndex": 1,
                          "startColumnIndex": 0, "endColumnIndex": 2},
                "cell": {"userEnteredFormat": {
                    "backgroundColor": hex_to_rgb("414ecf"),
                    "textFormat": {"foregroundColor": {"red":1,"green":1,"blue":1},
                                   "bold": True, "fontSize": 12}
                }},
                "fields": "userEnteredFormat(backgroundColor,textFormat)"
            }
        },
        {"updateDimensionProperties": {
            "range": {"sheetId": oneriler_sheet_id, "dimension": "COLUMNS",
                      "startIndex": 0, "endIndex": 1},
            "properties": {"pixelSize": 200}, "fields": "pixelSize"
        }},
        {"updateDimensionProperties": {
            "range": {"sheetId": oneriler_sheet_id, "dimension": "COLUMNS",
                      "startIndex": 1, "endIndex": 2},
            "properties": {"pixelSize": 500}, "fields": "pixelSize"
        }},
    ]}
).execute()

print("✓ Öneriler tab'ı dolduruldu")

print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("✓ Tüm düzeltmeler tamamlandı")
print("  1. Öneriler tab'ı → eklendi")
print("  2. YouTube URL sütunu → eklendi")  
print("  3. Hyperlink formülleri → eklendi")
print("  4. Renkler → uygulandı")
print("  5. Öneriler → Sheets'e yazıldı")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")