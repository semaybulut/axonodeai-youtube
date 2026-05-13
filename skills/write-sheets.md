# SKILL: write-sheets
# AxonodeAI YouTube Brain
# Google Sheets Veri Yazımı — 5 Tab Otomatik Güncelleme

---

## GÖREV

Ajanlar ve komutlar tarafından üretilen verileri (SEO paketleri, analitikler,
izleyici geri bildirimleri) Google Sheets üzerindeki ilgili tablara doğru
formatta yaz. Bu skill /youtube komutunun final adımında çağrılır.
Primary key: VID-XXX ve VPT-XXX — her yerde tutarlı.

---

## GEREKLİ KURULUM

### .env
```
GOOGLE_SHEETS_ID=               <- Sheets URL'sindeki ID
GOOGLE_SHEETS_RANGE_TAKVIM=     <- İçerik Takvimi!A:J
GOOGLE_SHEETS_RANGE_ANALYTICS=  <- YouTube Analytics!A:Q
GOOGLE_SHEETS_RANGE_VIRAL=      <- Viral Patterns!A:L
GOOGLE_SHEETS_RANGE_IZLEYICI=   <- Izleyici Sesi!A:I
```

### Sheets ID Nerede?
```
https://docs.google.com/spreadsheets/d/[BU_KISIM]/edit
                                         ^^^^^^^^^^^
                                      GOOGLE_SHEETS_ID
```

### Gerekli Kütüphane
```bash
pip install google-api-python-client google-auth
```

### OAuth Scope (fetch-analytics.md'de zaten eklendi)
```
https://www.googleapis.com/auth/spreadsheets
```

---

## SHEET YAPISI

### Sheet 1 — İçerik Takvimi

Tab adı: Icerik Takvimi

SÜTUNLAR:
```
A: VID Key        -> VID-001, VID-002...
B: Video Tipi     -> Trend Analizi / Tutorial / Kariyer / Girişim
C: Renk Kodu      -> #414ecf / #d2c7ff / #f4b5de
D: Başlık         -> Video başlığı
E: Yayın Tarihi   -> YYYY-MM-DD
F: Durum          -> Fikir / Planlandı / Çekimde / Post / Yayında / Fikir (İzleyici Talebi)
G: Analytics Link -> =HYPERLINK("#'YouTube Analytics'!A"&MATCH(A2,'YouTube Analytics'!A:A,0),A2)
H: IG Post        -> Bağlantılı Instagram postu
I: IG Haftası     -> Hangi haftada yayınlanacak
J: Notlar         -> Serbest alan
```

RENK KODLAMA (conditional formatting):
```
Fikir                   -> #f0eee9 (açık gri)
Fikir (İzleyici Talebi) -> #fdebd0 (açık turuncu) -- izleyici taleplerini ayırt eder
Planlandı               -> #cc4dbf (açık mor)
Çekimde                 -> #ffd166 (sarı)
Post                    -> #71d6d9 (açık mavi)
Yayında                 -> #60d878 (açık yeşil)
```

---

### Sheet 2 — YouTube Analytics

Tab adı: YouTube Analytics

SÜTUNLAR:
```
A: VID Key              -> VID-001
B: Takvim Link          -> =HYPERLINK("#'Icerik Takvimi'!A"&MATCH(A2,'Icerik Takvimi'!A:A,0),A2)
C: Başlık               -> Video başlığı
D: Yayın Tarihi         -> YYYY-MM-DD
E: Video Tipi           -> Trend / Tutorial / Kariyer / Girişim
F: İzlenme              -> Sayı
G: Benzersiz İzleyici   -> Sayı
H: Ort. İzlenme Süresi  -> Dakika:Saniye
I: Retention Oranı      -> Yüzde
J: CTR                  -> Yüzde
K: Toplam İzlenme Dk    -> Sayı
L: Öneri Trafiği        -> Yüzde
M: Arama Trafiği        -> Yüzde
N: Beğeni               -> Sayı
O: Yorum                -> Sayı
P: Abone Artışı         -> Sayı (+ veya -)
Q: Son Güncelleme       -> YYYY-MM-DD
```

ALARM (conditional formatting):
```
CTR < %2        -> J sütunu kırmızı
Retention < %30 -> I sütunu kırmızı
Retention > %50 -> I sütunu yeşil
CTR > %5        -> J sütunu yeşil
```

---

### Sheet 3 — Viral Patterns

Tab adı: Viral Patterns

SÜTUNLAR:
```
A: VPT Key              -> VPT-001
B: Video URL            -> YouTube linki
C: Kanal                -> Kanal adı
D: Başlık               -> Video başlığı
E: İzlenme              -> Sayı
F: Yayın Tarihi         -> YYYY-MM-DD
G: Hook Tipi            -> İddia / Soru / Şok / Hikaye / Vadi
H: Başlık Formülü       -> Formül 1 / 2 / 3 / 4 / 5
I: Thumbnail Özelliği   -> Yüz var, yüksek kontrast vb.
J: En Güçlü Özellik     -> Serbest metin
K: Kullanılabilir mi    -> Evet / Hayır / Kısmen
L: Analiz Tarihi        -> YYYY-MM-DD
```

---

### Sheet 4 — İzleyici Sesi (YENİ)

Tab adı: Izleyici Sesi
Tab rengi: Turuncu (#f4a261) — diğer tablardan görsel ayrım için

SÜTUNLAR:
```
A: Tarih           -> YYYY-MM-DD (hangi /youtube çalışması)
B: VID Key         -> VID-XXX (yorumun geldiği video)
C: Kategori        -> Soru / Istek_Konu / Elestiri / Ovgu
D: Yorum (özet)    -> Max 100 karakter, yazar adı olmadan
E: Beğeni          -> Sayı
F: Tema            -> Kısa etiket (örn: "kurulum", "araç seçimi")
G: Video Önerildi? -> Bekliyor / Planlandı / Evet
H: Bağlı VID       -> Eğer video yapıldıysa VID-XXX
I: Notlar          -> Serbest alan
```

ALARM (conditional formatting):
```
Kategori = Istek_Konu VE Beğeni >= 5 -> D sütunu yeşil arka plan
Kategori = Elestiri   VE Beğeni >= 3 -> D sütunu sarı arka plan
```

---

## SHEETS KURULUMU (İlk Kez)

### Tabs Oluştur
```
1. docs.google.com/spreadsheets → Yeni oluştur
2. Dosya adı: AxonodeAI YouTube Brain
3. Tab adları:
   - Icerik Takvimi
   - YouTube Analytics
   - Viral Patterns
   - Oneriler
   - Izleyici Sesi     <- YENİ
4. URL'den Sheets ID'yi kopyala → .env'e yaz
5. python scripts/setup_sheets.py çalıştır
```

### Başlık Satırları

```python
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
    ],
    "Izleyici Sesi": [
        ["Tarih", "VID Key", "Kategori", "Yorum (özet)",
         "Beğeni", "Tema", "Video Önerildi?", "Bağlı VID", "Notlar"]
    ]
}
```

---

## YAZMA OPERASYONLARI

### Operasyon 1 — İçerik Takvimi Güncelle

Ne zaman: idea-generator yeni video fikirleri üretince
Mantık:
- Sheet 1'i oku — mevcut VID key'leri al
- Yeni fikirdeki VID key mevcut mu kontrol et
- Mevcut değilse → yeni satır ekle
- Mevcutsa → sadece Durum ve Notlar sütununu güncelle

**Durum Notu — İzleyici Talebi:**
Fikir AUDIENCE_VOICE kaynağından geldiyse (idea-generator IDEAS[x].kaynak == "AUDIENCE_VOICE"):
→ F sütununa "Fikir (İzleyici Talebi)" yaz
→ Normal "Fikir" değil — fark önemli

```python
# Yeni satır ekleme
values = [[
    "VID-002", "Tutorial", "#f0eee9",
    "AI Agent Sistemleri — Veri Biliminde Kullanım",
    "2026-05-14", "Planlandı",
    "=HYPERLINK(\"#'YouTube Analytics'!A\"&MATCH(A2,'YouTube Analytics'!A:A,0),A2)",
    "", "", ""
]]
```

---

### Operasyon 2 — Analytics Sheet Güncelle

Ne zaman: content-indexer analitik veri çekince
Mantık:
- Sheet 2'yi oku — mevcut VID key'leri al
- VID key mevcut değilse → yeni satır ekle
- Mevcutsa → tüm metrik sütunlarını güncelle (A hariç)

Güncellenen alanlar (her /youtube'da):
```
F: İzlenme
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
Q: Son Güncelleme -> bugünün tarihi
```

---

### Operasyon 3 — Viral Patterns Sheet Güncelle

Ne zaman: fetch-viral-videos yeni viral video analiz edince
Mantık:
- Sheet 3'ü oku — mevcut VPT key'leri al
- VPT key mevcut mu kontrol et
- Mevcut değilse → yeni satır ekle
- Mevcutsa → atla (viral video verisi değişmez)

```python
# Yeni satır formatı
["VPT-001", "https://...", "Kanal Adı", "Video Başlığı",
 150000, "2026-04-15", "İddia", "Formül 1",
 "Yüz var, yüksek kontrast", "Güçlü iddia hook",
 "Evet", "2026-05-09"]
```

---

### Operasyon 4 — İzleyici Sesi Sheet Güncelle (YENİ)

Ne zaman: Her /youtube'da AUDIENCE_VOICE verisi varsa

Mantık:
1. Sheet 4'ü oku — mevcut yorum özetlerini al (D sütunu)
2. Yeni gelen AUDIENCE_VOICE yorumlarını karşılaştır
3. Yeni yorum varsa → yeni satır ekle
4. Mevcut yorumun "Video Önerildi?" durumu değiştiyse → G ve H sütununu güncelle

```python
# Yeni satır formatı
["2026-05-13", "VID-001", "Istek_Konu",
 "CrewAI hakkında da video yapar mısın?",
 7, "araç/CrewAI", "Bekliyor", "", ""]

# Video yapıldıysa güncelleme:
# G sütunu: "Bekliyor" -> "Planlandı" veya "Evet"
# H sütunu: "" -> "VID-005"
```

**Frekans Takibi:**
Aynı tema birden fazla yorumda geçiyorsa tek satır tut, Notlar sütununa
"Frekans: X" yaz. Yeni satır açma.

---

## BAĞLANTI FORMÜLLERI

### Sheet 1 → Sheet 2 (G sütunu)
```
=HYPERLINK("#'YouTube Analytics'!A"&MATCH(A2,'YouTube Analytics'!A:A,0),A2)
```
VID-001'e tıklayınca direkt Analytics sheet'inde o satıra gider.

### Sheet 2 → Sheet 1 (B sütunu)
```
=HYPERLINK("#'Icerik Takvimi'!A"&MATCH(A2,'Icerik Takvimi'!A:A,0),A2)
```
Analytics'ten takvime tek tıkla geçiş.

---

## HATA YÖNETİMİ

**Sheets ID bulunamıyor:**
→ ".env dosyasında GOOGLE_SHEETS_ID eksik" yaz
→ Dur

**403 Forbidden:**
→ "Sheets erişim izni yok, OAuth scope kontrol et" yaz
→ Dur

**Sekme mevcut değil ("Izleyici Sesi" veya başka tab):**
→ "Tab bulunamadı — python scripts/setup_sheets.py çalıştır" yaz
→ Dur, sekme oluşturulmadan yazma

**Duplicate VID key:**
→ Yeni satır ekleme, mevcut satırı güncelle
→ "VID-XXX güncellendi" yaz

**Boş veri:**
→ Boş hücre bırak, null yazma
→ Devam et

**Quota / Yazma hatası:**
→ Terminale hata logunu bas
→ "Sheets yazma başarısız — knowledge/outputs/rapor/ yerel raporu geçerli" yaz
→ Zinciri durdurma, knowledge/ yazma devam eder

---

## SINIRLAR

- Başlık satırını (1. satır) asla değiştirme
- VID key ve VPT key'i asla değiştirme — primary key
- Formül sütunlarını (G ve B) üzerine yazma
- Sheets dışına veri gönderme
- Yorum sahibinin adını D sütununa yazma — gizlilik

---

**END write-sheets**
