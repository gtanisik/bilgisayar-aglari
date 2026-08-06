---
marp: true
theme: custom-theme
paginate: true
header: 'Bilgisayar Ağları ve İnternet | Modül 4: Veri Bağı Katmanı'
footer: 'Adapted from D. E. Comer (Prentice-Hall)'
---

<!-- _class: lead -->
# Modül 4: Veri Bağı Katmanı, LAN ve Kablosuz Ağlar

**Prof. Douglas E. Comer** ders materyalinden uyarlanmıştır.

---

# Konular

- Erişim teknolojileri
- Ara bağlantı teknolojileri
- Yerel alan ağı (LAN) paketleri, çerçeveleri ve topolojileri
- Ortam erişim mekanizmaları ve IEEE MAC alt katmanı
- Kablolu LAN teknolojileri (Ethernet ve 802.3)
- Kablosuz Ağ Teknolojileri
- LAN Genişletmeleri
- Anahtarlar ve anahtarlamalı ağlar

---

<!-- _class: lead -->
# Erişim Teknolojileri

---

# Erişimin Tanımı

- Sağlayıcı ve abone arasındaki "son kilometrede (last mile)" kullanılır
- Gayri resmi olarak dar bant (narrowband) veya geniş bant (broadband) olarak sınıflandırılır
- Darboğaz (bottleneck) olmayabilir
- Birçoğu asimetriktir, aşağı yönde (downstream) daha yüksek veri hızı sağlar

> 📷 *[Görsel: Sağlayıcı tesisi ile abone konumu arasındaki aşağı yönlü ve yukarı yönlü veri akışı diyagramı — yakında eklenecek]*

- Not: Aşağı yönde olan taraf hizmet için bir ücret öder

---

# Erişim Teknolojisi Türleri

- Dar bant (128 Kbps'den az)
  - Çevirmeli ağ (Dialup)
  - Bütünleşik Hizmetler Dijital Ağı (ISDN)
  - Ortadan kayboluyor
- Geniş bant (128 Kbps'den fazla)
  - Dijital Abone Hattı (DSL)
  - Kablo modemler
  - Kablosuz (ör. Wi-Fi ve 4G)

---

# Dijital Abone Hattı (DSL) Teknolojileri

- Yerel döngüyü (local loop) veri ve POTS arasında paylaşmak için frekans bölmeli çoğullama (frequency-division multiplexing - FDM) kullanır
- Başlangıç noktası (head-end) ekipmanı DSL Erişim Çoklayıcısıdır (DSLAM)
- Asimetrik Dijital Abone Hattı (ADSL)
  - 255 aşağı yönlü taşıyıcı frekansı, 31 yukarı yönlü (upstream)
  - Maksimum aşağı yönlü veri hızı 8.45 Mbps'dir
  - Taşıyıcı frekansların uyarlanabilir seçimi

> 📷 *[Görsel: POTS, yukarı yönlü ve aşağı yönlü kanalların frekans spektrumu — yakında eklenecek]*

---

# Kablo Modem Teknolojisi

- Verileri CATV koaksiyel kablo sistemi üzerinden gönderir
- Standart DOCSIS'tir (Data-Over-Cable Service Interface Specification)
- Başlangıç noktası (head-end) ekipmanı Kablo Modem Sonlandırma Sistemi (CMTS) olarak bilinir
- Sürüm 1.x frekans bölmeli çoğullama (FDM) kullanır
- Maksimum aşağı yönlü veri hızı 52 Mbps'dir
- Bant genişliği (bandwidth) birden fazla abone arasında paylaşılır
- Her abone bant genişliğinin 1/N'sini alır
- Kablo şirketi N'yi seçer

---

# Diğer Erişim Teknolojileri

- Hibrit sistemler optik fiber artı bakır içerir
  - Kaldırıma Kadar Fiber (FTTC)
  - Binaya Kadar Fiber (FTTB)
  - Tesis Tesisine Fiber (FTTP)
  - Eve Kadar Fiber (FTTH)
- Kilit soru: Aşağı yöndeki her noktada ne kadar kapasite gereklidir?
- Cevap: Uç noktaların ortak trafiğe sahip olup olmadığına bağlıdır
  - Yayınlar (broadcasts) paylaşılır
  - Bireysel iletişimler paylaşılmaz

---

# Diğer Erişim Teknolojileri (devamı)

- Kablosuz
  - Wi-Fi
  - WIMAX
  - Uydu
  - 3G ve 4G hücresel servisler
- Kiralık noktadan noktaya devreler (ör. T1 veya kesirli T1)

---

<!-- _class: lead -->
# Ara Bağlantı Teknolojileri

---

# İnternetin Çekirdeğindeki Ara Bağlantılar

- Genellikle büyük ISP'ler tarafından ihtiyaç duyulur
- Devreler ortak taşıyıcılardan (telefon şirketleri) kiralanır
- Bir Veri Servis Birimi / Kanal Servis Birimi (DSU / CSU) ile sonlandırılır
- Yukarı yönlü arayüz, birçok düşük hızlı erişim bağlantısını birleştirir
- Temel fikir: Sese dayalı veri hızları
  - Temel veri hızı: tek dijital ses kanalı (64 Kbps)
  - Daha yüksek veri hızlı devreler ses kanallarının katlarından oluşturulur
- SONET kodlaması ve çerçevelemesi (framing) kullanılır

---

# Kiralık Devrelerin Örnek Veri Hızları

| İsim | Ses Devreleri | Bit Hızı | Konum |
|---|---|---|---|
| temel hız (basic rate) | 1 | 0.064 Mbps | - |
| T1 | 24 | 1.544 Mbps | Kuzey Amerika |
| T2 | 96 | 6.312 Mbps | Kuzey Amerika |
| T3 | 672 | 44.736 Mbps | Kuzey Amerika |
| E1 | 30 | 2.048 Mbps | Avrupa |
| E2 | 120 | 8.448 Mbps | Avrupa |
| E3 | 480 | 34.368 Mbps | Avrupa |

- Kuzey Amerika'da kullanılan T standartları
- Avrupa'da kullanılan E standartları
- Not: T öneki, veri hızının yanı sıra kodlamayı da belirtir; yalnızca veri hızı, Dijital Sinyal Seviyesi (DS) standartlarıyla verilir

---

# Yüksek Kapasiteli Veri Devreleri

| Bakır Adı | Optik Adı | Ses Devreleri | Bit Hızı |
|---|---|---|---|
| STS-1 | OC-1 | 810 | 51.840 Mbps |
| STS-3 | OC-3 | 2430 | 155.520 Mbps |
| STS-12 | OC-12 | 9720 | 622.080 Mbps |
| STS-24 | OC-24 | 19440 | 1,244.160 Mbps |
| STS-48 | OC-48 | 38880 | 2,488.320 Mbps |
| STS-192 | OC-192 | 155520 | 9,953.280 Mbps |

- STS standartları bakır arayüzü belirtir
- OC standartları optik fiber arayüzü belirtir
- OC standartlarındaki C eki tek kanal (single channel) anlamına gelir

---

<!-- _class: lead -->
# Yerel Alan Ağları: Paketler, Çerçeveler, Topolojiler

---

# Ağlar

- Fiziksel iletişim sistemlerinden farklıdır
- Birden çok uç noktayı bağlar
- İki geniş kategori:
  - Devre anahtarlamalı (Circuit switched)
  - Paket anahtarlamalı (Packet switched)

---

# Devre Anahtarlamalı Ağlar

- Uç nokta çiftleri arasında noktadan noktaya iletişim sağlar
- Gönderici ve alıcı arasında yol (path) kurar
- Devre oluşturma, kullanma ve sonlandırma için ayrı adımlar
- Performans, yalıtılmış bir fiziksel yola eşdeğerdir
- Devre şu şekilde olabilir:
  - Kalıcı/hazırlanmış (uzun süre yerinde bırakılır)
  - Anahtarlamalı (isteğe bağlı oluşturulur)
- Konsept: Kullanıcı, altyapının bir parçasını bir süre için kiralar

---

# Paket Anahtarlamalı Ağlar

- İnternetin temelini oluşturur
- Paylaşılan ortam (shared media) üzerinden iletişimi çoğullar
- Tüm veriler paketlere bölünür (maksimum boyut sabittir)
- Gönderici bir paketi gönderdikten sonra, ikinci bir paketi göndermeden önce başkalarına iletim şansı tanır
- Keyfi (arbitrary), eşzamansız iletişim
- İletişim başlamadan önce kurulum gerekmez
- İstatistiksel çoğullama nedeniyle performans değişir
- Konsept: Temeldeki altyapı kullanıcılar arasında paylaşılır

---

# Devre ve Paket Anahtarlamasının Gösterimi

- Devre anahtarlama, 1'e 1 ayrılmış bağlantılar sağlar
> 📷 *[Görsel: Devre anahtarlamalı ağ diyagramı — yakında eklenecek]*

- Paket anahtarlama, istatistiksel TDM paylaşımı sağlar
> 📷 *[Görsel: Paket anahtarlamalı ağ diyagramı — yakında eklenecek]*

---

# Paket Anahtarlamalı Ağların Kategorileri

| İsim | Açılımı | Açıklama |
|---|---|---|
| LAN | Yerel Alan Ağı (Local Area Network) | En ucuzu; tek bir odayı veya tek bir binayı kapsar |
| MAN | Metropol Alan Ağı (Metropolitan Area Network) | Orta maliyet; büyük bir şehri veya metropolü kapsar |
| WAN | Geniş Alan Ağı (Wide Area Network) | En pahalısı; birden fazla şehirdeki siteleri kapsar |

- Herkes "AN" ile biten isimleri sever:

| İsim | Açılımı | Açıklama |
|---|---|---|
| PAN | Kişisel Alan Ağı (Personal Area Network) | Kulaklıklar için kullanılan, bir bireyin etrafındaki alanı kapsar |
| SAN | Depolama Alanı Ağı (Storage Area Network) | Bir veri merkezindeki disk çiftliği ile işlemciler arasındaki mesafeyi kapsar |
| CAN | Çip Alanı Ağı (Chip Area Network) | Tek bir çipi kapsar ve işlemci, bellekler vb. bağlar |

---

# Standart Organizasyonları ve Eğilimleri

- Standart organizasyonları ve akademik bölümler, protokol yığınının belirli katmanlarını vurgular ve aşağıdaki görüşlere yol açar:

> 📷 *[Görsel: W3C, IETF, IEEE ve ders kitaplarının hangi ağ katmanlarına odaklandığını gösteren diyagram — yakında eklenecek]*

---

# IEEE 802 Modeli ve Standartları

- IEEE (Elektrik ve Elektronik Mühendisleri Enstitüsü)
  - Profesyonel mühendisler topluluğu
  - Satıcıdan bağımsız teknolojileri standartlaştırır
- Proje 802
  - LAN/MAN standartları komitesi
  - 1980 yılında organize edildi
  - Katman 1 ve katman 2 standartlarına odaklanır
  - Katman 2'yi iki alt katmana (sub-layer) ayırır:
    - Mantıksal Bağlantı Kontrolü (LLC)
    - Ortam Erişim Kontrolü (MAC)

---

# Örnek IEEE Standartları

| ID | Konu |
|---|---|
| 802.1 | Üst katman LAN protokolleri |
| 802.2 | Mantıksal bağlantı kontrolü |
| 802.3 | Ethernet |
| 802.4 | Token bus (dağıtıldı) |
| 802.5 | Token Ring |
| 802.6 | Metropol Alan Ağları (dağıtıldı) |
| 802.7 | Koaksiyel Kablo kullanan Geniş Bant LAN (dağıtıldı) |
| 802.9 | Bütünleşik Hizmetler LAN (dağıtıldı) |
| 802.10 | Birlikte Çalışabilen LAN Güvenliği (dağıtıldı) |
| 802.11 | Kablosuz LAN (Wi-Fi) |
| 802.12 | Talep önceliği |

---

# Daha Fazla Örnek IEEE Standartları

| ID | Konu |
|---|---|
| 802.13 | Kategori 6 - 10Gb LAN |
| 802.14 | Kablo modemler (dağıtıldı) |
| 802.15 | Kablosuz PAN |
| 802.15.1 | (Bluetooth) |
| 802.15.4 | (ZigBee) |
| 802.16 | Geniş Bant Kablosuz Erişim |
| 802.16e | (Mobil) Geniş Bant Kablosuz |
| 802.17 | Esnek paket halkası |
| 802.18 | Radyo Düzenleyici TAG |
| 802.19 | Birlikte Yaşama TAG |
| 802.20 | Mobil Geniş Bant Kablosuz Erişim |
| 802.21 | Ortamdan Bağımsız Geçiş |
| 802.22 | Kablosuz Bölgesel Alan Ağı |

---

# Standartların Tanımladıkları

- Ağ topolojisi (şekli)
- Uç nokta adresleme şeması
- Çerçeve (frame) formatı
- Ortam erişim mekanizması
- Fiziksel katman yönleri ve kablolama

---

# Dört LAN Topolojisinin Gösterimi

> 📷 *[Görsel: Veriyolu (Bus), Halka (Ring), Ağ (Mesh) ve Yıldız (Star) topolojilerinin şekilleri — yakında eklenecek]*

- Her topolojinin avantajları ve dezavantajları vardır

---

# Uç Nokta Adresleme Şeması

- Bir LAN üzerindeki her istasyona benzersiz bir adres atanır
- Her paket bir hedef adresi belirtir
- LAN donanımı, hangi istasyon(lar)ın bir kopya alacağını belirlemek için paketteki adresi kullanır

---

# Adresleme için IEEE Standardı

- Resmi adı: IEEE Ortam Erişim Kontrolü adresi (MAC adresi)
- Gayri resmi olarak Ethernet adresi olarak adlandırılır
- Her adres 48 bit uzunluğundadır
- Cihaz üretildiğinde Ağ Arayüz Kartına (NIC) atanır
- Alt alanlara ayrılır:
  - 3 baytlık Organizasyonel Benzersiz Kimlik (OUI)
  - 3 baytlık Ağ Arayüz Denetleyicisi (NIC)

---

# Bir IEEE 48-Bit Adresindeki Alanların Gösterimi

> 📷 *[Görsel: MAC adresinin 3 baytlık OUI ve 3 baytlık NIC alanlarını gösteren diyagram — yakında eklenecek]*

- Adres türleri

| Adres Türü | Anlamı ve Paket Teslimatı |
|---|---|
| tekli yayın (unicast) | Hedef tek bir bilgisayardır; sadece o bilgisayar paketin bir kopyasını almalıdır |
| yayın (broadcast) | Hedef ağdaki tüm bilgisayarlardır; her biri paketin bir kopyasını almalıdır |
| çoklu yayın (multicast) | Bir ağdaki bilgisayarların bir alt kümesi paketin bir kopyasını almalıdır |

---

# Gelen Bir Paketi İşleme Algoritması

- **Amaç:** Bir LAN üzerinden gelen bir paketi işlemek
- **Yöntem:**
  1. Paketten hedef adresi, D'yi çıkarın;
  2. Eğer (D "benim adresim" ile eşleşiyorsa) { paketi kabul et ve işle; }
  3. Değilse eğer (D yayın (broadcast) adresi ile eşleşiyorsa) { paketi kabul et ve işle; }
  4. Değilse eğer (D üyesi olduğum bir çoklu yayın (multicast) grubu adresiyle eşleşiyorsa) { paketi kabul et ve işle; }
  5. Değilse { paketi yoksay; }

---

# Çerçeve Formatı

- Katman 2 paketine çerçeve (frame) denir
- Bir çerçevenin genel düzeni:
  - İsteğe bağlı başlangıç (prelude)
  - BAŞLIK (HEADER)
  - YÜK (PAYLOAD)
  - İsteğe bağlı bitiş (postlude)
- Başlık genellikle sabit alanlara sahiptir
- Her teknoloji maksimum bir yük boyutu (payload size) uygular
- Not: Belirli çerçeve formatlarını daha sonra göreceğiz

---

# Çerçeveleme ve Seri İletişim Sistemleri

- Kiralık bir devre (leased circuit) üzerinden paket gönderdiğimizi düşünün
- Devre donanımı ya bir bit akışı ya da bir bayt (karakter) akışı sağlar
- Bir bayt akışı sağlayan donanımı ele alacağız
  - Çerçeve sınırları yoktur
  - Verilerde herhangi bir 8 bitlik değer görünebilir
- Böyle bir sistem üzerinden paketleri nasıl gönderebiliriz?
- Cevap: Gönderici ve alıcı, çerçeveleme (framing) konusunda anlaşmalıdır

---

# Kiralık Bir Devre ile Kullanılan Örnek Çerçeveleme

- Bir çerçevenin başlangıcını ve sonunu işaretlemek için SOH ve EOT karakterlerini kullanın

> 📷 *[Görsel: SOH, Başlık, Yük ve EOT içeren örnek çerçeveleme yapısı — yakında eklenecek]*

- Yük içinde bayt doldurma (byte stuffing) kullanın:

| Yük İçindeki Bayt | Gönderilen Dizi |
|---|---|
| SOH | ESC A |
| EOT | ESC B |
| ESC | ESC C |

---

# Bayt Doldurmanın Gösterimi

> 📷 *[Görsel: Orijinal verinin bayt doldurma ile nasıl değiştirildiğini gösteren diyagram — yakında eklenecek]*

- İnternet, seri devreler üzerinden iletim için SLIP veya PPP (standartlar) kullanır
- Bir bit akışını aktaran sistemler için bit doldurma (bit stuffing) teknikleri de mevcuttur

---

<!-- _class: lead -->
# Ortam Erişim Mekanizmaları (IEEE MAC Alt Katmanı)

---

# MAC Protokolleri

- Paylaşılan ortama erişimi kontrol eder
- İki tür kanal tahsisi:
  - Statik
  - Dinamik
- Genel prensip: Statik kanal tahsisi, iletişim kuran varlıkların kümesi önceden bilindiğinde ve değişmediğinde yeterlidir; çoğu ağ bir tür dinamik kanal tahsisi gerektirir.

---

# Ortam Erişim Mekanizmalarının Sınıflandırılması

> 📷 *[Görsel: Medya erişim protokollerinin (Kontrollü, Çoklu Erişim, Kanalizasyon) taksonomi ağacı — yakında eklenecek]*

---

# Kanalizasyon (Channelization) Protokolleri

- Temel çoğullama tekniklerini kullanır ve genişletir
- Statik veya dinamik olabilir
- Üç temel tür:

| Protokol | Açılımı |
|---|---|
| FDMA | Frekans Bölmeli Çoklu Erişim (Frequency Division Multi-Access) |
| TDMA | Zaman Bölmeli Çoklu Erişim (Time Division Multi-Access) |
| CDMA | Kod Bölmeli Çoklu Erişim (Code Division Multi-Access) |

---

# Kontrollü Erişim Protokolleri

- Üç ana form

| Tür | Açıklama |
|---|---|
| Yoklama (Polling) | Merkezi denetleyici istasyonları tekrar tekrar yoklar ve her birinin bir paket iletmesine izin verir |
| Rezervasyon (Reservation) | İstasyonlar bir sonraki veri iletimi turu için talep gönderir |
| Token Geçişi (Token Passing) | İstasyonlar bir token (jeton) dolaştırır; token'ı her aldığında, istasyon bir paket iletir |

- Üçü de pratikte kullanılmıştır

---

# Yoklamalı (Polled) Erişim Algoritması

- **Amaç:** Paket iletimini yoklama yoluyla kontrol etmek
- **Yöntem:**
  - Denetleyici sonsuza kadar tekrarlar {
      Bir S istasyonu seçin ve S'ye bir yoklama mesajı gönderin;
      S'nin bir paket göndererek veya pas geçerek yanıt vermesini bekleyin;
    }

---

# Rezervasyon Tabanlı Erişim Algoritması

- Genellikle uydu sistemleriyle kullanılır
- İstasyonlar gönderecek verileri varsa bir denetleyiciye haber verir
- **Amaç:** Rezervasyon yoluyla paket iletimini kontrol etmek
- **Yöntem:**
  - Denetleyici sonsuza kadar tekrarlar {
      Gönderilecek paketi olan istasyonların bir listesini oluşturun;
      Listedeki her istasyonun iletim yapmasına izin verin;
    }

---

# Token Geçişli Erişim Algoritması

- Token olarak bilinen özel bir paket göndericiler arasında dolaşır
- İstasyon token her geldiğinde bir paket gönderir
- **Amaç:** Token geçişi yoluyla paket iletimini kontrol etmek
- **Yöntem:**
  - Ağdaki her bilgisayar şunu tekrarlar {
      Token'ın gelmesini bekleyin;
      Gönderilmeyi bekleyen varsa bir paket iletin;
      Token'ı sonraki istasyona gönderin;
    }

---

# Örnek Rastgele Erişim Protokolleri

| Tür | Açıklama |
|---|---|
| ALOHA | Hawaii'de erken bir radyo ağında kullanılan tarihi protokol; ders kitaplarında popülerdir ve analiz etmesi kolaydır, ancak gerçek ağlarda kullanılmaz |
| CSMA / CD | Çarpışma Algılamalı Taşıyıcı Dinlemeli Çoklu Erişim. Orijinal Ethernet'in temeli ve en yaygın kullanılan rastgele erişim protokolü |
| CSMA / CA | Çarpışma Önlemeli Taşıyıcı Dinlemeli Çoklu Erişim. Wi-Fi kablosuz ağlarının temeli |

---

# Aloha

- Hawaii'deki erken ağda kullanıldı (ALOHAnet)
- Gelen ve giden olmak üzere iki taşıyıcı frekans
- Merkezi verici gelen her paketi yeniden yayınladı (outbound)

> 📷 *[Görsel: Merkezi verici ile uzak istasyonlar arasındaki iletişim şeması — yakında eklenecek]*

- Gelen paketler çarpışırsa, her gönderici rastgele bir süre bekler ve yeniden iletir
- Kanal kullanımı %20'nin altında

---

# CSMA / CD

- Orijinal Ethernet'te (1973) kullanıldı
- Paylaşılan ortama erişim sağlar
- Temel özellikler:
  - Taşıyıcı Dinleme (Carrier Sense - CS)
  - Çoklu Erişim (Multiple Access - MA)
  - Çarpışma Algılama (Collision Detection - CD)
- İkili üstel geri çekilme (binary exponential backoff) kullanır

---

# CSMA / CD Algoritması

- **Yöntem:**
  - x değişkenini standart geri çekilme aralığı olan d'ye ayarlayın;
  - Bir paket hazır olduğunda, CS (erişim için bekle) yapın;
  - Paket arası boşluk (interpacket gap) için gecikme;
  - Paketi iletmeye çalışın ve CD (Çarpışma Algılama) yapın;
  - While (iletim sırasında çarpışma meydana geldi) {
      q'yu 0 ile x arasında rastgele bir gecikme olarak seçin;
      q mikrosaniye geciktir;
      x'i sonraki tur için gerekirse iki katına çıkar;
      Paketi yeniden iletmeye çalışın ve CD yapın;
    }

---

# CSMA / CA

- CSMA / CD'ye alternatif
- Kablosuz ağlarda (Wi-Fi) kullanılır
- Sinyallerin sınırlı mesafesi (δ) olduğu için gereklidir
- Örnek: bilgisayar 2 ve 3 iletişim kurduğunda bilgisayar 1 iletimi alamaz

> 📷 *[Görsel: Bilgisayar 1, 2 ve 3 arasındaki mesafe sınırlarını (δ) gösteren diyagram — yakında eklenecek]*

- Bilgisayar 2 ve 3'ün menzilindeki tüm bilgisayarlara iletimin gerçekleşeceği bildirilmelidir

---

# CSMA / CA Gösterimi

> 📷 *[Görsel: Bilgisayar 1, 2 ve 3 arasında RTS, CTS ve veri paketi iletimi sırasını gösteren şema — yakında eklenecek]*

- İletişim kuran çift, paket iletiminden önce RTS ve CTS değiş tokuşu yapar
- Bilgisayar 2 veya 3'ten δ'dan daha az uzaklıktaki herhangi bir bilgisayar RTS / CTS mesajlarından en az birini duyar

---

<!-- _class: lead -->
# Kablolu LAN teknolojileri (Ethernet ve 802.3)

---

# Kablolu LAN Teknolojileri

- 1980'ler boyunca teknolojilerin ve ürünlerin patlaması
- 1990'larda konsolidasyon
- Şu anda: bir de facto kablolu LAN standardı: **Ethernet**

---

# Ethernet Teknolojisi

- 1973'te Xerox PARC'ta icat edildi
- 1978'de Digital, Intel ve Xerox (DIX) tarafından standartlaştırıldı
- Çerçeve 14 baytlık bir başlığa ve ardından 46 ila 1500 baytlık yüke sahiptir
- Çerçeve formatı ve adresleme neredeyse hiç değişmeden hayatta kaldı

> 📷 *[Görsel: Hedef adres, kaynak adres, tür, yük ve CRC içeren Ethernet çerçeve formatı diyagramı — yakında eklenecek]*

---

# Ethernet Adres Filtreleme

- Hatırlatma: İstasyon, hedef adres şunlarla eşleşirse çerçevenin bir kopyasını kabul eder:
  - İstasyonun tekli yayın (unicast) adresi
  - Yayın (broadcast) adresi (tümü 1)
  - İstasyonun dinlediği bir çoklu yayın (multicast) adresi
- Diğer çerçeveler yok sayılır
- Karışık mod (promiscuous mode), bir istasyonun adrese bakılmaksızın tüm çerçeveleri almasına olanak tanır
  - Wireshark gibi protokol analiz yazılımının temeli

---

# Soru

Bir Ethernet çerçevesinin bitlerine çerçeve kablo boyunca iletilirken bakılırsa, çerçevenin tekli yayın (unicast) hedef adresine gönderilip gönderilmediğini hangi bit belirtir?
*(İpucu: 48 bitlik MAC adresi biçimine, Ethernet başlık biçimine ve bayt ve bit sıralamasına (Modül 2) bakın.)*

---

# Çerçeve Türü Alanı (Frame Type Field)

- Çerçeve başlığında 2 sekizli (octet) alan
- Gönderici tarafından çerçevenin içeriğini tanımlamak için ayarlanır
- Alıcı tarafından çerçevenin nasıl işleneceğini belirlemek için kullanılır
- Değerler standartlaştırılmıştır
- Örnekler:
  - Tür 0x0800 IPv4 datagramı için kullanılır
  - Tür 0x86DD IPv6 datagramı için kullanılır
  - Tür 0x0806 ARP için kullanılır

---

# Çerçeve Çoğullamayı Çözmenin (Demultiplexing) Gösterimi

> 📷 *[Görsel: Gelen çerçevenin türe (ör. 86DD) göre IPv4 veya IPv6 modüllerine ayrılmasını gösteren diyagram — yakında eklenecek]*

- Çerçeve geldiğinde gerçekleştirilir
- Genellikle protokol yazılımı tarafından ele alınır
- Çerçeve türü alanı incelenir ve çerçeve uygun protokol modülüne aktarılır; tanınmayan türler atılır

---

# IEEE'nin Ethernet Sürümü

- 1983'te IEEE standardı 802.3 olarak standartlaştırıldı
- Yaygın olarak benimsenmedi
- Başlık türü alanı, çerçeve uzunluğu olarak yeniden yorumlandı
- Sekiz baytlık yük LLC / SNAP başlığı tarafından işgal edildi

> 📷 *[Görsel: IEEE 802.3 çerçeve formatı, LLC/SNAP başlığı ve uzunluk alanı detayı — yakında eklenecek]*

---

# Ethernet Kablolaması

- Üç nesil boyunca gelişti:
  - Thicknet (Kalın ağ)
  - Thinnet (İnce ağ)
  - Bükümlü çift (Twisted pair)
- Çeşitli olası ağ kablolama şemalarını gösterir

---

# Thicknet Kablolama Gösterimi

> 📷 *[Görsel: Kalın Ethernet kablosu, sonlandırıcı, alıcı-verici ve AUI kablosunu gösteren diyagram — yakında eklenecek]*

- Tipik olarak tavanda ağır koaksiyel kablo
- Her bilgisayar kabloya bağlanır

---

# Thinnet Kablolama Gösterimi

> 📷 *[Görsel: Bilgisayarlar arasında noktadan noktaya giden Thinnet kablosunu ve sonlandırıcıyı gösteren diyagram — yakında eklenecek]*

- Esnek koaksiyel kablo
- Bağlantılar bilgisayarlar arasında noktadan noktaya çalışır
- Dezavantaj: kullanıcı ağ bağlantısını kesebilir

---

# Bükümlü Çift (Twisted Pair) Ethernet Kablolama Gösterimi

> 📷 *[Görsel: Bilgisayarların merkezi bir hub'a bükümlü çift kablolama ile bağlandığı diyagram — yakında eklenecek]*

- RJ45 konektörleri kullanan korumasız veya korumalı bükümlü çiftler
- Birden çok çift tam çift yönlü (full-duplex) çalışmaya izin verir
- Her bilgisayar merkezi hub'a bağlanır
- Topoloji fiziksel yıldız (star), ancak mantıksal veriyoludur (bus)
- Hub, "kutu içindeki veriyolu" ("bus in a box") olarak bilinir

---

# Bükümlü Çift Ethernet Teknolojilerinin Evrimi

- Bükümlü çift Ethernet'in çeşitli varyantları oluşturulmuştur
- Varyantlar, veri hızı ve gereken kablolamaya göre farklılık gösterir

| Tasarım (Designation) | İsim | Veri Hızı | Kullanılan Kablo |
|---|---|---|---|
| 10BaseT | Bükümlü Çift Ethernet | 10 Mbps | Kategori 5 |
| 100BaseT | Hızlı (Fast) Ethernet | 100 Mbps | Kategori 5E |
| 1000BaseT | Gigabit Ethernet | 1 Gbps | Kategori 6 |

---

<!-- _class: lead -->
# Kablosuz Ağ Teknolojileri

---

# Kablosuz Ağlar

- Birçok türü mevcuttur
- Teknolojiler şunlara göre farklılık gösterir:
  - Kapsanan mesafe
  - Veri hızları
  - Elektromanyetik enerjinin fiziksel özellikleri
    - Duvarlar gibi engelleri geçme yeteneği
    - Parazite (interference) duyarlılık
  - İzole kanal (isolated channel) vs. paylaşılan kanal (shared channel)

---

# Kablosuz Ağların Taksonomisi

- Kablosuz teknolojileri sınıflandırmaya yardımcı olmak için temel bir taksonomi kullanırız:
  - Yerel Alan Ağları (LANs)
  - Metropol Alan Ağları (MANs)
  - Geniş Alan Ağları (WANs)
  - Kişisel Alan Ağları (PANs)
- Not: Bazı teknolojiler birden fazla kategoriyi kapsadığından terminoloji nitelikseldir (qualitative)

---

# Kişisel Alan Ağı (PAN)

- Terminoloji öncelikle kablosuz ağlarda kullanılır
- Kısa mesafeyi kapsar
- Tek bir kullanıcıya adanmıştır (paylaşılmaz)
- Örnek PAN teknolojileri:

| Tür | Amaç |
|---|---|
| Bluetooth | Kulaklık veya fare gibi küçük bir çevresel cihaz ile cep telefonu veya bilgisayar arasındaki kısa mesafeli iletişim |
| Kızılötesi (InfraRed) | Çoğunlukla el tipi bir kumanda ile yakındaki bir sistem (bilgisayar veya eğlence merkezi) arasında görüş hattı (Line-of-sight) iletişimi |
| ZigBee | Elektrikli cihazların Akıllı Şebekeye bağlanmasını sağlayan, bir konut büyüklüğündeki mesafeler üzerinden iletişim |

---

# ISM Kablosuz Bantları

- ISM, Endüstriyel, Bilimsel ve Tıbbi (Industrial, Scientific, and Medical) anlamına gelir
- Elektromanyetik spektrumun lisanssız kullanıma sunulan bölgesi
- Kablosuz LAN'lar ve PAN'lar (ör. telsiz telefonlar) için kullanılır
- Üç ayrı bant:
  - 902 MHz (26 MHz bant genişliği)
  - 2.4 GHz (83.6 MHz bant genişliği)
  - 5.725 GHz (125 MHz bant genişliği)
- *Lisanssız olması düzenlemesiz olduğu anlamına gelmez.*

---

# Kablosuz LAN'lar ve Wi-Fi

- Çeşitli kablosuz LAN'lar yaratıldı
- Satıcılar 1990'larda açık standartlara yöneldi ve IEEE standartlarının çoğunu 802.11 altında sağladı
- 1999'da satıcılar Wi-Fi Alliance'ı kurdu
- Örnek IEEE kablosuz standartları:

| IEEE Standardı | Frekans Bandı | Veri Hızı | Modülasyon | Çoğullama |
|---|---|---|---|---|
| orijinal 802.11 | 2.4 GHz | 1 veya 2 Mbps | FSK | DSSS / FHSS |
| 802.11b | 2.4 GHz | 5.5 ve 11 Mbps | PSK | DSSS |
| 802.11g | 2.4 GHz | 22 ve 54 Mbps | çeşitli | OFDM |
| 802.11n | 2.4 GHz | 54 - 600 Mbps | çeşitli | OFDM |

---

# Yayılı Spektrum (Spread Spectrum) İletimi

- Tek bir kanal için birden çok frekans kullanır
- Performansı artırabilir veya gürültüye karşı bağışıklık sağlayabilir
- Başlıca yayılı spektrum teknikleri:

| İsim | Açılımı | Açıklama |
|---|---|---|
| DSSS | Doğrudan Sıralı Yayılı Spektrum (Direct Sequence Spread Spectrum) | CDMA'ya benzer, bir gönderici birden çok frekans oluşturmak için giden veriyi bir diziyle çarpar ve alıcı şifreyi çözmek için aynı diziyle çarpar |
| FHSS | Frekans Atlamalı Yayılı Spektrum (Frequency Hopping Spread Spectrum) | Gönderici veri iletmek için bir dizi frekans kullanır ve alıcı veriyi çıkarmak için aynı frekans dizisini kullanır |
| OFDM | Dik Frekans Bölmeli Çoğullama (Orthogonal Frequency Division Multiplexing) | Taşıyıcıların birbirine karışmayacağı şekilde iletim bandının birçok taşıyıcıya bölündüğü bir frekans bölmeli çoğullama şeması |

---

# Daha Fazla IEEE Kablosuz LAN Standardı

| Standart | Amaç |
|---|---|
| 802.11e | Düşük seğirme (jitter) garantisi gibi iyileştirilmiş hizmet kalitesi (QoS) |
| 802.11h | 802.11a gibi, ancak spektrum ve güç kontrolü ekler (Avrupa'da kullanım için) |
| 802.11i | Gelişmiş Şifreleme Standardı dahil gelişmiş güvenlik; tam sürüm WPA2 olarak bilinir |
| 802.11k | İletim gücü dahil olmak üzere radyo kaynağı yönetimi sağlayacak |
| 802.11p | Otoyoldaki araçlar ve araçtan yol kenarına ayrılmış Kısa Menzilli İletişim (DSRC) |
| 802.11r | Bağlantıyı kaybetmeden erişim noktaları (AP) arasında dolaşım (roaming) yeteneğinin iyileştirilmesi |
| 802.11s | Bir dizi düğümün otomatik olarak bir ağ oluşturduğu ve paketleri ilettiği bir örgü (mesh) ağ için önerildi |

---

# Kablosuz LAN Mimarisi

- IEEE, kablosuz LAN iletişimi için iki olası mod tanımlar
- Altyapı (Infrastructure) modu
  - Kablosuz cihazlar bir erişim noktası (access point - AP) üzerinden iletişim kurar
  - AP'ler birbirine ve (genellikle) internete bağlanır
  - Tipik kullanımlar: kurumsal kablosuz LAN, internet kafe
- Ad hoc modu
  - Kablosuz cihazlar arasında doğrudan iletişim
  - Yönlendirme (forwarding) mümkündür
  - Nadiren kullanılır

---

# Altyapı Modu Kablosuz LAN Gösterimi

- Bir AP için Temel Hizmet Seti (Basic Service Set - BSS), AP'yi duyabilen cihazlar kümesi olarak tanımlanır
- AP'ler kablolu ağ üzerinden birbirine bağlanır

> 📷 *[Görsel: Üç AP, bunların kapsama alanları (BSS) ve birbirlerine bağlı oldukları anahtarlama (switch) yapısı — yakında eklenecek]*

---

# Pratik Hususlar ve İlişkilendirme (Association)

- Pratikte BSS'ler örtüşebilir (belirli bir kablosuz cihaz birden fazla AP'yi duyabilir)

> 📷 *[Görsel: İki AP'nin menzilinde olan bir bilgisayarı gösteren çakışan BSS diyagramı — yakında eklenecek]*

- Sorunu çözmek için her cihaz aynı anda yalnızca bir AP ile ilişkilendirilir (associates)

---

# Pratik Hususlar: Wi-Fi Kanalları

- Kuzey Amerika için 2.4 GHz aralığında 11 kanal tanımlanmıştır
- Kötü haber: 22 MHz bant genişliği kanalların çakıştığı anlamına gelir
- İyi haber: 1, 6 ve 11. kanallar parazit olmadan aynı anda çalışabilir

> 📷 *[Görsel: Wi-Fi kanallarının 22 MHz bant genişliğindeki çakışmasını gösteren frekans diyagramı — yakında eklenecek]*

---

# 802.11 Çerçeve Formatındaki Adresler

- 802.11 çerçevesi bir Ethernet çerçevesi ile aynı değildir
- Her 802.11 çerçevesi dört MAC adresi içerir:
  - Kaynak (örneğin, kablosuz cihaz)
  - Hedef AP (ilişkilendirilmiş AP)
  - İnternet yolundaki yönlendirici (Router)
  - Ad hoc modu için ekstra adres

> 📷 *[Görsel: 4 farklı MAC adresi alanı içeren 802.11 çerçeve formatı — yakında eklenecek]*

---

# Erişim Noktaları (AP) Arasında Koordinasyon

- Koordineli yaklaşım
  - İlk tasarım
  - Hücresel telefona benzer
  - AP'ler pürüzsüz geçiş (handoff) sağlamak için iletişim kurar
- Koordinasyonsuz yaklaşım
  - Daha sonraki alternatif
  - AP'ler iletişim kurmaz
  - Kablosuz cihaz, bir AP ile bağlantısı koptuğunda ilişkilendirmeyi değiştirir
  - Daha düşük genel maliyet

---

# CSMA/CA Protokolü (İnceleme)

- Kablosuz LAN'larda kullanılan CSMA/CD alternatifi
- İletişim kuran çiftin menzilindeki istasyonların iletişimin ne zaman başladığını bilmesine olanak tanır
- Göndermeye Hazır (Ready-To-Send - RTS) ve Göndermeye Uygun (Clear-To-Send - CTS) mesajlarının değişimini gerektirir
- Protokolün verimli ve doğru olmasını sağlamak için her mesajla ilişkili gecikme vardır

---

# CSMA/CA Protokol Ayrıntıları

- SIFS — Kısa Çerçeve Arası Boşluk (Short Inter-Frame Space), 10 µsec
- DIFS — Dağıtılmış Çerçeve Arası Boşluk (Distributed Inter-Frame Space), 50 µsec
- Slot Süresi, 20 µsec

> 📷 *[Görsel: DIFS, RTS, SIFS, CTS, veri ve ACK mesajlarının zaman çizelgesi diyagramı — yakında eklenecek]*

---

# Kablosuz MAN Teknolojisi (WiMax)

- WiMax standardı, IEEE 802.16, iki tür sağlar
  - Sabit (802.16-2004) — uç nokta hareket etmez
  - Mobil (802.16e-2005) — uç nokta hareket eder
- Kullanımları:
  - Göçebe kullanıcılar için yüksek hızlı ara bağlantı
  - DSL veya kablo modeme "son kilometre" alternatifi
  - Birleştirilmiş veri ve telekomünikasyon erişimi
  - Bir tesisin internet bağlantısı için yedek olarak
  - Wi-Fi erişim noktalarından sağlayıcıya geri taşıma (backhaul)
  - Şirket tesisleri arasında özel bağlantılar
  - Küçük ve büyük ISP'ler arası bağlantı

---

# WiMax Kullanımlarının Gösterimi

- Yüksek kapasiteli geri taşıma (backhaul) için kullanılan sabit WiMax, Görüş Hattı (Line-Of-Sight - LOS) gerektirir

> 📷 *[Görsel: Servis sağlayıcı ile Wi-Fi bölgesi arasındaki LOS geri taşıma bağlantısını gösteren diyagram — yakında eklenecek]*

---

# Kablosuz PAN'lar için Standartlar

- Endüstriyel ve tüketici ürünlerinde kullanılır
- Kısa komutlar için optimize edilmiş uzaktan kumanda protokolleri (yüksek veri hızına ihtiyaç duymaz)

| Standart | Amaç |
|---|---|
| 802.15.1a | Bluetooth teknolojisi (1 Mbps; 2.4 GHz) |
| 802.15.2 | PAN'lar arasında bir arada yaşama (girişimsizlik) |
| 802.15.3 | Yüksek hızlı PAN (55 Mbps; 2.4 GHz) |
| 802.15.3a | Ultra Geniş Bant (UWB) yüksek hızlı PAN (110 Mbps; 2.4 GHz) |
| 802.15.4 | ZigBee teknolojisi – uzaktan kumanda için düşük veri hızlı PAN |
| 802.15.4a | Düşük güç kullanan alternatif düşük veri hızlı PAN |

---

# Diğer Kısa Mesafeli Kablosuz Teknolojiler

- Kızılötesi Veri Birliği (IrDA)
  - Standartlar ailesi (2.4 Kbps ila 16 Mbps veri hızı)
  - Birkaç metrelik menzil
  - 30 dereceyi kaplayan koni ile yönlü iletim
  - Genellikle düşük güç tüketimi
- Radyo Frekansı ile Tanımlama (RFID) etiketleri
  - 140'tan fazla RFID standardı vardır
  - Pasif RFID etiketleri, okuyucunun sinyalinden güç alır
  - Aktif RFID etiketleri, uzun yıllar dayanan bir pil içerir
  - 100 MHz'den daha düşük ila 868-954 MHz frekansları

---

# Kablosuz WAN Teknolojileri

- Hücresel iletişim sistemleri
- Uydu iletişim sistemleri

---

# Hücresel Telefonlar ve Veri Ağı

- Dünyada bilgisayarlardan daha fazla cep telefonu var
- Akıllı telefon artık gelişmekte olan tüm ülkelerde tercih edilen ağ arayüzüdür
- Cep telefonu sağlayıcıları İnternet protokollerine geçiş yaptı

---

# Mevcut Hücresel Sistem Mimarisi

- Hücre (Cell), mobil anahtarlama sistemine bağlanan bir kuleye sahiptir
- Her mobil anahtarlama sistemi PSTN veya İnternete bağlanır

> 📷 *[Görsel: Hücre kuleleri, Mobil Anahtarlama Merkezleri ve Genel Anahtarlamalı Telefon Ağı (PSTN) bağlantıları — yakında eklenecek]*

- Geçiş (handoff) kararı altyapı tarafından alınır

---

# Teorik ve Gerçek Hücreler

> 📷 *[Görsel: Mükemmel altıgenlerle teorik hücreler ve örtüşen düzensiz alanlarla gerçek hücreler — yakında eklenecek]*

- Sorunlar şunları içerir: örtüşme ve boşluklar

---

# Hücre Boyutu ve Beklenen Cep Telefonu Yoğunluğu

- Ders kitabı diyagramları eşit büyüklükte hücreleri gösterir
- Pratikte hücre boyutu beklenen cep telefonu sayısıyla ilişkilidir
- Yüksek nüfuslu alanlarda daha küçük hücreler kullanılır
- Kırsal alanlarda daha büyük hücreler kullanılır

---

# Frekans Ataması

- Hedef: Paraziti (interference) en aza indirmek
- Prensip: Bitişik iki hücre aynı frekansı kullanmazsa parazit en aza indirilebilir.
- Yöntem: Bitişik iki hücreye aynı frekansın atanmayacağı bir frekans ataması tasarlayın
- Teknik: Tekrarlanabilen bir desen oluşturun
- Küme (cluster) yaklaşımı olarak bilinir

---

# Kullanılan Örnek Kümeler

> 📷 *[Görsel: 3, 4, 7 ve 12 hücreli farklı küme desenleri — yakında eklenecek]*

- Kümedeki her hücreye benzersiz bir frekans atanır
- Çoğaltıldığında, kümeler 2 boyutlu yüzeyi kaplar
- Matematiksel olarak bu kavram "düzlemi döşeme"dir (tiling the plane)

---

# Küme Çoğaltmasının Gösterimi

> 📷 *[Görsel: Bitişik hücrelerin aynı frekansı paylaşmasını önleyen, harflerle ifade edilen küme çoğaltması — yakında eklenecek]*

- Bitişik hiçbir hücre çiftine aynı frekans atanmaz

---

# Hücresel Ağların Dört Nesli

- **1G** analog kullandı (1970'ler - 1980'ler)
- **2G ve 2.5G** ses için dijital sinyaller kullanır (1990'lar-)
- **3G ve 3.5G** ayrıca 400 Kbps ile 2 Mbps arasındaki hızlarda veri aktarımını içerir (2000'ler-)
- **4G**, daha yüksek veri hızları ve televizyon gibi gerçek zamanlı multimedya desteği sunar (2008-)

---

# Hücresel Teknolojiler

- Birçok rekabet eden standart
- Avrupa Posta ve Telekomünikasyon İdareleri Konferansı, Avrupa için Mobil İletişim için Küresel Sistem (GSM) olarak bilinen bir TDMA teknolojisini seçti
- ABD'de her taşıyıcı kendi standartlarını oluşturdu
  - Motorola, TDMA kullanan iDEN'i yarattı
  - Diğerleri, CDMA kullanan IS-95A'yı benimsedi
- Japonya, TDMA kullanan PDC'yi seçti

---

# 2G Kablosuz Standartlarının Özeti

| Nesil | Yaklaşım | Standart |
|---|---|---|
| 2G | GSM | GSM |
| 2.5G | GSM | GPRS |
| 2.5G | GSM | EDGE (EGPRS) |
| 2.5G | GSM | EDGE Evolution |
| 2.5G | GSM | HSCSD |
| 2G | CDMA | IS-95A |
| 2.5G | CDMA | IS-95B |
| 2G | TDMA | iDEN |
| 2G | TDMA | IS-136 |
| 2G | - | PDC |

- Not: 2.5G standartları, 3G'nin bazı özelliklerini ekleyerek 2G standartlarını genişletir

---

# Üçüncü Nesil Standartlar

- 2G standartları birleştirildi ve genişletildi:

| Halefi Olduğu | Standart | Yaklaşım |
|---|---|---|
| IS-136, IS-95A, EDGE, PDC | WCDMA | UMTS |
| UMTS | HSDPA | UMTS |
| IS-95B | 1xRTT | CDMA |
| 1xRTT | EVDO | CDMA |
| 1xRTT | EVDV | CDMA |

- EVDO ve EVDV veri aktarım standartları, 2.4 Mbps veya 3.1 Mbps'de veri sunmak için yaklaşık aynı zamanda gelişti
- HSDPA 14 Mbps'ye ulaşabilir

---

# Dördüncü Nesil Standartlar

- Başlangıçta ITU, 4G terimini kullanmadan önce yüksek performans konusunda ısrar etti
- Sonunda ITU, ara teknolojilerin 4G olarak "tanıtılmasına" izin verdi

| Sınıflandırma | Standart |
|---|---|
| 4G olarak tanıtılabilir | HSPA+, HTC Evo 4G, LTE, WiMAX |
| IMT-Advanced'e bağlı kalır | LTE Advanced, WiMAX Advanced |

---

# Uydu Türlerinin İncelenmesi

- **Alçak Dünya Yörüngesi (Low Earth Orbit - LEO)**
  - Gökyüzünde hareket ediyormuş gibi görünür
  - Dünya yüzeyini kaplamak için 66 uyduluk bir küme gerektirir
- **Orta Dünya Yörüngesi (Medium Earth Orbit - MEO)**
  - Kutupları kaplar
  - Genel iletişim için nadiren kullanılır
- **Sabit Yörünge (Geostationary Earth Orbit - GEO)**
  - Gökyüzünde sabit görünür
  - Dünya yüzeyini kaplamak için sadece üç uydu gerekir

---

# Dünya Yüzeyinin GEO Kapsamı

- En iyi durumda sadece üç uyduya ihtiyaç vardır

> 📷 *[Görsel: Dünyanın etrafındaki üç sabit uyduyu ve kapsama alanlarını gösteren diyagram — yakında eklenecek]*

- Kapsanan yüzey alanı "ayak izi" (footprint) olarak bilinir
- Mesafenin Dünya'nın çapına oranı yaklaşık olarak ölçeklidir

---

# VSAT Uydu Teknolojisi

- Çok Küçük Açıklıklı Terminal (Very Small Aperture Terminal) anlamına gelir
- Parabolik anten gelen sinyali odaklar

> 📷 *[Görsel: Çanak antene gelen ve odaklanan sinyali gösteren diyagram — yakında eklenecek]*

- Örnek kullanım: Bir şirketin perakende mağazalarını bağlamak

---

# VSAT Teknolojisi İle Kullanılan Frekans Bantları

- Birden çok bant mevcuttur
- Her bandın dezavantajları vardır

| Bant | Frekans | Ayak İzi | Sinyal Gücü | Yağmurun Etkisi |
|---|---|---|---|---|
| C Band | 3 - 7 GHz | Büyük | Düşük | Orta |
| Ku | 10 - 18 GHz | Orta | Orta | Orta |
| Ka | 18 - 31 GHz | Küçük | Yüksek | Şiddetli |

---

# Küresel Konumlandırma Sistemi (GPS)

- 24 uydu
- 6 yörünge düzleminde düzenlenmiş
- Sivil versiyon 20 ile 2 metre arasında bir doğruluğa sahiptir
- Veri ağı (data networking) ile ilgisi:
  - Doğru zamanı sağlar
  - Bir veri ağındaki uzak noktaları senkronize etmek için kullanılabilir (bazı protokoller tarafından ihtiyaç duyulur)

---

# Yazılım Tanımlı Radyo (Software Defined Radio)

- Yazılımla programlanabilir radyo olarak da bilinir
- Araştırmalardan ortaya çıkan yeni yaklaşım
- Heyecan verici olasılıklar
- Sabit radyo bileşenlerini, programlanabilir bir işlemci tarafından kontrol edilebilen mekanizmayla değiştirir
- Spektrumu daha iyi kullanabilir
- Potansiyel dezavantaj: kullanıcı, polis veya acil durum araçlarına müdahale eden parametreleri seçebilir

---

# Bir Yazılım Radyosunda Kontrol Edilen Özellikler

| Özellik | Açıklama |
|---|---|
| Frekans | Belirli bir zamanda kullanılan kesin frekans kümesi |
| Güç | Vericinin yaydığı güç miktarı |
| Modülasyon | Sinyal ve kanal kodlaması ile modülasyonu |
| Çoğullama | CDMA, TDMA, FDMA ve diğerlerinin herhangi bir kombinasyonu |
| Sinyal Yönü | Antenler belirli bir yöne ayarlanabilir |
| MAC Protokolü | Çerçeveleme ve MAC adreslemenin tüm yönleri |

- Etkinleştiren teknolojiler:
  - Frekansları seçmek ve gücü kontrol etmek için ayarlanabilir analog filtreler
  - Yönü seçmek için çoklu anten yönetimi

---

# Çoklu Anten Yönetimi

- Gereklidir çünkü:
  - Hiçbir tek anten tüm frekansları idare edemez
  - Yönlü sinyaller iletişime odaklanmada önemlidir
- Çoklu Giriş Çoklu Çıkış (Multiple-Input Multiple-Output - MIMO) teknolojisi iletim veya alımı hedefleyebilir

---

<!-- _class: lead -->
# LAN Genişletmeleri (LAN Extensions)

---

# Ağ Tasarımı Ödünleşimleri (Tradeoffs)

- Ağ teknolojisi şunlar için tasarlanmıştır:
  - Kapsanan mesafe
  - Maksimum veri hızı
  - Maliyet
- LAN teknolojileri veri hızını en üst düzeye çıkarır ve maliyeti en aza indirir
- Genel prensip: Maksimum uzunluk belirtimi, LAN teknolojisinin temel bir parçasıdır; LAN donanımı, sınırı aşan kablolarda doğru çalışmaz.

---

# LAN'ları Genişleten Teknolojiler

- LAN'ları genişletmek için çeşitli teknikler icat edilmiştir
- Üç ana genişletme teknolojisi:
  - Fiber modemler
  - Tekrarlayıcılar (Repeaters)
  - Köprüler (Bridges)

---

# Fiber Modemler

- Bir optik fiber üzerinden iletişim kurar
- Uzun mesafeyi kapsayabilir
- Standart ağ arayüzü sağlar (ör. Ethernet)
- Bilgisayar ve ağ arasındaki bağlantıyı genişletmek için kullanılabilir

> 📷 *[Görsel: İki fiber modem ile genişletilmiş optik fiber bağlantısı diyagramı — yakında eklenecek]*

---

# Tekrarlayıcılar (Repeaters)

- Katman 1'de çalışır (paketleri anlamaz)
- Sinyalleri tekrarlar ve güçlendirir
- Düşük maliyetli
- Örnek kullanım: bir kablo kutusundaki uzatılmış kızılötesi sensör

> 📷 *[Görsel: Kablo kutusu bağlantısı ile uzaktan sensör arasına yerleştirilmiş tekrarlayıcı şeması — yakında eklenecek]*

- Dezavantaj: Gürültüyü güçlendirir ve tekrarlar

---

<!-- _class: lead -->
# Anahtarlar (Switches) ve Anahtarlamalı Ağlar

---

# Köprü (Bridge)

- Başlangıçta iki LAN segmentini genişletmek için bağımsız (stand-alone) cihaz olarak satıldı
- Katman 2'de çalışır
- İki veya daha fazla segmenti bağlayabilir
- Her segmentte karışık modda (promiscuous mode) dinler ve her çerçevenin bir kopyasını diğer segmentlere gönderir
- Gürültüyü, çarpışmaları veya yanlış oluşturulmuş çerçeveleri kopyalamaz
- Bağlı segmentlerin tek ve büyük bir LAN gibi görünmesini sağlar
- Bilgisayar konumlarını otomatik olarak öğrenmek için çerçevelerdeki kaynak MAC adresini kullanır ve çerçeveleri filtrelemek için hedef MAC adresini kullanır

---

# Bir Köprünün Öğrenmesinin Gösterimi

> 📷 *[Görsel: İki LAN segmentini (Hub 1 ve Hub 2) birbirine bağlayan köprü diyagramı — yakında eklenecek]*

| Olay | Segment 1 Öğrenilenler | Segment 2 Öğrenilenler | Gönderilen Çerçeve |
|---|---|---|---|
| Köprü başlar | - | - | - |
| A, B'ye gönderir | A | - | Her İki Segmente |
| B, A'ya gönderir | A, B | - | Sadece Segment 1 |
| X yayın yapar (broadcasts)| A, B | X | Her İki Segmente |
| Y, A'ya gönderir | A, B | X, Y | Her İki Segmente |
| Y, X'e gönderir | A, B | X, Y | Sadece Segment 2 |
| C, Z'ye gönderir | A, B, C | X, Y | Her İki Segmente |
| Z, X'e gönderir | A, B, C | X, Y, Z | Sadece Segment 2 |

---

# Genel Prensip

- Bir köprü bağlı segmentlerde eşzamanlı faaliyete izin verdiğinden, bir segmentteki bir çift bilgisayar, başka bir segmentteki bir çift bilgisayar ile aynı anda iletişim kurabilir.
- Her segment ayrı bir çarpışma alanı (collision domain) oluşturur.

---

# Köprülerle İlgili Bir Sorun

- Bir köprü her zaman yayın (broadcast) ve çoklu yayın (multicast) çerçevelerini iletir
- Bir döngüdeki dört LAN segmentini bağlamak için kullanılan dört köprüyü düşünün

> 📷 *[Görsel: Döngü oluşturan dört köprü ve bağlı hub'ların diyagramı — yakında eklenecek]*

- Segmentlerden birine bağlı bir bilgisayar bir yayın çerçevesi gönderirse ne olur?
  - Çerçevenin kopyaları sonsuza kadar köprüler etrafında döner!

---

# Dağıtılmış Kapsayan Ağaç (Distributed Spanning Tree)

- Bir paketin bir köprü döngüsü etrafında dolaşmasını önler
- İlk protokol, Digital Equipment Corporation'da Perlman tarafından geliştirildi
- Köprü başlatıldığında (boot) her köprü tarafından çalıştırılır
- Köprülerin bir yönlendirme döngüsünü (forwarding cycle) kırmasına olanak tanır
- Kapsayan Ağaç Protokolü (Spanning Tree Protocol - STP) adı temel protokole uygulanır
- Genişletilmiş isimlerle birçok varyant oluşturulmuştur

---

# STP Nasıl Çalışır

- Başlangıçta (startup) yürütülür
- Dağıtılmış algoritma
  - Her köprü bağımsız olarak çalıştırır
  - Merkezi bir koordinasyon yoktur
- Algoritmanın hızla yakınsaması (converge) garanti edilir
- STP bitene kadar hiçbir veri paketi iletilmez

---

# STP Tarafından Atılan Adımlar

- Köprüler şunlar için kullanılan bir dizi STP mesajı (çerçeve) alışverişinde bulunur:
  - Bir kök köprü (root bridge) seçmek
  - Köke (root) giden en kısa yolu seçmek
- Her köprü, seçilen yol haricinde yayın (broadcast) veya çoklu yayın (multicast) yönlendirmeyi devre dışı bırakır
- Sonuç bir ağaçtır (tree)

---

# Köprüleme Canlı ve İyi Durumda

- Bağımsız (stand-alone) köprü cihazları nadiren kullanılır
- Köprü teknolojisi artık diğer cihazlara entegre edilmiştir:
  - DSL modemler
  - Kablo modemler
  - Wi-Fi "tekrarlayıcıları" (repeaters)
  - Uydu sistemleri

---

<!-- _class: lead -->
# Anahtarlama (Switching)

---

# Katman 2 Anahtarı (Layer 2 Switch)

- Fiziksel olarak Katman 2 hub'ına benzer
  - Ağ cihazıdır
  - Birden fazla bilgisayarı bağlar
  - Bilgisayarlar bir LAN segmentine bağlı görünür
- Mantıksal olarak bir dizi köprülü ağa (bridged networks) benzer
  - Anahtar sadece sinyalleri değil, paketleri anlar
  - Çekişme (contention) yoktur ve CSMA / CD'ye gerek yoktur
  - Portlar paralel çalışır
  - Anahtar, paketleri inceleyen servisleri içerebilir

---

# Bir Anahtarın Mantıksal İşlevi

> 📷 *[Görsel: Anahtar içindeki portlar ve simüle edilmiş köprüleri/Ethernet segmentlerini gösteren diyagram — yakında eklenecek]*

- Anahtar, köprülü (bridged) ağlarla aynı avantajı sunar: birden fazla aktarım eşzamanlı olarak gerçekleşebilir

---

# Gerçek Anahtar Mimarisi

> 📷 *[Görsel: Arayüzler ve anahtarlama yapısı (switching fabric) arasındaki bağlantı mimarisi — yakında eklenecek]*

- Yüksek iş çıkarma yeteneği (throughput) için kullanılan anahtarlama yapısı (switching fabric)

---

# Düşünce Problemi

Diyelim ki bir bilgisayar, bir Katman 2 anahtarındaki (Layer 2 switch) bir bağlantı noktasından (port) çıkarılıp başka bir bağlantı noktasına takılıyor. Bilgisayarın hiçbir paket göndermediğini varsayın. Bilgisayar kendisine gönderilen tekli yayın (unicast) çerçevelerini almaya devam edecek mi? Neden ya da neden olmasın?

---

# Sanal Yerel Alan Ağı (VLAN) Anahtarı

- **Fiziksel olarak:**
  - Geleneksel bir Katman 2 anahtarına (Layer 2 switch) benzer
  - Bilgisayarın bağlanabileceği bağlantı noktaları (port) vardır
- **Mantıksal olarak:**
  - Yönetici (manager) bir veya daha fazla yayın alanı (broadcast domain) yapılandırabilir
  - Her bağlantı noktası bir yayın alanına atanır
- Yayın veya çoklu yayın adresine gönderilen çerçeve yalnızca aynı yayın alanındaki bağlantı noktalarına yayılır

---

<!-- _class: lead -->
# Ağ Teknolojileri: Geçmiş ve Bugün

---

# Çok Çeşitli Ağ Teknolojileri

- LAN teknolojileri
  - Token ring (özellikle IBM Token Ring)
  - FDDI / CDDI
- WAN teknolojileri
  - X.25
  - Frame Relay
  - ATM
  - ISDN
  - MPLS
- Not: Daha uzun bir liste için 19. Bölüme bakın

---

# Asenkron Aktarım Modu (Asynchronous Transfer Mode - ATM) (devamı)

- ATM'de QoS (Hizmet Kalitesi)
  - Her aktarım (yani her TCP bağlantısı) için belirlenir
  - Kurulum süresi gerektirdi
  - Her anahtarın durumu koruduğu (maintained state) anlamına geliyordu
  - Yüksek hızda uygulanması (enforce) zor/imkansızdı
- ATM'nin başarısızlığına rağmen, savunucuları hala İnternet'in QoS'ye ihtiyacı olduğunu savunuyor

---

# Özet

- Kablosuz ağlar arasında PAN'lar, LAN'lar ve WAN'lar bulunur
- Hücresel telefonlar paket teknolojisini kullanıyor
- Uydu, verileri bir çanak anten aracılığıyla ulaştırabilir
- Yazılım tanımlı radyo (software-defined radio), kablosuz cihazlara esneklik katar
- LAN uzantıları, tekrarlayıcıları (repeaters) ve köprüleri (bridges) içerir
- Bir zamanlar bağımsız (stand-alone) cihazlar olan köprüler artık diğer cihazlara entegre edilmiştir
- Katman 2 anahtarı (Layer 2 switch), köprülü (bridged) ağlar gibi davranır

---

# Sorular?
