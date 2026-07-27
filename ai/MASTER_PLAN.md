# Bilgisayar Ağları ve İnternet - Türkçe Slayt Hazırlama Ana Planı (Master Plan)

## 1. Proje Amacı ve Kapsamı
Bu projenin amacı, Prof. Douglas E. Comer tarafından kaleme alınan **"Bilgisayar Ağları ve İnternet" (Computer Networks and Internets, 6th Edition)** kitabının ders notlarını (`Lecture_Notes.pdf` - 943 slayt, 7 modül) Üniversite Bilgisayar Mühendisliği lisans dersinde kullanılmak üzere Türkçeye çevirmek, modernize etmek ve **Marp (Markdown Presentation)** formatında düzenlemektir.

## 2. Telif Hakkı ve Atıf Politikası (Copyright Compliance)
Tüm hazırlanan slaytlarda ve belgelerde Prentice-Hall / Pearson Education telif hakkı kurallarına tam uyum sağlanacaktır.

* **Alt Bilgi (Footer)**: Her slaytın altında şu ibare yer alacaktır:
  > `© Douglas E. Comer / Prentice-Hall | Kaynak: netbook.cs.purdue.edu`
* **Kullanım Kapsamı**: Materyal üniversite içi eğitim, öğretim ve ders sunumu amacıyla hazırlanmaktadır. Detaylı bilgi için [COPYRIGHT.md](../COPYRIGHT.md) dosyasına bakabilirsiniz.

## 3. GitHub Proje Dizin Yapısı

```text
networks/
├── README.md                  # Ana GitHub tanıtım ve kullanım rehberi
├── COPYRIGHT.md               # Telif hakkı ve lisans bildirimleri
├── .gitignore                 # Derleme çıktıları ve geçici dosyaları hariç tutma
├── Makefile                   # Otomatik Marp PDF/HTML derleme betiği
├── templates/
│   └── slide-template.md      # Standart Marp slayt şablonu
├── slides/                    # Türkçe Marp sunum dosyaları
│   ├── mod01-introduction/
│   ├── mod02-applications/
│   ├── mod03-physical-layer/
│   ├── mod04-datalink-layer/
│   ├── mod05-internetworking/
│   ├── mod06-other-topics/
│   └── mod07-emerging-tech/
└── ai/                        # AI destekli çalışma belgeleri, takip ve notlar
    ├── MASTER_PLAN.md         # Ana plan ve strateji
    ├── PROGRESS.md            # İlerleme durumu ve tamamlanan slaytlar
    └── NOTES.md               # Türkçe Bilgisayar Ağları Terimler Sözlüğü
```

## 4. Modül Haritası

Ders notları 7 ana Modüle ayrılmıştır:

| Modül | İngilizce Başlık | Türkçe Başlık | Orijinal Sayfa Aralığı | Slayt Sayısı |
|---|---|---|---|---|
| **Modül 1** | Introductions, Course Overview, Protocols & Layering | Giriş, Ders Özeti, Protokoller ve Katmanlı Mimari | Sayfa 1 - 74 | 74 Slayt |
| **Modül 2** | Network Programming & Applications | Ağ Programlama ve Uygulama Katmanı | Sayfa 75 - 172 | 98 Slayt |
| **Modül 3** | Foundations of Data Communications & Physical Layer | Veri İletişimi Temelleri ve Fiziksel Katman | Sayfa 173 - 261 | 89 Slayt |
| **Modül 4** | Computer Network Technologies & Layer 2 Switching | Veri Bağı Katmanı, LAN, Ethernet, Wi-Fi, Anahtarlama | Sayfa 262 - 441 | 180 Slayt |
| **Modül 5** | Internetworking: IP, Routing & Transport Protocols | İnternet Çalışması: IP Adresleme, Yönlendirme, UDP, TCP | Sayfa 442 - 767 | 326 Slayt |
| **Modül 6** | Other Topics: Security, Management, Performance | Diğer Konular: Ağ Güvenliği, Ağ Yönetimi, Başarım ve NAT | Sayfa 768 - 895 | 128 Slayt |
| **Modül 7** | Emerging Technologies: SDN, Cloud, Mesh | Gelişen Teknolojiler: SDN, Bulut Bilişim, Kablosuz Ağlar | Sayfa 896 - 942 | 47 Slayt |
