# AxonodeAI YouTube Brain

Claude Code ile çalışan YouTube kanal yönetim sistemi.
`/youtube` komutu ile 4 ajan sırayla devreye girer —
analitik toplar, viral pattern bulur, video fikri üretir,
SEO paketi hazırlar, Google Sheets'e yazar.

---

## Hızlı Başlangıç

```bash
cd ~/GitHub/axonodeai-youtube
claude
/youtube
```

Sheets güncellemek için:
```bash
python scripts/sync_sheets.py
```

---

## Sistem Mimarisi
/youtube komutu
│
▼
AJAN 1: content-indexer
│ YouTube Analytics API + viral web araması
▼
AJAN 2: pattern-finder
│ Kendi video + viral karşılaştırma
▼
AJAN 3: idea-generator
│ Strateji kuralları + verilen söz
▼
AJAN 4: seo-optimizer
│ Başlık + açıklama + tag + thumbnail + hook
▼
ÇIKTILAR
├── Terminal raporu
├── knowledge/ klasörü güncelleme
└── Google Sheets güncelleme

---

## Dosya Haritası

### Komut

| Dosya | Ne İçeriyor |
|-------|-------------|
| `.claude/commands/youtube.md` | `/youtube` komutunun tam tanımı. 4 ajanı sırayla çalıştırır, her ajanın girdisi ve çıktısını tanımlar, final rapor formatını belirler. |

---

### Ajanlar

#### `agents/content-indexer.md` — Ajan 1
**Görevi:** Veri toplar, analiz yapmaz.

**Kullandığı dosyalar:**
- `skills/fetch-analytics.md` — YouTube Analytics API çağrıları
- `skills/fetch-viral-videos.md` — Viral video araması

**İki şerit çalışır:**
- Şerit A: Kendi kanalının Analytics verisi
  (izlenme, CTR, retention, trafik kaynağı, abone artışı)
- Şerit B: Nişte viral olan videoların analizi
  (başlık formülü, hook tipi, thumbnail yapısı)

**Çıktı:** `CONTENT_INDEX` objesi → pattern-finder'a geçer

---

#### `agents/pattern-finder.md` — Ajan 2
**Görevi:** İki şeridi karşılaştırır, pattern çıkarır.

**Kullandığı dosyalar:**
- `knowledge/viral-mechanism-library.md` — önceki pattern'ler
- `youtube-state-layer.md` — mevcut kanal durumu
- CONTENT_INDEX (Ajan 1 çıktısı)

**Yaptıkları:**
- CTR analizi: ortalama üstü/altı videoları tespit eder
- Retention analizi: düşüş noktalarını bulur
- Trafik analizi: öneri vs arama dağılımı
- Gap analizi: "Viral'de var, bende yok"
- `knowledge/viral-mechanism-library.md`'yi günceller

**Çıktı:** `PATTERNS` objesi → idea-generator'a geçer

---

#### `agents/idea-generator.md` — Ajan 3
**Görevi:** Veriye dayalı video fikirleri üretir.

**Kullandığı dosyalar:**
- `youtube-strategy.md` — içerik tipi kuralları, hedef kitle
- `youtube-state-layer.md` — verilen söz, blocked moves, renk takibi
- `knowledge/content-calendar.md` — mevcut takvim
- `knowledge/viral-mechanism-library.md` — uygulanabilir pattern'ler
- PATTERNS (Ajan 2 çıktısı)

**Kontroller (sırayla):**
1. Verilen söz var mı? → varsa ilk fikir o olmalı
2. İçerik denge kuralı → aynı tip arka arkaya gelmez
3. Thumbnail renk kuralı → aynı renk tekrar etmez
4. Mevcut planlanmış video sayısı → 3'ten azsa yeni üret
5. Viral pattern uyumu → her fikre en az 1 pattern ekle

**Çıktı:** `IDEAS` listesi → seo-optimizer'a geçer

---

#### `agents/seo-optimizer.md` — Ajan 4
**Görevi:** Her fikir için direkt kullanıma hazır SEO paketi üretir.

**Kullandığı dosyalar:**
- `youtube-seo-system.md` — başlık formülleri, tag sistemi, açıklama şablonu
- `youtube-state-layer.md` — thumbnail renk takibi
- `knowledge/viral-mechanism-library.md` — hook formülleri
- IDEAS (Ajan 3 çıktısı)

**Her fikir için ürettiği paket:**
BAŞLIK
Ana başlık (max 60 karakter — kontrol edilir)
Alternatif 1
Alternatif 2
AÇIKLAMA
İlk 2 satır (anahtar kelime + hook)
İçindekiler (zaman kodları)
Bu videoda öğrenecekler
Kaynaklar
AxonodeAI hakkında
Hashtagler
TAGLAR
10 sabit tag + 5 değişken tag = 15 tag
THUMBNAIL
Arka plan rengi (hex)
Metin rengi (hex)
Thumbnail metni (max 4 kelime)
Yüz ifadesi
Başlıkla birlikte mesaj
HOOK TASLAGI
0-30 saniye konuşma metni
Hook tipi (İddia/Soru/Şok/Hikaye/Vadi)
KONTROL LİSTESİ
Yayın öncesi 12 madde

---

### Skill Dosyaları

| Dosya | Ne Yapıyor | Kim Kullanıyor |
|-------|------------|----------------|
| `skills/fetch-analytics.md` | YouTube Data API v3 + Analytics API çağrılarını tanımlar. OAuth2 ile kanal istatistikleri, video detayları, retention, CTR, trafik kaynağı çeker. | content-indexer |
| `skills/fetch-viral-videos.md` | Nişte viral olan videoları bulur. Başlık, thumbnail, hook, yapı analizini çıkarır. YouTube Transcript API ile hook metni alır. | content-indexer |
| `skills/write-sheets.md` | Google Sheets'e yazma operasyonlarını tanımlar. 4 tab için şema ve yazma mantığı. | seo-optimizer (final adım) |
| `skills/write-knowledge.md` | `knowledge/` klasörüne yazma formatlarını tanımlar. VID-XXX.md, VPT-XXX.md, viral-mechanism-library.md şablonları. | pattern-finder, seo-optimizer |

---

### Sistem Dosyaları

Bu dosyalar ajanların kural seti — her çalışmada okunur.

| Dosya | Ne İçeriyor | Hangi Ajan Okur |
|-------|-------------|-----------------|
| `youtube-strategy.md` | Kanal kimliği, hedef kitle, içerik tipleri (Trend/Tutorial/Kariyer/Girişim/Vlog), haftalık yayın takvimi, büyüme stratejisi, içerik sıralama kuralları | idea-generator |
| `youtube-seo-system.md` | Başlık formülleri, açıklama şablonu, tag sistemi (sabit+değişken), thumbnail kuralları, algoritma kuralları, SEO kontrol listesi | seo-optimizer |
| `youtube-state-layer.md` | Dinamik durum dosyası. Son yayınlanan video, yayın takvimi, içerik denge takibi, thumbnail renk takibi, analitik snapshot, stratejik öneriler, blocked moves. Her /youtube sonrası güncellenir. | idea-generator, pattern-finder, seo-optimizer |
| `youtube-production-template.md` | Video üretim şablonu. Video kartı, konuşma metni şablonu (hook/giriş/bölümler/özet/CTA), görsel plan, b-roll listesi, kaynak listesi, grafik listesi, üretim kontrol listesi | idea-generator |
| `youtube-viral-mekanizma.md` | 12 video, 8.1M izlenme analizi. 6 kanıtlanmış hook tipi, 4 retention mekanizması, 3 CTA stratejisi, kaçınılacaklar, en iyi performans yapısı. | pattern-finder, idea-generator, seo-optimizer |
| `podcast-system.md` | Podcast marka kimliği, bölüm akışı, YouTube'dan podcast'e dönüştürme protokolü, show notes şablonu. Henüz aktif değil — 5-10 video sonrası başlatılacak. | — (şimdilik pasif) |

---

### Knowledge Klasörü

Sistemin kalıcı hafızası. Her `/youtube` çalışmasında güncellenir.

| Dosya/Klasör | Ne İçeriyor | Kim Yazar |
|--------------|-------------|-----------|
| `knowledge/my-videos/VID-XXX.md` | Her video için profil. SEO, analitik, performans notları, içerik yapısı, bağlantılar. Primary key: VID-001, VID-002... | write-knowledge skill |
| `knowledge/viral-patterns/VPT-XXX.md` | Her viral video için analiz. Başlık, thumbnail, hook, yapı analizi. AxonodeAI için uygulama notu. Primary key: VPT-001, VPT-002... | write-knowledge skill |
| `knowledge/viral-mechanism-library.md` | Temizlenmiş pattern kütüphanesi. Şu an 5 pattern. Her /youtube çalışmasında büyür. Birden fazla videoda doğrulanınca "Kanıtlanmış" olur. | pattern-finder |
| `knowledge/content-calendar.md` | Yayın takvimi tablosu. VID key, tip, başlık, tarih, durum. Google Sheets ile senkron. | idea-generator |
| `knowledge/analytics-snapshot.md` | Son analytics özeti. Kanal özeti, video performansları, alarmlar, trafik analizi. Her çalışmada üzerine yazılır. | content-indexer |
| `knowledge/outputs/` | Her /youtube çalışmasının tam raporu. YYYY-MM-DD-youtube-rapor.md formatında. Silinmez, arşiv olarak kalır. | seo-optimizer (final adım) |

---

### Python Scriptleri

Ajan dosyaları davranış kuralı tanımlar.
Gerçek API çağrıları bu scriptler tarafından yapılır.

| Script | Ne Yapıyor | Ne Zaman Çalıştırılır |
|--------|------------|----------------------|
| `scripts/sync_sheets.py` | Tüm videoların Analytics verisini çekip Sheets'e yazar. Retention, CTR, izlenme, beğeni, yorum, abone. | Her /youtube sonrası |
| `scripts/update_sheets_now.py` | Hızlı güncelleme. Sadece public video istatistiklerini yazar. | Günlük takip için |
| `scripts/fix_sheets.py` | Sheets'i sıfırdan kurar. Başlık satırları, renkler, conditional formatting, Oneriler tab. | Sheets bozulunca |
| `scripts/test_api.py` | OAuth token, YouTube Data API, Analytics API bağlantısını test eder. | Sorun giderme |
| `scripts/setup_sheets.py` | İlk kurulum scripti. Tab oluşturur, başlık satırlarını yazar. | Sadece ilk kurulumda |
| `scripts/get_token.py` | OAuth2 refresh token alır. Tarayıcı açar, izin alır, token'ı yazdırır. | Sadece ilk kurulumda |

---

### Google Sheets Yapısı

**Dosya:** AxonodeAI YouTube Brain
**Primary Key:** VID-XXX (her yerde aynı)

| Tab | Sütunlar | Renk Sistemi |
|-----|----------|--------------|
| Icerik Takvimi | VID Key, Video Tipi, Renk Kodu, Başlık, YouTube URL, Yayın Tarihi, Durum, Analytics Link, IG Post, IG Haftası, Notlar | Durum: yeşil/turuncu/lila. Tip: mor/mavi/pembe/sarı-yeşil |
| YouTube Analytics | VID Key, Takvim Link, Başlık, Yayın Tarihi, Tip, İzlenme, Benzersiz İzleyici, Retention, CTR, İzlenme Dk, Öneri %, Arama %, Beğeni, Yorum, Abone+/-, Son Güncelleme | CTR <2% kırmızı, >5% yeşil. Retention <30% kırmızı |
| Viral Patterns | VPT Key, URL, Kanal, Başlık, İzlenme, Tarih, Hook Tipi, Başlık Formülü, Thumbnail, En Güçlü Özellik, Kullanılabilir mi, Analiz Tarihi | — |
| Oneriler | Her /youtube çalışmasının SEO paketleri. VID-XXX için başlık alternatifleri, thumbnail brief, hook taslağı, taglar, viral pattern notları | Başlık satırı #414ecf |

**Çapraz navigasyon:**
- Icerik Takvimi G sütunu → ilgili Analytics satırına tek tıkla gider
- YouTube Analytics B sütunu → ilgili Takvim satırına tek tıkla gider

---

## API Kurulumu

### Gerekli API'ler
Google Cloud Console → axonodeai projesi

YouTube Data API v3      ✅ aktif
YouTube Analytics API    ✅ aktif
Google Sheets API        ✅ aktif

### OAuth2 Scopes
https://www.googleapis.com/auth/youtube.readonly
https://www.googleapis.com/auth/yt-analytics.readonly
https://www.googleapis.com/auth/spreadsheets

### .env Dosyası
YOUTUBE_REFRESH_TOKEN=
YOUTUBE_CLIENT_ID=
YOUTUBE_CLIENT_SECRET=
YOUTUBE_CHANNEL_ID=
GOOGLE_SHEETS_ID=

### İlk Kurulum (bir kere yapılır)
```bash
pip install google-auth-oauthlib google-api-python-client python-dotenv
python scripts/get_token.py    # tarayıcı açılır, izin ver
# token'ları .env'e yapıştır
python scripts/setup_sheets.py # Sheets tablarını kur
python scripts/test_api.py     # her şeyin çalıştığını doğrula
```

---

## Haftalık Rutin

```bash
# Salı sabahı — video yayınlamadan önce
cd ~/GitHub/axonodeai-youtube
claude
/youtube

# Sheets güncelle
python scripts/sync_sheets.py

# Video yayınla
# Sheets'te durumu güncelle: Fikir → Planlandı → Çekimde → Post → Yayında

# 7 gün sonra — gerçek analitik için
python scripts/sync_sheets.py
```

---

## Mevcut Durum
Kanal:    Sema - Axonode AI
Abone:    22
Video:    1 (VID-001 yayında)
VID-001:  Python Öğrenmek Yetmiyor — 2026
199 izlenme | 18 beğeni | 13 yorum
Retention: %20.3 | Öneri: %27.6
VID-002:  AI Agent Sistemleri — 14 Mayıs
VID-003:  Sağlıktan Veri Bilimine — 21 Mayıs
VID-004:  %57 Şirket AI Ajanı — 28 Mayıs

---

## Sonraki Adımlar
[ ] 15 Mayıs → sync_sheets.py çalıştır, CTR gelecek
[ ] VID-002 üretimi → 14 Mayıs hedefi
[ ] Podcast sistemi → 5-10 video sonrası aktif et
[ ] İngilizce kanal → 1000 abone sonrası
[ ] knowledge/outputs/ → rapor arşivi test et

---

**Repo:** github.com/semaybulut/axonodeai-youtube (private)
**Owner:** Sema | AxonodeAI
**Son Güncelleme:** 2026-05-10

