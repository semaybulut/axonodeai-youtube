# SKILL: write-sheets
# AxonodeAI YouTube Brain
# Google Sheets entegrasyonu — 3 sheet otomatik güncelleme

---

## GÖREV

Google Sheets'teki 3 sheet'i otomatik güncelle.
Bu skill /youtube komutunun final adımında çağrılır.
Primary key: VID-XXX ve VPT-XXX — her yerde tutarlı.

---

## GEREKLI KURULUM

### .env
GOOGLE_SHEETS_ID=               ← Sheets URL'sindeki ID
GOOGLE_SHEETS_RANGE_TAKVIM=     ← İçerik Takvimi!A:J
GOOGLE_SHEETS_RANGE_ANALYTICS=  ← YouTube Analytics!A:P
GOOGLE_SHEETS_RANGE_VIRAL=      ← Viral Patterns!A:L

### Sheets ID Nerede?
https://docs.google.com/spreadsheets/d/[BU_KISIM]/edit
↑
GOOGLE_SHEETS_ID

### Gerekli Kütüphane
pip install google-api-python-client google-auth

### OAuth Scope (fetch-analytics.md'de zaten eklendi)
https://www.googleapis.com/auth/spreadsheets

---

## SHEET YAPISI

### Sheet 1 — İçerik Takvimi

Tab adı: Icerik Takvimi
SÜTUNLAR:
A: VID Key        → VID-001, VID-002...
B: Video Tipi     → Trend Analizi / Tutorial / Kariyer / Girişim
C: Renk Kodu      → #414ecf / #d2c7ff / #f4b5de
D: Başlık         → Video başlığı
E: Yayın Tarihi   → YYYY-MM-DD
F: Durum          → Fikir / Planlandı / Çekimde / Post / Yayında
G: Analytics Link → =HYPERLINK("#'YouTube Analytics'!A"&MATCH(A2,'YouTube Analytics'!A:A,0),A2)
H: IG Post        → Bağlantılı Instagram postu
I: IG Haftası     → Hangi haftada yayınlanacak
J: Notlar         → Serbest alan
RENK KODLAMA (conditional formatting):
Fikir     → #f0eee9 (açık gri)
Planlandı → #cc4dbf (açık mor)
Çekimde   → #ffd166 (sarı)
Post      → #71d6d9 (açık mavi)
Yayında   → #60d878 (açık yeşil)

### Sheet 2 — YouTube Analytics
Tab adı: YouTube Analytics
SÜTUNLAR:
A: VID Key              → VID-001
B: Takvim Link          → =HYPERLINK("#'Icerik Takvimi'!A"&MATCH(A2,'Icerik Takvimi'!A:A,0),A2)
C: Başlık               → Video başlığı
D: Yayın Tarihi         → YYYY-MM-DD
E: Video Tipi           → Trend / Tutorial / Kariyer / Girişim
F: İzlenme              → Sayı
G: Benzersiz İzleyici   → Sayı
H: Ort. İzlenme Süresi  → Dakika:Saniye
I: Retention Oranı      → Yüzde
J: CTR                  → Yüzde
K: Toplam İzlenme Dk    → Sayı
L: Öneri Trafiği        → Yüzde
M: Arama Trafiği        → Yüzde
N: Beğeni               → Sayı
O: Yorum                → Sayı
P: Abone Artışı         → Sayı (+ veya -)
Q: Son Güncelleme       → YYYY-MM-DD
ALARM SATIRI (conditional formatting):
CTR < 2%        → J sütunu kırmızı
Retention < 30% → I sütunu kırmızı
Retention > 50% → I sütunu yeşil
CTR > 5%        → J sütunu yeşil

### Sheet 3 — Viral Patterns
Tab adı: Viral Patterns
SÜTUNLAR:
A: VPT Key              → VPT-001
B: Video URL            → YouTube linki
C: Kanal                → Kanal adı
D: Başlık               → Video başlığı
E: İzlenme              → Sayı
F: Yayın Tarihi         → YYYY-MM-DD
G: Hook Tipi            → İddia / Soru / Şok / Hikaye / Vadi
H: Başlık Formülü       → Formül 1 / 2 / 3 / 4 / 5
I: Thumbnail Özelliği   → Yüz var, yüksek kontrast vb.
J: En Güçlü Özellik     → Serbest metin
K: Kullanılabilir mi    → Evet / Hayır / Kısmen
L: Analiz Tarihi        → YYYY-MM-DD

---

## SHEETS KURULUMU (İlk Kez)

### Sheets'i Manuel Oluştur
docs.google.com/spreadsheets → Yeni oluştur
Dosya adı: AxonodeAI YouTube Brain
Tab 1 adını değiştir: Icerik Takvimi
Tab 2 ekle: YouTube Analytics
Tab 3 ekle: Viral Patterns
Her tab için başlık satırını ekle (1. satır)
URL'den Sheets ID'yi kopyala → .env'e yaz

### Başlık Satırları API ile Yaz
```python
# İlk kurulumda bir kere çalıştır
headers = {
    "Icerik Takvimi": [
        ["VID Key", "Video Tipi", "Renk Kodu", "Başlık",
         "Yayın Tarihi", "Durum", "Analytics Link",
         "IG Post", "IG Haftası", "Notlar"]
    ],
    "YouTube Analytics": [
        ["VID Key", "Takvim Link", "Başlık", "Yayın Tarihi",
         "Video Tipi", "İzlenme", "Benzersiz İzleyici",
         "Ort. İzlenme Süresi", "Retention", "CTR",
         "Toplam İzlenme Dk", "Öneri Trafiği", "Arama Trafiği",
         "Beğeni", "Yorum", "Abone Artışı", "Son Güncelleme"]
    ],
    "Viral Patterns": [
        ["VPT Key", "Video URL", "Kanal", "Başlık",
         "İzlenme", "Yayın Tarihi", "Hook Tipi",
         "Başlık Formülü", "Thumbnail Özelliği",
         "En Güçlü Özellik", "Kullanılabilir mi", "Analiz Tarihi"]
    ]
}
```

---

## YAZMA OPERASYONLARI

### Operasyon 1 — İçerik Takvimi Güncelle
Ne zaman: idea-generator yeni video fikirleri üretince
Mantık:

Sheet 1'i oku — mevcut VID key'leri al
Yeni fikirdeki VID key mevcut mu kontrol et
Mevcut değilse → yeni satır ekle
Mevcutsa → sadece Durum ve Notlar sütununu güncelle

API Çağrısı — Yeni Satır Ekle:
POST https://sheets.googleapis.com/v4/spreadsheets/{id}/values/{range}:append
params:
valueInputOption: USER_ENTERED
body:
values: [[
"VID-002",
"Tutorial",
"#d2c7ff",
"AI Agent Sistemleri — Veri Biliminde Kullanım",
"2026-05-14",
"Planlandı",
"=HYPERLINK("#'YouTube Analytics'!A"&MATCH(A2,'YouTube Analytics'!A:A,0),A2)",
"",
"",
""
]]
API Çağrısı — Mevcut Satır Güncelle:
PUT https://sheets.googleapis.com/v4/spreadsheets/{id}/values/{range}
params:
valueInputOption: USER_ENTERED

### Operasyon 2 — Analytics Sheet Güncelle

Ne zaman: content-indexer analitik veri çekince
Mantık:

Sheet 2'yi oku — mevcut VID key'leri al
VID key mevcut mu kontrol et
Mevcut değilse → yeni satır ekle
Mevcutsa → tüm metrik sütunlarını güncelle (A hariç)

Güncellenen alanlar:
F: İzlenme (her çalışmada güncellenir)
G: Benzersiz İzleyici
H: Ort. İzlenme Süresi
I: Retention Oranı
J: CTR
K: Toplam İzlenme Dk
L: Öneri Trafiği
M: Arama Trafiği
N: Beğeni
O: Yorum
P: Abone Artışı
Q: Son Güncelleme → bugünün tarihi

### Operasyon 3 — Viral Patterns Sheet Güncelle
Ne zaman: fetch-viral-videos yeni viral video analiz edince
Mantık:

Sheet 3'ü oku — mevcut VPT key'leri al
VPT key mevcut mu kontrol et
Mevcut değilse → yeni satır ekle
Mevcutsa → atla (viral video verisi değişmez)

Yeni satır formatı:
["VPT-001", "https://...", "Kanal Adı", "Video Başlığı",
150000, "2026-04-15", "İddia", "Formül 1",
"Yüz var, yüksek kontrast", "Güçlü iddia hook",
"Evet", "2026-05-09"]

---

## BAĞLANTI FORMÜLLERI

### Sheet 1 → Sheet 2 Bağlantısı (G sütunu)
=HYPERLINK("#'YouTube Analytics'!A"&MATCH(A2,'YouTube Analytics'!A:A,0),A2)

VID-001'e tıklayınca direkt Analytics sheet'inde o satıra gider.

### Sheet 2 → Sheet 1 Bağlantısı (B sütunu)
=HYPERLINK("#'Icerik Takvimi'!A"&MATCH(A2,'Icerik Takvimi'!A:A,0),A2)

Analytics'ten takvime tek tıkla geçiş.

---

## HATA YÖNETİMİ

**Sheets ID bulunamıyor:**
→ ".env dosyasında GOOGLE_SHEETS_ID eksik" yaz
→ Dur

**403 Forbidden:**
→ "Sheets erişim izni yok, OAuth scope kontrol et" yaz
→ Dur

**Duplicate VID key:**
→ Güncelle, yeni satır ekleme
→ "VID-XXX güncellendi" yaz

**Boş veri:**
→ Boş hücre bırak, null yazma
→ Devam et

---

## SINIRLAR

- Başlık satırını (1. satır) asla değiştirme
- VID key'i asla değiştirme — primary key
- Formül sütunlarını (G ve B) üzerine yazma
- Sheets dışına veri gönderme

---

**END write-sheets**
