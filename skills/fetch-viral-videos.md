# SKILL: fetch-viral-videos
# AxonodeAI YouTube Brain
# Viral video analizi — public veri + manuel analiz

---

## GÖREV

Belirlenen nişte viral olan videoları bul.
Her video için başlık, thumbnail, hook, yapı analizini çıkar.
Bu skill content-indexer tarafından çağrılır.

---

## VİRAL VİDEO BULMA STRATEJİSİ

### Kriter 1 — Performans Eşiği
Türkçe kanallar için:

50.000+ izlenme VEYA
Kanal ortalamasının 3 katı izlenme

İngilizce kanallar için:

500.000+ izlenme VEYA
Kanal ortalamasının 5 katı izlenme

### Kriter 2 — Niş Uyumu
Dahil:

Yapay zeka kariyer içeriği
Veri bilimi tutorial
AI araç tanıtımı
Machine learning açıklama
AI ile para kazanma
Teknoloji kariyer geçişi
İşin geleceği / Future of work

Hariç:

Saf yazılım geliştirme (web, mobil)
Oyun geliştirme
Kripto / finans
Genel motivasyon

### Kriter 3 — Tazelik
Öncelikli: Son 90 gün
Kabul edilir: Son 12 ay
Hariç: 12 aydan eski (trendler değişiyor)

---

## ARAMA STRATEJİSİ

### YouTube Data API ile Arama
GET https://www.googleapis.com/youtube/v3/search
params:
part: snippet
q: [arama terimi]
type: video
order: viewCount
publishedAfter: [90 gün önce ISO format]
relevanceLanguage: tr
maxResults: 10

### Türkçe Arama Terimleri
"yapay zeka kariyer 2026"
"veri bilimi nasıl öğrenilir"
"AI araçları 2026"
"yapay zeka ile para kazanma"
"veri bilimi yol haritası"
"machine learning başlangıç"
"AI agent nedir"
"ChatGPT iş hayatı"
"veri bilimine geçiş"
"yapay zeka geleceği"

### İngilizce Arama Terimleri
"data science career 2026"
"AI tools for beginners"
"machine learning explained"
"AI agent tutorial"
"data science roadmap 2026"
"how to learn AI 2026"
"AI career change"
"future of work AI"

### Takip Edilecek Kanallar
Türkçe:

Axonode AI nişindeki Türkçe kanallar
Her /youtube çalışmasında güncellenir

İngilizce:

Data science / AI kariyer kanalları
100K+ abone, niş uyumlu

### Başlangıç Kanal Listesi (Manuel Eklenecek, Zamanla Büyür)

Türkçe:
- UC6rmKwzCf-PZh93ylgd1Q5w - Verinin Mutfağı
- UCsGwZ3006CuJWcA5J3UPVWw - CodeWithBOD
- UCsT0YIqwnpJCM-mx7-gSA4Q - TEDx Talks
- UCatnasFAiXUvWwH8NlSdd3A - Evrim Ağacı

İngilizce:
- UCeVMnSShP_Iviwkknt83cww - CodeWithHarry
- UC2UXDak6o7rBm23k3Vv5dww - Tina Huang
- UCKWaEZ-_VweaEx1j62do_vQ - IBM Technology
- UCV0qA-eDDICsRR9rPcnG7tw - Joma Tech
- UCLLw7jmFsvfIVaUFsLs8mlQ - Luke Barousse
- UCWv7vMbMWH4-V0ZXdmDpPBA - Programming with Mosh
- UC7cs8q-gJRlGwj4A8OmCmXg - Alex The Analyst
- UCBwmMxybNva6P_5VmxjzwqA - Apna College
- UCteRPiisgIoHtMgqHegpWAQ - Sundas Khalid
- UCktMIWomeuj4pwvBb-OBwMw - Infinite Codes
- UC_fyAp919RnkKmBrMXGwnUQ - Google Career Certificates
- UCJQJAI7IjbLcpsjWdSzYz0Q - Thu Vu
- UCU-aPpP8BxAd4mDoP0OL4jQ - Agatha
- UC8butISFwT-Wl7EV0hUK0BQ - freeCodeCamp.org
- UCCwwTJbIWJKnGNdT0Dk4b5Q — Ken Jee (data science career)
- UC7cs8q-gJRlGwj4A8OmCmXg — Alex The Analyst
- UCiT9RITQ9PW6BhXK0y2jaeg — Nicholas Renotte (ML tutorials)
- UCA-mWX9CvCTVFWRMb9bKc9w - Dan Martell
- UCQ4FNww3XoNgqIlkBqEAVCg - Iman Gadzhi
- UCk2U-Oqn7RXf-ydPqfSxG5g - Mel Robbins
- UCC8wczy7734jKPhiR2UkS9A - Wholesale Ted
- UCiGWNa6QK6CiKPvv5-YPv8g - Sabrina Ramonov
- UCdNj_PP__5kKtjZabuEjbqA - Dan Kieft
- UCwAnu01qlnVg1Ai2AbtTMaA - Jeff Su
- UC7kCeZ53sli_9XwuQeFxLqw - Ticker Symbol: YOU
- UCnhbNiPnXAdMOOHiVACiAvw - The Wade Report
- UCuvjQYKukKjVyhSVxQibgOw - The Calum Johnson Show
- UCW0cG4zyFG8oKAlOom4KonQ - Henrik Kniberg
- UC_RovKmk0OCbuZjA8f08opw - Futurepedia
- UCcrH_UUxL4KFjS3pwaXvMXA - Sandy Lee AI
- UCh9nVJoWXmFb7sLApWGcLPQ - codebasics
- UCkkgrhDCJheXQNIFqUVw0_g - ComputerConcepts
- UCZf_9SblvM8iTTkouFEcHtA - Marina Wyss - AI & Machine Learning
- UCDybamfye5An6p-j1t2YMsg - Mo Chen
- UC0GmdVKZhMM3Rmielp4oVAA - Stefanovic
- UC1BfD4tqpp-M7Y6zaAypupA - Christine Jiang
- UC5if156HvOYGeYgpdjFCVCw - Anton's Library
- UCuyfszBAd3gUt9vAbC1dfqA - Avery Smith | Data Analyst

---

## ANALİZ SÜRECİ

### Adım 1 — Video Listesi Oluştur
Arama API'den gelen sonuçlar + takip listesindeki kanallar
→ Performans kriterini geçenleri filtrele
→ Niş kriterini geçenleri filtrele
→ Tazelik kriterini geçenleri filtrele
→ Max 10 video seç (en yüksek performanslı)
→ VPT-001, VPT-002... olarak key ata

### Adım 2 — Public Veri Çek
GET https://www.googleapis.com/youtube/v3/videos
params:
part: snippet,statistics,contentDetails
id: [video_id]
Çekilen veriler:

İzlenme sayısı
Beğeni sayısı
Yorum sayısı
Video süresi
Başlık
Açıklama (ilk 500 karakter)
Taglar
Yayın tarihi

### Adım 3 — Başlık Analizi
Her video başlığı için analiz et:
UZUNLUK:

Karakter sayısı say
60 karakterin altında mı?

FORMÜL TESPİT:
Formül 1: [İddia] — [Yıl/Bağlam]  → örnek: "Python Yetmiyor — 2026"
Formül 2: [Soru] — [İpucu]         → örnek: "AI Nedir? — Her Şey Değişiyor"
Formül 3: [Sayı] [Konu] [Fayda]    → örnek: "5 AI Aracı — 2026 İçin"
Formül 4: Kontrarian               → örnek: "Kimse Söylemedi — Gerçek Şu"
Formül 5: Tutorial                 → örnek: "AI Agent Kurulumu — Adım Adım"
GÜÇLÜ KELIMELER:

Yıl var mı? (2026, 2025)
Sayı var mı? (5, 3, 10)
Güçlü iddia var mı? (yetmiyor, değişiyor, bitti)
Merak uyandırıcı mı? (kimse söylemedi, gerçek şu)
Fayda vaat ediyor mu? (nasıl, adım adım, rehber)

ANAHTAR KELİMELER:

Başlıktaki arama odaklı kelimeler neler?

### Adım 4 — Thumbnail Analizi
Thumbnail URL'yi çek:
snippet.thumbnails.maxres.url
Analiz et:
METIN:

Kaç kelime var?
Hangi kelimeler?
Font büyük mü?

GÖRSEL:

Yüz var mı?
İfade tipi nedir?

RENK:

Dominant arka plan rengi
Metin rengi
Kontrast yüksek mi?

KOMPOZISYON:

Yüz sol mu sağ mı?
Metin nerede?
Grafik element var mı?

3 SANİYE TESTİ:

Küçük ekranda mesaj anlaşılıyor mu?
Başlıkla birlikte güçlü mesaj veriyor mu?

### Adım 5 — Hook Analizi
NOT: Hook analizi için videonun transcript'i gerekiyor.
YouTube Data API transcript vermez.
Aşağıdaki yöntemleri sırayla dene:
Yöntem 1 — YouTube Transcript API (python kütüphanesi):
pip install youtube-transcript-api
from youtube_transcript_api import YouTubeTranscriptApi
transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['tr','en'])
İlk 30 saniyeyi al:
first_30 = [t for t in transcript if t['start'] <= 30]
Yöntem 2 — Manuel analiz notu:
Transcript alınamıyorsa:

Açıklamadan hook ipuçları çıkar
Yorum bölümünden izleyici tepkisini oku
"Hook analizi mevcut değil" notu ekle

Hook analiz kriterleri:

Açılış cümlesi nedir?
Hook tipi: İddia / Soru / Şok / Hikaye / Vadi
İzleyiciye vadi var mı?
Neden şimdi izlemeli sorusu cevaplanıyor mu?
Süre: kaç saniyede ana konuya geçiyor?

### Adım 6 — Yapı Analizi
contentDetails.duration'dan video süresini al.
Açıklamadaki chapter timestamp'lerini parse et.
Eğer chapter varsa:

Bölüm sayısı
Her bölüm süresi
Giriş süresi
Özet/CTA süresi

Eğer chapter yoksa:

Toplam süreyi not et
"Chapter analizi mevcut değil" yaz

CTA analizi (açıklamadan):

Yorum CTA'sı var mı?
Abone CTA'sı var mı?
Sonraki video bağlantısı var mı?

---

## ÇIKTI FORMATI

```python
viral_video = {
    "vpt_key": "VPT-001",
    "url": "https://youtube.com/watch?v=...",
    "video_id": "...",
    "kanal": "...",
    "kanal_id": "...",

    # Temel veriler
    "baslik": "...",
    "yayin_tarihi": "YYYY-MM-DD",
    "sure_dakika": 0,
    "izlenme": 0,
    "begeni": 0,
    "yorum": 0,
    "begeni_oran": 0.0,

    # Başlık analizi
    "baslik_analiz": {
        "karakter_sayisi": 0,
        "formul": "...",
        "guclu_kelimeler": [],
        "yil_var": True/False,
        "sayi_var": True/False,
        "iddia_var": True/False,
        "anahtar_kelimeler": []
    },

    # Thumbnail analizi
    "thumbnail_analiz": {
        "url": "...",
        "yuz_var": True/False,
        "metin_kelime_sayisi": 0,
        "metin_icerik": "...",
        "dominant_renk": "...",
        "metin_rengi": "...",
        "kontrast": "Yüksek/Orta/Düşük",
        "ifade_tipi": "...",
        "kompozisyon": "...",
        "axonodeai_icin_not": "..."
    },

    # Hook analizi
    "hook_analiz": {
        "mevcut": True/False,
        "acilis_cumlesi": "...",
        "hook_tipi": "...",
        "vadi_var": True/False,
        "sure_saniye": 0,
        "axonodeai_uygulamasi": "..."
    },

    # Yapı analizi
    "yapi_analiz": {
        "bolum_sayisi": 0,
        "giris_suresi_dakika": 0,
        "chapter_var": True/False,
        "cta_tipi": [],
        "axonodeai_uygulamasi": "..."
    },

    # Değerlendirme
    "axonodeai_icin": {
        "kullanilabilir_mi": "Evet/Hayır/Kısmen",
        "neden": "...",
        "en_guclu_ozellik": "...",
        "nasil_uyarlarim": "..."
    },

    "analiz_tarihi": "YYYY-MM-DD"
}
```

---

## VIRAL PATTERNS KLASÖRÜ GÜNCELLEME

Her analiz sonrası:
knowledge/viral-patterns/VPT-XXX.md oluştur
İçerik:
VPT-XXX — [Video Başlığı]
Kanal: ...
İzlenme: ...
Tarih: ...
Başlık Analizi
...
Thumbnail Analizi
...
Hook Analizi
...
Yapı Analizi
...
AxonodeAI İçin
...
---

## HATA YÖNETİMİ

**Arama sonucu boş:**
→ Farklı arama terimi dene (listeden bir sonraki)
→ 3 denemeden sonra "viral video bulunamadı" yaz

**Transcript alınamıyor:**
→ Yöntem 2'ye geç
→ "Hook analizi mevcut değil" notu ekle
→ Devam et

**Video private veya silindi:**
→ Listeyi geç
→ Bir sonraki videoya geç

**Quota hatası:**
→ Dur
→ "YouTube API quota aşıldı" yaz
→ Kaç video analiz edilebildiğini yaz

---

## SINIRLAR

- Public veri dışına çıkma
- Tahmin etme, veri ne diyorsa onu yaz
- Transcript yoksa hook bölümünü boş bırak
- Max 10 viral video per çalışma — quota koru

---

**END fetch-viral-videos**
