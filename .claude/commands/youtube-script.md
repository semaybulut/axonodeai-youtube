# /youtube-script
**Versiyon:** 2.0
**Owner:** Sema | AxonodeAI

**Kullanım:**
```
/youtube-script VID-XXX
```

**Görevi:**
SEO paketi hazır olan video için tam konuşma metni üret.
Görsel plan, b-roll listesi ve üretim kontrol listesi dahil.

---

## BAŞLAMADAN ÖNCE

Şu dosyaları oku:
- `knowledge/my-videos/VID-XXX.md` — SEO paketi, araştırma notları
- `youtube-production-template.md` — konuşma metni yapısı
- `youtube-strategy.md` — hedef kitle, kanal kimliği
- `youtube-viral-mekanizma.md` — hook formülleri, retention mekanizmaları
- `knowledge/viral-mechanism-library.md` — kanıtlanmış pattern'ler
- `youtube-state-layer.md` — verilen söz, mevcut durum

VID key belirtilmezse:
→ `youtube-state-layer.md`'deki bir sonraki planlanmış videoyu bul
→ "VID-XXX için mi yazayım?" diye sor

VID dosyası yoksa:
→ "/youtube-konu ile önce SEO paketi oluşturalım. Konuyu söyle."

---

## ADIM 1 — VİDEO PROFİLİ OKU

`knowledge/my-videos/VID-XXX.md` dosyasından çek:
```
Başlık: [X]
İçerik tipi: [X]
Hedef süre: [X dakika]
Hook taslağı: [varsa]
Araştırma notları: [çarpıcı veriler, kaynaklar]
Bölüm yapısı: [varsa]
```

Araştırma notu yoksa:
→ `/youtube-konu` mantığıyla hızlı web araştırması yap
→ En az 3 veri noktası topla

---

## ADIM 2 — HOOK SEÇİMİ (0-30 saniye)

`knowledge/viral-mechanism-library.md` ve `youtube-viral-mekanizma.md`'den
bu video tipine en uygun hook tipini seç.

**Hook tipi karar matrisi:**
Hook tipleri (sırayla dene, en güçlüsünü seç):
```
Tutorial → Vadi Hook
  "Bu videonun sonunda X yapmış olacaksın"

Trend Analizi → Şok/Veri Hook
  "[İstatistik]. Bu biz veri bilimciler için ne anlama geliyor?"

Kariyer/POV → Hikaye veya İtiraf Hook
  "X ay önce [durum]. Bugün [sonuç]. Aradaki fark şuydu..."

Girişim/Para → Somut Sayı Hook
  "[Para miktarı] — [nasıl] — [süre]"

İddia Hook → 
  "X artık yeterli değil"
```
1. İddia Hook — "X artık yeterli değil"
2. Soru Hook — "Neden X hala çalışıyor?"
3. Şok Hook — "X şirketi Y'yi işten çıkardı — çünkü..."
4. Hikaye Hook — "3 ay önce X yaptım, şimdi Y oldu"
5. Vadi Hook — "Bu videoyu izledikten sonra X yapabileceksin"

Seçilen hook tipini ve gerekçesini yaz:
"Bu video için [X] hook seçildi — çünkü [araştırma/pattern gerekçesi]"

**Hook metni (kelimesi kelimesine):**
```
[Dikkat çekici açılış — en güçlü cümle, araştırmadan en çarpıcı veriyi kullan]
[Neden izlemeli — somut, spesifik fayda]
[Video vadi — net 1 cümle]

Tahmini süre: [X saniye]
```

---

## ADIM 3 — GİRİŞ (30 sn - 1 dk)

```
[Konu bağlamı — neden bu konu şimdi önemli]
[Varsa araştırma verisi — "McKinsey'e göre..." / "2026 itibarıyla..."]
[İzleyiciye söz — bu videodan ne öğrenecekler, somut]
[Yapı — "X bölümde anlatacağım, hadi başlayalım"]
```

---

## ADIM 4 — BÖLÜMLER

Hedef süreye göre bölüm sayısı belirle:
```
8-10 dk  → 3 bölüm
10-12 dk → 4 bölüm
12-15 dk → 5 bölüm
```

Her bölüm için şu yapıyı uygula:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BÖLÜM [X]: [BAŞLIK]
Tahmini zaman: [X:XX - X:XX]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

(Bölüm Hook)
[1-2 cümle — bu bölümde ne öğrenecekler]
[Merak bırak — neden önemli]

(Ana İçerik)
[Ana bilgi — somut, spesifik, jargonsuz]
[Veri veya örnek — araştırma notlarından çek]
[Açıklama — neden önemli, nasıl çalışıyor]
[Gerçek hayat analojisi — youtube-viral-mekanizma.md'den]

(Sema Bağlantısı — her bölümde 1 tane)
[Kişisel deneyim veya veri bilimine geçiş bağlantısı]
[Hedef kitleyle empati — "Sen de bunu yaşıyor olabilirsin"]

(Pratik Çıkarım)
[1 somut aksiyon — izleyici ne yapmalı]

(Bölüm Geçişi)
[Sonraki bölüme köprü — merak bırak]
"Bir sonraki bölümde [X] — ama önce [Y]..."
```

**Retention mekanizmaları** (`youtube-viral-mekanizma.md`'den):
- Her 2-3 dakikada bir: "Bir sonraki madde bu arada en önemlisi..."
- Sayılı liste kullan: "Birinci madde... İkinci madde..."
- Tehdit → Çözüm yolu: rakam ile aç, çözümle devam et
- Kademeli seviye yapısı: temel → orta → ileri

---

## ADIM 5 — ÖZET (Son 2 dakika)

```
"Özetle:"
- Bölüm 1: [tek cümle — somut]
- Bölüm 2: [tek cümle — somut]
- Bölüm 3: [tek cümle — somut]

[En önemli çıkarım — izleyici 1 şey hatırlayacaksa ne olsun]
[Bu bilgiyi hemen nerede kullanabilir]
```

---

## ADIM 6 — CTA (Son 30 saniye)

`youtube-viral-mekanizma.md` → CTA Stratejileri bölümünü uygula.

```
[Yorum CTA — spesifik soru, genel değil]
Örnek: "Sen hangi araçla başladın, yorumda yaz."
Örnek: "Bu konuda en çok neyi merak ediyorsun?"

[Abone CTA — neden abone olunmalı, kısa]
"Her hafta [niş konu] içerikleri için abone ol."

[Sonraki video CTA — söz ver, merak bırak]
"Bir sonraki videoda [konu] anlatacağım — kaçırma."
```

---

## ADIM 7 — GÖRSEL PLAN

```
ZAMAN    | KONUŞMA ÖZETI       | EKRAN GÖRSELİ        | KAYNAK
---------|---------------------|----------------------|----------
0:00     | Hook açılışı        | Yüz — kamera         | —
0:30     | Konu bağlamı        | B-roll               | Pexels
1:00     | Bölüm 1 başlığı     | Geçiş kartı          | AE şablon
1:05     | Veri / istatistik   | İstatistik kartı     | AE şablon
...      | ...                 | ...                  | ...
Son 2dk  | Özet                | Özet kartı           | AE şablon
Son 30sn | CTA                 | End screen           | AE şablon
```

---

## ADIM 8 — B-ROLL LİSTESİ

```
SAHNE                | TİP          | KAYNAK          | DURUM
---------------------|--------------|-----------------|-------
[sahne 1]            | Kişisel      | Kendin çek      | [ ]
[sahne 2]            | Stock        | Pexels          | [ ]
[sahne 3]            | Ekran kaydı  | Kendin al       | [ ]
```

**Ücretsiz stock kaynakları:**
- Pexels.com, Pixabay.com, Coverr.co, Mixkit.co

---

## ADIM 9 — TAHMİNİ SÜRE DAĞILIMI

```
Hook + Giriş:   X dakika
Bölüm 1:        X dakika
Bölüm 2:        X dakika
Bölüm 3:        X dakika
Özet + CTA:     X dakika
━━━━━━━━━━━━━━━━━━━━━━━━
TOPLAM:         X dakika
Hedef:          [X dakika]
Fark:           [+X / -X]
```

---

## ADIM 10 — ÜRETİM KONTROL LİSTESİ

```
Çekim Öncesi:
[ ] Konuşma metni tamamlandı
[ ] Görsel plan tamamlandı
[ ] B-roll listesi tamamlandı
[ ] Kaynaklar toplandı
[ ] Grafik şablonlar hazırlandı

Çekim:
[ ] Ana konuşma çekildi
[ ] B-roll çekildi / indirildi
[ ] Ekran kayıtları alındı

Post Production:
[ ] Montaj tamamlandı
[ ] Grafikler eklendi
[ ] Müzik eklendi
[ ] Renk düzeltme yapıldı
[ ] Ses düzeltme yapıldı

Yayın:
[ ] Türkçe SRT oluşturuldu
[ ] İngilizce SRT oluşturuldu
[ ] Thumbnail hazırlandı
[ ] Başlık yazıldı (final — yayınlanan)
[ ] Açıklama yazıldı
[ ] Taglar eklendi
[ ] End screen eklendi
[ ] Playlist eklendi
[ ] İlk yorum hazırlandı (pinlenecek)
```

---

## ADIM 11 — KAYDET

`knowledge/my-videos/VID-XXX.md` dosyasına ekle:

```markdown
## KONUŞMA METNİ
**Oluşturulma:** YYYY-MM-DD (/youtube-script ile)
**Hook Tipi:** [X]
**Seçilme Gerekçesi:** [1 cümle]

### Hook
[metin]

### Giriş
[metin]

### Bölüm 1: [başlık]
[metin]

### Bölüm 2: [başlık]
[metin]

### Bölüm 3: [başlık]
[metin]

### Özet
[metin]

### CTA
[metin]
```

State layer güncelle:
```
VID-XXX durumu: "Script Hazır"
```

Sheets güncelle:
```bash
python scripts/sync_sheets.py
```

---

## ADIM 12 — SONRAKİ ADIM

Script tamamlandıktan sonra söyle:
"Video çekilip yayınlandığında `/youtube-publish VID-XXX` çalıştır.
Sistem performansı takip edecek ve bir sonraki videoya öğretecek."

---

**END /youtube-script**
