# COMMAND: /youtube-publish VID-XXX
# Video yayın kaydı ve performans takibi
**Versiyon:** 2.0
**Owner:** Sema | AxonodeAI

**Kullanım:**
```
/youtube-publish VID-XXX           → ilk 48 saat kaydı
/youtube-publish VID-XXX --update  → 7 gün sonra tam analitik
```

**Görevi:**
Video yayınlandığında çalıştır.
Gerçek verileri çek, sisteme kaydet, öğrenen mekanizmayı güncelle.

---

## BAŞLAMADAN ÖNCE

Şu dosyaları oku:
- `knowledge/my-videos/VID-XXX.md` — video profili
- `knowledge/analytics-snapshot.md` — kanal ortalamaları
- `knowledge/viral-mechanism-library.md` — mevcut pattern'ler
- `youtube-state-layer.md` — mevcut durum
- `skills/fetch-analytics.md` — API çağrı kuralları

---
## STANDART AKIŞ (Parametresiz)
1.  Videonun ilk yayın verilerini API'den çek.
2.  `knowledge/my-videos/VID-XXX.md` dosyasını "Yayında" durumuna çek.
3.  Sheets "Icerik Takvimi" sekmesini "✅ Yayında" olarak güncelle.

---
## ADIM 0 — YORUM ANALİZİ (--update'e özgü)
skills/fetch-comments.md'yi çalıştır — son video için.
AUDIENCE_VOICE verisini write-knowledge'a gönder:
→ knowledge/audience-voice.md güncelle (Bölüm A + B)
→ Google Sheets Izleyici Sesi tabını güncelle

---

## ADIM 1 — VİDEO BİLGİSİ AL

`knowledge/my-videos/VID-XXX.md` dosyasını aç.

Eksik alanlar varsa kullanıcıdan iste:

```
YouTube URL: [video linki — yayınlanan]
Yayın tarihi: [YYYY-MM-DD]
Final başlık: [yayınlanan başlık — SEO paketindeki ile aynı mı?]
Kullanılan thumbnail rengi: [hex]
Kullanılan hook tipi: [İddia/Soru/Şok/Hikaye/Vadi]
Kullanılan başlık formülü: [Öneri Odaklı/Arama Odaklı/Soru/İddia vs.]
```

---

## ADIM 2 — ANALİTİK ÇEK

`skills/fetch-analytics.md` kurallarını uygula.

`scripts/sync_sheets.py` çalıştır:
```bash
python scripts/sync_sheets.py
```

Çekilen veriler:
```
İzlenme sayısı: [X]
Benzersiz izleyici: [X]
Ortalama izlenme süresi: [X:XX]
Retention: [%X]
CTR: [%X]
Trafik kaynakları:
  Öneri sistemi: [%X]
  Arama: [%X]
  Dış trafik: [%X]
  Direkt: [%X]
Beğeni: [X]
Yorum: [X]
Abone değişimi: [+X / -X]
```

**NOT:** İlk 48 saatte veriler tam gelmeyebilir.
Eksik alanları "Birikme devam ediyor" olarak işaretle.
Şunu yaz: "Tam analitik için 7 gün sonra `/youtube-publish VID-XXX --update` çalıştır."

---

## ADIM 3 — PERFORMANS SINIFLANDIRMASI

`knowledge/analytics-snapshot.md`'den kanal ortalamalarını çek.

```
CTR Karşılaştırma:
  Kanal ortalaması: [%X]
  Bu video:         [%Y]
  Fark:             [+X / -X puan]
  Durum:            [✅ Ortalama üstü / ⚠️ Ortalama altı / 🚨 Alarm]

Retention Karşılaştırma:
  Kanal ortalaması: [%X]
  Bu video:         [%Y]
  Fark:             [+X / -X puan]
  Durum:            [✅ / ⚠️ / 🚨]

Abone Artışı:
  Kanal ortalaması: [+X/video]
  Bu video:         [+Y]
  Durum:            [✅ / — Normal / ⚠️ Düşük]
```

**Alarm durumları:**
- CTR %2 altında → "Thumbnail veya başlık değişikliği düşün"
- Retention %30 altında → "Hook veya içerik sorunu"
- Yorum 0 → "CTA güçlendir"

---

## ADIM 4 — PERFORMANS BAĞLANTISI GÜNCELLE

Bu adım sistemin kendini eğittiği yerdir.

### 4A — VID Dosyasını Güncelle

`knowledge/my-videos/VID-XXX.md` → PERFORMANS BAĞLANTISI bölümünü doldur:

```markdown
## PERFORMANS BAĞLANTISI
**Güncelleme:** YYYY-MM-DD [48 saat / 7 gün]

Başlık formülü: [X]
Hook tipi:      [X]
İçerik tipi:    [X]
CTR:            [%X]
Retention:      [%X]
Abone artışı:   [+X]

Kanal ortalamasıyla karşılaştırma:
CTR:       Bu video %X | Ort. %X | [+X / -X puan]
Retention: Bu video %X | Ort. %X | [+X / -X puan]
Abone:     Bu video +X | Ort. +X | [+X / -X]

Ne işe yaradı:
[CTR iyi ise: "Başlık formülü X + Hook Y iyi çalıştı"]
[Retention iyi ise: "Bölüm yapısı Z izleyiciyi tuttu"]

Ne işe yaramadı:
[Düşük performans varsa: sebep tahmini]

Bir sonraki videoya not:
[Bu videodan 1-2 spesifik ders]
```

### 4B — Viral Mechanism Library Güncelle

`knowledge/viral-mechanism-library.md` → PERFORMANS VERİSİ bölümünü güncelle:

```markdown
## PERFORMANS VERİSİ — [tarih güncelleme]

### Hook Performansı (Kendi Kanal Verisi)
| Hook Tipi   | Video   | CTR  | Retention | Sonuç     |
|-------------|---------|------|-----------|-----------|
| [İddia]     | VID-001 | %X   | %X        | ✅ / ⚠️   |
| [Vadi]      | VID-002 | %X   | %X        | ✅ / ⚠️   |

En iyi CTR → Hook tipi: [X]
En iyi Retention → Hook tipi: [X]

### Başlık Formülü Performansı
| Formül          | Video   | CTR  | Sonuç   |
|-----------------|---------|------|---------|
| Öneri Odaklı   | VID-001 | %X   | ✅ / ⚠️ |
| Arama Odaklı   | VID-002 | %X   | ✅ / ⚠️ |

### İçerik Tipi → Abone Artışı
| Tip           | Video   | Abone+ | Sonuç   |
|---------------|---------|--------|---------|
| Trend Analizi | VID-001 | +X     | ✅ / ⚠️ |
| Tutorial      | VID-002 | +X     | ✅ / ⚠️ |

### SONUÇ (2+ video verisi varsa yaz)
"[Formül] başlık + [Hook] hook → en yüksek CTR"
"[Tip] içerik tipi → en yüksek abone artışı"

### Kanıtlanmış Pattern'ler (2+ videoda iyi performans)
[Birden fazla videoda doğrulanmış pattern'leri buraya taşı]

### Kaçınılacaklar (2+ videoda düşük performans)
[Düşük performans veren yapıları buraya ekle]
```

### 4C — Analytics Snapshot Güncelle

`knowledge/analytics-snapshot.md` tamamını güncelle:

```markdown
# ANALİTİK SNAPSHOT
**Son Güncelleme:** YYYY-MM-DD

## API DURUMU
YouTube Data API v3:   ✅ kurulu
YouTube Analytics API: ✅ kurulu
Google Sheets API:     ✅ kurulu

## KANAL ÖZETI
| Metrik | Değer | Önceki | Değişim |
|--------|-------|--------|---------|
| Toplam Abone | X | X | +X |
| Toplam İzlenme | X | X | +X |
| Video Sayısı | X | X | +X |

## KANAL ORTALAMALARI ([X video üzerinden])
CTR ortalaması:           [%X]
Retention ortalaması:     [%X]
Abone artışı/video:       [+X]
Öneri sistemi trafiği:    [%X]

## VİDEO PERFORMANSLARI
| VID Key | Başlık | CTR | Retention | Abone+ | Genel |
|---------|--------|-----|-----------|--------|-------|
| VID-001 | [kısa] | %X  | %X        | +X     | ✅/⚠️  |
| VID-002 | [kısa] | %X  | %X        | +X     | ✅/⚠️  |

## EN İYİ PERFORMANS
CTR: VID-XXX — [%X] — [başlık formülü]
Retention: VID-XXX — [%X] — [hook tipi]
Abone+: VID-XXX — [+X] — [içerik tipi]

## ALARMLAR
🚨 Aktif: [alarm varsa]
⚠️ Dikkat: [uyarı varsa]
✅ Temiz: [alarm yoksa]
```

---

## ADIM 5 — STATE LAYER GÜNCELLE

`youtube-state-layer.md`:

```markdown
### Son Yayınlanan Video (güncelle)
Video No: VID-XXX
Başlık: [başlık]
Tip: [tip]
Tarih: [tarih]
URL: [url]
CTR: [%X]
Retention: [%X]

### Stratejik Öneriler (güncelle)
[Performans verilerine göre yeni öneriler]
[Düşük CTR varsa → thumbnail önerisi]
[Düşük retention varsa → hook önerisi]

### Blocked Moves (güncelle)
[Düşük performans gösteren yapıları ekle]
```

---

## ADIM 6 — SHEETS GÜNCELLE

```bash
python scripts/sync_sheets.py
```

**⚠️ İlk 24-72 saatte analytics boş döner.**
Script "Birikme devam ediyor" yazarsa bu normaldir — Sheets'e o haliyle yazar.
7 gün sonra `/youtube-publish VID-XXX --update` ile tekrar çalıştır.

**--update flag nedir:**
`/youtube-publish VID-XXX --update` komutu şunu yapar:
- Adım 1-3'ü atla (zaten yapıldı)
- Adım 4'ten başla → tam analitik çek
- Adım 4B → viral-mechanism-library.md güncelle (2+ video varsa kanıtla)
- Adım 6 → sync_sheets.py tekrar çalıştır

## ADIM 7 — PUBLISH RAPORU

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PUBLISH RAPORU: VID-XXX
[Başlık]
Tarih: [YYYY-MM-DD]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ANALİTİK (İlk 48 Saat):
İzlenme:   [X]
CTR:       [%X]  [✅ / ⚠️ / 🚨]
Retention: [%X]  [✅ / ⚠️ / 🚨]
Abone:     [+X]

Kanal Ortalamalarıyla Karşılaştırma:
CTR:       Bu video %X | Kanal ort. %X | [+X / -X puan]
Retention: Bu video %X | Kanal ort. %X | [+X / -X puan]
Abone:     Bu video +X | Kanal ort. +X | [+X / -X]

PERFORMANS BAĞLANTISI:
Başlık formülü [X]: CTR %X getirdi
Hook tipi [X]: Retention %X getirdi
İçerik tipi [X]: Abone +X getirdi

Bu Videodan Öğrenilenler:
✅ [İyi çalışan — tekrar et]
⚠️ [Dikkat — geliştir]
❌ [İşe yaramadı — kaçın]

Bir Sonraki Video İçin:
→ Hook: [önerilen tip + gerekçe]
→ Başlık: [önerilen formül + gerekçe]
→ Thumbnail: [sıradaki renk]

ALARM:
[Varsa alarm durumları ve önerileri]

Güncellenen Dosyalar:
✅ knowledge/my-videos/VID-XXX.md
✅ knowledge/viral-mechanism-library.md
✅ knowledge/analytics-snapshot.md
✅ youtube-state-layer.md
✅ Google Sheets — İçerik Takvimi
✅ Google Sheets — YouTube Analytics

Sonraki Adım:
7 gün sonra tam analitik için:
/youtube-publish VID-XXX --update
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## ADIM 8 — 7 GÜN GÜNCELLEME AKIŞI (--update)

Eğer `--update` bayrağı kullanılmışsa (7 gün sonra):
Aynı adımları tekrar et, farklar:
- VID dosyasını "7 Gün Analitik" başlığıyla güncelle

1.  **Analitik Çekimi**: API üzerinden tam performans verilerini çek.
2.  **Snapshot Arşivi**: 
    *   Mevcut `analytics-snapshot.md` dosyasının bir kopyasını oluştur.
    *   Bu kopyayı `knowledge/outputs/snapshot/YYYY-MM-DD-snapshot.md` olarak kaydet.
3.  **Haftalık Ortalama**: Kanal ortalamalarını yeniden hesapla
    *   `knowledge/outputs/kanal-haftalik-ortalamalar.md` dosyasını aç.
    *   Dosyanın sonuna bugünün tarihi ve güncel kanal ortalamalarını içeren **YENİ BİR SATIR** ekle.
    *   *Kural*: Eski satırlara asla dokunma, sadece ekleme yap.
4.  **Pattern Doğrulama**: Verileri `knowledge/viral-mechanism-library.md` ile karşılaştır ve pattern'i güncelle. Viral mechanism library'yi yeniden değerlendir:
    - İlk 48 saatte iyi ama 7 günde düşen → "Test ediliyor" olarak kal
    - 7 günde de iyi → "Kanıtlanmış" olarak işaretle
    - İlk 48 saatte düşük ama 7 günde toparlandı → "Arama trafiği gecikmeli geliyor" notu ekle

## HATA YÖNETİMİ
- Video ID bulunamazsa dur ve uyar.
- Veri yetersizse (3 videodan az) ortalamalar tablosuna ilgili hücre için "Veri yetersiz" yaz.

**END /youtube-publish**
