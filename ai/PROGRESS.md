# İlerleme Durumu (Progress Tracking)

Bu belge, **Bilgisayar Ağları ve İnternet** dersi Türkçe Marp slaytlarının hazırlanma durumunu takip eder.

Durum Simgeleri:
- 🔴 **Henüz Başlamadı** (Not Started)
- 🟡 **Taslak Aşamasında / Çevriliyor** (In Progress)
- 🟢 **Tamamlandı ve Gözden Geçirildi** (Completed & Reviewed)

---

## Genel Özet
- **Toplam Modül Sayısı**: 7 Modül
- **Toplam Slayt Sayısı (Orijinal PDF)**: ~943 Slayt
- **Oluşturulan Slayt Sayısı (Türkçe)**: ~784 Slayt (build-up slaytlar birleştirildi)
- **Tamamlanan Modüller**: 7 / 7 (taslak)
- **Görseller**: Tüm modüllerde placeholder — yakında eklenecek
- **Genel İlerleme**: Taslak %100 · Gözden Geçirilmiş %28 (Mod1+Mod2)

---

## Modül Bazlı Detaylı İlerleme Tablosu

| Modül | Başlık / Konu | Orijinal Slayt | Oluşturulan Slayt | Hedef Slayt Dosyası | Durum | Notlar |
|---|---|---|---|---|---|---|
| **Modül 1** | Giriş, Ders Özeti, Protokoller ve Katmanlama | 74 | ~70 | `slides/mod01-introduction/mod01_giris_ve_katmanlama.md` | 🟢 Tamamlandı | Orijinal görseller (300 DPI, şeffaf PNG) entegre. |
| **Modül 2** | Ağ Programlama ve Uygulama Katmanı | 98 | ~83 | `slides/mod02-applications/mod02_uygulama.md` | 🟢 Tamamlandı | Slayt slayt PDF ile karşılaştırılarak gözden geçirildi. SMTP oturum renklendirmesi, placeholder görseller mevcut. |
| **Modül 3** | Veri İletişimi Temelleri ve Fiziksel Katman | 89 | 70 | `slides/mod03-physical-layer/mod03_fiziksel.md` | 🟡 Taslak Hazır | Metin tamam, görseller placeholder. Slayt slayt gözden geçirme yapılmadı. |
| **Modül 4** | Veri Bağı Katmanı, LAN, Ethernet, Wi-Fi | 180 | 125 | `slides/mod04-datalink-layer/mod04_veribagi.md` | 🟡 Taslak Hazır | Metin tamam, görseller placeholder. Slayt slayt gözden geçirme yapılmadı. |
| **Modül 5** | İnternet Çalışması: IP, Yönlendirme, Taşıma Katmanı | 326 | 232 | `slides/mod05-internetworking/mod05_internetworking.md` | 🟡 Taslak Hazır | Metin tamam, görseller placeholder. Slayt slayt gözden geçirme yapılmadı. |
| **Modül 6** | Ağ Güvenliği, Ağ Yönetimi, Başarım ve NAT | 128 | 112 | `slides/mod06-other-topics/mod06_diger_konular.md` | 🟡 Taslak Hazır | Metin tamam, görseller placeholder. Slayt slayt gözden geçirme yapılmadı. |
| **Modül 7** | Gelişen Teknolojiler (SDN, Bulut, Sensör Ağları) | 47 | 44 | `slides/mod07-emerging-tech/mod07_yeni_teknolojiler.md` | 🟡 Taslak Hazır | Metin tamam, görseller placeholder. Slayt slayt gözden geçirme yapılmadı. |

---

## Güncelleme Günlüğü (Changelog)
* **2026-08-06**: Modül 3-7 taslak slaytları oluşturuldu. Görsel içeren slaytlar placeholder bırakıldı (`> 📷 [Görsel: ...]`). Build-up (kademeli) slaytlar birleştirildi. Makefile'a `--html` bayrağı eklendi, CSS'e protokol log renk stilleri (`.srv` kırmızı, `.cli` mavi) eklendi.
* **2026-08-06**: Modül 2 son gözden geçirme: SMTP, FTP, TELNET, DNS, Özet slaytları orijinal PDF'e sadık şekilde güncellendi. Host → "Ana Bilgisayar" terminolojisi düzeltildi.
* **2026-07-31**: Modül 2 slaytları sayfa sayfa gözden geçirilerek revize edildi (PDF Sayfa 75-117 / Slayt 1-31). "Contact" terimi "bağlantı / bağlantı kurma" olarak güncellendi.
* **2026-07-29**: Modül 1 görsel ve slayt yapısı revize edildi. Kullanılmayan SVG dosyaları temizlendi, tüm şekiller şeffaf background PNG olarak entegre edildi.
* **2026-07-28**: Modül 1 Türkçe Marp slaytları tamamlandı. 3B İnternet Referans Modeli SVG çizimi üretildi.
* **2026-07-27**: Proje yapısı, Ana Plan, İlerleme Belgesi, Terimler Sözlüğü ve Marp Şablonu oluşturuldu.

---

## Sıradaki Adımlar
1. Modül 3-7 için görsellerin PDF'ten çıkarılması ve placeholder'ların gerçek görsellerle değiştirilmesi.
2. Modül 3 slayt slayt gözden geçirme (Modül 2 sürecindeki gibi).
3. Tüm modüller derlendikten sonra `make all` ile HTML/PDF çıktısı alınması.
