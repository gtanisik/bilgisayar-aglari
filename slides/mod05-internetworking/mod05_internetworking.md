---
marp: true
theme: custom-theme
paginate: true
header: 'Bilgisayar Ağları ve İnternet | Modül 5: İnternetworking'
footer: 'Adapted from D. E. Comer (Prentice-Hall)'
---

<!-- _class: lead -->
# Modül 5: İnternet Çalışması — IP, Yönlendirme ve Taşıma Katmanı

**Prof. Douglas E. Comer** ders materyalinden uyarlanmıştır.

---
# Konular

- Taşıma katmanı (transport layer) protokolünün özellikleri ve teknikleri
- Kullanıcı Veri Birimi Protokolü (UDP) ile mesaj taşıma
- İletim Kontrol Protokolü (TCP) ile akış (stream) taşıma
- Yönlendirme algoritmaları ve protokolleri
- İnternet çoklu yayın (multicast) ve çoklu yayın yönlendirmesi (multicast routing)

---
<!-- _class: lead -->
# İnternet Kavramı ve İnternet Mimarisi

---
# İnternet Nedir?

- Kullanıcılar için hizmetler ve uygulamalardır:
  - Web ve e-ticaret
  - E-posta, mesajlaşma, anlık mesajlaşma
  - Sosyal ağlar ve bloglar
  - Müzik ve video indirme (ve yükleme)
  - Sesli ve görüntülü telekonferans

- Ağ profesyonelleri için bir altyapıdır:
  - Yukarıdaki hizmetlerin çalıştığı platform
  - Hızla büyür

---
# İnternet'in Büyümesi

> 📷 *[Görsel: İnternet'teki bilgisayar sayısının yıllara göre lineer büyüme grafiği — yakında eklenecek]*

- Grafik, her yıl İnternet üzerindeki bilgisayar sayısını göstermektedir.

---
# İnternet'in Büyümesi (Logaritmik Ölçek)

> 📷 *[Görsel: İnternet'teki bilgisayar sayısının yıllara göre logaritmik büyüme grafiği — yakında eklenecek]*

- Grafik, her yıl İnternet üzerindeki bilgisayar sayısını göstermektedir.

---
# İnternet'in Gerçek Boyutu

- Önceki grafikler biraz yanıltıcıdır:
  - Alan Adı Sistemi (DNS) taranarak elde edilmiştir.
  - Sadece IP adresleri olan sunucuları (hosts) raporlar.
- Yaklaşık 2000 yılından bu yana birçok İnternet cihazı:
  - Sabit bir IP adresine sahip değildir.
  - Bir ağ adresi çeviri (NAT) kutusu (örneğin, kablosuz yönlendirici) arkasından bağlanır.
- Gerçek boyutu ölçmek zordur.

---
# İnternet Mimarisi ve Tasarımı

- Temel prensipler:
  - İnternet, mevcut hizmetleri ve icat edilecek yeni hizmetleri barındıracak şekilde tasarlanmıştır.
  - İnternet, herhangi bir ağ teknolojisini barındıracak ve her teknolojinin uygun olduğu yerde kullanılmasına izin verecek şekilde tasarlanmıştır.

---
# İnternet Felsefesi

- Altyapı:
  - Paket iletişim hizmeti sağlar.
  - Ekli tüm uç noktaları (endpoints) eşit kabul eder (herhangi bir uç nokta diğerine paket gönderebilir).
  - Paket içeriğini kısıtlamaz veya dikte etmez.
  - Altta yatan ağ teknolojilerini kısıtlamaz veya dikte etmez.

- Ekli uç noktalar:
  - Diğer uç noktalardaki uygulamalarla iletişim kurmak için ağı kullanan uygulamaları çalıştırır.
  - Tüm içeriği kontrol eder ve tüm hizmetleri sağlar.

---
# İnternet Felsefesinin Avantajları

- Heterojen altyapı ağlarını barındırır.
- Rastgele uygulama ve hizmetleri barındırır.
- İletişimi hizmetlerden ayırır.

---
# İnternet

- "Ağların ağı" (network of networks) yaklaşımını izler.
- Rastgele ağların dahil edilmesine izin verir.
- Bireysel ağları birbirine bağlamak için IP yönlendiricileri (routers) kullanır.
- Her yönlendiricinin iki veya daha fazla ağa bağlanmasına izin verir.

> 📷 *[Görsel: Ağlar ve yönlendiriciler arasındaki bağlantı diyagramı — yakında eklenecek]*

---
# İnternet Mimarisi: Mantıksal Görünüm

- İnternet'e bağlı bilgisayarlara ana bilgisayar (host) denir.
- Bir ana bilgisayar için İnternet tek bir devasa ağ gibi görünür.

> 📷 *[Görsel: Ana bilgisayarlar ve devasa ağ mantıksal görünümü — yakında eklenecek]*

---
# İnternet Mimarisi: Fiziksel Görünüm

- Yönlendiriciler (routers) ile birbirine bağlanan heterojen ağlardan oluşur.
- Her ana bilgisayar bir ağa bağlanır.

> 📷 *[Görsel: Yönlendiriciler üzerinden bağlı farklı ağlar ve ana bilgisayarların fiziksel görünümü — yakında eklenecek]*

---
<!-- _class: lead -->
# İnternet Adresleme (Internet Addressing) Konusuna Girmeden Önce

---
# Durum

- İnternet adresleme, İnternet Protokolü (IP) tarafından tanımlanır.
- IP değişmektedir:
  - Mevcut sürüm 4'tür (IPv4).
  - Yeni sürüm 6'dır (IPv6).

---
# İnternet Protokolünün Tarihçesi

- IP, 1978'de TCP'den ayrıldı.
- Sürüm 1-3 hızla bir kenara bırakıldı; sürüm 4 araştırmacılar tarafından kullanılan ilk sürüm oldu.
- 1990'ların başına gelindiğinde, 32 bitlik adres alanının "yakında" tükeneceği endişesiyle yeni bir IP sürümü talep eden bir hareket başladı.
- 1993'te, IETF teklifler aldı ve bir uzlaşma sağlamak için bir çalışma grubu oluşturdu.
- 1995'te yeni bir sürüm önerildi ve belgeler yazıldı.

---
# Yeni IP Sürümünün Arka Planı

- Çeşitli gruplar özellikler hakkında görüş bildirdi:
  - Kablo şirketleri yayın (broadcast) teslimatı için destek istedi.
  - Telefon şirketleri yakında herkesin bağlantı yönelimli (connection-oriented) bir ağ teknolojisi (ATM) kullanacağını savundu.
  - Bazı gruplar mobilite istedi.
  - Ordu daha iyi güvenlik için baskı yaptı.
- Bir uzlaşmaya varıldı: IP sürüm 6 (IPv6) yukarıdakilerin hepsini içerir.

---
# IPv4'ü Değiştirmenin Zorlu Mücadelesi

- IP'yi değiştirmek zordur çünkü:
  - IP, İnternet protokollerinin kalbinde yer alır.
  - IP'nin 4. sürümü kendini kanıtlamış bir geçmişe sahiptir.
  - Mevcut IP sürümünün başarısı inanılmazdır — protokol; donanım teknolojilerindeki, heterojen ağlardaki değişikliklere ve son derece büyük ölçeklere uyum sağlamıştır.

---
# Kum Saati Modeli

> 📷 *[Görsel: Çeşitli uygulamalar ve ağlar arasında merkezde IP'nin bulunduğu kum saati modeli — yakında eklenecek]*

- IP ortada yer alır; onu değiştirmek, İnternet'teki tüm ana bilgisayarları ve yönlendiricileri değiştirmek demektir.

---
# Yaklaşımımız

- Günümüz İnternet'inde hem IPv4 hem de IPv6 alakalı ve önemlidir.
- Ders boyunca:
  - Genel kavramları tartışacağız.
  - IPv4 ve IPv6'nın bu kavramları nasıl uyguladığını göreceğiz.

---
<!-- _class: lead -->
# İnternet Adresleme (Internet Addressing)

---
# İnternet'te Adresleme

- Bir internet ağı üzerinde MAC adreslerini kullanabilir miyiz?
- Hayır: Heterojenlik şu anlama gelir:
  - Birden fazla türde MAC adresi vardır.
  - Bir ağda anlamlı olan MAC adresi başka bir ağda anlamlı değildir.
- Çözüm:
  - MAC adreslerinden bağımsız yeni bir adresleme şeması oluşturmak.

---
# İki Adres Biçimi

- Kimlik (Identity):
  - Her uç noktaya (endpoint) atanan benzersiz numara.
  - Ethernet adresine benzer.
- Konum Belirleyici (Locator):
  - Uç nokta adresi konum bilgisini kodlar, örneğin:
    - Coğrafi konum
    - Bir hizmet sağlayıcısına göre konum
    - Belirli bir fiziksel ağ üzerindeki bilgisayar

---
# Akılda Tutulması Gereken İki Prensip

- Hem kimlik hem de konum belirleyici formların bazı durumlarda avantajları vardır; hiçbir form her durumda en iyisi değildir.
- Adresleme doğal olarak yönlendirme (routing) ile bağlantılıdır; bir adresleme şeması seçimi, rotaları hesaplama ve sürdürme maliyetini etkiler.

---
# IPv4 Adresleme Şeması

- Her İnternet ana bilgisayarına benzersiz bir numara atanır.
- IPv4 adresi olarak bilinen 32 bitlik ikili değerdir.
- Sanal adrestir, MAC adresinden türetilmemiştir.
- İki parçaya ayrılır:
  - Önek (Prefix), fiziksel ağı tanımlar (konum belirleyici).
  - Sonek (Suffix), ağ üzerindeki bir ana bilgisayarı tanımlar (kimlik).

---
# Noktalı Ondalık Gösterim (IPv4)

- İnsanlar için uygundur.
- IPv4 adresini sekizer bitlik (octet) sekizli gruplara böler.
- Her sekizliyi noktalarla ayırarak ondalık (decimal) olarak temsil eder.
- Örnekler:

| 32-bit İkili (Binary) Sayı | Eşdeğer Noktalı Ondalık |
| :--- | :--- |
| `10000001 00110100 00000110 00000000` | 129.52.6.0 |
| `11000000 00000101 00110000 00000011` | 192.5.48.3 |
| `00001010 00000010 00000000 00100101` | 10.2.0.37 |
| `10000000 10000000 11111111 00000000` | 128.128.255.0 |

---
# Önek ve Sonek Arasındaki Bölünme

- Orijinal şema (Sınıflı Adresleme - classful addressing):
  - Her adres sekizli (8 bit) sınırında bölünürdü.
  - Bölünme, adresin kendisinden hesaplanabilirdi.
- Mevcut şema (Sınıfsız Adresleme - classless addressing):
  - Resmi adı Sınıfsız Etki Alanları Arası Yönlendirme (CIDR).
  - Bölünmeye rastgele bit konumunda izin verilir.
  - Sınır (boundary), adresin dışında belirtilmelidir.

---
# Adres Maskesi (Address Mask)

- Sınıfsız adresleme ile birlikte gereklidir.
- Bir ağ ile ilişkilendirilir.
- O ağ için adreslerin ağ öneki (network prefix) ve ana bilgisayar soneki (host suffix) olarak nasıl bölüneceğini belirtir.
- 32 bitlik ikili değerdir:
  - 1 bitleri öneke karşılık gelir.
  - 0 bitleri soneke karşılık gelir.
- Altı bitlik öneki belirten örnek maske:
  `11111100 00000000 00000000 00000000`

---
# CIDR Gösterimi

- İnsanlar tarafından adres maskesini girmek için kullanılır.
- Noktalı ondalık hatalarını önler.
- Adresin ardına bir eğik çizgi (slash) ve X tamsayısı eklenir; burada X, önek bitlerinin sayısıdır.
- Örnek:
  - Noktalı ondalıkta 26 bitlik bir maske şöyledir:
    `255.255.255.192`
  - CIDR bunu sadece şu şekilde yazar:
    `/26`

---
# CIDR ve Noktalı Ondalık Eşdeğerlikleri Tablosu

| Uzunluk (CIDR) | Adres Maskesi | Notlar |
| :--- | :--- | :--- |
| `/17` | `255.255.128.0` | |
| `/18` | `255.255.192.0` | |
| `/19` | `255.255.224.0` | |
| ... | ... | ... |
| `/24` | `255.255.255.0` | 3-sekizli sınırı |
| ... | ... | ... |
| `/32` | `255.255.255.255` | Tümü 1'ler (ana bilgisayara özel maske) |

---
# CIDR Neden Faydalıdır?

- İnternet Servis Sağlayıcıları (ISP) IP adresleri atar.
- N tane bilgisayarı olan kurumsal bir müşterinin N tane adrese ihtiyacı vardır.
- CIDR, ISP'nin sayıyı 2'nin en yakın kuvvetine yuvarlamasına olanak tanır.
- Örnek:
  - ISP'nin `128.211.0.0/16` adres bloğuna sahip olduğunu varsayalım.
  - Müşterinin 12 bilgisayarı var.
  - ISP, müşteriye 4 bitlik bir sonek atar.
  - Kullanılan maske `/28`'dir.
  - Örnek: Müşteriye `128.211.0.16/28` atanır.
  - Müşteri sahasındaki her bilgisayar benzersiz son 4 bite sahiptir.

---
# /28 Adres Bloğu Örneği

- Ağ Öneki (Network Prefix): `128.211.0.16 /28`
- En Yüksek Ana Bilgisayar Adresi: `128.211.0.30`
- En Düşük Ana Bilgisayar Adresi: `128.211.0.17`
- Adres Maskesi: `255.255.255.240`

---
# Özel IPv4 Adresleri

- Bazı adres biçimleri ayrılmıştır:

| Önek | Sonek | Adres Türü | Amaç |
| :--- | :--- | :--- | :--- |
| tümü 0'lar | tümü 0'lar | bu bilgisayar | önyükleme (bootstrap) sırasında kullanılır |
| ağ | tümü 0'lar | ağ | bir ağı tanımlar |
| ağ | tümü 1'ler | yönlendirilmiş yayın | belirtilen ağda yayın (broadcast) |
| tümü 1'ler | tümü 1'ler | sınırlı yayın | yerel ağda yayın |
| 127 | herhangi | geridöngü (loopback) | test |

- Geridöngü adresi (`127.0.0.1`) test için kullanılır. Paketler yerel ana bilgisayardan asla ayrılmaz.
- `240.0.0.0/8` ve üzeri adresler çoklu yayındır (multicast).

---
# Ana Bilgisayar Adresi Sayısı

- Belirli bir ağ öneki için, tümü 0'lar ve tümü 1'ler olan soneklerin özel bir anlamı vardır.
- Sonuç: Bir sonek N bite sahipse, ağda $2^N - 2$ tane ana bilgisayar (host) bulunabilir.

---
# IP Adresleme Prensibi

Bir IP adresi belirli bir bilgisayarı tanımlamaz. Bunun yerine, her IP adresi bir bilgisayar ile bir ağ arasındaki bağlantıyı tanımlar.

- Sonuç: Birden fazla ağ bağlantısı olan bir yönlendirici (router) veya ana bilgisayara, her bağlantı için bir IP adresi atanmalıdır.
- Not: Birden fazla ağ bağlantısı olan ana bilgisayara çok bağlantılı (multi-homed) ana bilgisayar denir.

---
# IPv4 Adres Ataması Örneği

> 📷 *[Görsel: Ağlar ve yönlendiriciler (routers) üzerindeki IPv4 adres atamalarını gösteren diyagram — yakında eklenecek]*

- Her ağa benzersiz bir önek (prefix) atanır.
- Bir ağdaki her ana bilgisayara benzersiz bir sonek (suffix) atanır.

---
# IPv6 Ana Bilgisayar Adresleri

- IPv4 gibi:
  - İkili (binary) değerdir.
  - Konum belirleyici önek (locator prefix) ve benzersiz kimlik sonekine (unique ID suffix) bölünmüştür.
  - Bir ağa olan bağlantıyı tanımlar.
- IPv4'ten farklı olarak:
  - 128 bit uzunluğundadır.
  - Sonek, MAC adresinden türetilebilir.
  - 3 seviyeli bir adres hiyerarşisi vardır.

---
# IPv6 3 Seviyeli Hiyerarşisi

| K bit | 64 - K bit | 64 bit |
| :--- | :--- | :--- |
| KÜRESEL ÖNEK | ALT AĞ (SUBNET) | ARAYÜZ (INTERFACE / BİLGİSAYAR) |

- Önek boyutu ISP tarafından seçilir.
- Alt ağ (subnet) alanı, bir organizasyonun birden fazla ağa sahip olmasına olanak tanır.

---
# IPv6 Adres Türleri

- **Tek noktaya yayın (Unicast):** Adres tek bir bilgisayara karşılık gelir. Adrese gönderilen bir veri paketi (datagram), o bilgisayara giden en kısa yol (shortest path) boyunca yönlendirilir.
- **Çoklu yayın (Multicast):** Adres bir bilgisayar grubuna karşılık gelir ve gruptaki üyelik her an değişebilir. IPv6, veri paketinin bir kopyasını grubun her bir üyesine teslim eder.
- **Herhangi bir noktaya yayın (Anycast):** Adres, ortak bir öneki paylaşan bir bilgisayar grubuna karşılık gelir. Adrese gönderilen bir veri paketi, tam olarak bilgisayarlardan birine (örneğin, göndericiye en yakın olan bilgisayara) teslim edilir.

---
# İki Nokta Üst Üste Hex (Colon Hex) Gösterimi

- Adresleri girmek için insanlar tarafından kullanılan sözdizimsel bir formdur.
- IPv4'ün noktalı ondalık gösteriminin yerini alır.
- 16 bitlik grupları iki nokta üst üste işaretiyle (:) ayrılmış onaltılık (hexadecimal) düzende ifade eder.
- Örnek:
  `105.220.136.100.255.255.255.255.0.0.18.128.140.10.255.255`  
  şu hale gelir:  
  `69DC:8864:FFFF:FFFF:0:1280:8C0A:FFFF`

---
# İki Nokta Üst Üste Sıkıştırması (Colon Compression)

- Birçok IPv6 adresi uzun sıfır dizileri içerir.
- Birbirini izleyen sıfırlar iki adet iki nokta üst üste (`::`) ile değiştirilebilir.
- Örnek:
  `FF0C:0:0:0:0:0:0:B1`  
  şu şekilde yazılabilir:  
  `FF0C::B1`

---
# IPv6'yı Benimsemek İçin İki Ana Neden

- Daha fazla adres:
  - Sonunda IPv4 adresleri tükenecektir.
  - IPv6 ihtiyacımız olandan çok daha fazla adres sağlar (Dünya yüzeyinin metrekaresi başına 1024 adres!).
- İlgi ve heyecan:
  - Araştırmacılar IPv6'yı aksiyonun bir parçası olma fırsatı olarak görüyor.
  - Endüstriler IPv6'yı gelir artırma fırsatı olarak görüyor.

---
<!-- _class: compact -->
# IPv6 ve Çocuklar

- Ünlü Ebeveynin Çocuğu (İnternet Protokolü sürüm 6):
  - Büyüklük bekleniyor ve beklentiler çok yüksek.
  - Çocuğun başarısı genellikle ebeveyninki ile karşılaştırılır (IPv6'nın başarısı IPv4 ile karşılaştırılır).
  - Takdir kazanmak için çocuğun ebeveynden daha iyi performans göstermesi gerekir.
  - Çocuğun ebeveynin "gölgesinde" büyüdüğünü söylüyoruz.
  - Kötü haber: Mühendislikteki "ikinci sistem sendromu" (second-system syndrome) olarak bilinen kural devreye giriyor.

---
<!-- _class: lead -->
# İnternet Protokolü Paketleri (IP Datagramları)

---
# İnternet Paketleri

Uyumsuz ağları içerdiği için, İnternet belirli bir donanım paketi formatını benimseyemez. Heterojenliği barındırmak için, İnternet Protokolü (IP) donanımdan bağımsız bir paket formatı tanımlar.

---
# IP Veri Paketi (IP Datagram)

- İnternet'te kullanılan sanal paket formatıdır.
- Bir ağ çerçevesi (network frame) ile aynı genel düzene sahiptir:
  - Başlık (Header)
  - Veri Alanı (payload alanı olarak bilinir)
- Başlık formatı protokol sürümüne (IPv4 veya IPv6) göre belirlenir.
- Yükün (payload) boyutu uygulama tarafından belirlenir:
  - Maksimum yük neredeyse 64K sekizlidir (octets).
  - Tipik bir veri paketi boyutu 1500 sekizlidir.

---
# IPv4 Veri Paketi Başlığı

- Çoğu başlık alanının sabit bir boyutu ve konumu vardır.
- Başlık; kaynağı (source), hedefi (destination) ve içerik türünü (content type) belirtir.

> 📷 *[Görsel: IPv4 Veri Paketi Başlık Düzeni — yakında eklenecek]*

---
# Birkaç Ayrıntı

- **KAYNAK IP ADRESİ** (SOURCE IP ADDRESS) alanı, orijinal kaynağın IPv4 adresini verir.
- **HEDEF IP ADRESİ** (DESTINATION IP ADDRESS) alanı, nihai hedefin IPv4 adresini verir.
- Ara yönlendirici (router) adresleri başlıkta yer almaz.
- Başlık boyutu:
  - Neredeyse hiçbir İnternet veri paketi (datagram) seçenekleri (options) içermez.
  - Bu nedenle başlık uzunluğu genellikle 20 sekizlidir (octets).

---
# IPv6 Başlık Düzeni

- Birden fazla başlık kullanılır: temel (base) artı sıfır veya daha fazla isteğe bağlı uzantı (extension) başlığı.

> 📷 *[Görsel: IPv6 Başlık Düzeni — yakında eklenecek]*

- Uzantı başlıkları ve/veya yük (payload) temel başlıktan çok daha büyük olabilir.

---
# IPv6 Temel Başlık (Base Header) Formatı

- Akış Etiketi (Flow Label) alanı, veri paketinin (datagram) bir akış (flow) ile ilişkilendirilmesine izin verir.

> 📷 *[Görsel: IPv6 Temel Başlık Formatı — yakında eklenecek]*

---
# Başlıkları Tanımlama

- Her başlık bir **SONRAKİ BAŞLIK** (NEXT HEADER) alanı içerir.
- Değer, sonraki öğenin türünü belirtir.
- Her katman 4 protokolüne (UDP, TCP vb.) de bir tür atanmıştır.

---
# Sonraki Başlık (Next Header) Alanının Örnek Kullanımı

- Bir veri paketi temel başlık (base header) ve taşıma (transport) protokolü içerdiğinde başlıkların gösterimi:
  `Temel Başlık (NEXT=TCP) -> TCP Verisi`
- Bir veri paketi ayrıca isteğe bağlı bir rota başlığı (route header) içerdiğinde başlıkların gösterimi:
  `Temel Başlık (NEXT=ROUTE) -> Rota Başlığı (NEXT=TCP) -> TCP Verisi`

---
# Bir Uzantı Başlığının Boyutu

- Sabit uzunluktaki başlıklar:
  - Boyut, standartlar belgesinde belirtilmiştir.
  - Protokol yazılımı boyut sabitini (size constant) içerir.
- Değişken uzunluktaki başlıklar:
  - Boyut gönderici tarafından belirlenir.
  - Başlık, açık (explicit) bir uzunluk alanı içerir.

---
# Paket İşleme Üzerindeki Sonuçlar

- Bir IPv6 veri paketi (datagram) alan bir ana bilgisayarı veya yönlendiriciyi düşünün.
- Veri paketi bir dizi uzantı başlığı içerir.
- Her uzantı başlığı açık bir uzunluk alanı içerebilir.
- Veri paketini ayrıştırmak (parse) için IP yazılımının başlıklar arasında yineleme yapması (iterate) gerekir.
- Sonuç: IPv6'yı işlemek ekstra genel maliyet (overhead) getirebilir.

---
<!-- _class: lead -->
# Veri Paketi Yönlendirme (Datagram Forwarding)

---
# İnternet İletişim Paradigması

- Her veri paketi (datagram) bağımsız olarak ele alınır.
- Veri paketi kaynak bilgisayarda oluşturulur.
- Kaynak, veri paketini en yakın yönlendiriciye gönderir.
- Yönlendirici, veri paketini hedefe giden yoldaki bir sonraki yönlendiriciye iletir.
- Son yönlendirici, veri paketini hedefe teslim eder.
- Veri paketi her adımda tek bir fiziksel ağdan geçer.

---
# Veri Paketi Yönlendirme

- Yoldaki her yönlendirici ve başlangıçtaki ana bilgisayar tarafından gerçekleştirilir.
- Veri paketi için bir sonraki durağı (next hop) aşağıdakilerden biri olarak seçer:
  - Yol boyunca bir sonraki yönlendirici
  - Nihai hedef
- Ağ başına bir girişe sahip bir yönlendirme tablosu (forwarding table) kullanır.
- Önemli nokta: Yönlendirme tablosunun boyutu, İnternet'teki ağ sayısıyla orantılıdır.

---
# Yönlendirme Tablosu Girişi

- Sadece IP adreslerini kullanır (MAC adreslerini kullanmaz).
- Şunları içerir:
  - Hedef ağ IP öneki
  - Hedef ağ için adres maskesi
  - Bir sonraki durağın (next hop) IP adresi

---
# Bir IPv4 Yönlendirme Tablosu Örneği

> 📷 *[Görsel: Çeşitli ağlar, yönlendiriciler ve örnek bir IPv4 yönlendirme tablosu — yakında eklenecek]*

- Uygulamada, tablo genellikle varsayılan (default) bir giriş içerir.

---
# Önek Çıkarma (Prefix Extraction)

- Yönlendirme paradigması:
  - Yönlendirme (forwarding) yaparken ağ önekini kullan.
  - Teslim (delivering) yaparken ana bilgisayar adresini kullan.
- Kavramsal yönlendirme adımı:
  - Her bir yönlendirme tablosu girişindeki hedef ile veri paketinin hedef adresi olan D'yi karşılaştır.
  - Karşılaştırma sırasında yalnızca ağ önekini incele.
- Not: Yönlendirme tablosundaki maske, karşılaştırmayı verimli hale getirir:
  `if ( (Mask[i] & D) == Destination[i] ) forward to NextHop[i];`

---
# En Uzun Önek Eşleşmesi (Longest Prefix Match)

- Sınıfsız adresleme, yönlendirme tablosu girişlerinin belirsiz (ambiguous) olabileceği anlamına gelir.
- Örnek: `128.10.2.3` hedefini ve şu iki girişi içeren bir tabloyu düşünün:
  - `128.10.0.0 / 16` (sonraki durak A)
  - `128.10.2.0 / 24` (sonraki durak B)
- Hedef her ikisiyle de eşleşir!
- Çözüm: En uzun öneke sahip eşleşmeyi seçin (örnekte B sonraki durağını alın).
- Buna en uzun önek eşleşmesi (longest prefix match) denir.

---
# Veri Paketi Kapsülleme (Datagram Encapsulation)

- Altta yatan ağ donanımı veri paketlerini (datagrams) anlamadığı için gereklidir.
- Veri paketinin tamamı, çerçevenin (frame) yük (payload) alanında seyahat eder.
- Çerçeve başlığı (Frame Header), bir sonraki durağın (next hop) MAC adresini içerir.
- Çerçeve sadece bir ağ üzerinden seyahat etmek için kullanılır: Çerçeve bir sonraki durağa ulaştığında, veri paketi çıkarılır ve çerçeve atılır.
- Veri paketi uçtan uca (end-to-end) sağlam kalır.

---
# Kapsülleme Çizimi

> 📷 *[Görsel: Veri paketinin kaynak, yönlendiriciler ve hedef arasında çerçeveler içinde kapsüllenerek nasıl taşındığını gösteren diyagram — yakında eklenecek]*

---
# İnternet İletişiminin Anlambilimi (Semantics)

- IP, "en iyi çaba teslimatı" (best effort delivery) anlambilimini kullanır.
- IP her veri paketini (datagram) teslim etmeye çalışır, ancak veri paketinin şunlara maruz kalabileceğini belirtir:
  - Kaybolma
  - Çoğaltılma (Duplicated)
  - Gecikme (Delayed)
  - Sıra dışı teslimat (Delivered out-of-order)
  - Bitleri bozulmuş olarak teslimat (Delivered with bits scrambled)
- Motivasyon: Herhangi bir altyapı ağına uyum sağlamak.
- Not: Uygulamada IP çalışır ve iyi çalışır.

---
# MTU ve Ağ Heterojenliği

- Her ağ teknolojisi, bir pakette gönderilebilecek en büyük veri miktarını belirleyen bir Maksimum Aktarım Birimi (Maximum Transfer Unit - MTU) belirler.
- Örnek: Ethernet MTU'su 1500 sekizlidir (octets).
- Bir veri paketi en fazla ağ MTU'su kadar büyük olabilir.
- Farklı MTU değerlerine sahip iki ağ arasındaki bir senaryo, bazı büyük veri paketlerinin ilerlemesini engelleyebilir.

---
# Veri Paketi Parçalanması (Datagram Fragmentation)

- Heterojen MTU'lara uyum sağlama tekniğidir.
- Veri paketi MTU'yu aşarsa gereklidir.
- Orijinal veri paketi, parça (fragment) adı verilen daha küçük veri paketlerine bölünür.
- Parçanın başlığı, orijinal veri paketi başlığından türetilir.
- Her parça bağımsız olarak yönlendirilir.
- IPv4, yönlendiricilerin (routers) parçalama yapmasına izin verir.
- IPv6, gönderen ana bilgisayarın parçalama yapmasını gerektirir.
- Hem IPv4 hem de IPv6 için önemli prensip:
  Parçaları nihai hedef birleştirir (reassembles).

---
# Parçalanmanın (Fragmentation) Genel Fikri

- Yükü (payload) bir dizi veri paketine (datagrams) bölün.
- Not: Kuyruk (tail) parçası diğerlerinden daha küçük olabilir.

> 📷 *[Görsel: Orijinal veri paketi yükünün birden çok IP parçasına bölünme diyagramı — yakında eklenecek]*

---
# IPv4 Parçalama Detayları

- Veri paketi başlığı, parçalamayı kontrol eden sabit alanlar içerir.
- FLAGS (Bayraklar) alanındaki bir bit, belirli veri paketinin bir parça mı yoksa tam bir veri paketi mi olduğunu belirtir.
- Ek bir FLAGS biti, parçanın orijinal veri paketinin kuyruğunu (sonunu) taşıyıp taşımadığını belirtir.
- OFFSET (Kaydırma) alanı, yükün orijinal veri paketindeki nereye ait olduğunu belirtir.

---
# IPv6 Parçalama Detayları

- Daima orijinal kaynak tarafından gerçekleştirilir, asla yönlendiriciler tarafından yapılmaz.
- Kural: Bir IPv6 veri paketi İnternet'ten geçerken hiçbir başlık değişikliğine izin verilmez.
- Sonuçlar:
  - Kaynak, yol MTU'sunu (path MTU) keşfetmelidir.
  - Ayrı bir uzantı başlığı parçalama bilgilerini (IPv4 ile aynı öğeleri) içerir.
- Veri paketinin parçalanabilir kısmı bazı uzantı başlıklarını içerebilir.

---
# IPv6 Parçalanmasının Gösterimi

> 📷 *[Görsel: Bir IPv6 veri paketinin parçalanamaz ve parçalanabilir bölümlerine ayrılarak parçalanmasını gösteren diyagram — yakında eklenecek]*

- Bir veri paketi parçalara (fragments) bölünür.

---
# Parçaları Toplama (Collecting Fragments)

- Hedef, gelen parçaları toplar.
- İLGİLİ parçaları gruplamak için KİMLİK (IDENTIFICATION) alanı kullanılır.
- OFFSET (Kaydırma) alanı, alıcının orijinal yükü (payload) yeniden oluşturmasını sağlar.
- SON PARÇA (LAST FRAGMENT) biti, alıcının tüm parçaların ne zaman geldiğini bilmesini sağlar.
- Bir parça zaman aşımı süresi içinde gelmezse, veri paketinin tamamı atılır.

---
# Düşünce Sorusu

- Varsayalım ki:
  - Bir satıcı, bir bilgisayar ile bir Ethernet anahtarı arasına sığan bir ağ güvenlik cihazı satıyor.
  - Cihaz, bilgisayarın gönderdiği her IP veri paketini şifreliyor.
  - Şifreleme, yüke (payload) yalnızca üç baytlık ekstra veri ekliyor.
- Ölçümler, cihaz etkinleştirildiğinde verimin (throughput) önemli ölçüde düştüğünü gösteriyor.
- Düşük verimin nedenini açıklayın.

---
<!-- _class: lead -->
# Adres Çözümleme (Address Resolution)

---
# Veri Paketi İletiminin Gözden Geçirilmesi

- Ana bilgisayar veya yönlendiricinin göndereceği bir veri paketi vardır.
- IP, veri paketinin hedef adresini yönlendirme tablosunda aramak için en uzun önek eşleşmesini (longest-prefix match) kullanır ve şunları elde eder:
  - Sonraki durağın (next hop) IP adresi.
  - Üzerinden gönderileceği ağ (birden fazla ağ bağlantısı olması durumunda).
- IP, veri paketini çerçeve (frame) içine kapsüller (tüm veri paketi çerçevenin yük alanına yerleştirilir).
- Sonuçta ortaya çıkan çerçeve sonraki durağa gönderilmeye hazır mıdır?
  Hayır!

---
# Donanım ve Protokol Adresleme

- Altta yatan ağ donanımı:
  - Yalnızca MAC adreslerini anlar.
  - Giden her çerçevenin sonraki durağın MAC adresini içermesini gerektirir.
- IP yönlendirme:
  - Yalnızca (soyut) IP adresleriyle ilgilenir.
  - Sonraki durağın IP adresini hesaplar.
- Sonuç:
  Bir çerçeve gönderilebilmesi için sonraki durağın IP adresi bir MAC adresine çevrilmelidir (translated).

---
# Adres Çözümleme

- IP adresini, donanımın anladığı eşdeğer MAC adresine çevirir.
- IP adresi çözümlenmiş (resolved) kabul edilir.
- Bir seferde tek bir fiziksel ağ ile sınırlıdır.
- Örnek: X bilgisayarının Y bilgisayarına gönderim yaptığını düşünelim.

> 📷 *[Görsel: Çeşitli ağlar, yönlendiriciler üzerinden bilgisayar X'ten Y'ye yönlendirme rotası — yakında eklenecek]*

- Her durakta (hop) bir MAC adresi gereklidir.

---
# MAC Adresleri ile İlgili Bir Örnek

> 📷 *[Görsel: MAC ve IP adresleri, yönlendiriciler R1 ve R2 üzerinden X ve Y arasındaki paket iletim süreci tablosu — yakında eklenecek]*

- Bir ana bilgisayar veya yönlendirici bir sonraki durağın MAC adresini nasıl bulabilir?

---
# Adres Çözümleme Protokolü (ARP)

- Ethernet üzerinden IPv4 için tasarlanmıştır.
- Aynı fiziksel ağdaki iki bilgisayar tarafından kullanılır.
- Bir bilgisayarın diğer bir bilgisayarın MAC adresini bulmasını sağlar.
- 2. katmanda (layer 2) çalışır.
- Mesaj alışverişi yapmak için ağı kullanır.
- Adres arayan bilgisayar bir istek (request) gönderir ve diğeri buna cevap (reply) verir.

---
# ARP Alışverişi Örneği

- Varsayalım ki:
  - Bir Ethernet'e dört bilgisayar bağlıdır.
  - B bilgisayarının göndereceği bir veri paketi vardır.
- B Bilgisayarı:
  - Sonraki durak adresini (IC) bulmak için yönlendirme tablosunu kullanır.
  - Bir ARP isteği yayınlar (broadcasts): "IP adresi IC olan bir bilgisayar arıyorum."
- C Bilgisayarı:
  - İsteği alır ve yanıtlar; "IP adresi IC olan bilgisayar benim."

---
# ARP Mesaj Alışverişinin Gösterimi

> 📷 *[Görsel: W, X, Y, Z bilgisayarlarının bağlı olduğu Ethernet anahtarı üzerinden ARP mesajlarının (istek ve cevap) yayınlanma diyagramı — yakında eklenecek]*

- İstek (Request) tüm bilgisayarlara yayınlanır (broadcast).
- Sadece hedeflenen alıcı yanıt verir.
- Cevap (Reply) tek noktaya yayın (unicast) olarak gönderilir.

---
# ARP Mesaj Formatı

- Aşağıdakilere izin verecek kadar geneldir:
  - Rastgele üst düzey protokol adresi.
  - Rastgele donanım adresi.
- Uygulamada sadece IP ve 48 bitlik Ethernet adresleriyle kullanılır.

> 📷 *[Görsel: ARP Mesaj Formatı (Donanım Adresi Türü, Protokol Adresi Türü, Gönderen ve Hedef Adresler vb.) — yakında eklenecek]*

---
# ARP Kapsülleme (Encapsulation)

- ARP mesajı, donanım çerçevesinin (hardware frame) yük alanına (payload area) yerleştirilir.
- Ethernet ile kullanıldığında tür `0x0806`'dır.
- Göndermeden önce kaynak ve hedef MAC adresleri çerçeve başlığına (frame header) eklenmelidir.

> 📷 *[Görsel: ARP Mesajının Çerçeve İçinde Kapsüllenme Yapısı — yakında eklenecek]*

---
# ARP Algoritması ve Ön Bellekleme (Caching)

- **Verilen:** Gelen bir ARP isteği (request) veya yanıtı (response)
- **Amaç:** Mesajı işlemek ve ARP önbelleğini güncellemek
- **Yöntem:**
  Gönderenin IP adresi I'yı ve MAC adresi M'yi çıkar (extract)
  Eğer (adres I zaten ARP önbelleğinde ise) {
    İlgili MAC adresini M ile değiştir;
  }
  Eğer (mesaj bir istek ise ve hedef "ben" isem) {
    Önbellekte mevcut giriş yoksa gönderenin girişini ekle;
    Bir yanıt (response) oluştur ve gönder;
  }

---
# Protokol ve MAC Adresleme Arasındaki Sınır

- ARP, donanım adreslerini izole ederek üstteki katmanların yalnızca IP adreslerini kullanmasını sağlar.

> 📷 *[Görsel: Uygulama, Taşıma ve İnternet katmanlarında IP adreslerinin, Ağ Arayüzü ve Fiziksel katmanlarda MAC adreslerinin kullanımı — yakında eklenecek]*

---
# Düşünce Sorusu

- ARP bazen bir güvenlik açığı olarak gösterilir.
- Birisi belirli bir ağa erişim sağlarsa, paketleri durdurmak (intercept) için ARP'den nasıl yararlanabilir?

---
# IPv6 ile Adres Bağlama (Address Binding)

- IPv6, ARP kullanmaz.
- Bunun yerine IPv6, IPv6 Komşu Keşfi (IPv6 Neighbor Discovery - IPv6-ND) olarak bilinen yeni bir adres bağlama mekanizması tanımlar.
- IPv6-ND:
  - Bir komşu önbelleği (neighbor cache) tutar.
  - Önbelleği her zaman güncel tutar.
- IPv6-ND operasyonu:
  - Komşuları bulmak ve önbelleği doldurmak için çoklu yayın (multicast) isteği gönderir.
  - Komşuya herhangi bir veri paketi gönderilmese bile, komşuları periyodik olarak yoklar (polls).

---
<!-- _class: lead -->
# Hata Bildirim Mekanizması

---
# IP Hata Tespiti ve Raporlama

- Hatırlayalım, IP veri paketlerinin (datagrams) şunlara maruz kalmasına izin verir:
  - Kaybolma
  - Çoğaltılma
  - Gecikme
  - Sıra dışı teslimat
- Hata raporlamaya neden ihtiyaç duyulur?
- Cevap: "En iyi çaba" (best-effort) teslimatı "dikkatsiz" (careless) demek değildir — tasarım, temeldeki ağlardaki hataları tanıtmak için değil tolere etmek için amaçlanmıştır.
- IP, tespit edildiğinde sorunları raporlar.

---
# Genel Hata Tespiti

- Çeşitli temel hata tespit mekanizmaları mevcuttur.
- Örnekler:
  - Eşlik bitleri (Parity bits) ve diğer ileri hata kodları iletim hatalarını tespit edebilir.
  - Bir CRC hatalı bir çerçeveyi tespit edebilir.
  - IP başlık sağlama toplamı (checksum) hatalı bir veri paketi başlığını tespit edebilir.
  - IP'nin TTL'si (hop sınırı) bir yönlendirme döngüsünü (routing loop) tespit edebilir.
  - Yeniden birleştirme zamanlayıcısı kaybolan parçaları (fragments) tespit edebilir.
- Sadece bazı hata türleri raporlanabilir.

---
# İnternet Kontrol Mesajı Protokolü (ICMP)

- IP'nin gerekli ve ayrılmaz bir parçasıdır.
- Hataları orijinal kaynağa raporlar.
- Mesajları taşımak için IP kullanır.
- Her biri belirli bir formata ve içeriğe sahip birçok mesaj türü tanımlar.
- Hata raporlarının yanı sıra bilgi mesajları da içerir.
- ICMPv4 ve ICMPv6 birçok mesajı paylaşır.

---
# Örnek ICMP Mesajları

| Numara | Tür (Type) | Amaç |
| :--- | :--- | :--- |
| 0 | Yankı Yanıtı (Echo Reply) | `ping` programı tarafından kullanılır |
| 3 | Hedefe Ulaşılamıyor | Veri paketi teslim edilemedi |
| 5 | Yönlendirme (Redirect) | Ana bilgisayar bir rotayı değiştirmeli |
| 8 | Yankı İsteği (Echo Request) | `ping` programı tarafından kullanılır |
| 11 | Süre Aşıldı | TTL süresi doldu veya parçalar (fragments) zaman aşımına uğradı |
| 12 | Parametre Sorunu | IP başlığı hatalı |
| 30 | Traceroute | `traceroute` programı tarafından kullanılır |

- En çok kullanılan ICMP mesajları, `ping` programı tarafından gönderilen ve alınan 8 ve 0'dır.

---
# ICMP Kapsülleme

- İki seviyeli kapsülleme (encapsulation) yapılır:
  - ICMP mesajı bir IP veri paketinde kapsüllenir.
  - IP veri paketi bir ağ çerçevesinde kapsüllenir.

> 📷 *[Görsel: ICMP mesajının IP başlığı ve çerçeve başlığı ile birlikte kapsüllenme yapısı — yakında eklenecek]*

---
# Bir ICMP Hata Raporu Örneği

- S (Kaynak) ana bilgisayarı, hedef D için bir veri paketi oluşturur.
- S, TTL'yi 255'e ayarlar ve veri paketini gönderir.
- Veri paketi İnternet'in ortasında bir döngüye (loop) ulaşır.
- Veri paketi, TTL sıfıra ulaşana kadar döngü etrafında dolaşır.
- TTL'yi sıfıra indiren yönlendirici (router):
  - S'ye tip 11 ICMP mesajı gönderir.
  - Soruna neden olan veri paketini atar (discards).

---
<!-- _class: lead -->
# Yapılandırma (Configuration)

---
# Protokol Yapılandırması

- Protokoller kullanılmadan önce birçok öğe ayarlanmalıdır:
  - Her ağ arayüzünün IP adresi
  - Her ağ için adres maskesi
  - Yönlendirme tablosundaki başlangıç değerleri
- Bu işlem protokol yapılandırması (protocol configuration) olarak bilinir.
- Genellikle işletim sistemi başlatıldığında (boot) gerçekleşir.
- İki temel yaklaşım vardır:
  - Manuel
  - Otomatik

---
# Manuel Yapılandırma

- IP yönlendiricileri (routers) veya kalıcı (permanent) bir IP adresi olan ana bilgisayarlar için kullanılır.
- Yönetici (Manager):
  - Yapılandırmayı bir kez girer.
  - Yapılandırmanın kalıcı depolamaya kaydedilmesini belirtir.
  - Arayüzler Komut Satırı Arayüzü (CLI) ve web'i içerir.
- İşletim Sistemi (OS):
  - Cihaz her başlatıldığında (boot) kalıcı depolamadan değerleri alır.

---
# Otomatik Yapılandırma

- Esas olarak ana bilgisayarlar için kullanılır.
- Başlangıçta disksiz iş istasyonları (diskless workstations) için oluşturulmuştur.
- Temel fikir:
  - Yapılandırma bilgilerini elde etmek için ağı kullan.
  - Protokol yazılımını yapılandır ve ardından uygulamaları çalıştırmaya başla.
- Görünürdeki paradoks:
  - Otomatik yapılandırma, bilgisayarın protokol parametreleri yapılandırılmadan önce bilgisayarın bir ağı kullanabilmesini gerektirir.

---
# Paradoksu Çözmenin Yolları

- Katman 3 parametrelerini elde etmek için katman 2 protokollerini kullanın, ardından daha yüksek katmanları elde etmek için katman 3'ü kullanın:
  - Tarihi yaklaşımdır.
  - Ethernet yayınına (broadcast) dayanır.
  - Ağdaki bir bilgisayar isteklere yanıt verir.
- Tüm parametreleri elde etmek için katman 3'ü kullanın:
  - Mevcut yaklaşımdır.
  - IP yayınına (IPv4) veya çoklu yayınına (IPv6) dayanır.
  - Yönlendiricilerin istekleri uzak bir sunucuya iletebileceği (forward) anlamına gelir.

---
# Dinamik Ana Bilgisayar Yapılandırma Protokolü (DHCP)

- Otomatik yapılandırma için standart protokoldür.
- Servis sağlayıcılarının (ISP) yanı sıra özel işletmelerde de popülerdir.
- Ana bilgisayar bir istek yayınlar (broadcasts/multicasts) ve bir yanıt alır.
- Tek bir mesaj alışverişi, ana bilgisayarın şunları elde etmesini sağlar:
  - Kullanılacak bir IP adresi ve adres maskesi
  - Varsayılan bir yönlendiricinin (default router) IP adresi
  - Bir DNS sunucusunun adresi
  - Bir DNS adı
  - Önyüklenecek (boot) bir görüntünün konumu (isteğe bağlı)

---
# DHCP Mesaj Formatı

- İstekler (requests) ve yanıtlar (responses) için aynı mesaj formatı kullanılır.

> 📷 *[Görsel: DHCP Mesaj Formatı (OP, HTYPE, CLIENT IP, OPTIONS vb.) — yakında eklenecek]*

---
# DHCP Protokolü

- Protokolün önemli özellikleri:
  - Kaybolma veya çoğaltmadan (duplication) kurtarır.
  - Güç kesintisi ve yeniden başlatmanın (restart) ardından eşzamanlı istek (request) taşmasını (flooding) önler.
  - Ana bilgisayar, DHCP sunucusunu bir kez keşfeder ve gelecekteki etkileşimler için sunucu adresini önbelleğe (cache) alır.
- BOOTstrap Protokolü'nden (BOOTP) türetilmiştir, ancak dinamik adres ataması ekler.

---
# Adres Kiralama Paradigması (Address Lease Paradigm)

- DHCP sunucusu:
  - Bir dizi IP adresine sahiptir.
  - Bir istek (request) geldiğinde kümeden bir adres seçer.
  - Belirli bir T süresi boyunca adres için bir kiralama (lease) yayınlar.
- İstemci (Client):
  - Bir adres alır ve T zaman birimi için bir zamanlayıcı başlatır.
  - İletişim kurmak için adresi kullanır.
  - Zamanlayıcının süresi dolduğunda, sunucunun kiralamayı yenilemesini ister.
  - Ya bir yenileme alır ve zamanlayıcıyı yeniden başlatır ya da adresi kullanmayı bırakır.

---
# Düşünce Sorusu

- Adreslerin nasıl atandığını (assigned) düşünün.
- DHCP kullanan bir ISP, belirli bir zamanda bir müşteriye hangi IP adresini atayacağını seçebilir.
- İki yaklaşım vardır:
  - ISP, her müşteriye daha önce hangi adresin atandığını hatırlayabilir ve aynı adresi kullanabilir.
  - ISP, adresleri rastgele (random) atayabilir, yani müşteri aynı adresi elinde tutamaz.
- Birçok ISP, adresi sık sık değiştirmeye çalışır.
- Neden?

---
# IPv6 Yapılandırması

- DHCPv6 tanımlanmıştır, ancak...
- IPv6, IPv6 otomatik yapılandırma (IPv6 autoconfiguration) olarak bilinen yeni bir prosedürü tercih eder.
- Genel fikir: Ana bilgisayar, bir sunucu kullanmadan bir adres üretebilir (generate).
- Motivasyon: İki ana bilgisayarın daha fazla altyapı olmadan iletişim kurmasını sağlamak.

---
# IPv6 Otomatik Yapılandırma Adımları

- Bir ağ öneki edinin:
  - Geleneksel olarak bir `/64` öneki kullanılmasıdır.
  - Küresel geçerli (globally-valid) önek bir yönlendiriciden elde edilebilir.
  - Yönlendirici yoksa yerel kapsamlı (local-scope) önek oluşturulur.
- Benzersiz bir sonek (suffix) oluşturun.
- Ağdaki başka hiçbir kimsenin ortaya çıkan adresi kullanmadığını doğrulayın.

---
# Uygulamada IPv6 Otomatik Yapılandırması

- Benzersiz bir ana bilgisayar sonekine ihtiyaç vardır.
- `/64` ağ için 64 bitlik bir ana bilgisayar soneki gerekir.
- Önerilen yaklaşım:
  - MAC adresinden başlayın (küresel olarak benzersiz, ancak yalnızca 48 bit).
  - 64 bitlik bir değer oluşturun.
- IEEE standardı EUI-64, bir IEEE MAC adresinin 48 bitinin 64 bitlik bir ana bilgisayar sonekine nasıl yerleştirileceğini belirtir.

---
<!-- _class: lead -->
# Ağ Adres Çevirisi (Network Address Translation - NAT)

---
# NAT Motivasyonu

- IPv4 adresleri tükeniyordu.
- ISP'ler herhangi bir zamanda bir müşteriyi tek bir IP adresiyle sınırlamak isterken, müşteriler birden fazla cihazın çevrimiçi olmasını istiyor.
- Mühendisler her iki sorunu da çözmenin bir yolu olarak Ağ Adresi Çevirisini (NAT) icat ettiler.

---
# NAT Operasyonu

- Kavramsal olarak, NAT cihazı bir sahadaki bilgisayarlar ile İnternet'in geri kalanı arasında bulunur.
- Saha (Site):
  - Sadece bir adet küresel geçerli IP adresine ihtiyaç duyar.
  - İnterneti kullanan birden fazla yerel ana bilgisayara (host) sahip olabilir.
- Yerel ana bilgisayar İnternet'e tam erişime sahiptir.
- Hizmet şeffaftır (transparent):
  - Yerel ana bilgisayarlardaki protokollerde değişiklik yapılmaz.
  - İnternet sunucularındaki protokollerde değişiklik yapılmaz.

---
# NAT'ın Kavramsal Organizasyonu

- NAT cihazı satır içi (in-line) konumdadır.
- İnternet'ten bakıldığında, saha tek bir bilgisayar gibi görünür.
- Saha içinden bakıldığında, her bilgisayarın İnternet'e bağımsız bir bağlantısı var gibi görünür.

> 📷 *[Görsel: NAT Cihazının İnternet ile Çoklu Bilgisayara Sahip Saha Arasındaki Konumu — yakında eklenecek]*

---
# NAT Tarafından Kullanılan Adresler

- NAT cihazı, sahadaki bilgisayarlara IP adresleri dağıtmak için bir DHCP sunucusu çalıştırır.
- Atanan adresler IPv6 yerel bağlantı (link-local) veya IPv4 özel (private) adresleridir.

| Blok | Açıklama |
| :--- | :--- |
| `10.0.0.0/8` | Sınıf A özel adres bloğu |
| `169.254.0.0/16` | Sınıf B özel adres bloğu |
| `172.16.0.0/12` | 16 bitişik Sınıf B bloğu |
| `192.168.0.0/16` | 256 bitişik Sınıf C bloğu |

- NAT, saha ve İnternet arasında geçen veri paketlerindeki kaynak ve/veya hedef adresleri çevirir.

---
# NAT Çeşitleri

- Temel NAT (Basic NAT):
  - Yalnızca IP adreslerini çevirir.
  - Uygulamada nadiren kullanılır.
- NAPT (Ağ Adresi ve Port Çevirisi):
  - IP adresi ve taşıma katmanı (transport-layer) port numaralarını çevirir.
  - En yaygın kullanılan NAT türüdür.
- İki Kez NAT (Twice NAT):
  - DNS sunucusu ile çalışır.
  - NAPT'ye ek olarak gelen iletişimi kabul etme yeteneği sağlar.

---
# Temel NAT Örneği

- Varsayalım ki:
  - NAT kutusu `128.210.24.6` küresel geçerli IP adresine sahiptir.
  - Sahadaki bir bilgisayarın özel adresi `192.168.0.1`'dir.
  - Bilgisayar, `198.133.219.25` İnternet sitesiyle iletişim kurar.
- Sonuçlanan çeviri (translation):
  - Özel Adres Sahasından Çıkış: SRC=`192.168.0.1`, DST=`198.133.219.25`
  - İnternete Doğru (NAT Tarafından): SRC=`128.210.24.6`, DST=`198.133.219.25`
  - İnternetten Dönüş: SRC=`198.133.219.25`, DST=`128.210.24.6`
  - Özel Adres Sahasına (NAT Tarafından): SRC=`198.133.219.25`, DST=`192.168.0.1`

---
# NAT'ın Uygulanması (Implementation)

- NAT cihazı dahili bir çeviri tablosu (translation table) tutar.
- Tablo, hem giden hem de gelen veri paketleri için çevirileri depolar.
- Sahadaki bilgisayar ilk kez İnternet'e veri paketi gönderdiğinde değerler otomatik olarak doldurulur.
- Önceki örnek için çeviri tablosu:

| Yön | Alan | Eski Değer | Yeni Değer |
| :--- | :--- | :--- | :--- |
| dışarı | IP Kaynak | 192.168.0.1 | 128.210.24.6 |
| dışarı | IP Hedef | 198.133.219.25 | -- değişiklik yok -- |
| içeri | IP Kaynak | 198.133.219.25 | -- değişiklik yok -- |
| içeri | IP Hedef | 128.210.24.6 | 192.168.0.1 |

---
# Taşıma Katmanı NAT (NAPT)

- TCP, UDP ve ICMP'yi yönetir.
- IP adreslerinin yanı sıra TCP/UDP protokol port numaralarını da çevirir.
- Bir sahadaki birden fazla bilgisayarın aynı İnternet hizmetiyle parazit olmadan (interference) aynı anda iletişim kurmasına izin verir.
- Örnekler:
  - Bir sahadaki iki bilgisayar aynı anda iTunes'tan şarkı indirir.
  - Bir sahadaki üç bilgisayar aynı anda Google ile iletişim kurar.

---
# NAPT Çevirisi Örneği

- Varsayalım ki:
  - Sahadaki bilgisayarlar, `192.168/16` özel adres bloğundan atanmış özel adreslere sahiptir.
  - Sahadaki iki bilgisayarın her biri, `128.210.19.20` bilgisayarındaki TCP port `30000` ile iletişim kurar.
- NAPT her biri için yeni bir port numarası seçer ve çevirir:

| Yön | Alanlar | Eski Değer | Yeni Değer |
| :--- | :--- | :--- | :--- |
| dışarı | IP SRC:TCP SRC | 192.168.0.1:30000 | 128.10.24.6:40001 |
| dışarı | IP SRC:TCP SRC | 192.168.0.2:30000 | 128.10.24.6:40002 |
| içeri | IP DEST:TCP DEST | 128.10.24.6:40001 | 192.168.0.1:30000 |
| içeri | IP DEST:TCP DEST | 128.10.24.6:40002 | 192.168.0.2:30000 |

---
# Uygulamada NAT

- Birçok tüketici ürününde NAT yerleşiktir.
- Örnekler:
  - Kablo ve DSL modemler
  - Kablosuz yönlendiriciler (wireless routers)
- Çoğu kablosuz yönlendiricinin hem kablolu hem de kablosuz ağ bağlantıları sağladığını unutmayın; tüm bağlantılarda NAT sağlarlar.

> 📷 *[Görsel: Kablosuz Yönlendirici, Modem ve İnternet Bağlantısı Düzeni — yakında eklenecek]*

---
<!-- _class: lead -->
# Taşıma Katmanı Protokolleri: Özellikler ve Teknikler

---
# Bir Ağ Ne Sağlamalıdır?

- Bir olasılık: ağ merkezli (network centric)
  - Ağ; e-posta, web vb. gibi tüm hizmetleri sunar.
  - Ana bilgisayar hizmetlere erişir.
  - Ağ; kullanıcının kimliğini doğrular, güvenilirliği (reliability) yönetir.
  - Müşteri-sağlayıcı iletişimi (customer-provider communication) olarak bilinir.
- Diğer olasılık: ağ sadece iletişimi (communication) sağlar
  - Ağ yalnızca paketleri aktarır.
  - Uygulamalar, güvenilirlik, akış kontrolü (flow control) ve kimlik doğrulama dâhil olmak üzere geri kalan her şeyi halleder.
  - Uçtan uca iletişim (end-to-end communication) olarak bilinir.

---
# Uçtan Uca (End-To-End) İlkesi

- İnternet'teki temel kavram.
- Ağ, "en iyi çaba" (best-effort) ile paket aktarımı sağlar.
- Uç noktalar (Endpoints):
  - İletişimi kontrol eder.
  - Tüm güvenilirliği (reliability) sağlar.
- Sonuç:
  İnternet protokol paketindeki en karmaşık protokollerin bazıları yönlendiricilerden (routers) ziyade ana bilgisayarlarda çalışır.

---
# Taşıma Katmanı (Transport Layer)

- Uygulamalar (Application) ve IP (İnternet katmanı) arasındaki katmandır.

> 📷 *[Görsel: Uygulama (Katman 5), Taşıma (Katman 4), İnternet (Katman 3), Ağ Arayüzü ve Fiziksel Katman Modeli — yakında eklenecek]*

- Belirli bir ana bilgisayardaki birden fazla uygulamanın diğer ana bilgisayarlardaki uygulamalarla iletişim kurmasını sağlar.
- Mesajları taşımak için IP kullanır.

---
# Bir Taşıma Protokolünün Yönetebileceği Sorunlar

- Gönderen ve alıcı arasındaki hız uyumsuzluğunu giderme (speed mismatch).
- Veri paketi kaybını tespit etme ve kurtarma.
- Kopya paketleri ortadan kaldırma (duplicate packets).
- Mesajların sırayla ulaşmasını garanti etme.
- İnternet'teki tıkanıklığa (congestion) yanıt verme.
- Geciken paketlerin yanlış yorumlanmasını (misinterpreted) önleme.
- Verilerin aktarım sırasında bozulmadığını doğrulama (corrupted).
- Her iki tarafın da iletişim kurmayı kabul ettiğinden emin olma.
- Not: Belirli bir taşıma protokolü tüm sorunları yönetmeyebilir.

---
# Taşıma Protokollerinin Kullandığı Teknikler (devamı)

- Yeniden iletim ile olumlu onay (Positive acknowledgement with retransmission):
  - Alıcı, bir paket ulaştığında göndereni bilgilendirmek için bir onay (acknowledgement) gönderir.
  - Gönderen, onay belirtilen bir süre içinde ulaşmazsa paketi yeniden iletir (retransmits).
- Kayan pencere (Sliding window):
  - Bir paket iletip bir onay beklemek yerine, gönderen K paket iletir ve her onay geldiğinde başka bir paket iletir.

---
# İnternet'te Kullanılan Taşıma Protokolleri

- İnternet'te kullanılan iki birincil taşıma (transport) protokolü:
  - Kullanıcı Veri Birimi Protokolü (User Datagram Protocol - UDP)
  - İletim Kontrol Protokolü (Transmission Control Protocol - TCP)
- Seçim, uygulama protokolü tarafından belirlenir:
  - Birçok uygulama tek bir taşıma protokolünün kullanımını belirtir (örneğin, e-posta aktarımı TCP kullanır).
  - Bazı uygulamalar her ikisinin de kullanılmasına izin verir (örneğin, DNS sorguları UDP veya TCP yoluyla gönderilebilir).
- Hatırlatma: Her taşıma protokolünün bazı şaşırtıcı özellikleri (characteristics) vardır.

---
<!-- _class: lead -->
# Kullanıcı Veri Birimi Protokolü (UDP) İle Mesaj Taşıma

---
# Kullanıcı Veri Birimi Protokolü (UDP)

- Kullanıldığı yerler:
  - Başlatma (startup) sırasında
  - VoIP ve bazı video uygulamaları için
- İnternet trafiğinin %10'undan azını oluşturur.
- Bazı İnternet Servis Sağlayıcıları (ISP) tarafından engellenir.

---
# UDP Özellikleri

- Uçtan uca (End-to-end)
- Bağlantısız iletişim (Connectionless communication)
- Mesaj odaklı arayüz (Message-oriented interface)
- "En iyi çaba" anlambilimi (Best-effort semantics)
- Rastgele etkileşim (Arbitrary interaction)
- İşletim sistemi bağımsızlığı (Operating system independence)
- Tıkanıklık veya akış kontrolü yok (No congestion or flow control)

---
# Uçtan Uca İletişim

- UDP, uygulamalar arasında iletişim sağlar.
- Gönderen (Sending) UDP:
  - Uygulamadan giden mesajı kabul eder.
  - Mesajı bir Kullanıcı Veri Paketine (User Datagram) yerleştirir.
  - Kullanıcı Veri Paketini bir IP veri paketinde kapsüller (encapsulates) ve gönderir.
- Alan (Receiving) UDP:
  - IP'den gelen Kullanıcı Veri Paketini kabul eder.
  - Mesajı çıkarır (extracts) ve alıcı uygulamaya teslim eder.
- Not: Mesaj ağ tarafından değiştirilmez.

---
# Bağlantısız İletişim (Connectionless Communication)

- UDP kullanan bir uygulama şunları yapabilir:
  - Herhangi bir alıcıya mesaj gönderme (evrensel - universal)
  - İstediği zaman gönderme (asenkron - asynchronous)
  - İstediği zaman göndermeyi durdurma (sonlandırılmamış - unterminated)
- Yani, gönderen şunları yapmaz:
  - Göndermeden önce ağı bilgilendirmez (yani bir iletişim kanalı kurmaz).
  - Göndermeden önce diğer uç noktayı bilgilendirmez.
  - Ağ veya diğer uç noktaya başka mesaj gönderilmeyeceğini bildirmez.

---
# Mesaj Odaklı Arayüz

- UDP:
  - Mesajları (veri bloklarını) kabul eder ve teslim eder.
  - Tüm mesajların aynı boyutta olmasını gerektirmez, ancak maksimum bir mesaj boyutu tanımlar.
  - İletim için giden her Kullanıcı Veri Paketini (User Datagram) tek bir IP veri paketine yerleştirir.

---
# UDP Mesaj Boyutu

- UDP, 64K sekizliye (octets) kadar mesajlara izin verir.
- Pratik bir sınır olarak, bir Kullanıcı Veri Paketinin boyutu, IP veri paketindeki yük alanı ile sınırlıdır.
- Maksimum IP yükü 64K sekizli eksi IP başlığının boyutudur.
- Bu nedenle, maksimum UDP yükü 64K sekizli eksi IP ve UDP başlıklarının boyutudur (genellikle 64K sekizli eksi 28).
- Uygulama, maksimum UDP yüküne kadar herhangi bir mesaj boyutunu seçebilir.

---
# Büyük ve Küçük Mesajlar

- Bir uygulama 10K sekizli bir mesaj gönderirse ne olur?
  - Mesaj bir IP veri paketine sığar, ancak ağ çerçeveleri (network frames) daha küçük bir MTU'ya sahiptir (genellikle 1500 sekizli).
  - Bu nedenle büyük bir mesaj göndermenin sonucu: **IP Parçalanması! (IP Fragmentation!)**
- Bir uygulama 20 sekizli gibi küçük bir mesaj boyutu seçerse ne olur?
  - **Verimsizlik! (Inefficiency!)**

---
# Optimal (En Uygun) Bir Mesaj Boyutu Seçmek

- Bir uygulama hangi boyutta mesaj göndermelidir?
- Optimal UDP mesaj boyutu S = M – H'dir.
  - M, yol MTU'sudur (yani yoldaki minimum MTU).
  - H, IP ve UDP başlıklarının boyutudur.
- M'yi bulmak, bir uygulamanın şunları yapmasını gerektirir:
  - Katmanlaşmayı (layering) ihlal edip IP'den yönlendirme bilgisi elde etmek.
  - Not: IPv4 için yalnızca yerel MTU bilinir.
- Özet: Bir uygulamanın S'yi hesaplaması zor/imkânsız olabilir.

---
# UDP Anlambilimi (Semantics)

- UDP teslimat için IP'yi kullanır ve aynı anlambilimini sunar!
- UDP paketi:
  - Kaybolabilir (Lost)
  - Çoğaltılabilir (Duplicated)
  - Gecikebilir (Delayed)
  - Sıra dışı teslim edilebilir (Delivered out of order)
  - Veri bitleri değiştirilmiş (altered) olarak teslim edilebilir.
- Not 1: UDP bu tür hataları ortaya çıkarmaz; hatalar alttaki ağlardan kaynaklanır.
- Not 2: UDP, verileri korumak için isteğe bağlı bir sağlama toplamı (checksum) içerir (ancak sağlama toplamı devre dışı bırakılabilir).

---
# "En İyi Çaba" (Best-Effort) Anlambilimini Kullanmak

- Sorular:
  - "En iyi çaba" anlambilimi uygulamalar için mantıklı mı?
  - Bir programcı neden UDP'yi seçsin?
- Cevaplar:
  - Gerçek zamanlı ses ve görüntü uygulamaları için kayıp bir mesajı yeniden iletmek mantıklı değildir; çünkü yeniden iletilen paket kullanılmak için çok geç ulaşır.
  - Sıra dışı (out-of-order) teslimatı halletmek için UDP'ye ilave gerçek zamanlı protokoller eklenebilir.

---
# Rastgele Etkileşim (Arbitrary Interaction)

- UDP, uygulamalar arasında rastgele etkileşime izin verir:
  - 1'den 1'e
  - 1'den çoğa
  - Çoktan 1'e
  - Çoktan çoğa
- Uygulama programcısı etkileşim türünü seçer.
- Tek bir mesajı birden fazla alıcıya gönderme yeteneği değerli olabilir.

---
# Etkileşimin Verimli Uygulanması

- Kilit nokta: UDP, mesajları teslim etmek için IP yayınını (broadcast) veya çoklu yayınını (multicast) kullanabilir.
- Bir grup ana bilgisayara verimli teslimat sağlar.
- Örnek: `255.255.255.255` IPv4 hedef adresine gönderilen UDP paketi yerel ağdaki tüm ana bilgisayarlara teslim edilir (IPv6'nın tüm düğümlere çoklu yayın adresi vardır).
- Göndericinin bireysel kopyalar (individual copies) iletmesine gerek yoktur.
- Uygulamanın, sunucunun üzerinde çalıştığı bilgisayarı bilmeden bir sunucu bulmasını sağlar.
- Yayın (Broadcast), bazı uygulamalar için UDP'nin TCP'ye göre önemli bir avantajıdır.

---
# İşletim Sistemi Bağımsızlığı

- Amaç, heterojen bilgisayarlardaki uygulamaların etkileşime girmesini sağlamaktır.
- İşletim sistemine özgü tanımlayıcılardan (identifiers) kaçınılmalıdır, örneğin:
  - İşlem Kimlikleri (Process IDs)
  - Görev adları (Task names)
- Bunun yerine, herhangi bir işletim sisteminden türetilmeyen uygulama tanımlayıcıları oluşturun.

---
# UDP Uygulama Tanımlayıcıları

- 16 bitlik tamsayı, UDP protokol port numarası (protocol port number) olarak bilinir.
- UDP kullanan her uygulama bir port numarası almalıdır.
- Gönderen (Sending) UDP:
  - Alıcı ana bilgisayardaki hedef uygulamayı belirlemek için UDP başlığına bir port numarası yerleştirir.
  - Ayrıca gönderen uygulamanın port numarasını da içerir.
- Alan (Receiving) UDP:
  - Uygun uygulamayı seçmek için başlıktaki değeri kullanır.
- UDP protokol port numaraları tüm bilgisayarlarda evrenseldir ve işletim sistemine bağlı değildir.

---
# Bir Uygulamayı Tanımlama

- Hem gönderen hem de alan uygulamaların bir port numarasına ihtiyacı vardır.
- Port numaralarının ataması (assignment) uygulama türüne bağlıdır.
- Standartlaştırılmış hizmet sunan uygulama (Sunucu - Server):
  - Hizmet için iyi bilinen (well-known) bir port numarası kullanır.
  - Değeri 1024'ten küçüktür.
  - Örnek: TFTP hizmeti UDP port 69 kullanır.
- Diğer uygulamalar (İstemci - Client):
  - Yerel işletim sisteminden bir port numarası talep eder.
  - Değeri 49151'den büyüktür.

---
# Bir Hizmetle (Service) İletişim Kurmak İçin Atılan Adımlar

- Yerel işletim sisteminden kullanılmayan bir yerel port numarası iste.
- İşletim sisteminden yerel bilgisayarın IP adresini al.
- İletişim kurulacak hizmetin port numarasını ara (look up).
- Hizmeti çalıştıran bir bilgisayarın alan adını (domain name) al ve bir IP adresiyle eşle.
- Kaynak port alanı yerel port numarasına ve hedef port alanı hizmetin port numarasına ayarlanmış bir UDP veri paketi (datagram) oluştur.
- UDP veri paketinin bir IP veri paketinde kapsüllenmesini (encapsulated) ve yukarıda elde edilen IP adresleri kullanılarak gönderilmesini iste.

---
# İyi Bilinen UDP Portlarına (Well-Known UDP Ports) Örnekler

| Port Numarası | Açıklama |
| :--- | :--- |
| 0 | Ayrılmış (Reserved - asla atanmaz) |
| 7 | Yankı (Echo) |
| 9 | İptal (Discard) |
| 11 | Aktif Kullanıcılar (Active Users) |
| 13 | Gündüz (Daytime) |
| 15 | Ağ Durum Programı |
| 17 | Günün Sözü (Quote of the Day) |
| 19 | Karakter Üreticisi (Character Generator) |
| 37 | Zaman (Time) |
| 42 | Ana Bilgisayar Adı Sunucusu |
| 43 | Kimdir (Who Is) |
| 53 | Alan Adı Sistemi (DNS) |
| 67, 68 | BOOTP veya DHCP (Sunucu ve İstemci) |
| 69 | Basit Dosya Aktarımı (TFTP) |
| 161, 162 | Basit Ağ Yönetim Protokolü (SNMP) ve Tuzakları (Traps) |

---
# UDP Veri Paketi (Datagram) Formatı

- Son derece ince bir katmandır.
- Kullanıcı Veri Paketi (User Datagram), başlık ve yük (payload) olmak üzere ikiye ayrılır.
- Başlık sadece 8 sekizli (octets) içerir:
  - UDP KAYNAK PORTU (UDP SOURCE PORT)
  - UDP HEDEF PORTU (UDP DESTINATION PORT)
  - UDP MESAJ UZUNLUĞU (UDP MESSAGE LENGTH)
  - UDP SAĞLAMA TOPLAMI (UDP CHECKSUM)
- Soru: Neden uzunluğa ihtiyaç duyulur?

---
# UDP Sağlama Toplamı (Checksum)

- 16 bitlik 1'e tümleyen (1s-complement) sağlama toplamıdır.
- Veriler dahil tüm UDP paketini kapsar (Hatırlatma: IP, yük için sağlama toplamı yapmaz).
- İsteğe bağlıdır: Sıfır değeri, göndericinin bir sağlama toplamı hesaplamadığı anlamına gelir.
- IP adreslerini içeren ilave bir sözde başlık (pseudo header) içerir.
- IPv4 sözde başlık örneği:
  `IP KAYNAK ADRESİ`, `IP HEDEF ADRESİ`, `SIFIR`, `PROTOKOL`, `UDP UZUNLUĞU`

---
# Sözde Başlığın (Pseudo Header) Amacı

- Alıcı, mesajın doğru bilgisayara ve o bilgisayardaki doğru uygulamaya ulaştığını doğrulayabilir.
- NAT için sonuç: NAT, IP kaynak veya hedef adresini değiştirirse UDP sağlama toplamını (checksum) yeniden hesaplamalıdır.
- Not: Sözde başlıklar katmanlaşma ihlallerinin (layering violations) başka bir örneğidir.

---
# UDP Kapsülleme (Encapsulation)

- Kullanıcı Veri Paketi (User Datagram) bir IP veri paketinde seyahat eder.
- İki seviyeli kapsülleme (encapsulation) oluşur:
  `Çerçeve Başlığı -> IP Başlığı -> UDP Başlığı -> UDP Yükü`
- Not: Uygulamanın UDP Yük alanına (Payload field) yerleştirdiği mesajın, kendi başlık ve yük alanları da olabilir.

---
<!-- _class: lead -->
# İletim Kontrol Protokolü (Transmission Control Protocol - TCP) (Akış Taşıma - Stream Transport)

---
# İletim Kontrol Protokolü (TCP)

- İnternet'te kullanılan birincil taşıma katmanı protokolüdür.
- Tüm İnternet trafiğinin yaklaşık %90'ını oluşturur (bazı tahminler daha yüksektir).
- Güvenilirlik (reliability) sağlar.
- Programcılara cazip gelir.

---
# TCP Özellikleri

- Uçtan uca (End-to-end) iletişim
- Bağlantı yönelimli paradigma (Connection-oriented paradigm)
- Noktadan noktaya (Point-to-point) bağlantılar
- Tam güvenilirlik (Complete reliability)
- Tam çift yönlü (Full-duplex) iletişim
- Akış arayüzü (Stream interface)
- Güvenilir bağlantı başlatma (Reliable connection startup)
- Zarif bağlantı kapatma (Graceful connection shutdown)

---
# Uçtan Uca İletişim

- TCP, uygulama çiftleri (pairs of applications) arasında iletişim sağlar.
- Bir ana bilgisayardaki uygulamanın başka bir ana bilgisayardaki uygulamayla iletişim kurmasını sağlar.
- Belirli bir bilgisayardaki birden fazla uygulamanın müdahale (interference) olmadan aynı anda iletişim kurmasını sağlar.
- Uygulamaları ayırt etmek için protokol port numaralarını kullanır.
- Not: TCP portları UDP portlarından tamamen bağımsızdır.

---
# Uçtan Uca İlkesi ve Taşıma Protokolleri

- Taşıma (transport) protokolleri uç sistemlerde (end systems) çalışır ve temeldeki İnternet'i sanal bir ağ olarak görür.

> 📷 *[Görsel: İki Ana Bilgisayar Arasında Taşıma Katmanı Bağlantısının Mantıksal ve Yönlendiriciler Üzerinden Fiziksel Yolu — yakında eklenecek]*

- IP, TCP paketlerini okumaz veya yorumlamaz.
- Veri paketlerini yönlendirirken, yönlendirici yalnızca 1'den 3'e kadar olan katmanları (layer 1-3) işler.

---
# TCP Protokol Port Numaraları

- Uygulamaları tanımlamak için 16 bitlik tamsayılar kullanılır.
- Her uygulamanın bir port numarasına ihtiyacı vardır.
- TCP'nin iyi bilinen (well-known) port atamaları UDP atamalarından bağımsızdır.
- Ancak, insanlara yardımcı olmak için, hizmet her iki taşıma yoluyla da (transport) mevcutsa aynı değer seçilir.
- Örnekler:
  - Hem UDP hem de TCP, Alan Adı Sistemi (DNS) için port 53'ü atar.
  - Hem UDP hem de TCP, Yankı (Echo) hizmeti için port 7'yi atar.

---
# Protokol Portları, Dörtlü Tanım (Four-Tuple) ve Akışlar

- Kilit kavram: Bir TCP bağlantısı bir çift uç noktaya (endpoints) karşılık geldiğinden, bağlantı şu dört öğe tarafından tanımlanır:
  - IP kaynak adresi
  - TCP kaynak portu
  - IP hedef adresi
  - TCP hedef portu
- Yaygın olarak "dörtlü" (four-tuple) olarak adlandırılır.
- Web sunucusu gibi bir uygulamanın neden aynı anda birden çok istemciyle (client) iletişim kurabildiğini açıklar.
- İlginç bir şekilde, bir TCP akışını tanımlamak için bir çerçeveden (frame) dörtten fazla değerin çıkarılması gerekir.

---
# TCP'nin Bağlantı Yönelimli (Connection-Oriented) Paradigması

- Telefon görüşmesine (telephone call) benzer.
- Uygulama çifti (Pair of applications) şunları yapmalıdır:
  - İletişimden önce bir TCP bağlantısı kurmak (Establish).
  - İşlem bittiğinde bağlantıyı sonlandırmak (Terminate).
- Önemli içgörüler:
  - Yalnızca iki uç nokta (endpoint) bir bağlantı olduğunu bildiği için bir TCP bağlantısı sanaldır.
  - TCP'nin "canlı tutma" (keep-alive) mesajları yoktur: Uygulamalar veri göndermediği sürece hiçbir paket değiş tokuş edilmez.

---
# Sınırlı Etkileşim (Limited Interaction)

- Bir TCP bağlantısı yalnızca bir uygulama çifti arasında iletişim sağlar.
- Buna noktadan noktaya (point-to-point) iletişim denir.
- TCP bağlantısı şunları desteklemez:
  - Rastgele (arbitrary) bir gönderici kümesinden alım
  - İkiden fazla uç noktaya sahip çok noktalı (multi-point) bağlantılar
  - Yayın (Broadcast) veya çoklu yayın (multicast) teslimi

---
# TCP Güvenilirlik Garantisi

- TCP tam güvenilirlik sağlar.
- Şunları telafi eder:
  - Kayıp (Loss)
  - Çoğaltılma (Duplication)
  - Sıra dışı (out of order) teslimat
- Bunları altta yatan ağlara ve yönlendiricilere (routers) aşırı yüklenmeden yapar.
- TCP aşağıdaki garantiyi verir:
  **"Veriler teslim edilecek veya gönderen (eninde sonunda) bilgilendirilecektir."**

---
# TCP Güvenilirliği

- Zaman aşımı ve yeniden iletimi (timeout-and-retransmission) kullanır.
- Alıcı, veriler geldiğinde gönderene bir onay (ACK - acknowledgement) döndürür.
- Gönderen onayı bekler ve hiçbir onay gelmezse verileri yeniden iletir (retransmits).

---
# TCP Yeniden İletiminin (Retransmission) Gösterimi

> 📷 *[Görsel: Host 1 ve Host 2 Arasında TCP İletişimi, Onaylama ve Yeniden İletim Diyagramı — yakında eklenecek]*

- Bir paket kaybolduğunda ve yeniden iletim zamanlayıcısının süresi dolduğunda, mesaj (Message 3) yeniden iletilir (retransmit) ve ardından onaylanır (ACK 3).

---
# TCP Yeniden İletimi (Retransmission) Neden Zordur?

- İnternet için tasarlanmış olan TCP:
  - Gidiş-dönüş gecikmeleri (Round-trip delays) bağlantılar arasında farklılık gösterir.
  - Gidiş-dönüş gecikmeleri zaman içinde değişir.
- Çok uzun süre beklemek, gereksiz gecikmeye neden olur.
- Yeterince uzun süre beklememek, gereksiz kopyalar gönderir.
- TCP'nin başarısının anahtarı: **Uyarlanabilir yeniden iletim (adaptive retransmission)**.

---
# İnternet Ne Kadar Kötü?

- Eski günlerde: Gecikmeler saniye seviyesinde ve yüksek değişkenliğe sahipti.
- Günümüzde: Gecikmeler saniye seviyesinde ve yüksek değişkenliğe sahiptir.
- Örnek: İrlanda'dan Kaliforniya'ya gidiş-dönüş ölçümleri (2009).

---
# Uyarlanabilir Yeniden İletim (Adaptive Retransmission)

- Her bir bağlantının gidiş-dönüş süresini sürekli olarak tahmin edin (estimate).
- Gidiş-dönüş tahminine göre yeniden iletim zamanlayıcısını (timer) ayarlayın.
- Bekleme süresi dinamik olarak değişir.

---
# Kayan Pencere (Sliding Window) Mekanizmasının İncelenmesi

- Taşıma (transport) protokolleri kayan pencere mekanizmasını kullanır.
- Fikir, bir onay (acknowledgement) beklemeden önce birden fazla paket göndermektir.
- Pencere boyutu nispeten küçüktür (milyonlarca değil, onlarca paket).
- Motivasyon, verimi (throughput) artırmaktır.

---
# TCP'nin Kayan Penceresinin Gösterimi

> 📷 *[Görsel: Kayan Pencerenin Gönderilmemiş, Zaten Onaylanmış Kısımları ve Onaylar Geldikçe İlerleyişi — yakında eklenecek]*

---
# Kayan Pencere Veri Hızını (Data Rate) Nasıl Geliştirir?

- K (örneğin 4) paketlik bir pencere boyutu, veri hızını K faktörü kadar (stop-and-go modeline göre) artırır.

> 📷 *[Görsel: Kayan Pencere Mekanizması ile Stop-and-Go Karşılaştırması — yakında eklenecek]*

---
# TCP Akış Kontrolü (Flow Control) ve TCP Penceresi

- Akış kontrol mekanizması (Flow control mechanism), gönderilen verileri alıcının hızıyla (receiver's speed) koordine eder.
- Veri hızı (data rate) yerine arabellek (buffer) boyutu kullanılır.
- Alıcı, gönderene başlangıç arabellek boyutunu söyler.
- Her bir onay (acknowledgement), arabellekte kalan alanı belirtir.
- Pencere ilanı (window advertisement) olarak bilinir.

---
# TCP Akış Kontrolünün Gösterimi

> 📷 *[Görsel: Gönderici ve Alıcı Arasında TCP Akış Kontrolü ve Pencere Güncellemeleri — yakında eklenecek]*

- "Window" (Pencere) değişkeni, alıcının mevcut arabellek kapasitesine göre güncellenir ve onaylanır.

---
# TCP Tıkanıklık Kontrolü (Congestion Control) ve Yavaş Başlama (Slow Start)

- TCP, ağdaki tıkanıklığı (congestion) anlamak için kayıp veya gecikmedeki değişiklikleri kullanır.
- Tıkanıklık algılandığında, gönderen TCP pencere (window) boyutunu geçici olarak azaltır.
- Bir paket kaybolduğunda, TCP efektif (effective) pencereyi geçici olarak mevcut değerinin yarısına (1/2) indirir.
- Daha sonra TCP yavaşça pencereyi tekrar artırır.
- Bir bağlantı başladığında da tıkanıklık önleme (congestion avoidance) kullanılır:
  - Geçici olarak bir parçalık (segment) pencere boyutu kullan.
  - ACK geldiğinde pencere boyutunu ikiye katla.
  - Buna yavaş başlama (slow start) denir.

---
# Tam Çift Yönlü İletişim (Full-Duplex Communication) (devamı)

- Her TCP paketi hem ileri (forward) hem de geri (reverse) veri akışları (streams) için alanlar içerir:
  - İleri yönde gönderilen veriler için sıra numarası (Sequence number).
  - Alınan veriler için onay numarası (Acknowledgement number).

---
# Akış Arayüzü (Stream Interface)

- Bağlantı kurulduktan sonra, TCP gönderici uygulamadan (sending application) bir veri baytları akışını (stream) kabul eder ve bunları aktarır.
- Gönderici uygulama, her bir istekte (request) geçirilecek veri miktarını seçebilir.
- Sürpriz: TCP baytları paketler halinde nasıl gruplayacağına karar verir.
- Bu akış arayüzü (stream interface) olarak bilinir.
- Sonuç: Veriler alıcı (receiving) uygulamaya, gönderici uygulamanın ürettiği parçalardan farklı (differ) parçalar (chunks) halinde aktarılabilir.

---
# Bağlantı Başlatma ve Kapatma (Startup And Shutdown)

- Zorlu bir problem.
- Paketler şu durumlara düşebilir:
  - Kayıp
  - Çoğaltılmış
  - Gecikmiş
  - Sıra dışı teslim edilmiş
- Her iki uç da çökebilir ve yeniden başlatılabilir (crash and reboot).
- Her iki tarafın da bağlantıyı başlatmayı/sonlandırmayı kabul ettiğinden emin olmak gerekir.

---
# Güvenilir Bağlantı Başlatma

- TCP, tekrarlama problemlerini (replay problems) önleyen güvenilir bir bağlantı başlatmayı garanti eder.
- 3 yönlü el sıkışma (3-way handshake) ile gerçekleştirilir:
  - Host 1 (SYN Gönderir) -> Host 2
  - Host 2 (SYN + ACK Gönderir) -> Host 1
  - Host 1 (ACK Gönderir) -> Host 2
- Her bir taraf rastgele olarak bir başlangıç sıra numarası (sequence number) seçer.

---
# Zarif Bağlantı Kapatma (Graceful Connection Shutdown)

- Başlangıçtaki 3 yönlü el sıkışmaya benzer.
- Bağlantı sonlandırmasıyla ilgili hiçbir belirsizlik olmayacağını garanti eder.
  - Host 1 (FIN + ACK Gönderir) -> Host 2
  - Host 2 (FIN + ACK Gönderir) -> Host 1
  - Host 1 (ACK Gönderir) -> Host 2

---
# TCP Parça (Segment) Formatı

- TCP paketine segment (parça) denir.
- Segment, aktarım için IP içinde kapsüllenir (encapsulated).
- SYN, FIN, ACK ve veri (data) için tek bir format kullanılır.

> 📷 *[Görsel: Kaynak, Hedef Portları ve Sıra Numaraları vb. İçeren TCP Segment Formatı — yakında eklenecek]*

---
<!-- _class: lead -->
# Yönlendirme Algoritmaları (Routing Algorithms) ve Yönlendirme Protokolleri (Routing Protocols)

---
# Tarihsel Perspektif

- 1960'larda Bilgi İşlem:
  - Ana bilgisayarlar (Mainframes)
  - Delikli kartlarla toplu (batch) işleme
  - Genellikle kuruluş başına bir bilgisayar
- 1970'lerde Bilgi İşlem:
  - Mini bilgisayarlar
  - Kuruluş başına birkaç bilgisayar
  - Akılsız (Dumb) terminaller

---
# Geleneksel Geniş Alan Ağları (WAN'lar)

- 1960'ların ana bilgisayar çağında geliştirildi.
- Yerel Alan Ağları (LAN'lar) ve Kişisel Bilgisayarlardan (PC'ler) önce gelir.
- Temel motivasyon:
  - Bir sahadaki ana bilgisayarı diğer sahalardaki ana bilgisayarlara bağlamak.
  - Kaynak paylaşımına (resource sharing) izin vermek.
- Dinamik yönlendirmeyi (dynamic routing) kullanan ilk sistemlerdir.

---
# Geleneksel WAN Mimarisi

- Her sahaya "paket anahtarı" (packet switch) olarak bilinen özel bir cihaz yerleştirilir.
- Paket anahtarı şunları sağlar:
  - Sahadaki ana bilgisayar(lar) için yerel bağlantılar.
  - Diğer sahalara uzun mesafeli bağlantılar.
- Sahalar arası bağlantı:
  - Kiralık dijital devreler (Leased digital circuits).
  - Müşteri tarafından sağlanan modemlerle kiralık ham bakır veya fiber.

---
# Geleneksel WAN'da Kullanılan Paket Anahtarı

- Özel amaçlı (Special-purpose), bağımsız bir cihazdır.
- Paket yönlendirmeye (packet forwarding) adanmıştır.
- Şunlara sahip küçük bir bilgisayardır:
  - İşlemci (Processor)
  - Bellek (Memory)
  - Kalıcı depolamada program
  - G/Ç (I/O) arayüzleri

---
# Geleneksel Paket Anahtarının Kavramsal Görünümü

> 📷 *[Görsel: Yerel bilgisayarlar için G/Ç arayüzleri, uzak sahalar için G/Ç arayüzleri, bellek ve işlemci içeren paket anahtarı yapısı — yakında eklenecek]*

- Bellek, paketleri depolamak için gereklidir.

---
# Depola ve İlet (Store And Forward) Paradigması

- Paket anahtarlamada (packet switching) kullanılan temel paradigmadır.
- İşlem:
  - Arayüz donanımı, gelen her paketi bellekteki bir sıraya (queue) yerleştirir.
  - İşlemci, sıradaki bir sonraki paketi sürekli olarak alır ve hedefine doğru yönlendirir.
- Motivasyon: Bellek, arka arkaya (back-to-back) gelen kısa paket patlamalarını (burst of packets) barındıran bir arabellektir.
- Önemli nokta: Paket trafiği patlamalı (bursty) olma eğilimindedir.

---
# Geleneksel WAN Mimarisi Örneği

- Her sahadaki paket anahtarı (packet switch) diğer sahalara bağlanır.
- Devreler (circuits) trafiği ve istenen sağlamlığı barındırır.

> 📷 *[Görsel: Çeşitli sahalardaki paket anahtarlarının birbirine dijital devrelerle bağlı olduğu örnek WAN mimarisi — yakında eklenecek]*

---
# Geleneksel WAN Adresleme

- İnternet adreslemeye benzer hiyerarşik (hierarchical) modeldir.
- Kavramsal iki seviyeli hiyerarşi:
  `( saha, sahadaki bilgisayar )`
- Uygulamada, saha başına bir paket anahtarı ve yerel bilgisayarlar için K bağlantı olması, adres hiyerarşisinin şu olduğu anlamına gelir:
  `( paket anahtarı, anahtar üzerindeki yerel bağlantı )`

---
# Geleneksel WAN Adreslemesinin Gösterimi

> 📷 *[Görsel: Paket anahtarları (3 ve 4) ve bağlı bilgisayarlar arasındaki [saha, bilgisayar] formatlı hiyerarşik adresleme diyagramı — yakında eklenecek]*

- Bir adresin iki bölümü tek bir ikili sayı (binary number) oluşturmak üzere birleştirilir.

---
# Sonraki Durak Yönlendirmesi (Next-Hop Forwarding)

- IP veri paketi yönlendirmesine (forwarding) benzer.
- Her paket bir hedef adresi içerir.
- Yönlendirme, bir adresin yalnızca paket anahtarı (packet switch) bölümünü kullanır; teslimat (delivery) adresin geri kalanını kullanır.
- Eğer paket hedef paket anahtarına ulaşmışsa, yerel olarak bağlı olan bilgisayara teslim et.
- Aksi takdirde, hedef sahaya daha yakın olan başka bir paket anahtarına yönlendir.

---
# Paket Yönlendirme Algoritması

- **Verilen:** Bir paket anahtarına ulaşan gelen paket
- **Uygulanacak:** Sonraki durak (next-hop) yönlendirme adımı
- **Yöntem:**
  Hedef adresini paketten çıkar ve paket anahtarı (P) ile bilgisayara (C) böl;
  Eğer (P, "benim" paket anahtar numaramla aynıysa) {
    Paketi yerel bilgisayar C'ye teslim et;
  } değilse {
    Bir sonraki durağı (next hop) seçmek için P'yi kullan ve paketi seçilen bağlantı üzerinden bir sonraki durağa yönlendir;
  }

---
# WAN Yönlendirme Tablosu

- IP yönlendirme tablosuna benzer.
- Tablodaki her giriş (entry) bireysel bir bilgisayara değil, bir anahtara (switch) atıfta bulunur.

> 📷 *[Görsel: Üç paket anahtarlı bir örnek WAN ve Anahtar 2 için Yönlendirme Tablosu — yakında eklenecek]*

---
# Modern WAN Mimarisi

- IP teknolojisini kullanır.
- Sahadaki bir yönlendiricinin (router) şunları vardır:
  - Sahadaki ağlara yerel bağlantılar
  - Diğer sahalardaki yönlendiricilere uzun mesafeli bağlantılar
- Tipik kullanım: Bir kuruluşun tüm sahalarını birbirine bağlamak.

---
# Modern WAN Bağlantılarının Gösterimi

> 📷 *[Görsel: LAN (örneğin Ethernet) ile yerel bilgisayarların, diğer sahalara bağlanan bir yönlendirici (Router) üzerinden iletişimi — yakında eklenecek]*

- Geleneksel bir IP yönlendiricisi kullanır.
- Tipik uzak bağlantı kiralık bir veri devresidir (leased data circuit).
- Yönlendirici ayrıca İnternet'e bağlantı sağlayabilir.

---
<!-- _class: lead -->
# Yönlendirme Algoritmaları ve İnternet Yönlendirmesi (Internet Routing)

---
# Yönlendirme Tablosu Oluşturmak

- İki temel yaklaşım vardır:
- **Statik yönlendirme (Static routing)**
  - İnternet ana bilgisayarlarında (hosts) kullanılır.
  - Girişler (entries) sistem başlatıldığında (boot) eklenir ve değişmez.
- **Dinamik yönlendirme (Dynamic routing)**
  - Paket anahtarlarında ve IP yönlendiricilerinde kullanılır.
  - Başlangıç girişleri sistem başlatıldığında eklenir.
  - Yönlendirme yazılımı (routing software) ağı sürekli olarak izler, en kısa yolları hesaplar ve yönlendirme tablosunu günceller.

---
# Statik Yönlendirme

- Çoğu ana bilgisayarda kullanılır.
- Ana bilgisayarın K ağ bağlantısı varsa, yönlendirme tablosunda yalnızca K+1 giriş vardır.
- Her ağ bağlantısı için bir tane olmak üzere K giriş:
  - Ağ için IP öneki (prefix)
  - Ağ için adres maskesi (mask)
  - Ağ için arayüz (interface)
- Son giriş: Varsayılan rota (default route)
  - Varsayılan IP yönlendirici adresi
  - Varsayılan yönlendirici için arayüz

---
# Dinamik Yönlendirme

- Yönlendirme Yazılımı (Routing Software):
  - Her paket anahtarında veya yönlendiricide çalışır.
  - En kısa yolları (shortest paths) hesaplar ve yerel yönlendirme tablosuna girişler yükler.
- Ağı bir grafik (graph) olarak modeller:
  - Düğümler (Nodes)
  - Kenarlar (Edges) veya bağlantılar (links)

---
# Örnek Grafik ve Sonraki Durak (Next-Hop) Yönlendirme Tabloları

> 📷 *[Görsel: 4 düğümlü bir örnek ağ grafiği ve her bir düğüm için sonraki durak yönlendirme tabloları (düğüm 1, 2, 3, 4) — yakında eklenecek]*

---
# Dinamik Yönlendirme Hedefleri

- **Hedefler:**
  - Tutarlı, en uygun rotalar (Consistent, optimal routes).
  - Arızaları barındırmak için otomatik rota değişikliği (Automatic route change).
- Her düğüm (paket anahtarı veya yönlendirici) katılır.
- Bir düğümdeki yönlendirme yazılımı, diğer düğümlerdeki yönlendirme yazılımıyla bilgi alışverişinde bulunur.
- Dağıtılmış hesaplama (Distributed computation).
- Kullanılan iki temel algoritma:
  - Mesafe-Vektör (Distance-Vector - DV)
  - Bağlantı-Durumu Yönlendirmesi (Link-State Routing - LSR)

---
# Mesafe-Vektör (Distance-Vector - DV) Yönlendirmesi

- Erken dönem birçok yönlendirme protokolünde kullanılan yaklaşımdır.
- Bellman Ford olarak da bilinir.
- Düğüm (Node):
  - Komşulardan bilgi alır.
  - Tüm komşulardan gelen bilgileri yerel bilgilerle birleştirir.
  - İşlenmiş bilginin bir kopyasını tüm komşularına gönderir.

---
# DV Nasıl Çalışır?

- Bir katılımcı, periyodik olarak her komşusuna bir rota ilanı (route advertisement) gönderir.
- İlan, ulaşılabilir sahaları ve her birine olan mesafeyi belirtir.
  - "X sahasına ulaşabilirim ve onun bana olan mesafesi Y'dir."
  - "Z sahasına ulaşabilirim ve onun bana olan mesafesi W'dur."
- Komşu, ilanı alır ve yönlendirme tablosunu günceller.
- Bir sonraki turda, komşular kendi komşularına ilanlarını gönderirler.

---
# Mesafe-Vektör Algoritması

- İlan geldiğinde kullanılır.
- İlandaki her öğeyi inceleyin:
  - Eğer komşu X sahasına ulaşabiliyorsa ve ben ulaşamıyorsam, yönlendirme tabloma X için komşuyu bir sonraki durak olarak ekle.
  - Eğer zaten komşunun bir sonraki durak olduğu X'e giden bir rotam varsa, rotadaki mesafeyi ilan edilen mesafeyle değiştir.
  - Eğer X'e, komşu üzerinden gitmekten daha pahalı bir rotam varsa, bir sonraki durağı komşu olarak değiştir.

---
# Bir Rotanın Mesafesini Ölçmek

- Olası ölçüler (measures):
  - Duraklar (Hops)
  - Gecikme (Delay)
  - Verim (Throughput)
  - Ekonomik veya idari maliyet
- Birçok protokol "durakları" (hops) kullanır, ancak yönlendirme yazılımı genellikle bir yöneticinin (manager) idari durak sayıları (administrative hop counts) atamasına izin verir.

---
# Bağlantı-Durumu Yönlendirmesi (Link-State Routing - LSR)

- Mesafe-vektör'ün (DV) başlıca alternatifidir.
- Her düğüm:
  - Bağlantı durumu (link status) bilgilerini gönderir.
  - En kısa yolları bağımsız olarak hesaplar.
  - Başkaları tarafından gerçekleştirilen hesaplamaya güvenmez.
- İsim (Name):
  - Resmi adı Link-State veya Link-Status Routing'dir.
  - Temel algoritmadan türetilen ve biraz yanıltıcı bir terim olan Önce En Kısa Yol (Shortest Path First - SPF) olarak da adlandırılır.

---
# LSR Nasıl Çalışır?

- Doğrudan bağlı olan (directly-connected) her düğüm çifti periyodik olarak:
  - Aralarındaki bağlantıyı test eder.
  - Aşağıdaki mesajlardan birini yayınlar (broadcasts):
    - "X ve Y arasındaki bağlantı açık (up)." veya
    - "X ve Y arasındaki bağlantı kapalı (down)."
- Her düğüm:
  - Gelen yayın mesajlarını toplar ve bir grafik (graph) oluşturur.
  - Bir yönlendirme tablosu hesaplamak için Dijkstra'nın SPF algoritmasını kullanır.

---
# İnternet Yönlendirmesinin Gözden Geçirilmesi

- Ana bilgisayarlar (Hosts):
  - Statik yönlendirmeyi kullanır.
  - Girişler (Entries) sistem başlatıldığında (boot) yönlendirme tablosuna yerleştirilir ve değişmeden kalır.
- Yönlendiriciler (Routers):
  - Dinamik yönlendirmeyi kullanır.
  - Başlangıç girişleri sistem başlatıldığında yönlendirme tablosuna yerleştirilir ve yönlendirme yazılımı girişleri sürekli olarak günceller.

---
# Ana Bilgisayar Yönlendirmesine Örnek (Host Routing)

> 📷 *[Görsel: Bir ana bilgisayardaki yönlendirme tablosu ile R1 yönlendiricisi üzerinden ağa bağlantı şeması — yakında eklenecek]*

- Varsayılan rotadaki (default route) sonraki durağa varsayılan yönlendirici (default router) denir.

---
# Dinamik İnternet Yönlendirmesine Neden İhtiyaç Duyulur?

- Yönlendirici:
  - Yalnızca birkaç ağa doğrudan bağlantısı vardır.
  - Bir veri paketini herhangi bir hedefe nasıl yönlendireceğini bilmesi gerekir.

> 📷 *[Görsel: R1 ve R2 yönlendiricileri ve 3 farklı ağ üzerinden yönlendirme şeması — yakında eklenecek]*

- Örnekte: Yönlendirici R1 ağ 2 hakkında, R2 ise ağ 1 hakkında bilgi edinmelidir.

---
# Önemli Prensip

Hiçbir tek yönlendirme protokolü (single routing protocol) İnternet'in tamamında kullanılamaz; çünkü bunun getirdiği genel yük (overhead) çok yüksektir.

---
# Otonom Sistem (Autonomous System) Kavramı

- İnternet bir dizi yönlendirme etki alanına (routing domains) bölünmüştür.
- Her yönlendirme etki alanı:
  - Otonom sistem (Autonomous system - AS) olarak bilinir.
  - Benzersiz bir numara atanmıştır.
- Genel olarak, bir AS, tek bir idari otorite altındaki (under one administrative authority) yönlendiriciler ve ağların bitişik bir kümesidir.
- Kesin bir tanım yoktur; büyük bir ISP (İnternet Servis Sağlayıcı) veya büyük bir şirket olarak düşünebilirsiniz.
- AS, yönlendirme bilgilerini başka bir AS'ye geçirmeden önce toplar ve özetler.

---
# İki Tür İnternet Yönlendirme Protokolü

- İç Ağ Geçidi Protokolleri (Interior Gateway Protocols - IGPs):
  - Bir otonom sistem içinde kullanılır.
  - IGP seçimi her AS tarafından yapılır.
  - Kurulumu ve yönetimi nispeten kolaydır.
- Dış Ağ Geçidi Protokolleri (Exterior Gateway Protocols - EGPs):
  - Otonom sistemler arasında kullanılır.
  - Kurulumu ve yapılandırması daha karmaşıktır.
  - Hangi bilgilerin açığa çıkacağını kontrol eden politika kısıtlamalarını (policy constraints) içerir.

---
# IGP ve EGP'lerin Gösterimi

> 📷 *[Görsel: Otonom Sistem 1 ve 2 içerisinde IGP'lerin kullanıldığı, iki sistem arasında ise EGP kullanıldığı bir mimari diyagram — yakında eklenecek]*

- Her AS'de kullanılan metrikler farklılık gösterebileceği için doğrudan karşılaştırma imkânsızdır.

---
# Rota ve Veri Akışı Prensibi (Route And Data Flow)

- Veriler (Data), rotaların (routes) ters yönünde akar.
- Örnek: ISP1, Q müşterisine giden rotayı (route) ilan eder ve Q müşterisi için trafik (veri) alır.

> 📷 *[Görsel: Rota ilanlarının bir yöne, verinin (Data) ise ters yöne aktığı ISP1 ve ISP2 arası iletişim modeli — yakında eklenecek]*

---
<!-- _class: lead -->
# İnternet Yönlendirme Protokolleri

---
# Sınır Ağ Geçidi Protokolü (Border Gateway Protocol - BGP)

- İnternet'te kullanılan birincil Dış Ağ Geçidi Protokolüdür (EGP).
- İnternet'in merkezindeki Katman 1 (Tier 1) ISP'ler tarafından kullanılır.
- Mevcut sürüm 4'tür (BGP-4).
- Özellikleri:
  - Otonom sistemler (AS) arasında yönlendirme sağlar.
  - Politikalar (policies) için hükümler (provisions) içerir.
  - Geçiş rotalarını (transit routes), terminal (uç) rotalarından ayırır.
  - Güvenilir taşıma (TCP) kullanır.
  - Yol bilgilerini (path information) gönderir.

---
# BGP Yollarının (Paths) Gösterimi

- Değiştirilmiş Mesafe-Vektör (Modified Distance-Vector) protokolüdür.
- İlan (Advertisement), bir mesafe yerine bir yol (path) içerir.
- Yol (Path), hedefe giden otonom sistemleri listeler.
- Örnek:
  - "X ağına ulaşmak için, Z, Y, W... yolu boyunca gönderiyorum."
- Yol bilgisi, alıcının politikalar uygulayabileceği anlamına gelir (örneğin, alıcı, N numaralı AS'den geçen tüm rotaları yoksaymayı seçebilir).

---
# Yönlendirme Bilgi Protokolü (Routing Information Protocol - RIP)

- En eski İç Ağ Geçidi Protokollerinden (IGP) biridir.
- Özellikleri:
  - Durak sayımı (hop-count) metriğini kullanan Mesafe-Vektördür (Distance-Vector).
  - UDP (güvenilmez taşıma) üzerinden gönderilir.
  - CIDR öneklerini (prefixes) ilan eder.
  - Varsayılan rota (default route) yayılımı için bir olanak içerir.
  - Yayın (Broadcast) veya çoklu yayın (multicast) teslimi.
- Mevcut sürüm 2'dir (RIP2).

---
# RIP2 Paket Formatı

- Yönlendirme protokolleri uygulama katmanında (katman 5 - layer 5) çalışır.

> 📷 *[Görsel: RIP2 Paket Formatı (Komut, Sürüm, Ağ Adresi, Ağ Maskesi, Sonraki Durak ve Mesafe alanları vb.) — yakında eklenecek]*

---
# Açık İlk En Kısa Yol Protokolü (Open Shortest Path First - OSPF)

- Açık bir standart olmak üzere IETF tarafından oluşturulmuştur (tescilli protokollere bir tepki olarak).
- Özellikleri:
  - İç Ağ Geçidi Protokolü (IGP).
  - CIDR öneklerini ilan eder.
  - Kimliği doğrulanmış (Authenticated) mesaj alışverişi.
  - BGP'den rotaları içe aktarabilir (import).
  - Bağlantı-durumu (Link-state) algoritmasıdır.
  - Çok erişimli (multi-access) ağlar için destek sağlar.
  - Büyük ağı alanlara (areas) böler.

---
# Bir OSPF Grafiğinin Gösterimi

> 📷 *[Görsel: OSPF yönlendiricileri (R1-R6) ve aralarındaki ağ bağlantılarından oluşan OSPF grafiği — yakında eklenecek]*

- Grafik, bazı bağlantıların paylaşılan (shared) bir ağ üzerinden geçmesine rağmen her bir yönlendirici çifti arasında bir bağlantı gösterir.

---
# Ara Sistem - Ara Sistem (Intermediate System - Intermediate System / IS-IS)

- Başlangıçta DECNET V protokollerinin bir parçasıydı.
- LSR (Bağlantı-Durumu Yönlendirmesi) yaklaşımını kullanır.
- Başlangıçta:
  - Fazlasıyla özellikli (over featured) kabul edildi.
  - İnternet'te yaygın olarak kabul görmedi.
  - OSPF'nin gölgesinde kaldı.
- Sonunda:
  - OSPF özellikler eklendikçe karmaşıklaştı.
  - IS-IS kabul görmeye başladı.

---
<!-- _class: lead -->
# Yönlendirme Problemleri (Routing Problems)

---
# Sezginin (Intuition) Başarısız Olduğu Yerler

- Yönlendirme (Routing), borulardan akan suya veya otoyollardaki trafiğe benzemez:
  - Çoklu yol yönlendirmesi (Multi-path routing) zordur.
  - En kısa yol boyunca değilse kapasite kullanılmadan kalabilir.
- En az durak sayısı (hops) her zaman en iyisi olmayabilir:
  - İki Ethernet durağını ve bir uydu durağını karşılaştırın.
- Tıkanıklığın (congestion) etrafından dolanmak basit değildir ve her zaman büyük bir iyileşme sağlamaz:
  - Sıra dışı (out-of-order) paketlere neden olabilir (TCP buna tepki verir).
  - Rota çırpınmasına (route flapping) neden olabilir.

---
# Döngüler (Loops) ve Yakınsama (Convergence)

- Yönlendirme döngüsü (Routing loop):
  - Dairesel (Circular) rotalardır.
  - "İyi haberler" geriye doğru (backward) akarsa meydana gelebilir.
- Yavaş yakınsama (sonsuza kadar sayma - count to infinity) sorunu ortaya çıkar:
  - Rotalar bir değişiklikten sonra yakınsayamayabilir (fail to converge).
  - Bir yönlendirme döngüsünün devam etmesine neden olabilir.

---
# İyi Haberlerin Nasıl Geriye Akabileceği (Backwash)

- Üç yönlendirici (A, B, C) ve bir N ağının olduğu bir hikaye:

> 📷 *[Görsel: N Ağı ve A, B, C Yönlendiricileri arasındaki bağlantılar — yakında eklenecek]*

- Uygulamada, modern DV protokolleri şunları yapan buluşsal yöntemler (heuristics) kullanır:
  - Geri akışı (backflow) ortadan kaldırır.
  - Bir arızadan (failure) sonra değişiklikleri kilitler (lock down).

---
# Diğer Yönlendirme Problemleri

- Kara delik (Black hole):
  - Yönlendirme sistemi, bir hedef kümesi için olan paketleri sessizce atıldıkları (silently discarded) bir yere gönderir.
  - Yönlendirme güncelleme (routing update) paketleri kaybolursa meydana gelebilir.
- Rota çırpınması (Route flapping - yakınsama eksikliği / lack of convergence):
  - Rotalar salınım (oscillate) yapmaya devam eder.
  - Eşit uzunluktaki yollar (equal-length paths) neden olabilir.

---
# Yönlendirme Genel Yükü (Routing Overhead)

- Yönlendirme protokollerinden gelen trafik bir "genel yüktür" (overhead).
- Özel durumlar:
  - DV (Mesafe-Vektör) ilanları (advertisements) büyük olma eğilimindedir.
  - LSR (Bağlantı-Durumu Yönlendirmesi) yayını (broadcast) kullanır.
- Temel ödünleşim (Fundamental tradeoff):
  - Yönlendirme alışverişlerinin (routing exchanges) sıklığını (frequency) azaltmak genel yükü (overhead) düşürür.
  - Yönlendirme alışverişlerinin sıklığını artırmak, bir arıza (failure) ile arıza etrafından yeniden yönlendirme (rerouting) arasındaki süreyi azaltır.

---
<!-- _class: lead -->
# İnternet Çoklu Yayın (Internet Multicast) ve Çoklu Yayın Yönlendirmesi (Multicast Routing)

---
# IPv4 Çoklu Yayın (Multicast)

- Erken dönemlerde tanımlanmıştır; gayri resmi olarak "Deering çoklu yayını" (Deering multicast) denir.
- İnternet çapında çoklu yayın dağıtımı (dissemination) sağlar.
- `224.0.0.0` ile `239.255.255.255` arasındaki IPv4 adreslerini kullanır (orijinal Sınıf D adres alanı).
- Teorik olarak, İnternet'teki herhangi bir ana bilgisayar (host) şunları yapabilir:
  - İstediği zaman herhangi bir gruba katılabilir veya ayrılabilir.
  - İstediği zaman herhangi bir gruba bir veri paketi (datagram) gönderebilir.
- İnternet çapında çoklu yayın yaygın olarak kullanılmamaktadır (not widely deployed).

---
# IPv6 Çoklu Yayın (Multicast)

- IPv6'nın temel bir parçasıdır.
- IPv6 yayını (broadcast) yasaklar, ancak eşdeğer olan çoklu yayın (multicast) grupları tanımlar:
  - Tüm yönlendiriciler (All routers)
  - Tüm düğümler (All nodes)

---
# İnternet Grup Yönetimi Protokolü (IGMP)

- Bir ana bilgisayarın bir çoklu yayın (multicast) grubuna katılmasına (join) veya gruptan ayrılmasına (leave) izin verir.
- Tek bir ağ ile sınırlıdır (ana bilgisayar yerel yönlendirici ile konuşur).
- Bir ağdaki ilk ana bilgisayar yeni bir gruba katıldığında veya bir ağdaki son ana bilgisayar bir gruptan ayrıldığında, ağdaki yönlendirici(ler) çoklu yayın rotalarını buna göre değiştirir.

---
# IP Çoklu Yayın ve Ethernet Teslimatı

- Ethernet üzerinden IP çoklu yayın gönderirken:
  - Ethernet çoklu yayın özelliği (capability) kullanılabilir.
  - IP çoklu yayın adresi, bir Ethernet çoklu yayın adresiyle eşlenir (mapped).
- Problem:
  - Çoğu arayüz donanımı, aynı anda kullanılabilecek Ethernet çoklu yayın adreslerinin sayısını sınırlar.
  - İpucu: Birkaç çoklu yayın adresi kullanın ve belirli bir paketin nasıl işlenmesi gerektiğine yazılımın (software) karar vermesine izin verin.

---
# Çoklu Yayın Yönlendirme Protokolleri (Multicast Routing Protocols)

- Çoklu yayın rotalarını İnternet geneline yaymak (propagate) için gereklidir.
- Hedefler:
  - Bir gruptaki tüm katılımcıların, gruba gönderilen paketleri aldığından emin olmak.
  - Bir ana bilgisayar dinlemedikçe (listening) çoklu yayını bir ağ boyunca taşırmaktan (flooding) kaçınmak.
- Genel yaklaşım:
  - Her çoklu yayın grubu için grafik-teorik bir ağaç (tree) oluştur.
  - Çoklu yayını ağacın bağlantıları (links) boyunca yönlendir.
- İpucu: X grubu hakkında bilgi sahibi olan bir yönlendiriciye ulaşana kadar İnternet'in "merkezine" doğru X grubu için bir istek gönder.

---
# Örnek Çoklu Yayın Yönlendirme Protokolleri

- Birçok çoklu yayın yönlendirme protokolü önerilmiştir.
- Birkaç örnek:

| Protokol | Tür (Type) |
| :--- | :--- |
| DVMRP | Yapılandırma ve Tünelleme (Configuration-and-Tunneling) |
| CBT | Çekirdek Tabanlı Keşif (Core-Based-Discovery) |
| PIM-SM | Çekirdek Tabanlı Keşif (Core-Based-Discovery) |
| PIM-DM | Taşırma ve Budama (Flood-And-Prune) |
| MOSPF | Bağlantı Durumu - Link-State (bir kuruluş içinde) |

---
# Özet (Summary)

- İnternet, Otonom Sistemlere (Autonomous Systems) ayrılmıştır.
- Otonom Sistemler arasında EGP'ler (Dış Ağ Geçidi Protokolleri) kullanılır.
- Otonom Sistemler içinde IGP'ler (İç Ağ Geçidi Protokolleri) kullanılır.
- İnternet yönlendirme protokolleri şunları içerir:
  - Sınır Ağ Geçidi Protokolü (Border Gateway Protocol - BGP)
  - Yönlendirme Bilgi Protokolü (Routing Information Protocol - RIP)
  - Açık İlk En Kısa Yol Protokolü (Open Shortest Path First - OSPF)
  - Ara Sistem - Ara Sistem (IS-IS)
- Çoklu yayın (Multicast) yönlendirme protokolleri tanımlanmıştır, ancak yaygın kullanımda değildir.

---
<!-- _class: lead -->
# Sorular?
