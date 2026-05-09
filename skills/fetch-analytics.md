# SKILL: fetch-analytics
# AxonodeAI YouTube Brain
# YouTube Analytics API — OAuth ile tam erişim

---

## GÖREV

YouTube Analytics API ve YouTube Data API v3 kullanarak
kanalın tüm analitik verilerini çek.
Bu skill content-indexer tarafından çağrılır.

---

## GEREKLİ KURULUM

### Gerekli API'ler
YouTube Data API v3        → video metadata
YouTube Analytics API      → gerçek analitik veriler

### .env Dosyası
YOUTUBE_CLIENT_ID=
YOUTUBE_CLIENT_SECRET=
YOUTUBE_REFRESH_TOKEN=
YOUTUBE_CHANNEL_ID=
GOOGLE_SHEETS_ID=

### OAuth Kurulum Adımları (Bir Kere Yapılır)
console.cloud.google.com → Proje: axonodeai
API & Services → Enable APIs:

YouTube Data API v3 → Enable
YouTube Analytics API → Enable


OAuth consent screen:

User type: External
App name: axonodeai-youtube
Scopes ekle:
https://www.googleapis.com/auth/youtube.readonly
https://www.googleapis.com/auth/yt-analytics.readonly
https://www.googleapis.com/auth/spreadsheets


Credentials → Create Credentials → OAuth 2.0 Client ID

Application type: Desktop app
İndir: client_secret.json


İlk token alma (terminalde bir kere):
pip install google-auth-oauthlib google-api-python-client
python scripts/get_token.py
Çıkan refresh_token'ı .env'e yaz

### Token Script (scripts/get_token.py)
```python
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    'https://www.googleapis.com/auth/youtube.readonly',
    'https://www.googleapis.com/auth/yt-analytics.readonly',
    'https://www.googleapis.com/auth/spreadsheets'
]

flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json', SCOPES)
credentials = flow.run_local_server(port=0)

print("ACCESS TOKEN:", credentials.token)
print("REFRESH TOKEN:", credentials.refresh_token)
```

---

## API ÇAĞRILARI

### Çağrı 1 — Kanal Bilgileri

GET https://www.googleapis.com/youtube/v3/channels
params:
part: snippet,statistics
mine: true
Dönen veriler:

Kanal adı
Toplam abone sayısı
Toplam izlenme sayısı
Toplam video sayısı
Kanal ID

### Çağrı 2 — Video Listesi
GET https://www.googleapis.com/youtube/v3/search
params:
part: snippet
channelId: [CHANNEL_ID]
type: video
order: date
maxResults: 50
Dönen veriler:

Video ID listesi
Başlıklar
Yayın tarihleri

### Çağrı 3 — Video Detayları
GET https://www.googleapis.com/youtube/v3/videos
params:
part: snippet,statistics,contentDetails
id: [video_id_listesi virgülle]
Dönen veriler:

İzlenme sayısı (public)
Beğeni sayısı
Yorum sayısı
Video süresi
Açıklama
Taglar

### Çağrı 4 — Analytics (Her Video İçin)
GET https://youtubeanalytics.googleapis.com/v2/reports
params:
ids: channel==MINE
startDate: [video_yayin_tarihi]
endDate: [bugün]
metrics: views,estimatedMinutesWatched,averageViewDuration,
averageViewPercentage,subscribersGained,
subscribersLost,likes,comments,shares,
cardClickRate,cardTeaserClickRate
dimensions: video
filters: video==[video_id]
Dönen veriler:

Gerçek izlenme sayısı
Toplam izlenme süresi (dakika)
Ortalama izlenme süresi
Ortalama izlenme yüzdesi (retention)
Abone artışı/kaybı
Etkileşim metrikleri

### Çağrı 5 — Trafik Kaynakları
GET https://youtubeanalytics.googleapis.com/v2/reports
params:
ids: channel==MINE
startDate: [video_yayin_tarihi]
endDate: [bugün]
metrics: views
dimensions: insightTrafficSourceType
filters: video==[video_id]
Dönen veriler:

YT_SEARCH: Arama trafiği
SUGGESTED_VIDEO: Öneri sistemi
EXTERNAL: Dış trafik
DIRECT: Direkt
BROWSE_FEATURES: Ana sayfa / Shorts feed

### Çağrı 6 — CTR (Click-Through Rate)
GET https://youtubeanalytics.googleapis.com/v2/reports
params:
ids: channel==MINE
startDate: [video_yayin_tarihi]
endDate: [bugün]
metrics: impressions,impressionClickThroughRate
dimensions: video
filters: video==[video_id]
Dönen veriler:

Gösterim sayısı
CTR yüzdesi

### Çağrı 7 — İzleyici Demografisi
GET https://youtubeanalytics.googleapis.com/v2/reports
params:
ids: channel==MINE
startDate: [30 gün önce]
endDate: [bugün]
metrics: viewerPercentage
dimensions: ageGroup,gender
Dönen veriler:

Yaş grupları ve yüzdeleri
Cinsiyet dağılımı

---

## VERİ BİRLEŞTİRME

Tüm çağrılardan gelen veriyi tek objeye birleştir:

```python
video_profile = {
    "vid_key": "VID-001",
    "video_id": "GBVSl9UgIDQ",
    "baslik": "...",
    "yayin_tarihi": "2026-05-08",
    "sure_dakika": 12,

    # Analytics
    "izlenme": 0,
    "ort_izlenme_suresi": "0:00",
    "retention_orani": 0.0,
    "ctr": 0.0,
    "izlenme_suresi_dakika": 0,

    # Trafik
    "trafik": {
        "oneri": 0.0,
        "arama": 0.0,
        "dis": 0.0,
        "direkt": 0.0,
        "anasayfa": 0.0
    },

    # Etkileşim
    "begeni": 0,
    "yorum": 0,
    "paylasim": 0,
    "abone_artisi": 0,

    # CTR
    "gosterim": 0,
    "ctr_yuzdesi": 0.0
}
```

---

## HATA YÖNETİMİ

**401 Unauthorized:**
→ "OAuth token geçersiz veya süresi dolmuş" yaz.
→ "scripts/get_token.py'yi tekrar çalıştır" mesajı ver.
→ Dur.

**403 Forbidden:**
→ "API erişim izni yok, scope'ları kontrol et" yaz.
→ Dur.

**429 Too Many Requests:**
→ "Quota aşıldı, yarın tekrar dene" yaz.
→ Dur.

**Video verisi boş:**
→ Yeni kanal olabilir, analytics henüz oluşmamış.
→ Mevcut veriyi al, eksik alanları null bırak.
→ "VID-XXX için analytics henüz yok" notu ekle.

---

## QUOTA TAKİBİ

YouTube Data API v3: 10.000 unit/gün

video.list isteği: 1 unit
search.list isteği: 100 unit
channels.list isteği: 1 unit
Analytics API: ayrı quota, limit yok

Her /youtube çalışmasında tahmini kullanım:
- channels.list: 1 unit
- search.list: 100 unit
- video.list (50 video): 50 unit
- Toplam: ~151 unit (limitin çok altında)

---

**END fetch-analytics**
