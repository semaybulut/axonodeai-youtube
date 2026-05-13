# SKILL: write-knowledge
# AxonodeAI YouTube Brain
# Yerel Bilgi Tabanı Yazımı — knowledge/ Klasörü Yönetimi

---

## GÖREV

Üretilen analizleri, stratejik güncellemeleri ve izleyici seslerini
knowledge/ klasörüne hiyerarşik ve silinmez şekilde yaz.
Bu skill /youtube komutunun final adımında çağrılır.

---

## DOSYA DAVRANIŞ TABLOSU

| Dosya/Klasör | Yol | Mod | Ne Zaman |
|---|---|---|---|
| Rapor arşivi | `knowledge/outputs/rapor/YYYY-MM-DD-youtube-rapor.md` | CREATE | Her /youtube ve /youtube-seri sonunda |
| İzleyici sesi — Global | `knowledge/audience-voice.md` Bölüm A | UPDATE | Her /youtube'da AUDIENCE_VOICE varsa |
| İzleyici sesi — Arşiv | `knowledge/audience-voice.md` Bölüm B | APPEND | Her /youtube'da AUDIENCE_VOICE varsa |
| Analytics snapshot (son) | `knowledge/analytics-snapshot.md` | OVERWRITE | Her /youtube çalışmasında |
| Analytics snapshot (arşiv) | `knowledge/outputs/snapshot/YYYY-MM-DD-snapshot.md` | CREATE | Sadece --update flag ile |
| Video profili (yayında) | `knowledge/my-videos/VID-XXX.md` | CREATE / UPDATE | YouTube URL'si olan videolar; analitik geldiyse güncelle |
| Video profili (pipeline) | `knowledge/pipeline/VID-XXX.md` | CREATE / UPDATE | SEO hazır, planlandı, çekimde — YouTube URL'si henüz yok |
| Viral video analizi | `knowledge/viral-patterns/VPT-XXX.md` | CREATE | Yeni VPT analiz edilince |
| Pattern kütüphanesi | `knowledge/viral-mechanism-library.md` | APPEND / UPDATE | Yeni pattern bulununca |
| Başarısızlık kaydı | `knowledge/viral-mechanism-library.md` → BAŞARISIZ DENEYLER bölümü | APPEND | Her /youtube Hafıza Damıtma adımında |
| İçerik takvimi | `knowledge/content-calendar.md` | UPDATE | idea-generator yeni fikir üretince |
| Haftalık ortalamalar | `knowledge/outputs/kanal-haftalik-ortalamalar.md` | APPEND | Her /youtube-publish --update'te |

**Mod açıklamaları:**
- CREATE → Yeni dosya oluştur, varsa üzerine yazma
- UPDATE → Sadece değişen bölümü güncelle, geri kalanına dokunma
- OVERWRITE → Tüm dosyayı yeniden yaz (sadece analytics-snapshot.md)
- APPEND → Dosyanın sonuna yeni blok ekle, eskiye dokunma

---

## YAZILACAK DOSYALAR

```
knowledge/
├── my-videos/VID-XXX.md              <- Sadece YAYINDA olan videolar (YouTube URL'si var)
├── pipeline/VID-XXX.md               <- SEO hazır / planlandı / çekimde (YouTube URL'si yok)
├── viral-patterns/VPT-XXX.md         <- Her viral video için analiz
├── audience-voice.md                 <- İzleyici sesi
├── viral-mechanism-library.md        <- Temizlenmiş pattern kütüphanesi
├── content-calendar.md               <- Yayın takvimi
├── analytics-snapshot.md             <- Son analytics özeti (Üzerine yazılır)
└── outputs/
    ├── rapor/                        <- Her /youtube çıktısı (Kalıcı)
    ├── snapshot/                     <- Haftalık analytics arşivi (Kalıcı)
    └── kanal-haftalik-ortalamalar.md <- Kanal büyüme takibi (Kalıcı/Satır eklenir)
```

### İki klasör arasındaki kural

`knowledge/pipeline/VID-XXX.md` → `knowledge/my-videos/VID-XXX.md` geçişi:
/youtube-publish VID-XXX çalıştırılınca:
1. pipeline/VID-XXX.md içine YouTube URL ve video_id ekle
2. Dosyayı my-videos/ klasörüne taşı
3. pipeline/ altındaki dosyayı sil

---

## DOSYA 1 — VID-XXX.md (Her Video İçin)

Konum:
- `knowledge/pipeline/VID-XXX.md` → YouTube URL'si olmayan (SEO hazır, planlandı, çekimde)
- `knowledge/my-videos/VID-XXX.md` → YouTube URL'si olan, yayındaki videolar

Ne zaman: Yeni video eklenince veya analytics güncellenince

### Şablon
```markdown
# VID-XXX — [Video Başlığı]
**Tip:** [Trend Analizi / Tutorial / Kariyer / Girişim]
**Yayın Tarihi:** YYYY-MM-DD
**YouTube URL:** https://youtu.be/[video_id]
**video_id:** [video_id]
**Durum:** [Planlandı / Yayında / Arşiv]
**Son Güncelleme:** YYYY-MM-DD

---

## SEO

**Başlık:** [Başlık — max 60 karakter]
**Taglar:** [tag1, tag2, tag3...]
**Thumbnail:** [renk hex] + [metin]

---

## ANALİTİK

| Metrik | Değer | Hedef | Durum |
|--------|-------|-------|-------|
| İzlenme | X | — | — |
| CTR | X% | >%3 | ✅/⚠️/❌ |
| Retention | X% | >%40 | ✅/⚠️/❌ |
| Yorum | X | — | — |
| Abone Artışı | X | — | — |

**Trafik Kaynakları:**
- Öneri sistemi: X%
- Arama: X%
- Dış trafik: X%
- Direkt: X%

---

## PERFORMANS NOTLARI

**Güçlü yönler:**
- [Ne iyi çalıştı]

**Alarm:**
- [Sorun varsa]

**Pattern bağlantısı:**
- Başlık formülü: [X] → CTR [X]%
- Hook tipi: [X] → Retention [X]%

---

## BAĞLANTILAR

**Bir önceki video:** [[VID-XXX]]
**Bir sonraki video:** [[VID-XXX]]
**Kullanılan viral pattern:** [[VPT-XXX]]
```

---

## DOSYA 2 — VPT-XXX.md (Her Viral Video İçin)

Konum: knowledge/viral-patterns/VPT-XXX.md
Ne zaman: fetch-viral-videos yeni viral video analiz edince

### Şablon
```markdown
# VPT-XXX — [Video Başlığı]
**Kanal:** [Kanal adı]
**URL:** [YouTube URL]
**İzlenme:** [Sayı]
**Yayın Tarihi:** YYYY-MM-DD
**Analiz Tarihi:** YYYY-MM-DD

---

## BAŞLIK ANALİZİ
Formül: [Formül 1/2/3/4/5]
Karakter: [XX/60]
Güçlü kelimeler: [kelime1, kelime2]

---

## THUMBNAIL ANALİZİ
Yüz var mı: Evet / Hayır
Metin kelime sayısı: X
Renk şema: [renkler]
Kontrast: Yüksek / Orta / Düşük
İfade tipi: Merak / Şaşkınlık / Ciddiyet

---

## HOOK ANALİZİ (İlk 30 sn)
Hook tipi: [İddia / Soru / Şok / Hikaye / Vadi]
Vadi var mı: Evet / Hayır
Aciliyet var mı: Evet / Hayır

---

## KULLANILABILIRLIK
AxonodeAI için uygulanabilir mi: Evet / Hayır / Kısmen
Nasıl uygulanır: [Öneri]
```

---

## DOSYA 3 — audience-voice.md (İZLEYİCİ SESİ)

Konum: knowledge/audience-voice.md
Ne zaman: Her /youtube'da AUDIENCE_VOICE verisi gelince
Mod: İKİ KATMANLI — Bölüm A UPDATE, Bölüm B APPEND

### Bölüm A Güncelleme Kuralı (Master Table)
Master Table'da eşleşen konu (aynı tema/talep) VAR:
→ Frekansı +1 artır
→ Son Tarihi bugünle güncelle
→ Kaynak Video sütununa yeni VID key'i ekle (virgülle)
→ Yeni satır açma

Master Table'da eşleşen konu YOK:
→ Yeni satır ekle
→ Durum: "⏳ Bekliyor"

Video planlandıysa:
→ Durum: "📋 Planlandı ([VID-XXX])"

Video yayınlandıysa:
→ Durum: "✅ Yanıtlandı"

### Bölüm B Ekleme Kuralı (Arşiv)
Dosyanın "# BÖLÜM B — PERİYODİK ARŞİV" satırından hemen sonra yeni blok ekle:

```markdown
## [YYYY-MM-DD] — [VID-XXX], [VID-XXX]

### Anlık Özet
Toplam yorum çekilen:  X
Toplam filtrelenen:    X
Kategorize edilen:     X
En fazla kategori:     [Kategori]
Acil öncelik:          [Konu] — X frekans
Genel duygu:           [Duygu]

### SORULAR
| VID | Yorum (özet) | Beğeni | Tema |
|-----|--------------|--------|------|
| [VID-XXX] | [yorum] | X | [tema] |

### İSTEK KONULAR
| VID | Yorum (özet) | Beğeni | İstenen Konu |
|-----|--------------|--------|--------------|
| [VID-XXX] | [yorum] | X | [konu] |

### ELEŞTİRİLER
| VID | Yorum (özet) | Beğeni | Konu |
|-----|--------------|--------|------|
| [VID-XXX] | [yorum] | X | [konu] |

### ÖVGÜLER
| VID | Yorum (özet) | Beğeni | Ne Beğendi |
|-----|--------------|--------|------------|
| [VID-XXX] | [yorum] | X | [ne beğendi] |
```

---

## DOSYA 4 — viral-mechanism-library.md

Konum: knowledge/viral-mechanism-library.md
Ne zaman: Yeni pattern bulununca

### Yeni Pattern Formatı
```markdown
## PATTERN — [PATTERN ADI]
**ID:** VPT-XXX
**Kategori:** [Hook / Başlık / Thumbnail / Yapı]
**Kaynak video:** VPT-XXX
**İzlenme:** X
**Doğrulama:** [Kaç videoda test edildi]

Kanıtlanmış: EVET / HAYIR
Kanıt kaynağı: [[VID-XXX]] (%X retention), [[VID-XXX]] (%X retention)
Son güncelleme: YYYY-MM-DD

**Gözlem:** [Ne yapıyor]
**Neden çalışıyor:** [Analiz]
**AxonodeAI uygulaması:** [Spesifik öneri]
**Kullanıldığı videolarım:** [[VID-XXX]], [[VID-XXX]]
**Ekleme tarihi:** YYYY-MM-DD
```

2+ videoda doğrulandıysa → başlığa "— KANITLANMIŞ" etiketi ekle.

---

## DOSYA 5 — content-calendar.md

Konum: knowledge/content-calendar.md
Ne zaman: idea-generator yeni fikir üretince
Mantık: Tablo güncellenir — Sheets ile senkron

### Şablon
```markdown
# İÇERİK TAKVİMİ
**Son Güncelleme:** YYYY-MM-DD

## YAYIN TAKVİMİ

| VID Key | Tip | Başlık | Yayın Tarihi | Durum |
|---------|-----|--------|--------------|-------|
| VID-001 | Trend Analizi | Python Öğrenmek Yetmiyor | 2026-05-08 | ✅ Yayında |
| VID-002 | Tutorial | AI Agent Sistemleri | 2026-05-14 | 📋 Planlandı |

## VERİLEN SÖZ TAKİBİ

| Söz | Verildiği Video | Hedef Video | Durum |
|-----|-----------------|-------------|-------|
| AI Agent anlatacağım | VID-001 | VID-002 | ⏳ Bekliyor |
```

AUDIENCE_VOICE kaynaklı fikirleri eklerken durum notu belirt:
```markdown
| VID-005 | Tutorial | [Konu] | YYYY-MM-DD | 💡 Fikir (İzleyici Talebi) |
```

---

## DOSYA 6 — analytics-snapshot.md

Konum: knowledge/analytics-snapshot.md
Ne zaman: Her /youtube çalışmasında
Mantık: Tüm dosyayı yeniden yaz (sadece son snapshot tutulur)

### Raporda Fallback Bilgisi
E�er herhangi bir şerit fallback kullandıysa snapshot'ın başına not ekle:
```markdown
# ANALİTİK SNAPSHOT
**Son Güncelleme:** YYYY-MM-DD HH:MM
**Veri Kaynağı:** API (normal) / ⚠️ Snapshot (API hatası nedeniyle)
```

---

## DOSYA 7 — RAPORLAR (ARŞİV)

Konum: knowledge/outputs/rapor/YYYY-MM-DD-youtube-rapor.md
Ne zaman: Her /youtube veya /youtube-seri sonunda
Mantık: CREATE — yeni dosya, eskiler silinmez

Rapor başlığına ekle:
```markdown
**Tarih:** YYYY-MM-DD HH:MM
**Veri Kaynakları:**
- Şerit A: API / ⚠️ Snapshot
- Şerit B: API / ⚠️ Arşiv (viral-patterns/)
- Şerit C: API / ⚠️ Snapshot (audience-voice.md)
```

---

## DOSYA 8 — SNAPSHOT ARŞİVİ

Konum: knowledge/outputs/snapshot/YYYY-MM-DD-snapshot.md
Ne zaman: /youtube-publish VID-XXX --update sonrasında
Mantık: analytics-snapshot.md'nin o günkü tam kopyası

---

## DOSYA 9 — KANAL HAFTALIK ORTALAMALAR

Konum: knowledge/outputs/kanal-haftalik-ortalamalar.md
Ne zaman: Her /youtube-publish --update çalışınca
Mantık: En alta YENİ SATIR ekle, eski satırlara asla dokunma

```
Tarih,Video Sayısı,Ort. CTR,Ort. Retention,Ort. İzlenme,Ort. Beğeni,Ort. Yorum
YYYY-MM-DD,X,%X,%X,Sayı,%X,%X
```

---

## YAZMA KURALLARI

- Mevcut dosyayı önce oku, sadece değişen kısmı güncelle
- Bağlantıları `[[VID-XXX]]` veya `[[VPT-XXX]]` formatında yaz
- Tarihleri her zaman `YYYY-MM-DD` formatında yaz
- Snapshot ve rapor dosyalarına `HH:MM` saatini ekle
- Boş alan bırakma — veri yoksa `—` veya `Henüz veri yok` yaz
- Silme yapma — güncelle veya ekle
- Klasör kontrolü: Yazma öncesi `outputs/rapor/` ve `outputs/snapshot/` varlığını kontrol et, yoksa oluştur

---

## HATA YÖNETİMİ

**Dosya bulunamıyor:**
→ Şablonu kullanarak yeni dosya oluştur
→ "VID-XXX.md oluşturuldu" yaz
→ Devam et

**Klasör erişimi yok:**
→ "knowledge/outputs/ alt klasörlerine erişilemiyor" yaz
→ Kullanıcıdan onay al, oluştur

**Snapshot eksik (arşivleme sırasında):**
→ Kullanıcıyı bildir
→ Mevcut analytics-snapshot.md içeriğiyle devam et

**Yazma izni yok:**
→ "knowledge/ klasörüne yazma izni yok" yaz
→ Dur

**Veri eksik:**
→ `—` yaz
→ Devam et

---

## SINIRLAR

- Başlık satırlarını değiştirme
- Primary key (VID-XXX, VPT-XXX) formatını değiştirme
- Arşiv dosyalarını silme veya üzerine yazma (outputs/rapor/, outputs/snapshot/, kanal-haftalik-ortalamalar.md)
- audience-voice.md'de eski Bölüm B bloklarına dokunma
- Yorum sahibi adlarını dosyalara yazma — gizlilik

---

**END write-knowledge**
