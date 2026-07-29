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

---

## 4. Slayt Hazırlama, İçerik ve Görsel Standartları (Modül 1 Deneyimleri & Kurallar)

Gelecek tüm modüllerde (Modül 2 - 7) strictly uygulanacak temel tasarım ve içerik prensipleri:

### A. Şekil ve Görsel Yönetimi Standartları
1. **ASCII / Metin Diyagramları Kesinlikle YASAK**: Şemalar ve mimari çizimler için asla ASCII art (`+----+`, ````text`) veya kod bloğu metinleri kullanılmayacaktır.
2. **Yüksek Çözünürlüklü Orijinal Görseller (300 DPI PNG)**:
   - Şema ve 3D diyagramlarda orijinal detay kaybını ve karmaşıklığı önlemek adına Prof. Douglas Comer'in orijinal ders PDF'inden kırpılan görseller tercih edilmelidir.
   - Görseller PDF'ten varsayılan 150 DPI yerine **300 DPI (`pdftoppm -r 300`)** piksel yoğunluğuyla alınarak kesinlikle bulanıklaşma/pikselleşme olmamalıdır.
3. **Şeffaf / Saydam Arka Plan (Transparent RGBA)**:
   - PDF'ten kesilen görsellerin fon renkleri Python (`PIL`) ile saydamlaştırılarak Marp slayt arka planıyla (`#f8f9fa`) pürüzsüz bütünleşmesi sağlanmalıdır.
4. **Görüntü İşleme ile Netleştirme & Doygunluk**:
   - Resimlerdeki çizgiler ve yazılar soluk görünmemeli; renk doygunluğu artırılmalı ve kenar keskinleştirme filtresi (`ImageFilter.SHARPEN`) uygulanmalıdır.
5. **Yatayda Ortalanma ve Eksiksiz Kırpma**:
   - Tüm görseller slaytta `![center height:...](images/...)` etiketiyle yatayda tam ortalanmalıdır.
   - Şekil kırpılırken alttaki bulutlar, oklar veya bağlam elemanları asla yarıda kesilmemelidir.
6. **Yalın Vektörel SVG Çizimleri**:
   - Orijinal görsel yerine Türkçe SVG kullanılacaksa oklar metinlerin (`Payload` vb.) veya harflerin üzerinden geçmemeli, metnin etrafından dolaşmalıdır.

### B. İçerik ve Slayt Yapısına Birebir Sadakat
1. **Gereksiz Özetleme ve Birleştirmeden Kaçınma**:
   - Orijinal PDF'teki slayt dizilimi ve sayfa yapısı birebir korunmalıdır. Ayrı ayrı duran anlatım slaytları tek bir özette birleştirilmemeli; her biri kendi başlığı ve detaylı maddeleriyle Türkçe slayt olarak sunulmalıdır.
2. **Biçimlendirme ve Liste Tutarlılığı**:
   - Liste maddelerinde keyfi tırnak işaretleri (`"..."`) kullanılmamalıdır. Orijinaldeki gibi temiz, tırnaksız ve tutarlı font/girinti yapısı tercih edilmelidir.
3. **Telif / Kaynak Gösterimi**:
   - Slayt alt bilgisinde (footer) bulunan `Adapted from D. E. Comer (Prentice-Hall)` ifadesi tüm uyarlama metinler ve görseller için akademik standartlara tam uygundur ve yeterlidir.

### C. Temiz Proje Yapısı (Clean Repository)
- Slaytlarda artık kullanılmayan veya yerini PNG'ye bırakan eski SVG/görsel dosyaları proje klasöründe (`images/`) kalıntı olarak bırakılmamalı, anında temizlenmelidir (`rm`).


