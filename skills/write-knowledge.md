# SKILL: write-knowledge
# AxonodeAI YouTube Brain
# knowledge/ klasörüne yaz — yerel vault güncelleme

---

## GÖREV

/youtube komutunun ürettiği tüm veriyi
knowledge/ klasörüne doğru formatta yaz.
Bu skill /youtube komutunun final adımında çağrılır.

---

## YAZILACAK DOSYALAR
knowledge/
├── my-videos/VID-XXX.md          ← Her video için profil
├── viral-patterns/VPT-XXX.md     ← Her viral video için analiz
├── viral-mechanism-library.md    ← Temizlenmiş pattern kütüphanesi
├── content-calendar.md           ← Yayın takvimi
└── analytics-snapshot.md         ← Son analytics özeti
---

## DOSYA 1 — VID-XXX.md (Her Video İçin)
Konum: knowledge/my-videos/VID-XXX.md
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

**En güçlü yön:**
[Hangi metrik iyi, neden]

**Geliştirilecek:**
[Hangi metrik düşük, ne yapılabilir]

**Pattern notları:**
[Bu videodan öğrenilen — bir sonraki videoya uygulanacak]

---

## İÇERİK YAPISI

**Hook tipi:** [İddia / Soru / Şok / Hikaye / Vadi]
**Bölüm sayısı:** X
**CTA tipi:** [Yorum / Abone / Sonraki video]

---

## BAĞLANTILAR

**Bir önceki video:** [[VID-XXX]]
**Bir sonraki video:** [[VID-XXX]]
**Bağlantılı IG post:** [IG post tarihi veya kodu]
**Kullanılan viral pattern:** [[VPT-XXX]]
```

---

## DOSYA 2 — VPT-XXX.md (Her Viral Video İçin)
Konum: knowledge/viral-patterns/VPT-XXX.md
Ne zaman: fetch-viral-videos yeni video analiz edince

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

**Başlık:** [Tam başlık]
**Karakter sayısı:** X/60
**Formül:** [Formül 1/2/3/4/5]
**Güçlü kelimeler:** [liste]
**Yıl var mı:** Evet/Hayır
**Sayı var mı:** Evet/Hayır
**Güçlü iddia var mı:** Evet/Hayır

---

## THUMBNAIL ANALİZİ

**Yüz var mı:** Evet/Hayır
**Metin:** [Thumbnail'daki kelimeler]
**Kelime sayısı:** X
**Arka plan rengi:** [hex veya tanım]
**Metin rengi:** [hex veya tanım]
**Kontrast:** Yüksek/Orta/Düşük
**İfade tipi:** [Merak/Şaşkınlık/Ciddiyet/Heyecan]
**Kompozisyon:** [Sol yüz sağ metin / diğer]

---

## HOOK ANALİZİ

**Hook tipi:** [İddia/Soru/Şok/Hikaye/Vadi]
**Açılış cümlesi:** [İlk cümle]
**Vadi var mı:** Evet/Hayır
**Hook süresi:** X saniye
**Transcript mevcut:** Evet/Hayır

---

## YAPI ANALİZİ

**Toplam süre:** X dakika
**Bölüm sayısı:** X
**Giriş süresi:** X dakika
**Chapter var mı:** Evet/Hayır
**CTA tipi:** [liste]

---

## AXONODEAI İÇİN

**Kullanılabilir mi:** Evet/Hayır/Kısmen
**En güçlü özellik:** [1 cümle]
**Nasıl uygularım:** [Spesifik öneri]
**Hangi video tipine uygun:** [Trend/Tutorial/Kariyer/Girişim]
**Öncelik:** Yüksek/Orta/Düşük

---

## BAĞLANTILAR

**Bu pattern kullanan videolarım:** [[VID-XXX]]
**Benzer pattern:** [[VPT-XXX]]
```

---

## DOSYA 3 — viral-mechanism-library.md
Konum: knowledge/viral-mechanism-library.md
Ne zaman: pattern-finder yeni pattern onaylayınca
Mantık: Ekleme yap, silme — sadece manuel

### Güncelleme Formatı

Dosyanın sonuna yeni pattern ekle:

```markdown
## PATTERN — [PATTERN ADI]
**ID:** VPT-XXX
**Kategori:** Hook / Başlık / Thumbnail / Yapı / CTA
**Kaynak video:** [VPT-XXX başlık]
**İzlenme:** X
**Doğrulama:** [Kaç videoda test edildi]

**Gözlem:**
[Ne yapıyor — spesifik ve somut]

**Neden çalışıyor:**
[Psikolojik veya algoritma gerekçesi]

**AxonodeAI uygulaması:**
[Benim için nasıl kullanırım — somut örnek]

**Kullanıldığı videolarım:**
- [[VID-XXX]] — nasıl uyguladım

**Ekleme tarihi:** YYYY-MM-DD
**Son güncelleme:** YYYY-MM-DD

---
```

### Dosya Başlığı (İlk Kurulumda Yaz)
```markdown
# VİRAL MEKANİZMA KÜTÜPHANESİ
**Owner:** Sema | AxonodeAI
**Son Güncelleme:** YYYY-MM-DD
**Toplam Pattern:** X

Bu dosya /youtube komutu çalıştıkça büyür.
Her pattern birden fazla videoda doğrulandıktan sonra
"Kanıtlanmış" olarak işaretlenir.

---

## KANITMLANMIŞ PATTERNLER
[Birden fazla videoda test edilmiş]

---

## TEST EDİLİYOR
[Henüz tek video verisi var]

---
```

---

## DOSYA 4 — content-calendar.md
Konum: knowledge/content-calendar.md
Ne zaman: idea-generator yeni fikir üretince
Mantık: Tablo güncellenir — Sheets ile senkron

### Şablon
```markdown
# İÇERİK TAKVİMİ
**Son Güncelleme:** YYYY-MM-DD

---

## YAYIN TAKVİMİ

| VID Key | Tip | Başlık | Yayın Tarihi | Durum |
|---------|-----|--------|--------------|-------|
| VID-001 | Trend Analizi | Python Öğrenmek Yetmiyor | 2026-05-08 | ✅ Yayında |
| VID-002 | Tutorial | AI Agent Sistemleri | 2026-05-14 | 📋 Planlandı |
| VID-003 | — | — | 2026-05-21 | 💡 Fikir |
| VID-004 | — | — | 2026-05-28 | 💡 Fikir |

---

## DURUM AÇIKLAMALARI

💡 Fikir      → idea-generator önerdi
📋 Planlandı  → Konu onaylandı, üretim başlamadı
🎬 Çekimde    → Aktif üretimde
✂️ Post       → Kurgu aşamasında
✅ Yayında    → Canlı
🗄️ Arşiv     → Yayından kaldırıldı

---

## İÇERİK DENGE (Son 5 Video)

| Tip | Sayı | Hedef |
|-----|------|-------|
| Trend Analizi | X | min 1/5 |
| Tutorial | X | min 1/5 |
| Kariyer/POV | X | min 1/5 |
| Girişim/Para | X | min 1/5 |

---

## VERİLEN SÖZ TAKİBİ

| Söz | Verildiği Video | Hedef Video | Durum |
|-----|-----------------|-------------|-------|
| AI Agent anlatacağım | VID-001 | VID-002 | ⏳ Bekliyor |
```

---

## DOSYA 5 — analytics-snapshot.md
Konum: knowledge/analytics-snapshot.md
Ne zaman: Her /youtube çalışmasında güncellenir
Mantık: Üzerine yaz — sadece son snapshot tutulur

### Şablon
```markdown
# ANALİTİK SNAPSHOT
**Son Güncelleme:** YYYY-MM-DD HH:MM

---

## KANAL ÖZETI

| Metrik | Değer | Önceki | Değişim |
|--------|-------|--------|---------|
| Toplam Abone | X | X | +X |
| Toplam İzlenme | X | X | +X |
| Son 28 Gün İzlenme | X | X | +X |

---

## VIDEO PERFORMANSLARI

| VID Key | Başlık | İzlenme | CTR | Retention | Durum |
|---------|--------|---------|-----|-----------|-------|
| VID-001 | Python... | X | X% | X% | ✅/⚠️/❌ |

---

## ALARMLAR

⚠️ Dikkat Gerektiren:
- [VID-XXX]: CTR %X — hedefin altında, thumbnail güncelle
- [VID-XXX]: Retention %X — hook sorunu olabilir

✅ İyi Performans:
- [VID-XXX]: CTR %X — ortalamanın üstünde

---

## TRAFIK ANALİZİ

**Öneri sistemi toplamı:** X%
**Arama toplamı:** X%
**Dış trafik toplamı:** X%

**En çok öneri getiren video:** VID-XXX
**En çok arama getiren video:** VID-XXX

---

## SONRAKİ /youtube İÇİN NOTLAR

[Bu snapshot'tan çıkan ve bir sonraki analizde
kontrol edilmesi gereken noktalar]
```

---

## YAZMA KURALLARI
Mevcut dosyayı önce oku
Sadece değişen kısmı güncelle
Bağlantıları [[VID-XXX]] formatında yaz
Tarihleri her zaman YYYY-MM-DD formatında yaz
Boş alan bırakma — veri yoksa "Henüz veri yok" yaz
Silme yapma — güncelle veya ekle

---

## HATA YÖNETİMİ

**Dosya bulunamıyor:**
→ Yeni oluştur, şablonu kullan
→ "VID-XXX.md oluşturuldu" yaz

**Yazma izni yok:**
→ "knowledge/ klasörüne yazma izni yok" yaz
→ Dur

**Veri eksik:**
→ "Henüz veri yok" yaz
→ Devam et

---

**END write-knowledge**