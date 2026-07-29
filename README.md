# Bilgisayar Ağları ve İnternet - Türkçe Ders Slaytları

[![Deploy Marp Slides to GitHub Pages](https://github.com/gtanisik/bilgisayar-aglari/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/gtanisik/bilgisayar-aglari/actions/workflows/deploy-pages.yml)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Slides-38bdf8?style=flat&logo=github)](https://gtanisik.github.io/bilgisayar-aglari/)

Bu depo, Üniversite Bilgisayar Mühendisliği lisans programında okutulacak olan **Bilgisayar Ağları ve İnternet** dersi için hazırlanmış Türkçe sunum slaytlarını içermektedir.

Slaytlar, Prof. Douglas E. Comer'in **"Computer Networks and Internets (6th Edition)"** kitabının resmi ders notları esas alınarak Türkçeye çevrilmiş ve [Marp (Markdown Presentation Ecosystem)](https://marp.app) formatında düzenlenmiştir.

* **🌐 Canlı Sunum Portalı**: [gtanisik.github.io/bilgisayar-aglari](https://gtanisik.github.io/bilgisayar-aglari/)
* **Resmi Depo (Repository)**: [github.com/gtanisik/bilgisayar-aglari](https://github.com/gtanisik/bilgisayar-aglari)

---

## 📁 Proje Yapısı

```text
.
├── README.md                  # Proje tanıtımı ve kullanım kılavuzu
├── COPYRIGHT.md               # Telif hakkı ve lisans bildirimleri
├── LICENSE                    # Creative Commons Attribution 4.0 International (CC BY 4.0)
├── Makefile                   # Marp PDF/HTML otomatik derleme komutları
├── .github/                   # CI/CD Otomasyon yapılandırması
│   └── workflows/
│       └── deploy-pages.yml   # GitHub Pages otomatik yayınlama iş akışı
├── scripts/                   # Yardımcı derleme betikleri
│   └── generate_index.py      # HTML portal indeksi & medya kopyalayıcı
├── templates/                 # Standart Marp slayt ve CSS şablonu
│   ├── custom-theme.css
│   └── slide-template.md
├── slides/                    # Türkçe Marp slayt dosyaları (.md ve görseller)
│   ├── mod01-introduction/
│   ├── mod02-applications/
│   ├── mod03-physical-layer/
│   ├── mod04-datalink-layer/
│   ├── mod05-internetworking/
│   ├── mod06-other-topics/
│   └── mod07-emerging-tech/
└── ai/                        # Planlama, terimler sözlüğü ve ilerleme takibi
    ├── MASTER_PLAN.md
    ├── PROGRESS.md
    └── NOTES.md
```

---

## 🛠️ Kurulum ve Sunumları Derleme

Sunumları düzenlemek ve PDF/HTML formatına dönüştürmek için **Marp CLI** gereklidir.

### 1. Marp CLI Kurulumu
Node.js ortamınız varsa:
```bash
npm install -g @marp-team/marp-cli
```
ya da macOS (Homebrew) ile:
```bash
brew install marp-cli
```

### 2. Slaytları PDF veya HTML Olarak Derleme
Tüm slaytları derlemek için `make` komutunu çalıştırabilirsiniz:

```bash
# Tüm slaytları PDF olarak derlemek için:
make pdf

# Tüm slaytları HTML olarak derlemek için:
make html

# Tek bir slaytı PDF'e dönüştürmek için:
marp --pdf slides/mod01-introduction/mod01_giris_ve_katmanlama.md -o mod01_giris.pdf
```

---

## 📚 Ders Modülleri (Course Modules)

- **Modül 1**: Giriş, Ders Özeti, Protokolcülük ve Katmanlı Mimari — [💻 Canlı Sunum](https://gtanisik.github.io/bilgisayar-aglari/mod01-introduction/mod01_giris_ve_katmanlama.html)
- **Modül 2**: Ağ Programlama ve Uygulama Katmanı (Soketler, HTTP, DNS, SMTP)
- **Modül 3**: Veri İletişimi Temelleri ve Fiziksel Katman (Sinyaller, İletim, Modülasyon)
- **Modül 4**: Veri Bağı Katmanı, LAN, Ethernet, Wi-Fi, Köprüleme ve L2 Anahtarlama
- **Modül 5**: İnternet Çalışması: IP Adresleme, Yönlendirme, UDP, TCP
- **Modül 6**: Ağ Güvenliği, Ağ Yönetimi, Başarım ve NAT
- **Modül 7**: Gelişen Teknolojiler (SDN, Bulut Bilişim, Sensör Ağları)

---

## 📜 Telif Hakkı ve Lisans (Copyright & License)

* **Orijinal Materyal**: Prentice-Hall / Pearson Education ve Prof. Douglas E. Comer'e aittir ([https://netbook.cs.purdue.edu](https://netbook.cs.purdue.edu)).
* **Türkçe Uyarlama**: Hazırlanan Türkçe slaytlar ve materyaller **[Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE)** lisansı ile açık kaynak olarak [github.com/gtanisik/bilgisayar-aglari](https://github.com/gtanisik/bilgisayar-aglari) adresinde sunulmuştur. Başka akademisyenler ve öğrenciler atıf vererek serbestçe kullanabilir ve değiştirebilir. Detaylar için [COPYRIGHT.md](COPYRIGHT.md) dosyasını inceleyiniz.
