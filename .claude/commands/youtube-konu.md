# /youtube-konu
**Versiyon:** 2.0
**Owner:** Sema | AxonodeAI

**Kullanım:**
```
/youtube-konu "konu başlığı"
```

**Görevi:**
Verilen konu için iki katmanlı araştırma yap, senin strateji ve SEO
sistemine göre tam kullanıma hazır paket üret. Kaydet.

---

## BAŞLAMADAN ÖNCE

Şu dosyaları oku:
- `CLAUDE.md` — genel kurallar
- `youtube-state-layer.md` — mevcut durum, blocked moves, renk takibi
- `youtube-strategy.md` — içerik tipi kuralları
- `youtube-seo-system.md` — SEO kuralları
- `youtube-viral-mekanizma.md` — hook formülleri ve retention mekanizmaları ← ZORUNLU
- `knowledge/viral-mechanism-library.md` — kanıtlanmış pattern'ler

---

## ADIM 1 — KONU PARSE

Kullanıcının girdiği konuyu al.

Konu yoksa sor:
"Hangi konu hakkında içerik yapmak istiyorsun?"

Konu gelmezse:
→ `youtube-state-layer.md`'deki bir sonraki planlanmış videoyu öner:
"Takvimde sıradaki konu [X]. Onun için mi hazırlayayım?"

---

## ADIM 2 — KATMAN 1: WEB ARAŞTIRMASI

Claude Code web search ile şunları ara:

**Arama 1 — Güncel veri ve raporlar:**
```
[konu] araştırma raporu 2025 2026
[konu] istatistik veri
[konu] trend analiz
```

**Arama 2 — Türkçe içerik boşluğu:**
```
[konu] Türkçe YouTube
[konu] nedir Türkçe
```

**Çıkar:**
- En az 3 çarpıcı istatistik veya veri (hook için)
- En az 2 doğrulanmış kaynak (açıklama için)
- Türkçe içerik boşluğu var mı?
- Konunun güncelliği: 2025-2026 verisi var mı?

---

## ADIM 3 — KATMAN 2: VİRAL VİDEO ARAŞTIRMASI

`skills/fetch-viral-videos.md` skill'ini çalıştır.

Arama:
```
[konu] YouTube viral 2025 2026
[konu] İngilizce YouTube izlenme
[konu] site:youtube.com most viewed
[konu] Türkçe YouTube izlenme
```

En az 3 viral video bul. Her video için:
```
- Başlık: [tam başlık]
- Başlık formülü: [Formül 1/2/3/4/5]
- İzlenme: [sayı]
- Hook tipi: [İddia/Soru/Şok/Hikaye/Vadi]
- Hook yapısı (ilk 30 sn)
- Thumbnail yapısı: [yüz var mı, metin, renk]
- Tahmini retention: [yorum oranından tahmin]
```

**Sentez:**
- Bu konuda hangi hook tipi daha çok çalışmış?
- Hangi başlık formülü daha çok izlenme almış?
- Türkçe'de içerik boşluğu nerede?
- İngilizce içerik en fazla nerede izlenme almış?
- Benim için en uygulanabilir pattern hangisi?

---

## ADIM 4 — STRATEJİ KONTROLÜ

Kontrol et:
```
1. Bu konu hangi video tipine giriyor?
   (Trend Analizi / Tutorial / Kariyer / Girişim / Vlog)

2. İçerik denge kuralı ihlal ediliyor mu?
   → youtube-state-layer.md → İçerik Denge Takibi bak
   → Aynı tip arka arkaya gelmesin

3. Blocked moves'da bu tip var mı?
   → youtube-state-layer.md → BLOCKED MOVES bölümü

4. Verilen söz önce gelmeli mi?
   → youtube-state-layer.md → Verilen Söz bölümü
   → Varsa bu sözü hatırlat ve bu konudan önce verilen söz gelmeli
   → Verilen söz bölümünü öner ve sor "[X] konusunda VID-XXX videosunda verilen sözünüz var, bu konudan devam etmemi ister misin?"
   → "Hayır" seçerse "Verilen söz konusunu es geçip devam etmemi onaylıyor musun?"
   → onay alınca devam et

5. Thumbnail rengi ne olmalı?
   → youtube-state-layer.md → Thumbnail Renk Takibi
   → Son kullanılan rengi tekrarlama
```

Kural ihlali varsa:
→ Kullanıcıya bildir
→ Çözüm öner, devam etmeden onay al

---

## ADIM 5 — SEO PAKETİ ÜRET

`youtube-seo-system.md` kurallarını eksiksiz uygula.

### BAŞLIK
```
Ana:     [max 60 karakter] ([X]/60)
Alt 1:   [alternatif formül]
Alt 2:   [farklı açı]

Kullanılan formül: [Öneri Odaklı / Arama Odaklı]
Neden: [1 cümle gerekçe — araştırma verisine dayandır]
```

### AÇIKLAMA
```
[İlk satır — anahtar kelime + hook — "daha fazla göster"den önce]
[İkinci satır — içerik tek cümleyle özeti]


ICINDEKILER

0:00 Giris
[dakika:saniye] [bolum adi]
[dakika:saniye] [bolum adi]
[dakika:saniye] [bolum adi]
[dakika:saniye] Ozet ve Sonraki Video


BU VIDEODA OGRENECEKLER

- [madde 1]
- [madde 2]
- [madde 3]
- [madde 4]
- [madde 5]


KAYNAKLAR

[Araştırmadan bulunan kaynaklar — tarihli]
[URL]


AXONODEAI HAKKINDA

Veri bilimine gecis yapiyorum.
Bu kanalda veri bilimi araclari, yapay zeka trendleri,
kariyer gecisi ve sektordan haftalik icgorular.

Her hafta yeni video. Abone ol.
Instagram @axonodeai


#[hashtag1] #[hashtag2] #[hashtag3]
```

### TAGLAR
```
[10 sabit tag — youtube-seo-system.md'den]
[5 değişken tag — konuya özel]
Toplam: 15/15
```

### THUMBNAIL
```
Arka plan rengi: [hex] — neden bu renk (renk takibine göre)
Metin rengi:     [hex]
Thumbnail metni: [max 4 kelime]
Yüz ifadesi:     [Merak / Şaşkınlık / Ciddiyet]
Başlıkla mesaj:  [thumbnail + başlık birlikte ne söylüyor]
```

### ARAŞTIRMA NOTLARI
```
Çarpıcı veri 1: [istatistik] — Kaynak: [X]
Çarpıcı veri 2: [istatistik] — Kaynak: [X]
Çarpıcı veri 3: [istatistik] — Kaynak: [X]

Viral video analizi:
  [Video 1 başlık] — [izlenme] — Hook: [tip] — Formül: [X]
  [Video 2 başlık] — [izlenme] — Hook: [tip] — Formül: [X]
  [Video 3 başlık] — [izlenme] — Hook: [tip] — Formül: [X]

Önerilen hook tipi: [X]
Gerekçe: [araştırma verisine dayalı 1 cümle]
```

### HOOK TASLAGI (0-30 saniye)
```
Hook tipi: [X]

[Dikkat çekici açılış — araştırmadan en güçlü veriyi kullan]
[Neden izlemeli — izleyiciye ne kazandıracak]
[Video vadi — 1 net cümle]

Tahmini süre: [X saniye]
```

---

## ADIM 6 — KONTROL LİSTESİ

```
[ ] Başlık 60 karakterin altında
[ ] Başlıkta yıl veya güçlü iddia var
[ ] Açıklama ilk 2 satırı anahtar kelime içeriyor
[ ] Bölüm zaman kodları var (tahmini)
[ ] 10 sabit tag eklendi
[ ] 5 konuya özel tag eklendi (toplam 15)
[ ] Thumbnail rengi tekrar etmiyor
[ ] İçerik tipi dengesi ihlal edilmiyor
[ ] Kaynaklar doğrulanmış (tarih var)
[ ] Blocked moves ihlali yok
[ ] Verilen söz kontrolü yapıldı
```

---

## ADIM 7 — KAYDET

### knowledge/ klasörüne yaz

`skills/write-knowledge.md` kurallarını uygula.

Sonraki VID key'i belirle:
→ `knowledge/my-videos/` klasörüne bak
→ Son VID key + 1

Dosya oluştur: `knowledge/my-videos/VID-XXX.md`

```markdown
# VID-XXX — [Başlık]
**Tip:** [Trend Analizi / Tutorial / Kariyer / Girişim]
**Planlanan Tarih:** YYYY-MM-DD
**Durum:** SEO Hazır
**Oluşturulma:** YYYY-MM-DD (/youtube-konu ile)

---

## SEO PAKETİ
[Başlık, açıklama, taglar, thumbnail, hook — tam format]

---

## ARAŞTIRMA NOTLARI
[Çarpıcı veriler, kaynaklar, viral video analizi]

---

## PERFORMANS BAĞLANTISI
Başlık formülü: [X]
Hook tipi: [X]
İçerik tipi: [X]
CTR: — (yayın sonrası doldurulacak)
Retention: — (yayın sonrası doldurulacak)
Abone artışı: — (yayın sonrası doldurulacak)
```

### State layer güncelle

`youtube-state-layer.md` → Yayın Takvimi tablosuna ekle:
```
| VID-XXX | [Tip] | [Başlık] | SEO Hazır | [Tarih] |
```

### Raporu kaydet

`knowledge/outputs/[TARIH]-konu-[konu-slug].md` oluştur.

### Sheets güncelle

Terminalde çalıştır:
```bash
python scripts/sync_sheets.py
```

---

## ADIM 8 — SONRAKİ ADIM

Paketi verdikten sonra sor:
"Tam konuşma metnini de üreteyim mi?
`/youtube-script VID-XXX` ile devam edebiliriz."

---

**END /youtube-konu**
