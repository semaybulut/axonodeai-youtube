# AxonodeAI YouTube Brain

Claude Code ile çalışan YouTube kanal yönetim sistemi.
5 komut, 4 ajan, 3 API, 1 Google Sheets — tam otomatik.

**Kanal:** Sema - Axonode AI
**Repo:** github.com/semaybulut/axonodeai-youtube (private)
**Son Güncelleme:** 2026-05-11

---

## Hızlı Başlangıç

```bash
cd ~/GitHub/axonodeai-youtube
claude
/youtube
```

Sheets güncelle:
```bash
python scripts/sync_sheets.py
```

---

## Komut Sistemi

5 komut mevcut. Hepsi `.claude/commands/` altında.

```
Haftalık rutin          → /youtube
Belirli konu araştır    → /youtube-konu "konu"
Script yaz              → /youtube-script VID-XXX
Seri planla             → /youtube-seri "seri" [sayı]
Video yayınlandı        → /youtube-publish VID-XXX
7 gün geçti             → /youtube-publish VID-XXX --update
```

---

### `/youtube` — Ana Komut

Her Salı video yayınlamadan önce çalıştır.
4 ajan sırayla devreye girer:

```
AJAN 1: content-indexer
→ YouTube Analytics API ile kendi kanal verisi
→ Web aramasıyla viral video analizi
→ İki şeridi CONTENT_INDEX'e toplar

AJAN 2: pattern-finder
→ Kendi video + viral karşılaştırma
→ CTR, retention, trafik analizi
→ Gap analizi: "Viral'de var, bende yok"
→ viral-mechanism-library.md günceller

AJAN 3: idea-generator
→ Verilen söz kontrolü (zorunlu — bozulmaz)
→ İçerik denge + renk kuralları
→ 3 video fikri üretir

AJAN 4: seo-optimizer
→ Her fikir için tam SEO paketi:
   Başlık (60 karakter kuralı)
   Açıklama şablonu
   15 tag
   Thumbnail brief
   Hook taslağı (0-30 sn)
   Kontrol listesi
```

---

### `/youtube-konu "konu"` — Araştırma + SEO

Belirli bir konu için iki katmanlı araştırma yapar:

```
Katman 1 — Web araştırması
→ Güncel raporlar, istatistikler, kaynaklar
→ Hook için çarpıcı veri

Katman 2 — Viral video araştırması
→ Bu konuda viral olan YouTube videoları
→ Hangi başlık, hook, thumbnail çalışmış

Çıktı:
→ Tam SEO paketi
→ knowledge/my-videos/VID-XXX.md oluşturulur
→ State layer güncellenir
→ Sheets güncellenir
```

Konu belirtilmezse sorar. Konu gelmezse takvimden önerir.

---

### `/youtube-script VID-XXX` — Konuşma Metni

SEO paketi hazır video için tam script üretir:

```
Hook → Giriş → Bölümler → Özet → CTA
+ Görsel plan tablosu
+ B-roll listesi
+ Üretim kontrol listesi (30 madde)

Hook tipi karar matrisi:
  Tutorial       → Vadi Hook
  Trend Analizi  → Şok/Veri Hook
  Kariyer/POV    → Hikaye/İtiraf Hook
  Girişim/Para   → Somut Sayı Hook
```

VID key belirtilmezse bir sonraki planlanmış videoyu önerir.

---

### `/youtube-seri "seri" [sayı]` — Seri Planlama

```
Sayı belirtilirse → direkt o kadar video üretir
Sayı belirtilmezse → ajan önerir, onay bekler

Her video için:
→ SEO paketi
→ Tam konuşma metni
→ Seri bağlantıları (önceki/sonraki video)

Çıktı:
→ knowledge/my-videos/VID-XXX.md (her video)
→ knowledge/seriler/[seri-slug].md (özet)
→ content-calendar.md güncellenir
→ state-layer.md güncellenir
→ Sheets güncellenir
```

---

### `/youtube-publish VID-XXX` — Yayın Kaydı

Video yayınlandığında çalıştır. Sistemin öğrenme mekanizması:

```
Gerçek analitikleri çeker (API)
Performans bağlantısını kurar:
  Başlık formülü → CTR
  Hook tipi      → Retention
  İçerik tipi   → Abone artışı

Günceller:
→ knowledge/my-videos/VID-XXX.md
→ knowledge/viral-mechanism-library.md
→ knowledge/analytics-snapshot.md
→ youtube-state-layer.md
→ Google Sheets

--update flag ile (7 gün sonra):
→ Tam analitik verisini çeker
→ Pattern'leri doğrular veya çürütür
→ Kanal ortalamalarını günceller
```

3+ video birikince ajan şunu yapabilir:
"Soru formülü başlık geçmişte ort. %4.1 CTR getirdi,
İddia formülü %2.8. Bu video için Soru formülü öneriyorum."

---

## Dosya Haritası

```
axonodeai-youtube/
│
├── CLAUDE.md                        ← Ajanın beyin dosyası
├── .env                             ← API credentials (git'e gitmiyor)
│
├── .claude/commands/
│   ├── youtube.md                   ← /youtube
│   ├── youtube-konu.md              ← /youtube-konu
│   ├── youtube-script.md            ← /youtube-script
│   ├── youtube-seri.md              ← /youtube-seri
│   └── youtube-publish.md           ← /youtube-publish
│
├── agents/
│   ├── content-indexer.md           ← Ajan 1: Veri topla
│   ├── pattern-finder.md            ← Ajan 2: Pattern bul
│   ├── idea-generator.md            ← Ajan 3: Fikir üret
│   └── seo-optimizer.md             ← Ajan 4: SEO hazırla
│
├── skills/
│   ├── fetch-analytics.md           ← YouTube Analytics API
│   ├── fetch-viral-videos.md        ← Viral video analizi
│   ├── write-sheets.md              ← Google Sheets'e yaz
│   └── write-knowledge.md           ← knowledge/ klasörüne yaz
│
├── [sistem dosyaları]
│   ├── youtube-strategy.md          ← Kanal stratejisi
│   ├── youtube-seo-system.md        ← SEO kuralları
│   ├── youtube-state-layer.md       ← Dinamik durum (her çalışmada güncellenir)
│   ├── youtube-production-template.md ← Video üretim şablonu
│   ├── youtube-viral-mekanizma.md   ← 12 video, 8.1M izlenme analizi
│   └── podcast-system.md            ← İleride aktif edilecek
│
├── knowledge/
│   ├── my-videos/VID-XXX.md         ← Her video profili + script + performans
│   ├── viral-patterns/VPT-XXX.md   ← Viral video analizleri
│   ├── seriler/[seri-slug].md       ← Seri özet dosyaları
│   ├── viral-mechanism-library.md   ← Kanıtlanmış pattern kütüphanesi
│   ├── content-calendar.md          ← Yayın takvimi
│   ├── analytics-snapshot.md        ← Son analitik özeti
│   └── outputs/                     ← /youtube rapor arşivi
│
└── scripts/
    ├── sync_sheets.py               ← Sheets güncelle (her /youtube sonrası)
    ├── update_sheets_now.py         ← Hızlı güncelleme
    ├── fix_sheets.py                ← Sheets sıfırdan kur
    ├── test_api.py                  ← API bağlantı testi
    ├── setup_sheets.py              ← İlk kurulum
    └── get_token.py                 ← OAuth token al
```

---

## Sistem Dosyaları — Ne İşe Yarar

| Dosya | Ne İçeriyor | Hangi Komut/Ajan Okur |
|-------|-------------|----------------------|
| `youtube-strategy.md` | Kanal kimliği, hedef kitle, içerik tipleri, yayın takvimi, büyüme stratejisi | idea-generator, /youtube-konu, /youtube-seri |
| `youtube-seo-system.md` | Başlık formülleri, açıklama şablonu, tag sistemi, thumbnail kuralları | seo-optimizer, /youtube-konu |
| `youtube-state-layer.md` | Son video, yayın takvimi, içerik dengesi, renk takibi, verilen söz, blocked moves. Her çalışmada güncellenir. | Tüm ajanlar + tüm komutlar |
| `youtube-production-template.md` | Video kartı, konuşma şablonu, görsel plan, b-roll, üretim kontrol listesi | /youtube-script, idea-generator |
| `youtube-viral-mekanizma.md` | 12 video 8.1M izlenme analizi. 6 hook tipi, 4 retention mekanizması, 3 CTA stratejisi | pattern-finder, idea-generator, seo-optimizer, /youtube-script |
| `podcast-system.md` | Podcast marka kimliği, bölüm akışı, show notes şablonu. 5-10 video sonrası aktif. | Şimdilik pasif |

---

## Knowledge Klasörü — Sistemin Hafızası

| Dosya/Klasör | Ne İçeriyor | Kim Yazar |
|--------------|-------------|-----------|
| `my-videos/VID-XXX.md` | Video profili: SEO paketi, script, performans bağlantısı, analitik | write-knowledge, /youtube-script, /youtube-publish |
| `viral-patterns/VPT-XXX.md` | Viral video analizleri: başlık, thumbnail, hook, yapı | write-knowledge |
| `seriler/[slug].md` | Seri özeti: video listesi, performans, durum | /youtube-seri |
| `viral-mechanism-library.md` | Pattern kütüphanesi. 5 pattern şu an. Her çalışmada büyür. 2+ videoda kanıtlanınca "Kanıtlanmış" olur. | pattern-finder, /youtube-publish |
| `content-calendar.md` | Yayın takvimi. Sheets ile senkron. | idea-generator, /youtube-konu, /youtube-seri |
| `analytics-snapshot.md` | Kanal özeti, video performansları, alarmlar, ortalamalar. Her çalışmada üzerine yazılır. | content-indexer, /youtube-publish |
| `outputs/` | /youtube rapor arşivi. YYYY-MM-DD-youtube-rapor.md. Silinmez. | seo-optimizer |

---

## Google Sheets

**Dosya:** AxonodeAI YouTube Brain
**Primary Key:** VID-XXX ve VPT-XXX (her yerde aynı)

| Tab | İçerik | Renk Sistemi |
|-----|--------|--------------|
| Icerik Takvimi | VID Key, Tip, Renk, Başlık, YouTube URL, Tarih, Durum, Analytics Link, IG Post, IG Haftası, Notlar | Durum: yeşil/turuncu/lila. Tip: mor/mavi/pembe/sarı-yeşil |
| YouTube Analytics | VID Key, Takvim Link, Başlık, Tarih, Tip, İzlenme, Retention, CTR, İzlenme Dk, Öneri %, Arama %, Beğeni, Yorum, Abone+/-, Güncelleme | CTR <2% kırmızı, >5% yeşil |
| Viral Patterns | VPT Key, URL, Kanal, Başlık, İzlenme, Tarih, Hook, Formül, Thumbnail, En Güçlü, Kullanılabilir, Tarih | — |
| Oneriler | /youtube çalışmalarının SEO paketleri + performans bağlantısı tablosu | Başlık #414ecf |

Çapraz navigasyon: Takvim G sütunu ↔ Analytics B sütunu (tek tıkla geçiş)

---

## API Durumu

```
YouTube Data API v3:   ✅ kurulu
YouTube Analytics API: ✅ kurulu
Google Sheets API:     ✅ kurulu
OAuth2 credentials:    ✅ .env'de
```

### .env Formatı
```
YOUTUBE_REFRESH_TOKEN=
YOUTUBE_CLIENT_ID=
YOUTUBE_CLIENT_SECRET=
YOUTUBE_CHANNEL_ID=
GOOGLE_SHEETS_ID=
```

### İlk Kurulum (bir kere yapılır)
```bash
pip install google-auth-oauthlib google-api-python-client python-dotenv
python scripts/get_token.py       # tarayıcı açılır, izin ver
# token'ları .env'e yapıştır
python scripts/setup_sheets.py    # Sheets tablarını kur
python scripts/test_api.py        # her şeyin çalıştığını doğrula
```

---

## Haftalık Rutin

```bash
# Salı sabahı — video yayınlamadan önce
cd ~/GitHub/axonodeai-youtube
claude
/youtube
python scripts/sync_sheets.py

# Video yayınla
# Sheets'te durumu güncelle: Fikir → Planlandı → Çekimde → Post → Yayında

# Video yayınlanınca
/youtube-publish VID-XXX

# 7 gün sonra
/youtube-publish VID-XXX --update
python scripts/sync_sheets.py
```

---

## Mevcut Durum

```
Kanal:    Sema - Axonode AI
Abone:    22
Video:    1 (VID-001 yayında)

VID-001 — Python Öğrenmek Yetmiyor — 2026
  199 izlenme | 18 beğeni | 13 yorum
  Retention: %20.3 | Öneri trafiği: %27.6
  Durum: Analitik birikme devam ediyor

VID-002 — AI Agent Sistemleri          → 14 Mayıs | SEO Hazır
VID-003 — Sağlıktan Veri Bilimine      → 21 Mayıs | SEO Hazır
VID-004 — %57 Şirket AI Ajanı          → 28 Mayıs | SEO Hazır

Viral Pattern Kütüphanesi: 5 pattern
```

---

## Sonraki Adımlar

```
[ ] 15 Mayıs → sync_sheets.py çalıştır, CTR gelecek
[ ] VID-001 → /youtube-publish VID-001 --update (7 gün geçince)
[ ] VID-002 üretimi → /youtube-script VID-002
[ ] Repo public yap → Claude.ai'a direkt bağla
[ ] Podcast sistemi → 5-10 video sonrası aktif et
[ ] İngilizce kanal → 1000 abone sonrası
```
