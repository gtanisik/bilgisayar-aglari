# Notlar ve Türkçe Bilgisayar Ağları Terimler Sözlüğü (NOTES.md)

Bu dosya, ders anlatımı sırasındaki özel notlar, terminoloji kararları ve ilerideki oturumlar için hatırlatmaları içerir.

---

## 1. Terimler Sözlüğü (Networking Terminology Glossary)

Ders materyalinde çeviri tutarlılığını sağlamak amacıyla belirlenen temel terimler:

| İngilizce Terim | Türkçe Karşılığı | Açıklama / Kullanım Notu |
|---|---|---|
| **Host / End System** | Ana Bilgisayar / Uç Sistem | Ağdaki iletişim uç noktaları |
| **Packet** | Paket | Ağ katmanı veri birimi (L3) |
| **Frame** | Çerçeve | Veri bağı katmanı veri birimi (L2) |
| **Datagram** | Verigram / Datagram | Bağlantısız paket (IP veya UDP birimi) |
| **Segment** | Segment / Bölüt | Taşıma katmanı veri birimi (TCP) |
| **Router** | Yönlendirici | L3 paketi yönlendiren ağ cihazı |
| **Switch** | Anahtar / Anahtarlayıcı | L2 çerçevesini anahtarlayan ağ cihazı |
| **Hub** | Göbek / Dağıtıcı | Fiziksel katman yineleyici cihazı |
| **Bridge** | Köprü | İki ağ segmentini L2'de bağlayan cihaz |
| **Gateway** | Geçit Yolu / Ağ Geçidi | Farklı protokol sistemlerini bağlayan cihaz |
| **Socket** | Soket | Uygulamanın ağa erişim kapısı |
| **Bandwidth** | Bant Genişliği | Veri aktarım kapasitesi (bps) |
| **Throughput** | Verim / İşleme Gücü | Birim zamanda aktarılan gerçek veri miktarı |
| **Latency / Delay** | Gecikme | Verinin ulaştırılması için geçen süre |
| **Jitter** | Seğirme / Gecikme Değişimi | Gecikmedeki dalgalanma miktar |
| **Attenuation** | Zayıflama | Sinyal gücünün mesafeyle azalması |
| **Multiplexing** | Çoklama | Tek kanaldan birden fazla sinyal iletimi |
| **Demultiplexing** | Tekleme / Ayrıştırma | Çoklanmış sinyalleri kanallara ayırma |
| **Handshake** | El Sıkışma / Anlaşma | İletişim kurma protokol adımı (3-way handshake) |
| **Header** | Başlık | Veri biriminin önüne eklenen kontrol bilgisi |
| **Payload** | Yük / Taşınan Veri | Başlık hariç asıl veri kısmı |
| **Encapsulation** | Kapsülleme | Üst katman verisini alt katman başlığına sarma |
| **Decapsulation** | Kapsül Açma | Alt katman başlığını çıkarıp veriyi yukarı iletme |
| **Broadcast** | Yayın / Yayınlama | Ağdaki herkese gönderme |
| **Multicast** | Çoklu Yayın | Belirli bir gruba gönderme |
| **Unicast** | Tekli Yayın | Tek bir alıcıya gönderme |
| **Flow Control** | Akış Kontrolü | Alıcının boğulmasını önleme |
| **Congestion Control** | Tıkanıklık Kontrolü | Ağın boğulmasını önleme |
| **Acknowledge (ACK)** | Onay / Alındı Bilgisi | Verinin ulaştığını bildiren yanıt |

---

## 2. Gelecek Oturumlar İçi Hazırlık Notları

* **Telif Hakkı Vurgusu**: Sunumların giriş slaytına ve alt bilgisine Prentice-Hall ve Prof. Douglas Comer telif notu mutlaka konulmalı.
* **Marp Çıktıları**: Ders anlatımında kullanılmak üzere HTML/PDF çıktıları otomatik olarak `Makefile` betiği ile derlenebilir.
* **Ders İçi Kod Örnekleri**: C/Python ile verilen Soket örnekleri ders ortamında çalıştırılabilir durumda hazırlanmalıdır.

---

## 3. Marp Şablon Yönetimi Notları

* **1. Yol (Uygulandı - CSS Teması)**: Tüm slaytların ortak görsel stilleri `templates/custom-theme.css` dosyasına taşındı. `Makefile` derleme adımlarına `--theme-set templates/custom-theme.css` eklendi. Slayt `.md` dosyalarında sadece `theme: custom-theme` tanımlanır. CSS'teki herhangi bir güncelleme tüm slaytlara otomatik yansır.
* **2. Yol (Gelecekte İhtiyaç Duyulursa - Metin İçeriği Dahil Etme)**:
  Slaytlarda tekrar eden sabit Markdown metin blokları (örneğin telif uyarısı, sabit öğretmen tanıtımı vb.) oluşursa `markdown-it-include` eklentisi uygulanabilir:
  1. `npm install -D markdown-it-include`
  2. Proje köküne `.marprc.js`:
     ```javascript
     module.exports = {
       engine: ({ marp }) => marp.use(require('markdown-it-include'))
     }
     ```
  3. Slaytlarda kullanım: `::: include templates/common-header.md :::`

