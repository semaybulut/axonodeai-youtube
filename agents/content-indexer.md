# AJAN 1: content-indexer
# AxonodeAI YouTube Brain
# /youtube komutunun ilk ajanı

---

## GÖREV

İki paralel şeritten veri topla:
- Şerit A: Kendi kanalının YouTube Analytics verisi
- Şerit B: Belirlenen viral videoların public verisi

Bu ajan veri toplar, analiz yapmaz.
Analiz pattern-finder'ın işi.

---

## ŞERIT A — KENDİ KANAL ANALİTİĞİ

### Kullanılacak Skill
skills/fetch-analytics.md

### Çekilecek Veriler

Her video için (VID-001'den başla, tüm videolar):
video_id:          YouTube video ID
vid_key:           VID-XXX (primary key)
baslik:            Video başlığı
yayin_tarihi:      YYYY-MM-DD
tip:               Trend Analizi / Tutorial / Kariyer / Girişim
sure_dakika:       Video süresi
--- ANALİTİK ---
izlenme:           Toplam izlenme sayısı
benzersiz_izleyici: Unique viewer sayısı
ort_izlenme_suresi: Dakika:Saniye formatında
retention_orani:   Yüzde olarak
ctr:               Tıklanma oranı yüzde
izlenme_suresi:    Toplam dakika
--- TRAFIK KAYNAKLARI ---
oneri_sistemi:     Yüzde — YouTube öneri
arama:             Yüzde — YouTube arama
dis_trafik:        Yüzde — dış kaynak
direkt:            Yüzde — direkt link
--- ETKİLEŞİM ---
begeni:            Sayı
yorum:             Sayı
kaydetme:          Sayı
paylasim:          Sayı
abone_artisi:      Bu videodan gelen net abone
--- İZLEYİCİ ---
ort_yas:           Yaş aralığı
cinsiyet:          Yüzde dağılım
ulke_top3:         En çok izlenen 3 ülke

### Zaman Aralığı
- Son 28 gün için detaylı veri
- Tüm zamanlar için toplam izlenme ve abone

---

## ŞERIT B — VİRAL VİDEO ANALİZİ

### Kullanılacak Skill
skills/fetch-viral-videos.md

### Hedef Video Listesi

Aşağıdaki kriterlere uyan videoları bul ve analiz et:

**Niş:** Yapay zeka, veri bilimi, AI kariyer, AI araçları
**Dil:** Türkçe öncelikli, İngilizce de dahil
**Performans kriteri:** 50.000+ izlenme veya kanal ortalamasının 3 katı

**Aranacak kanallar ve video tipleri:**
Türkçe kanallar:

Yapay zeka kariyer içeriği üreten kanallar
Veri bilimi tutorial kanalları
AI araç tanıtım kanalları

İngilizce kanallar:

Data science career content
AI tools tutorials
Machine learning explainers

### Her Viral Video İçin Çekilecek Veriler
vpt_key:           VPT-XXX (primary key)
url:               YouTube URL
kanal:             Kanal adı
baslik:            Video başlığı
yayin_tarihi:      YYYY-MM-DD
sure_dakika:       Video süresi
izlenme:           Toplam izlenme
--- BAŞLIK ANALİZİ ---
baslik_formulu:    Hangi formül kullanılmış
baslik_karakter:   Kaç karakter
anahtar_kelime:    Başlıktaki güçlü kelimeler
sayi_var_mi:       Evet / Hayır
yil_var_mi:        Evet / Hayır
guclu_iddia_var_mi: Evet / Hayır
--- THUMBNAIL ANALİZİ ---
yuz_var_mi:        Evet / Hayır
metin_kelime_sayisi: Kaç kelime
renk_sema:         Dominant renkler
kontrast:          Yüksek / Orta / Düşük
ifade_tipi:        Merak / Şaşkınlık / Ciddiyet / Heyecan
--- HOOK ANALİZİ (İlk 30 saniye) ---
hook_tipi:         İddia / Soru / Şok / Hikaye / Veri
hook_suresi:       Kaç saniye
vadi_var_mi:       "Bu videoda X öğreneceksin" var mı
aciliyet_var_mi:   Neden şimdi izlemeli
--- YAPI ANALİZİ ---
giris_suresi:      İlk bölüme kaç dakikada geçiyor
bolum_sayisi:      Kaç ana bölüm
tahmini_retention: Yorumlardan ve like oranından tahmin
cta_tipi:          Hangi CTA kullanılmış

---

## ÇIKTI FORMATI
CONTENT_INDEX = {
own_videos: [
{
vid_key: "VID-001",
video_id: "GBVSl9UgIDQ",
baslik: "Python Öğrenmek Yetmiyor...",
yayin_tarihi: "2026-05-08",
tip: "Trend Analizi",
sure_dakika: X,
izlenme: X,
benzersiz_izleyici: X,
ort_izlenme_suresi: "X:XX",
retention_orani: X,
ctr: X,
oneri_sistemi: X,
arama: X,
dis_trafik: X,
begeni: X,
yorum: X,
kaydetme: X,
abone_artisi: X
},
...
],
viral_videos: [
{
vpt_key: "VPT-001",
url: "...",
kanal: "...",
baslik: "...",
izlenme: X,
baslik_formulu: "...",
hook_tipi: "...",
thumbnail_analiz: {...},
yapi_analiz: {...}
},
...
],
toplam_kanal_izlenme: X,
toplam_abone: X,
analiz_tarihi: "YYYY-MM-DD"
}
---

## HATA YÖNETİMİ

**Analytics API erişim hatası:**
→ Dur. "Analytics API bağlantısı kurulamadı" yaz.
→ .env dosyasındaki credentials'ı kontrol et mesajı ver.
→ Devam etme.

**Viral video verisi eksik:**
→ Eksik alanı null bırak, devam et.
→ Eksik alanları raporda belirt.

**Quota aşımı:**
→ Dur. "YouTube API quota aşıldı" yaz.
→ Devam etme, önce onay al.

CRITICAL: API Fallback Logic
* fetch-analytics veya fetch-viral-videos skillerini çalıştırırken herhangi bir API hatası (Quota limit, Connection Error, 429 Error vb.) alırsan süreci durdurma.
* Böyle bir durumda doğrudan knowledge/analytics-snapshot.md dosyasını oku.
* CONTENT_INDEX raporunu bu snapshot verilerine dayanarak oluştur ve raporun başına "⚠️ VERİ KAYNAĞI: API Hatası nedeniyle snapshot kullanıldı" notunu düş.

---

## SINIRLAR

- Bu ajan veri toplar, yorum yapmaz
- Veriyi düzeltme, olduğu gibi ilet
- API'den gelmeyen veriyi tahmin etme
- Eksik veri varsa null yaz, uydurma

---

**END content-indexer**
