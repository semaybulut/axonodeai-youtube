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
Abone sayısı: 24
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

---

## YAYIN TAKVİMİ

| Video No | Tip | Konu | Durum | Tarih | Seri |
|----------|-----|------|-------|-------|------|
| 001 | Trend Analizi | Python Öğrenmek Yetmiyor | ✅ Yayında | 2026-05-08 | — |
| 002 | Tutorial | AI Agent Kur: Veri Biliminde Adım Adım — 2026 | 📋 SEO Hazır | 2026-05-14 | — |
| 003 | Kariyer / POV | Sağlıktan Veri Bilimine Geçtim — Kimse Söylemedi | 📋 SEO Hazır | 2026-05-21 | — |
| 004 | Trend Analizi | %57 Şirket AI Ajanı Kullanıyor — Sen Neredesin? | 📋 SEO Hazır | 2026-05-28 | — |
| 005 | Girişim / Para | AI ile Freelance: 2026'da Gerçekten Çalışan 3 Yol | 💡 Fikir | 2026-06-04 | — |
| 006 | Trend Analizi | Yapay Zeka Seni İşsiz mi Bırakacak? — Dürüst Cevap | 💡 Fikir | 2026-06-11 | — |
| 007 | Tutorial | DevOps Olmadan Veri Bilimcisi Olunur mu? — 2026 Gerçeği | 📋 SEO Hazır | 2026-06-18 | — |
| 008 | Kariyer / POV | 2026'da Veri Bilimi Sıfırdan — Tam Yol Haritam | 📝 Script Hazır | 2026-06-23 | Sıfırdan Veri Bilimcisi 1/6 |
| 009 | Tutorial | AI ile Veri Bilimi Öğrendim — Cursor, ChatGPT 2026 | 📝 Script Hazır | 2026-06-30 | Sıfırdan Veri Bilimcisi 2/6 |
| 010 | Kariyer / POV | Veri Bilimi 1. Ay — Ne Öğrendim, Nerede Takıldım? | 📝 Script Taslak | 2026-07-28 | Sıfırdan Veri Bilimcisi 3/6 |
| 011 | Kariyer / POV | Veri Bilimi 2. Ay — İlk Projem, İlk Hayal Kırıklığı | 📝 Script Taslak | 2026-08-25 | Sıfırdan Veri Bilimcisi 4/6 |
| 012 | Kariyer / POV | 3 Ay Veri Bilimi — Şimdi Ne Biliyorum, Devam mı? | 📝 Script Taslak | 2026-09-22 | Sıfırdan Veri Bilimcisi 5/6 |
| 013 | Kariyer / POV | 4 Ay Veri Bilimi — Ne Değişti, Ne Öğrendim? (Seri Sonu) | 📝 Script Taslak | 2026-10-20 | Sıfırdan Veri Bilimcisi 6/6 |

---

## İÇERİK DENGE TAKİBİ

### Tip Dağılımı (VID-001 → VID-013 toplam)
```
Trend Analizi:        3/13 (VID-001, VID-004, VID-006)
Tutorial / Araç:      3/13 (VID-002, VID-007, VID-009)
Kariyer / POV:        6/13 (VID-003, VID-008, VID-010, VID-011, VID-012, VID-013)
Girisim / Para:       1/13 (VID-005)
Vlog:                 0/13
```
Not: Kariyer/POV ağırlığı belgesel seriden geliyor. Aradaki haftalar Trend/Tutorial ile doldurulmalı.

### Topic Dağılımı (Rolling — Son 5 Video)
```
Yapay Zeka Kariyer:   1/5
AI Araclari:          0/5
Veri bilimi:          0/5
Isin Gelecegi:        1/5
Girisim / Para:       0/5
Healthcare baglantili: 1/7
```

### Kural
- Aynı tip arka arkaya gelmez
- Her 3 videodan 1 kariyer/kişisel/girişim olmalı
- Healthcare bağlantılı içerik max 1/7 olmalı — baskın olmasın
- Seri vaadi bozulmamalı

---

## THUMBNAIL RENK TAKİBİ

```
Video 001: #414ecf (mavi) ✅
Video 002: #f0eee9 (krem) — planlandı
Video 003: #d2c7ff (lila) — planlandı
Video 004: #414ecf (mavi) — planlandı (2 video gap, tekrar OK)
Video 005: — (henüz yok)
Video 006: — (henüz yok)
Video 007: #f0eee9 (krem) — planlandı
Video 008: #d2c7ff (lila) — seri V1 (farklı, OK)
Video 009: #f0eee9 (krem) — seri V2 (VID-007 ile 1 gap, OK)
Video 010: #d2c7ff (lila) — seri V3 (aylık, VID-009 ile gap var)
Video 011: #d2c7ff (lila) — seri V4 (aylık, arada regular video var)
Video 012: #d2c7ff (lila) — seri V5 (aylık, arada regular video var)
Video 013: #d2c7ff (lila) — seri V6 (aylık, arada regular video var)
```
Not: VID-010 ile VID-013 arası aylık yayın — aradaki haftalık regular videolar farklı renk kullanmalı.

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
İzlenme: 297 (2026-05-13 itibarıyla)
Beğeni: 21 (%7.1 oran — güçlü)
Yorum: 14 (%4.7 oran — güçlü)
Retention: 23.4% — ALARM (hedef %40-50)
CTR: Birikme devam ediyor (2026-05-15 sonrası)
Abone artışı: +7 (toplam 24)
Content suggesting this video: %27.6
Top kaynak kanallar:
  - Claude Code YouTube kanalı
  - Machine Learning Modelini Eğitme
```

---

## STRATEJİK ÖNERİLER (Şu An)

1. **VID-001 Retention Alarmı:** %23.4 (güncel) — hâlâ düşük. Olası neden: ilk 30 saniyede Vadi Hook yok. VID-002'de düzelt.
2. **VID-002 Hook:** Vadi tipi zorunlu — "Bu videonun sonunda AI agent kurmuş olacaksın." İlk 20 saniyede söyle.
3. **VID-002 Thumbnail:** #f0eee9 + #f94144 metin — "AI AGENT KUR"
4. **Altyazı:** VID-001 İngilizce altyazı eklendi mi kontrol et
5. **Yorum:** VID-001 14 yorum var — hepsine cevap ver (henüz verilmediyse)
6. **VID-001 beğeni/yorum oranı çok güçlü** — içerik kalitesi OK, sadece hook/yapı sorunu var
7. **VID-005 ve VID-006:** Fikir aşamasında — VID-004 yayına girdikten sonra SEO paket hazırla
8. **API:** ✅ Tüm API'ler kurulu. Gerçek CTR/Retention 2026-05-15 sonrası anlamlı hale gelir.
9. **SERİ EKLENDI:** VID-008-013 "Sıfırdan Veri Bilimcisi" planlandı. VID-008 script hazır, VID-010-013 taslak (çekim öncesi güncellenmeli).
10. **Aradaki haftalık boşluklar (2026-07-07, 07-14, 07-21 vb.):** Regular Trend/Tutorial içerik planlanmalı — belgesel episodlar aylık, kanal haftalık çalışmalı.

---

## BLOCKED MOVES (Şu An)

- Trend Analizi videosu ardı ardına yapma — Tutorial sırası
- Mavi (#414ecf) thumbnail tekrar kullanma — farklı renk seç
- AI Agent — Veri Bilimi sözünü erteleme — izleyici bekliyor
- VID-002 hook'unu değiştirme — Vadi Hook olarak kararlaştırıldı (2026-05-10)
- VID-010-013 scriptlerini güncellemeden çekim — gerçek ay verisi ZORUNLU
---

## VİRAL MEKANİZMA NOTLARI

→ Detay: youtube-viral-mekanizma.md
→ Pattern kütüphanesi: viral-mechanism-library.md

**END STATE LAYER**
