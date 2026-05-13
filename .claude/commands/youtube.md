# COMMAND: /youtube
# Haftalık rutin analiz ve planlama komutu

AxonodeAI YouTube kanalı için tam analiz ve içerik üretim komutu.
Bu komut çalıştırılınca 4 ajan sırayla devreye girer.
Her ajan bir öncekinin çıktısını girdi olarak kullanır.

---

## BAŞLAMADAN ÖNCE

Şunları oku:
1. CLAUDE.md → genel kurallar ve mevcut durum
2. youtube-state-layer.md → son video, verilen söz, blocked moves
3. youtube-strategy.md → içerik tipi kuralları

Okumadan ajan çalıştırma.

---

## AKIŞ
1.  **Ajan 1 (content-indexer)**: Veri topla (API veya Snapshot).
2.  **Ajan 2 (pattern-finder)**: Pattern ve Gap analizi yap.
3.  **Ajan 3 (idea-generator)**: 3 yeni video fikri üret.
4.  **Ajan 4 (seo-optimizer)**: SEO paketlerini hazırla.

---

## AJAN 1 — content-indexer

agents/content-indexer.md dosyasını oku ve çalıştır.

Görev:
- YouTube Analytics API ile kendi kanalının verilerini çek
- Özellikle son yayınlanan videoların detaylı analitiğini al
- Belirlenen viral videoları analiz et
- Ham veriyi bir sonraki ajana aktar

Çıktı:
CONTENT_INDEX = {
own_videos: [...],
viral_videos: [...]
}

Başarılı olunca: "✓ content-indexer tamamlandı" yaz ve devam et.
Başarısız olunca: dur, hata mesajını yaz, devam etme.

---

## AJAN 2 — pattern-finder

agents/pattern-finder.md dosyasını oku ve çalıştır.
Girdi: CONTENT_INDEX

Görev:
- Kendi videolarının performans pattern'lerini bul
- Viral videoların ortak özelliklerini çıkar
- İki şeridi karşılaştır: "Viral videolarda var, bende yok"
- knowledge/viral-mechanism-library.md güncelle

Çıktı:
PATTERNS = {
own_performance: {...},
viral_patterns: {...},
gaps: [...],
opportunities: [...]
}

Başarılı olunca: "✓ pattern-finder tamamlandı" yaz ve devam et.
Başarısız olunca: dur, hata mesajını yaz, devam etme.

---

## AJAN 3 — idea-generator

agents/idea-generator.md dosyasını oku ve çalıştır.
Girdi: PATTERNS

Görev:
- youtube-state-layer.md'deki "Verilen Söz" bölümünü kontrol et
- Verilen söz varsa ilk fikir MUTLAKA o olsun
- youtube-strategy.md içerik denge kurallarını uygula
- PATTERNS'taki fırsatlarla örtüşen 3 video fikri üret
- Her fikir için tip, tahmini performans gerekçesi yaz

Çıktı:
IDEAS = [
{
sira: 1,
tip: "Tutorial",
konu: "...",
neden: "...",
tahmini_performans: "..."
},
...
]

Başarılı olunca: "✓ idea-generator tamamlandı" yaz ve devam et.
Başarısız olunca: dur, hata mesajını yaz, devam etme.

---

## AJAN 4 — seo-optimizer

agents/seo-optimizer.md dosyasını oku ve çalıştır.
Girdi: IDEAS

Görev:
- youtube-seo-system.md kurallarını uygula
- Her fikir için eksiksiz SEO paketi hazırla
- Başlık 60 karakter kontrolü yap
- Thumbnail renk kuralını uygula (state layer'dan son rengi al)

Çıktı: Her fikir için tam SEO paketi

Başarılı olunca: "✓ seo-optimizer tamamlandı" yaz ve devam et.
Başarısız olunca: dur, hata mesajını yaz, devam etme.

---

## FINAL ADIM — Yaz ve Raporla

---

## ÇIKTI VE KAYIT SÜRECİ
Tüm ajanlar işini bitirdiğinde:

1.  **Terminal**: Raporu özet olarak ekrana yaz.
2.  **Skill (write-knowledge)**: 
    *   Final raporunu şu konuma kaydet: `knowledge/outputs/rapor/YYYY-MM-DD-youtube-rapor.md`.
    *   `knowledge/analytics-snapshot.md` dosyasını üzerine yazarak güncelle.
    *   knowledge/audience-voice.md → AUDIENCE_VOICE varsa güncelle (Bölüm A + B)
3.  **Skill (write-sheets)**: Oneriler ve Icerik Takvimi sekmelerini güncelle.

---

### 1. Google Sheets Güncelle
skills/write-sheets.md'yi çalıştır:
- İçerik Takvimi sheet'i → yeni video fikirleri ekle
- YouTube Analytics sheet'i → son video verilerini güncelle
- Viral Patterns sheet'i → yeni pattern'ler ekle

### 2. Knowledge Klasörünü Güncelle
skills/write-knowledge.md'yi çalıştır:
- knowledge/analytics-snapshot.md → güncelle
- knowledge/content-calendar.md → güncelle
- knowledge/viral-mechanism-library.md → yeni pattern varsa ekle
- knowledge/my-videos/ → analiz edilen videolar için VID-XXX.md güncelle

### 3. State Layer Güncelle
youtube-state-layer.md'yi güncelle:
- Verilen söz yerine getirildiyse temizle
- Yeni verilen söz varsa ekle
- Blocked moves güncelle
- Last Updated tarihi güncelle

---

## TERMİNAL RAPORU

Tüm adımlar tamamlanınca şu formatta yaz:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AXONODEAI /youtube — [TARİH]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ content-indexer   tamamlandı
✓ pattern-finder    tamamlandı
✓ idea-generator    tamamlandı
✓ seo-optimizer     tamamlandı
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SON VİDEO ANALİTİĞİ (VID-001)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
İzlenme:           [X]
CTR:               [X]%
Retention:         [X]%
Yorum:             [X]
Abone artışı:      [X]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ÖNERİLEN SONRAKI 3 VİDEO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[TİP] — [BAŞLIK]
Neden: [1 cümle]
Başlık: [SEO başlık]
Thumbnail: [renk + metin]
Taglar: [liste]
[TİP] — [BAŞLIK]
...
[TİP] — [BAŞLIK]
...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
YENİ VIRAL PATTERN'LER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Bu haftaki analiz sonuçları]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GÜNCELLENEN DOSYALAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ knowledge/analytics-snapshot.md
✓ knowledge/content-calendar.md
✓ knowledge/viral-mechanism-library.md
✓ youtube-state-layer.md
✓ Google Sheets: İçerik Takvimi
✓ Google Sheets: YouTube Analytics
✓ Google Sheets: Viral Patterns
✓ knowledge/audience-voice.md
✓ Google Sheets: İzleyici Sesi
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

---
### 4. Raporu Kaydet

Terminal çıktısının tamamını şuraya kaydet:
knowledge/outputs/rapor/YYYY-MM-DD-youtube-rapor.md

Format:
```markdown
# /youtube Raporu — [TARİH]

## ANALİTİK
[analytics özeti]

## VID-XXX SEO PAKETİ
[başlık, açıklama, taglar, thumbnail, hook]

## VID-XXX SEO PAKETİ
[...]

## VİRAL PATTERN'LER
[yeni pattern'ler]
```

Bu dosya kalıcı kayıt — silinmez, her çalışmada yeni dosya oluşturulur.

## HATA YÖNETİMİ
- Herhangi bir adımda API hatası alınırsa `knowledge/analytics-snapshot.md` üzerinden devam et.
- Rapor kaydedilirken `outputs/rapor/` klasörünün varlığını kontrol et, yoksa oluştur. 

**END /youtube KOMUTU**