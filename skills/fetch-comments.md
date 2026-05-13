# SKILL: fetch-comments
# AxonodeAI YouTube Brain
# YouTube Data API — İzleyici Yorum Analizi

---

## GÖREV

Belirtilen video(lar) için YouTube Data API kullanarak yorumları çek.
Her yorumu NLP mantığıyla 4 kategoriye sınıflandır.
AUDIENCE_VOICE veri yapısını oluşturarak content-indexer'a döndür.
Çıktı knowledge/audience-voice.md dosyasına eklenmek (append) edilmek üzere tasarlanmıştır.

Bu skill yorum yapmaz, sınıflandırır — analiz idea-generator'ın işidir.

---

## KAPSAM

Hangi videolar: Son 2 yayınlanmış video.
CONTENT_INDEX'ten own_videos listesinin ilk 2 elemanını al.
Yoksa knowledge/my-videos/ klasöründen en yeni 2 VID-XXX.md'yi oku.

Her /youtube komutunda son yayınlanan video için otomatik çağrılır.

---

## API PARAMETRELERİ

Endpoint: commentThreads.list
Part: snippet, replies
MaxResults: 20 (en alakali/populer yorumlar — kota tasarrufu)
Order: relevance (YouTube'un en alakali saydigi once gelir)
TextFormat: plainText
Kota maliyeti: ~2 birim/video (dusuk)

```python
youtube.commentThreads().list(
    part="snippet,replies",
    videoId=VIDEO_ID,
    maxResults=20,
    order="relevance",
    textFormat="plainText"
).execute()
```

Her yorum icin cekilen alanlar:
```
yorum_id:      comment.snippet.topLevelComment.id
metin:         comment.snippet.topLevelComment.snippet.textDisplay
begeni:        comment.snippet.topLevelComment.snippet.likeCount
tarih:         comment.snippet.topLevelComment.snippet.publishedAt
cevap_sayisi:  comment.snippet.totalReplyCount
```

Yazar adi knowledge/ dosyalarina yazilmaz — sadece islem sirasinda kullanilir.

---

## YORUM FİLTRESİ

Asagidaki yorumlari isleme alma:
- 5 kelimeden kisa olanlar ("harika video", "tesekkurler", "👍")
- Sadece emoji icerenler
- Spam link icerenler
- Kanal tanitim yorumlari

---

## KATEGORİZASYON — 4 KATEGORİ

Her filtrelenmis yorumu tek bir kategoriye ata.
Birden fazla ozellik varsa baskin olana gore siniflandir.

### Kategori 1 — SORU
Tanim: Izleyici bir seyi anlamak istiyor, bilgi talep ediyor.
Anahtar sinyaller: "?", "nasil", "nedir", "neden", "ne zaman", "hangi", "mumkun mu"
Ornekler:
- "LangChain'i Windows'ta nasil kurarım?"
- "Python bilmeden veri bilimi olur mu?"
- "Bu araclari kullanmak icin teknik gecmis sart mi?"

### Kategori 2 — İSTEK_KONU
Tanim: Izleyici belirli bir konuda video gormek istiyor.
Anahtar sinyaller: "anlatir misin", "yapar misin", "ceker misin", "hakkinda video",
"bekliyorum", "bekliyoruz", "istiyoruz", "sonraki videoda", "devam gelsin"
Ornekler:
- "CrewAI hakkinda da video yapar misin?"
- "AI Ajan kurulumu daha detayli gelsin"
- "Freelance veri bilimi konusunu bekliyorum"

### Kategori 3 — ELEŞTİRİ
Tanim: Izleyici teknik hata, eksiklik veya iyilestirme onerisi bildiriyor.
Anahtar sinyaller: "eksik", "anlamadim", "yanlis", "daha iyi olabilirdi", "hizli gectin",
ses/goruntu kalitesi sikayetleri, karsit gorusler
Ornekler:
- "Kurulum adimlarini cok hizli gectin"
- "Turkce kaynak linki de verseydin iyi olurdu"
- "Ses biraz derinden geliyor"

### Kategori 4 — ÖVGÜ
Tanim: Izleyici memnuniyetini, begenisini veya icerigin etkisini belirtiyor.
Anahtar sinyaller: "harika", "tesekkurler", "cok isime yaradi", "tam aradigim",
"harika olmus", "cok faydali"
Sadece kal: Icerik hakkinda spesifik bir sey soyleyen ovguler.
Jenerik "super" tipi yorumlar filtreden gecmez.
Ornekler:
- "Tam aradigim videoydu, hemen denedim"
- "Kariyer degistirme kismi cok gercekci"
- "Bu konuyu Turkce anlatan kimse yoktu, tesekkurler"

---

## SINIFLANDIRMA KARAR SIRASI

Her yorum icin bu sirada kontrol et, ilk eslesende dur:

1. "?" var mi veya sorgu kelimesi iceriyor mu?  -> SORU
2. Talep ifadesi var mi?                         -> ISTEK_KONU
3. Elestiri/sikayet/iyilestirme tonu var mi?    -> ELESTIRI
4. Spesifik begeni ifadesi var mi?              -> OVGU
5. Hicbiri -> filtrele, atla

---

## ÇIKTI FORMATI (AUDIENCE_VOICE)

```
AUDIENCE_VOICE = {
  "analiz_tarihi": "YYYY-MM-DD",
  "kapsanan_videolar": ["VID-001", "VID-002"],
  "toplam_yorum_cekilen": 40,
  "toplam_filtrelenen": 14,
  "kategorize_edilen": 26,

  "sorular": [
    {
      "vid_key": "VID-001",
      "yorum_id": "...",
      "metin": "LangChain'i Windows'ta nasil kurarım?",
      "begeni": 4,
      "tekrar_eden_tema": "kurulum / arac kullanimi"
    }
  ],

  "istek_konular": [
    {
      "vid_key": "VID-001",
      "yorum_id": "...",
      "metin": "CrewAI hakkinda da video yapar misin?",
      "begeni": 7,
      "istenen_konu": "CrewAI"
    }
  ],

  "elestiriler": [
    {
      "vid_key": "VID-001",
      "yorum_id": "...",
      "metin": "Kurulum adimlarini cok hizli gectin",
      "begeni": 2,
      "konu": "hiz / aciklama yeterliligi"
    }
  ],

  "ovguler": [
    {
      "vid_key": "VID-001",
      "yorum_id": "...",
      "metin": "Tam aradigim videoydu, hemen denedim",
      "begeni": 5,
      "ne_begendi": "pratik uygulanabilirlik"
    }
  ],

  "ozet": {
    "en_fazla_kategori": "Soru",
    "top_temalar": ["kurulum", "arac secimi", "kariyer gecisi"],
    "en_yuksek_begeni_yorum": "CrewAI hakkinda da video yapar misin?",
    "acil_oncelik": "CrewAI — 7 begeni, ISTEK_KONU",
    "genel_duygu": "Genel olarak pozitif, teknik kurulum konusunda merakli ve hafif kaygilı."
  }
}
```

---

## HATA YÖNETİMİ

Yorumlar kapali (video ayarlari):
-> "Comments are disabled for this video — VID-XXX atlandi" yaz.
-> Diger videodan devam et.
-> Hicbir videoda yorum yoksa AUDIENCE_VOICE = null dondur.

API quota asimi:
-> "Comments API quota asildi" yaz.
-> Dur, kullaniciya bildir.
-> knowledge/audience-voice.md'deki son bolumu referans al — devam edilebilir.

Video ID gecersiz:
-> Hatay raporla, o video icin islemi durdur.
-> Diger video varsa ondan devam et.

Filtreleme sonrasi 0 anlamli yorum:
-> "Anlamli yorum bulunamadi — VID-XXX" yaz.
-> AUDIENCE_VOICE.kategorize_edilen = 0 olarak dondur.
-> ozet.genel_duygu = "Yetersiz veri" yaz.
-> idea-generator bu durumu isler, zincir durmuyor.

20'den az ham yorum:
-> Tum mevcut yorumlari al, devam et.
-> AUDIENCE_VOICE basina "Uyari: Dusuk yorum hacmi — pattern guvenilirligi sinirli" notu ekle.

---

## SINIRLAR

- Yorum yazmaz, silmez, yanitlamaz — sadece okur
- Yazar adini knowledge/ dosyalarina yazmaz — gizlilik
- Sadece son 2 video — daha eskisine gitme
- maxResults=20 limitini asma — kota tasarrufu

---

**END fetch-comments**
