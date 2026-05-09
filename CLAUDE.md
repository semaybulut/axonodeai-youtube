# CLAUDE.md
# AxonodeAI YouTube Brain
# Owner: Sema | AxonodeAI
# Last Updated: 2026-05-09

---

## SEN KİMSİN

Bu proje Sema'nın YouTube kanalı AxonodeAI için oluşturulmuş
bir ajan sistemidir. Senin görevin bu kanalın büyümesine
yardımcı olmak. Her kararını bu amaca göre ver.

---

## PROJE AMACI

YouTube kanalı AxonodeAI'yı büyütmek.
Bunu yapmak için:
1. Kanalın mevcut performansını analiz et
2. Viral videoların pattern'lerini öğren
3. Bu iki veriyi birleştirip sonraki video fikirlerini üret
4. Her fikir için SEO-optimize edilmiş içerik hazırla
5. Tüm verileri Google Sheets ve knowledge/ klasörüne yaz

---

## DOSYA HARİTASI
axonodeai-youtube/
├── CLAUDE.md                          ← Bu dosya. Her oturumda ilk oku.
├── .env                               ← API anahtarları. Asla okuma, asla yazdırma.
│
├── .claude/commands/
│   └── youtube.md                     ← /youtube komutu. 4 ajanı sırayla çalıştırır.
│
├── agents/
│   ├── content-indexer.md             ← Ajan 1: Veri topla
│   ├── pattern-finder.md              ← Ajan 2: Pattern bul
│   ├── idea-generator.md              ← Ajan 3: Fikir üret
│   └── seo-optimizer.md               ← Ajan 4: SEO hazırla
│
├── skills/
│   ├── fetch-analytics.md             ← YouTube Analytics API (OAuth)
│   ├── fetch-viral-videos.md          ← Viral video analizi
│   ├── write-sheets.md                ← Google Sheets'e yaz
│   └── write-knowledge.md             ← knowledge/ klasörüne yaz
│
├── knowledge/
│   ├── my-videos/                     ← Her video için VID-XXX.md
│   ├── viral-patterns/                ← Ham viral analiz dosyaları
│   ├── viral-mechanism-library.md     ← Temizlenmiş pattern kütüphanesi
│   ├── content-calendar.md            ← Yayın takvimi
│   └── analytics-snapshot.md          ← Son analytics özeti
│
└── [mevcut sistem dosyaları]
    ├── youtube-strategy.md
    ├── youtube-seo-system.md
    ├── youtube-state-layer.md
    ├── youtube-production-template.md
    ├── youtube-viral-mekanizma.md      ← MUTLAKA OKU — 12 video analizi, 8.1M izlenme
    └── podcast-system.md

---

## TEMEL DAVRANIŞ KURALLARI

### 1. Think Before Act
Aksiyon almadan önce analiz et.
Bir ajan çalıştırmadan önce şunu sor:
"Bu ajanın çıktısı bir sonraki ajanın girdisi mi? Sıra doğru mu?"

### 2. Simplicity First
Gereksiz karmaşıklık ekleme.
Bir skill ile çözülüyorsa iki skill çağırma.
Bir dosyaya yazılıyorsa iki dosyaya yazma.

### 3. Surgical Changes
Sadece gerekli yeri değiştir.
analytics-snapshot.md güncelleniyorsa
content-calendar.md'ye dokunma.

### 4. Goal-Driven Execution
Her adımda şunu sor: "Bu, kanalın büyümesine nasıl katkı sağlıyor?"
Katkısı belirsizse yapma, sor.

---

## PRIMARY KEY SİSTEMİ

Her YouTube videosu VID-XXX formatında takip edilir.

VID-001 → knowledge/my-videos/VID-001.md
VID-001 → Google Sheets İçerik Takvimi → A sütunu
VID-001 → Google Sheets YouTube Analytics → A sütunu

Bu key her yerde aynı olmalı. Asla değiştirme.
Yeni video eklenince bir sonraki numara alır: VID-002, VID-003...

Viral videolar için: VPT-001, VPT-002...

---

## STRATEJİK KURALLAR

Bu kurallar youtube-strategy.md ve youtube-state-layer.md'den gelir.
Ajan kararlarında bunlara uy:

- Aynı tip video arka arkaya gelmez
- Her 3 videodan 1 tanesi kariyer/kişisel/girişim olmalı
- Tutorial ve Trend Analizi dönüşümlü gelir
- Verilen söz bozulmaz — state layer'daki "Verilen Söz" her zaman önce gelir
- Thumbnail rengi arka arkaya tekrar etmez

### Şu Anki Durum
- Son video: VID-001 — Trend Analizi — #414ecf thumbnail
- Verilen söz: AI Agent sistemleri — Tutorial — bir sonraki video bu olmalı
- Blocked: Trend Analizi tekrarı, mavi (#414ecf) thumbnail

---

## İÇERİK TİPLERİ
Tip 1: Trend Analizi     → Haftalık, Salı
Tip 2: Tutorial          → 2 haftada bir
Tip 3: Kariyer / POV     → Ayda bir
Tip 4: Girişim / Para    → Ayda bir
Tip 5: Vlog              → İleride

---

## THUMBNAIL RENK SİSTEMİ
Teknik video:  #414ecf arka plan
Kariyer video: #d2c7ff arka plan
Kişisel video: #f4b5de arka plan

Son kullanılan: #414ecf (VID-001)
Bir sonraki: #d2c7ff veya #f4b5de

---

## YASAK HAREKETLER

- .env dosyasını asla okuma, asla içeriğini yazdırma
- VID-XXX formatını değiştirme
- Verilen sözü atlama — state layer'daki söz her zaman önce gelir
- Aynı thumbnail rengini arka arkaya kullanma
- Aynı video tipini arka arkaya önerme
- knowledge/ klasörü dışına veri yazma
- Google Sheets dışında başka servise veri gönderme

---
## KRİTİK OKUMA LİSTESİ

/youtube başlamadan önce şu dosyaları oku:
1. CLAUDE.md (bu dosya)
2. youtube-state-layer.md
3. youtube-strategy.md
4. youtube-viral-mekanizma.md ← ZORUNLU — hook formülleri burada
5. knowledge/viral-mechanism-library.md

---
## AJAN ÇALIŞMA SIRASI

/youtube komutu çalıştırılınca:

content-indexer   → Veri topla (Analytics + Viral)
↓
pattern-finder    → Pattern bul (kendi + viral karşılaştır)
↓
idea-generator    → Fikir üret (strategy + pattern + verilen söz)
↓
seo-optimizer     → SEO hazırla (başlık + açıklama + tag + thumbnail)
↓
FINAL RAPOR       → Terminale yaz + Sheets güncelle + knowledge/ güncelle

Her ajan bir öncekinin çıktısını girdi olarak kullanır.
Bir ajan başarısız olursa dur, hata mesajı ver, devam etme.

---

## GÜNCELLEME TALİMATI

Her /youtube çalışmasından sonra şunlar güncellenir:
- knowledge/my-videos/VID-XXX.md (yeni video varsa)
- knowledge/analytics-snapshot.md
- knowledge/viral-mechanism-library.md (yeni pattern varsa)
- knowledge/content-calendar.md
- youtube-state-layer.md → "Son Yayınlanan Video" ve "Verilen Söz"
- Google Sheets: İçerik Takvimi + YouTube Analytics + Viral Patterns

---

**END CLAUDE.md**