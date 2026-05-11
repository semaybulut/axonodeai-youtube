# /youtube-seri
**Versiyon:** 2.0
**Owner:** Sema | AxonodeAI

**Kullanım:**
```
/youtube-seri "seri adı"      → ajan video sayısını önerir, sen onaylarsın
/youtube-seri "seri adı" 4    → direkt 4 video üretir
```

**Görevi:**
Çok videolu seri planla. Her video için SEO paketi + konuşma metni üret.
Seriyi content-calendar, state layer ve Sheets'e kaydet.

---

## BAŞLAMADAN ÖNCE

Şu dosyaları oku:
- `CLAUDE.md` — genel kurallar
- `youtube-state-layer.md` — mevcut takvim, blocked moves, renk takibi
- `youtube-strategy.md` — içerik denge kuralları
- `knowledge/content-calendar.md` — önümüzdeki haftalar dolu mu?
- `knowledge/viral-mechanism-library.md` — kanıtlanmış pattern'ler
- `youtube-viral-mekanizma.md` — hook ve retention teknikleri

---

## ADIM 1 — GİRDİ PARSE

```
Seri adı: [kullanıcının yazdığı]
Video sayısı: [belirtildiyse kullan → ADIM 3'e geç]
            [belirtilmediyse → ADIM 2'ye geç]
```

---

## ADIM 2 — VİDEO SAYISI KARAR
*(Sadece sayı verilmediyse)*

Konuyu analiz et:
- Bu konu kaç bölüme doğal olarak bölünür?
- Hedef süre: her video 8-15 en fazla 25 dk → konu başına ne gerekir?
- Takvim: `content-calendar.md`'de önümüzdeki kaç hafta boş?
- Strateji: aynı tip arka arkaya gelmesin — araya dengeleyici video lazım mı?

Öneri sun ve onay bekle:

```
"[Seri adı] için [X] video öneriyorum:

  Video 1: [Başlık önerisi] — [1 cümle neden]
  Video 2: [Başlık önerisi] — [1 cümle neden]
  Video 3: [Başlık önerisi] — [1 cümle neden]

Onaylıyor musun, yoksa video sayısını veya içerikleri
değiştirmemi ister misin?"
```

**Onay gelmeden üretime geçme.**

---

## ADIM 3 — İKİ KATMANLI ARAŞTIRMA

### Katman 1 — Web Araştırması
```
[seri konusu] araştırma raporu 2025 2026
[seri konusu] istatistik trend
[her video konusu] veri kaynak
```

Her video için:
- 2-3 çarpıcı istatistik (hook için)
- 1-2 doğrulanmış kaynak

### Katman 2 — Viral Video Araştırması
`skills/fetch-viral-videos.md` skill'ini çalıştır.

```
[seri konusu] tutorial seri YouTube viral
[seri konusu] playlist YouTube izlenme
[seri konusu] YouTube viral
```

Bul:
- Bu seri formatında viral olan örnekler
- Hangi hook tipi seri videolarında daha iyi çalışıyor?
- Rakip kanallar bu seriyi nasıl yapmış?
- Rakip kanallar bu konuyu seri yapmış mı?
- Gap: eksik olan ne?

---

## ADIM 4 — STRATEJİ KONTROLÜ

```
1. Seri hangi video tipine giriyor?
   (Tutorial ağırlıklı / Trend ağırlıklı / Karma)

2. İçerik dengesi:
   Seri X hafta kaplıyor.
   Bu sürede kariyer/girişim videosu gerekiyor mu?
   → Gerekiyorsa seri içine dengeleyici video ekle

3. Thumbnail renk planı:
   X video için renk rotasyonu belirle.
   Aynı renk arka arkaya gelmemeli.

4. Verilen söz kontrolü:
   Mevcut verilen söz varsa seriden önce mi gelmeli?

5. Seri videoları bağımsız izlenebilmeli:
   Seriyi bilmeden de anlaşılmalı.
```

Kural ihlali varsa:
→ Kullanıcıya bildir, çözüm öner, onay al

---

## ADIM 5 — SERİ PLANI ÜRETİMİ

*(Onay geldikten sonra)*

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SERİ: [Seri Adı]
Toplam: [X] video | Başlangıç: [Tarih]
Playlist önerisi: [playlist adı]
Seri hook'u: [seriyi 1 cümleyle anlatan genel hook]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Her video için:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VİDEO [X]/[TOPLAM] — VID-XXX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tip:          [Trend / Tutorial / Kariyer / Girişim]
Tarih:        [YYYY-MM-DD]
Önceki bağ:   [önceki videoya nasıl referans verecek]
Sonraki vadi: [bu videonun sonunda ne söylenecek]

BAŞLIK
Ana:   [max 60 karakter] ([X]/60)
Alt 1: [alternatif]
Alt 2: [alternatif]

AÇIKLAMA
[Tam açıklama şablonu — youtube-seo-system.md'den]

TAGLAR (15/15)
[10 sabit + 5 değişken]

THUMBNAIL
Arka plan: [hex]
Metin:     [hex]
Metin:     [max 4 kelime]
İfade:     [Merak / Şaşkınlık / Ciddiyet]
Mesaj:     [thumbnail + başlık = ne anlatıyor]

ARAŞTIRMA NOTLARI
Veri 1: [istatistik + kaynak]
Veri 2: [istatistik + kaynak]

HOOK TASLAGI (0-30 sn)
Hook tipi: [X]
"[hook metni]"

BÖLÜM YAPISI (tahmini)
Bölüm 1: [başlık] — [X:XX]
Bölüm 2: [başlık] — [X:XX]
Bölüm 3: [başlık] — [X:XX]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## ADIM 6 — TAM KONUŞMA METNİ

Seri önerisi bittikten sonra sor "Seri önerileri tamamlandı, script oluşturma adımına geçiyorum, onaylıyor musunuz"
Onay alınca devam et.
Her video için `/youtube-script` ADIM 2-9 yapısını uygula.

**Seri videolarına özel ekstra kurallar:**

Seri videolarında ekstra kural:
- Her bölüm önceki videoya 1 cümleyle referans ver
- Her bölüm sonraki videoya merak bırak
- Seri başlangıcında playlist'e abone ol vurgusu yap

```
Bölüm başında (Video 2+):
"Geçen hafta [önceki konuyu] konuştuk.
Bugün [bu konuyu] ele alıyoruz."
""Geçen hafta [önceki konuyu] konuştuk.
orda bahsettiğimiz gibi o detayı [bu konuda] ele alıyoruz."

Bölüm sonunda:
"Bir sonraki videoda [sonraki konu] — seri devam ediyor."
"Bir sonraki videoda [sonraki konu] bunun detaylıca inceleyeceğiz."

Seri başında (Video 1):
"Bu [X] videoluk serinin ilk bölümü.
Playlist'e ekleyin, her Salı yeni bölüm."

Seri sonunda (Son video):
"Bu [X] videoluk serinin son bölümüydü.
[Playlist adı] playlist'inde hepsine ulaşabilirsiniz."
"Bu [X] videoluk serinin son bölümüydü. Önceki detaylar için
[Playlist adı] playlist'inde hepsine ulaşabilirsiniz."
```

---

## ADIM 7 — KAYDET

### Her video için ayrı dosya

`knowledge/my-videos/VID-XXX.md`:

```markdown
# VID-XXX — [Başlık]
**Seri:** [Seri adı]
**Seri Sırası:** [X]/[Toplam]
**Tip:** [video tipi]
**Planlanan Tarih:** YYYY-MM-DD
**Durum:** Planlandı
**Oluşturulma:** YYYY-MM-DD (/youtube-seri ile)

## SEO PAKETİ
[Tam format]

## ARAŞTIRMA NOTLARI
[Veriler ve kaynaklar]

## KONUŞMA METNİ
[Tam script]

## PERFORMANS BAĞLANTISI
Başlık formülü: [X]
Hook tipi: [X]
İçerik tipi: [X]
CTR: — (yayın sonrası)
Retention: — (yayın sonrası)
Abone artışı: — (yayın sonrası)
```

### Seri özet dosyası

`knowledge/seriler/[seri-slug].md`:

```markdown
# Seri: [Seri Adı]
**Durum:** Planlandı
**Başlangıç:** YYYY-MM-DD
**Toplam:** [X] video
**Playlist:** [playlist adı]

## Video Listesi
| VID Key | Başlık | Tarih | Durum |
|---------|--------|-------|-------|
| VID-XXX | [başlık] | [tarih] | Planlandı |
...

## Seri Performansı (yayın sonrası doldur)
Ortalama CTR: —
Ortalama Retention: —
Toplam abone artışı: —
```

### Content calendar güncelle

`knowledge/content-calendar.md`'e ekle:

```markdown
| VID Key | Tip | Başlık | Tarih | Durum | Seri |
|---------|-----|--------|-------|-------|------|
| VID-XXX | Tutorial | [başlık] | [tarih] | Planlandı | [seri adı] 1/4 |
```

### State layer güncelle

`youtube-state-layer.md` → "Verilen Söz":

```
Seri başladı: [Seri adı]
Toplam: [X] video
Sıradaki: VID-XXX — [başlık] — [tarih]
```

### Sheets güncelle
### Google Sheets'e yaz — write-sheets skill

`skills/write-sheets.md` dosyasını oku ve uygula.

İçerik Takvimi tabına her video için satır ekle:
```
VID Key | Tip | Renk Kodu | Başlık | URL (boş) | Tarih | Durum: Planlandı | Seri bilgisi
```

---
```bash
python scripts/sync_sheets.py
```

---

## ADIM 8 — SERİ ÖZET RAPORU

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SERİ RAPORU: [Seri Adı]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Toplam video: [X]
Yayın aralığı: [başlangıç] - [bitiş]
Playlist: [önerilen isim]

Video Özeti:
VID-XXX | [tarih] | [kısa başlık] | [thumbnail rengi] | [hook tipi]
VID-XXX | [tarih] | [kısa başlık] | [thumbnail rengi] | [hook tipi]
...

İçerik Dengesi (seri sonrası):
Trend: X | Tutorial: X | Kariyer: X | Girişim: X
Kural ihlali: [YOK / UYARI: ...]

Thumbnail Renk Rotasyonu:
VID-XXX → [renk] ✓
VID-XXX → [renk] ✓
...

Güncellenen Dosyalar:
✅ knowledge/my-videos/ — [X] dosya oluşturuldu
✅ knowledge/seriler/[seri-slug].md — oluşturuldu
✅ knowledge/content-calendar.md — güncellendi
✅ youtube-state-layer.md — güncellendi
✅ Google Sheets — İçerik Takvimi güncellendi

Sonraki Adım:
Her video için çekim öncesi /youtube-script ile konuşma metnini doğrula.
Video yayınlandığında /youtube-publish VID-XXX ile kaydet.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

**END /youtube-seri**
