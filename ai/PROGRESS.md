# İlerleme Durumu (Progress Tracking)

Bu belge, **Bilgisayar Ağları ve İnternet** dersi Türkçe Marp slaytlarının hazırlanma durumunu takip eder.

Durum Simgeleri:
- 🔴 **Henüz Başlamadı** (Not Started)
- 🟡 **Taslak Aşamasında / Çevriliyor** (In Progress)
- 🟢 **Tamamlandı ve Gözden Geçirildi** (Completed & Reviewed)

---

## Genel Özet
- **Toplam Modül Sayısı**: 7 Modül
- **Toplam Slayt Sayısı**: 943 Slayt (Kaynak: `Lecture_Notes.pdf`)
- **Tamamlanan Modüller**: 1 / 7
- **Genel İlerleme**: %14.3

---

## Modül Bazlı Detaylı İlerleme Tablosu

| Modül | Başlık / Konu | Orijinal Slayt Sayısı | Hedef Slayt Dosyası | Durum | Notlar |
|---|---|---|---|---|---|
| **Modül 1** | Giriş, Ders Özeti, Protokoller ve Katmanlama | 74 | `slides/mod01-introduction/mod01_giris_ve_katmanlama.md` | 🟢 Tamamlandı | Slayt yapısı, terimler, şeffaf orijinal görseller (VPN dahil) ve temiz dizin yapısı ile tamamlandı. |
| **Modül 2** | Ağ Programlama ve Uygulama Katmanı | 98 | `slides/mod02-applications/mod02_uygulama.md` | 🔴 Henüz Başlamadı | Soketler, HTTP, DNS, SMTP, FTP |
| **Modül 3** | Veri İletişimi Temelleri ve Fiziksel Katman | 89 | `slides/mod03-physical-layer/mod03_fiziksel.md` | 🔴 Henüz Başlamadı | Sinyaller, İletim Ortamları, Modülasyon |
| **Modül 4** | Veri Bağı Katmanı, LAN, Ethernet, Wi-Fi | 180 | `slides/mod04-datalink-layer/mod04_veribagi.md` | 🔴 Henüz Başlamadı | Çerçeveleme, Köprüleme, L2 Anahtarlama |
| **Modül 5** | İnternet Çalışması: IP, Yönlendirme, Taşıma Katmanı | 326 | `slides/mod05-internetworking/mod05_internetworking.md` | 🔴 Henüz Başlamadı | IP, Subnetting, IPv6, UDP, TCP, BGP/OSPF |
| **Modül 6** | Ağ Güvenliği, Ağ Yönetimi, Başarım ve NAT | 128 | `slides/mod06-other-topics/mod06_diger_konular.md` | 🔴 Henüz Başlamadı | Kriptografi, Güvenlik Duvarları, SNMP |
| **Modül 7** | Gelişen Teknolojiler (SDN, Bulut, Sensor Ağları) | 47 | `slides/mod07-emerging-tech/mod07_gelisen_teknolojiler.md` | 🔴 Henüz Başlamadı | OpenFlow, Cloud Data Centers, Mesh |

---

## Güncelleme Günlüğü (Changelog)
* **2026-07-29**: Modül 1 görsel ve slayt yapısı revize edildi. Kullanılmayan SVG dosyaları temizlendi, tüm şekiller şeffaf background PNG olarak entegre edildi, VPN katmanlama slaytı eklendi ve 57-62. PDF slayt yapısı birebir korundu.
* **2026-07-28**: Modül 1 Türkçe Marp slaytları (`slides/mod01-introduction/mod01_giris_ve_katmanlama.md`) tamamlandı. 3B İnternet Referans Modeli SVG çizimi üretildi, Marp yerel görsel desteği (`--allow-local-files`) Makefile'a eklendi ve `make all` ile güncel PDF/HTML derlemeleri sağlandı.
* **2026-07-27**: Proje yapısı, Ana Plan (`MASTER_PLAN.md`), İlerleme Belgesi (`PROGRESS.md`), Terimler Sözlüğü (`NOTES.md`) ve Marp Şablonu (`templates/slide-template.md`) oluşturuldu.
