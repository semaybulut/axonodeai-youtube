# YOUTUBE STATE LAYER
**Version:** 1.4
**Owner:** Sema | AxonodeAI
**Last Updated:** 2026-05-11

---

## AÇIKLAMA

Bu dosya dinamiktir. Her /youtube komutu çalıştırıldığında güncellenir.
Statik kural değil — değişen durum takibi.

---

## MEVCUT DURUM

### Kanal Bilgileri
```
Kanal adı: Sema - Axonode AI
Abone sayısı: 22
Toplam video: 1
Yayın günü: Salı
Yayın saati: 09:00
```

### Son Yayınlanan Video
```
Video No: VID-001
Başlık: Python Öğrenmek Yetmiyor — 2026'da Veri Bilimi Gerçekten Ne İstiyor?
Tip: Trend Analizi
Tarih: 2026-05-08
URL: https://youtu.be/GBVSl9UgIDQ
Thumbnail arka plan: #414ecf
İngilizce altyazı: Kontrol gerekiyor
```

### Verilen Söz
```
"Bir sonraki videoda AI agent sistemlerini veri biliminde
nasıl kullanırsın, onu anlatacağım."
→ Bir sonraki video bu olmalı.
```
### VID-002 Kararlaştırılan Hook
Hook tipi: Vadi Hook (Tutorial için zorunlu — VID-001 retention alarmından çıkarılan ders)
Seçilen metin: "Bu videonun sonunda LangChain ile çalışan bir veri analizi ajanı
kurmuş olacaksın. Kod editörünü aç, birlikte yapıyoruz."
Kaynak karar: 2026-05-10-youtube-rapor.md + VPT-006 pattern
İlk 20 saniyede söylenecek — gecikmesiz.

---

## YAYIN TAKVİMİ

| Video No | Tip | Konu | Durum | Tarih |
|----------|-----|------|-------|-------|
| 001 | Trend Analizi | Python Öğrenmek Yetmiyor | ✅ Yayında | 2026-05-08 |
| 002 | Tutorial | AI Agent Kur: Veri Biliminde Adım Adım — 2026 | 📋 SEO Hazır | 2026-05-14 |
| 003 | Kariyer / POV | Sağlıktan Veri Bilimine Geçtim — Kimse Söylemedi | 📋 SEO Hazır | 2026-05-21 |
| 004 | Trend Analizi | %57 Şirket AI Ajanı Kullanıyor — Sen Neredesin? | 📋 SEO Hazır | 2026-05-28 |
| 005 | Girişim / Para | AI ile Freelance: 2026'da Gerçekten Çalışan 3 Yol | 💡 Fikir | 2026-06-04 |
| 006 | Trend Analizi | Yapay Zeka Seni İşsiz mi Bırakacak? — Dürüst Cevap | 💡 Fikir | 2026-06-11 |

---

## İÇERİK DENGE TAKİBİ

### Tip Dağılımı (Rolling — Son 5 Video / Plan dahil)
```
Trend Analizi:        3/6 (VID-001, VID-004, VID-006)
Tutorial / Araç:      1/6 (VID-002)
Kariyer / POV:        1/6 (VID-003)
Girisim / Para:       1/6 (VID-005)
Vlog:                 0/6
```

### Topic Dağılımı (Rolling — Son 5 Video)
```
Yapay Zeka Kariyer:   1/5
AI Araclari:          0/5
Veri bilimi:          0/5
Isin Gelecegi:        1/5
Girisim / Para:       0/5
Healthcare baglantili: 1/5
```

### Kural
- Aynı tip arka arkaya gelmez
- Her 3 videodan 1 kariyer/kişisel/girişim olmalı
- Healthcare bağlantılı içerik max 1/5 olmalı — baskın olmasın
- Seri vaadi bozulmamalı

---

## THUMBNAIL RENK TAKİBİ (Son 5 Video)

```
Video 001: #414ecf (mavi) ✅
Video 002: #f0eee9 (krem) — planlandı
Video 003: #d2c7ff (lila) — planlandı
Video 004: #414ecf (mavi) — planlandı (2 video gap, tekrar OK)
Video 005: — (henüz yok)
Video 006: — (henüz yok)
```

**Renk Tekrarı Kuralı:** Aynı renk arka arkaya 2 kez kullanılmaz.

## ALTYAZI TAKİBİ
VID-001: Kontrol gerekiyor — eklendi mi?
VID-002: Henüz yok — çekim sonrası eklenecek
Kural: Her videoda İngilizce altyazı zorunlu. /youtube-publish çalıştırılmadan önce kontrol edilir.
---

## ANALİTİK SNAPSHOT

### Video 001 Performansı
```
Yayın tarihi: 2026-05-08
İzlenme: 199 (2026-05-10 itibarıyla)
Beğeni: 18 (%9 oran — çok güçlü)
Yorum: 13 (%6.5 oran — çok güçlü)
Retention: 20.3% — ALARM (hedef %40-50)
CTR: Birikme devam ediyor (2026-05-15 sonrası)
Abone artışı: +5 (toplam 22)
Content suggesting this video: %27.6
Top kaynak kanallar:
  - Claude Code YouTube kanalı
  - Machine Learning Modelini Eğitme
```

---

## STRATEJİK ÖNERİLER (Şu An)

1. **VID-001 Retention Alarmı:** %20.3 — düşük. Olası neden: ilk 30 saniyede Vadi Hook yok. VID-002'de düzelt.
2. **VID-002 Hook:** Vadi tipi zorunlu — "Bu videonun sonunda AI agent kurmuş olacaksın." İlk 20 saniyede söyle.
3. **VID-002 Thumbnail:** #f0eee9 + #f94144 metin — "AI AGENT KUR"
4. **Altyazı:** VID-001 İngilizce altyazı eklendi mi kontrol et
5. **Yorum:** VID-001 13 yorum var — hepsine cevap ver (henüz verilmediyse)
6. **VID-001 beğeni/yorum oranı çok güçlü** — içerik kalitesi OK, sadece hook/yapı sorunu var
7. **VID-005 ve VID-006:** Fikir aşamasında — VID-004 yayına girdikten sonra SEO paket hazırla
8. **API:** ✅ Tüm API'ler kurulu. Gerçek CTR/Retention 2026-05-15 sonrası anlamlı hale gelir.

---

## BLOCKED MOVES (Şu An)

- Trend Analizi videosu ardı ardına yapma — Tutorial sırası
- Mavi (#414ecf) thumbnail tekrar kullanma — farklı renk seç
- AI Agent- Veri Bilimi sözünü erteleme — izleyici bekliyor
- VID-002 hook'unu değiştirme — Vadi Hook olarak kararlaştırıldı (2026-05-10)
---

## VİRAL MEKANİZMA NOTLARI

→ Detay: youtube-viral-mekanizma.md
→ Pattern kütüphanesi: viral-mechanism-library.md

**END STATE LAYER**
