---
marp: true
theme: custom-theme
paginate: true
header: 'Bilgisayar Ağları ve İnternet | Modül 7: Yeni Teknolojiler'
footer: 'Adapted from D. E. Comer (Prentice-Hall)'
---

<!-- _class: lead -->
# Modül 7: Yeni ve Gelişmekte Olan Ağ Teknolojileri

**Prof. Douglas E. Comer** ders materyalinden uyarlanmıştır.

---

## Konular
- Yazılım Tanımlı Ağlar (Software Defined Networking - SDN)
- Nesnelerin İnterneti (Internet Of Things)
- Ağdaki diğer eğilimler

---

<!-- _class: lead -->
# Yazılım Tanımlı Ağlar (SDN)

---

## Yazılım Tanımlı Ağlar Nedir?
- Ağ oluşturmadaki en popüler konulardan biri
- Pazarlamaya göre SDN:
  - Tüm insan hatalarını ortadan kaldırmanın bir yolu
  - Genel yönlendirmeyi iyileştiren bir teknoloji
  - Operasyonel maliyetleri %66 ila %80 oranında ortadan kaldıran bir yaklaşım
- Gerçekte SDN:
  - Programcılara ağ ekipmanları üzerinde daha fazla kontrol sağlayan bir teknoloji
  - Ağ yapılandırması ve yönetiminde bazı iyileştirmeler yapma potansiyeline sahip bir yaklaşım

---

## Motivasyon
- Eleman yönetiminden ağ yönetimine geçiş
- Tescilli standartlardan açık standartlara geçiş
- Ağ çapında yapılandırmayı otomatikleştirme ve birleştirme
- Katman başına kontrolden çapraz katmanlı kontrole değişim
- Veri merkezlerinde kullanılan sanallaştırmayı barındırma

---

## Arka Plan ve Tanımlar
- Terminoloji ağ ekipmanı mühendislerinden alınmıştır
- Veri düzlemi (data plane)
  - Paket işleme mekanizmalarını ifade eder
  - Tipik işlevler arasında paket sınıflandırma ve paket iletme bulunur
  - Kablo hızında (wire speed) çalışır
- Kontrol düzlemi (control plane)
  - Yönetimi ifade eder
  - Tipik işlevler arasında ağ yöneticisiyle etkileşim ve yönlendirme tablolarını değiştirme bulunur
  - Yavaş çalışır ve sadece değişiklik gerektiğinde devreye girer

---

## Ağ Cihazlarının Kavramsal Organizasyonu
- Veri düzlemi hız için ASIC donanımı kullanabilir
- Kontrol düzlemi bir TCP/IP yığını (TCP/IP stack) içerir

> 📷 *[Görsel: Ağ cihazlarının kontrol ve veri düzlemi organizasyonu — yakında eklenecek]*

---

## Kontrol Düzlemi Arayüz Modülleri
- Yöneticiler komut satırı arayüzü (CLI), web arayüzü ve SNMP arasından seçim yapabilir

> 📷 *[Görsel: CLI, WEB, SNMP arayüz modülleri — yakında eklenecek]*

---

## SDN Yaklaşımı: Harici Bir Denetleyici

> 📷 *[Görsel: Harici denetleyici ile SDN yaklaşımı — yakında eklenecek]*

---

## Pratikte
- Her denetleyici birden fazla cihazı çalıştırabilir
- Denetleyiciler tutarlı yapılandırma sağlamak için koordine olur

> 📷 *[Görsel: Çoklu denetleyiciler ve etki alanları — yakında eklenecek]*

---

## SDN İletişimi
- İki kavramsal olarak ayrı tür
  - Denetleyiciden ağ elemanına (Controller to network element)
  - Denetleyiciden denetleyiciye (Controller to controller)
- Kullanılan protokoller farklılık gösterebilir

---

## OpenFlow
- Denetleyici-eleman iletişimi için spesifikasyon
- Stanford'da tasarlandı
- Artık SDN için fiili endüstri standardı
- Şunları tanımlar:
  - Güvenli iletişim (SSL üzerinden)
  - Mesaj formatı
  - Yönetilecek öğeler
- SNMP'den tamamen farklıdır

---

## OpenFlow Model
- Akış tablosu (flow table) soyutlamasını kullanır
  - Veri düzleminin bir dizi akış tablosuna sahip olduğu varsayılır
  - Her akış tablosu paketlerin nasıl ayrıştırılacağını ve işleneceğini belirtir
- OpenFlow, yöneticinin her akış tablosundaki değerleri ayarlamasına izin verir
- Önemli not: Akış tablosu modeli, Ethernet anahtarlarında bulunan sınıflandırma donanımıyla yakından eşleşir

---

## Sınıflandırma
- Paket çoğullamasını çözme (packet demultiplexing) alternatifidir
- Aynı anda birden fazla katmandaki başlıkları inceler
- Bir çiftler dizisi kullanır: `(desen, eylem)`
- Burada:
  - Desen (pattern), paketlere karşı eşleştirilen bir kalıptır
  - Eylem (action), eşleşme başarılı olursa atılacak adımları belirtir

---

## Sınıflandırma Donanımı
- Donanım tüm desenleri paralel olarak kontrol eder
- Sonuç, son derece yüksek hızlı sınıflandırmadır

> 📷 *[Görsel: Sınıflandırma motoru donanımı — yakında eklenecek]*

---

## TCAM
- Üçlü İçerik Adreslenebilir Bellek (Ternary Content Addressable Memory) kısaltması
- Yüksek hızlı sınıflandırma için kullanılan donanım teknolojisi
- Desen üçlüdür çünkü her bit için değer 0, 1 veya "fark etmez" (don't care) olabilir
- TCAM tüm desenleri aynı anda eşleştirir ve eylemi ilk eşleşen tablo girişinde gerçekleştirir

---

## Örnek
- Zorluk
  - Bir çerçeve (frame) gelir
  - Çerçevenin bir web sunucusuna yönelik bir IPv4 veri birimi (datagram) taşıyıp taşımadığını belirlemek için gereken minimum adım sayısı nedir?
- Cevap
  - Çerçeve türü alanının IPv4 (0x0800) belirtip belirtmediğini kontrol et
  - IP protokol alanının TCP (6) belirtip belirtmediğini kontrol et
  - TCP hedef portunun bir web sunucusu (80) belirtip belirtmediğini kontrol et

---

## IPv6 Sınıflandırması
- En basit durum (sadece bir temel başlık)
  - Çerçeve türü alanı IPv6 (0x86DD) belirtir
  - Sonraki Başlık (Next Header) alanı TCP (6) belirtir
  - TCP hedef portu bir web sunucusu (80) belirtir
- Uzantı başlıkları için ek desenler gereklidir
- Örnek: Temel başlık artı bir rota başlığı (route header)
  - Çerçeve türü alanı IPv6 (0x86DD) belirtir
  - Sonraki Başlık alanı Rota Başlığı (43) belirtir
  - Sonraki Başlık alanı TCP (6) belirtir
  - TCP hedef portu bir web sunucusu (80) belirtir

---

<!-- _class: compact -->
## Bir OpenFlow Desenindeki Örnek Öğeler

| Alan (Field) | Anlamı (Meaning) |
|---|---|
| **Katman 2 alanları** | |
| Giriş Portu (Ingress Port) | Paketin ulaştığı anahtar portu |
| Meta veri (Metadata) | Ardışık düzende kullanılan 64 bitlik meta veri alanı |
| Ethernet kaynak (Ether src) | 48 bit Ethernet kaynak adresi |
| Ethernet hedef (Ether dst) | 48 bit Ethernet hedef adresi |
| Ethernet Türü (Ether Type) | 16 bit Ethernet türü alanı |
| VLAN id | Paketteki 12 bit VLAN etiketi |
| VLAN önceliği (VLAN priority) | 3 bit VLAN öncelik numarası |
| ARP işlem kodu (ARP opcode) | 8 bit ARP işlem kodu |
| **Katman 3 alanları** | |
| MPLS etiketi (MPLS label) | 20 bit MPLS etiketi |
| MPLS sınıfı (MPLS class) | 3 bit MPLS trafik sınıfı |
| IPv4 kaynak (IPv4 src) | 32 bit IPv4 kaynak adresi |
| IPv4 hedef (IPv4 dst) | 32 bit IPv4 hedef adresi |
| IPv6 kaynak (IPv6 src) | 128 bit IPv6 kaynak adresi |
| IPv6 hedef (IPv6 dst) | 128 bit IPv6 hedef adresi |
| IPv4 Protokol (IPv4 Proto) | 8 bit IPv4 protokol alanı |
| IPv6 Sonraki Başlık | 8 bit IPv6 sonraki başlık alanı |
| TOS | 8 bit IPv4 veya IPv6 Hizmet Türü (Type of Service) bitleri |

---

## Bir OpenFlow Desenindeki Örnek Öğeler (Devamı)

| Alan (Field) | Anlamı (Meaning) |
|---|---|
| **Katman 4 alanları** | |
| TCP/UDP/SCTP kaynak | 16 bit TCP/UDP/SCTP kaynak portu |
| TCP/UDP/SCTP hedef | 16 bit TCP/UDP/SCTP hedef portu |
| ICMP türü (ICMP type) | 8 bit ICMP türü alanı |
| ICMP kodu (ICMP code) | 8 bit ICMP kodu alanı |

---

## Örnekler
- Uçtan uca (End-to-end) katman 2 yolları
- Sadece hedefe değil, kaynağa dayalı yönlendirme
- Belirli bir MAC adresinden gelen tüm trafiğin belirli bir yol boyunca gönderilmesi
- Uygulama türüne göre trafiğin ayrıştırılması (segregation)
- 4'lü demetin (4-tuple) özet değerine (hash) dayalı çok yollu (multipath) yönlendirme
- Standart olmayan katman 3 protokollerinin taşınması

---

<!-- _class: lead -->
# Nesnelerin İnterneti (IoT)

---

## Nesnelerin İnterneti
- İnternetteki gömülü sistemler (embedded systems) için kullanılan garip bir terim
  - Genellikle insanlar tarafından çalıştırılmazlar
  - Birbirlerine veya bulut (cloud) hizmetlerine erişebilirler
- Örnekler
  - Bilimsel sensör sistemleri
  - Ev otomasyon sistemleri
  - Akıllı şebeke (Smart grid)
  - Perakende sistemleri

---

## Teknoloji Özellikleri
- Düşük güç (Low power)
  - Enerji hasadı (örn. kapı mandalı)
  - Çok yıllı pil ömrü
- Kablosuz iletişim (Wireless communication)
  - Çoğu durumda gereklidir
  - Hareketliliği (mobility) sağlar

---

## Kablosuz Örgü Ağ
- Bireysel düğümler (nodes) çok düşük güce (sınırlı menzile) sahip olduğunda faydalıdır
- Bazı düğümler doğrudan iletişim kuramasa bile bir dizi düğümün iletişim kurmasını sağlar
- Her düğüm, komşuları adına paketleri iletmeyi (forward) kabul eder

---

## Örnek
- ZigBee IP
  - ZigBee Alliance tarafından oluşturuldu
  - IEEE 802.15.4 kablosuz radyolarını kullanır
  - Akıllı şebeke (smart grid) için tasarlanmıştır
- ZigBee protokol yığını (protocol stack)
  - Amaç IPv6, TCP ve HTTP çalıştırmaktır
  - Diğer birçok protokolü içerir

---

## Özellikleri
- Hedef düşük güçtür ve sonuç şudur:
  - Son derece düşük veri hızı
  - Son derece küçük MTU
  - Sınırlı mesafe

| Özellik (Property) | Değer (Value) |
|---|---|
| Ağ oluşturma paradigması | Paket anahtarlama (Packet switching) |
| Maksimum veri hızı | 250 Kbps |
| Yük boyutu (MTU) | 102 sekizli (octets) |
| Maksimum mesafe | 10 metre |

---

## Yönlendirme
- Bir veya daha fazla sınır yönlendiricisi (border router)
  - Küresel İnternet'e bağlanır
  - Diğer düğümlerden daha güçlüdür
- ZigBee IP yönlendiricileri kümesi (ZIP routers)
  - Cihazlara (appliances) bağlanır
  - Bir örgü (mesh) oluşturur
  - Trafiği sınır yönlendiricisine iletir

---

## Yol Seçimi
- ZIP yönlendirici, bir sınır yönlendiricisine giden bir yol seçmelidir
- Sadece en güçlü iletim sinyaline sahip düğümü seçemez
- Hangi düğümün en güçlü sinyali (MLE) aldığını bulmak için kullanılan ek protokol

> 📷 *[Görsel: Yol seçimi ve ağ topolojisi — yakında eklenecek]*

---

## Çalıştırma
- IPv6 sadece 1280 veya daha yüksek bir MTU sunan ağlar üzerinde çalışabilir, ancak 802.15.4, 102'lik bir MTU'ya sahiptir
- Çözüm
  - 6LoWPAN adlı ek protokol
  - IP ve cihaz sürücüsü arasında ara katman (shim layer)

---

## Çalışma Şekli
- Gönderen taraf
  - Veri birimini (datagram) bir dizi bloğa böler
  - Her bloğu bir pakette iletir
- Alan taraf
  - Blokları bir veri biriminde birleştirir
  - Tüm veri birimini IPv6'ya teslim eder
- Notlar
  - Bloğa bölme işlemi IP parçalanmasını (IP fragmentation) kullanmaz
  - Parçalanmanın aksine, bölme ve yeniden gruplama her atlamada (hop) gerçekleştirilir

---

## Yönlendirme (Devamı)
- ZIP düğümleri, paketleri sınır yönlendiricisine doğru iletir
- Sınır yönlendiricisi
  - Giden paketleri İnternet'e gönderebilir
  - Diğer paketleri örgü üzerinden iletir
- İki ZIP düğümü iletişim kurarsa
  - Paket önce sınır yönlendiricisine gider
  - Sınır yönlendiricisi hedefe iletir

---

## Sınır Yönlendiricisinin Çalışması
- Sınır yönlendiricisi örgü üzerinden iletmek için
  - Örgünün topolojisini öğrenir
  - Örgü üzerinden her ZIP düğümüne giden bir yol hesaplar
  - IPv6 kaynak yönlendirmesini (source routing) kullanır
- IPv6 kaynak yönlendirmesi
  - IP içinde IP tünelleme (IP-in-IP tunneling) gerektirir (başlık değişikliği yasaktır)
  - Dış veri birimine bir dizi atlama (hop) içeren bir uzantı başlığı yerleştirir
  - Her ZIP düğümünün sadece komşularını bilmesi gerekir

---

## Kaynak Rotalarını Hesaplama
- Tüm düğümler kayıplı ve düşük güçlü ağlar için Yönlendirme Protokolü (RPL) çalıştırır
- Her düğüm ebeveynini sınır yönlendiricisine bildirir
- Sınır yönlendiricisindeki RPL kodu, Hedef Odaklı Yönlendirilmiş Asiklik Grafik (DODAG) oluşturur
- DODAG, kaynak rotalarını hesaplamak için kullanılır

---

## Örnek DODAG
- DODAG'daki yaylar (arcs) ebeveyne (sınır yönlendiricisine giden yola) işaret eder
- X düğümüne giden kaynak rotası, X'ten sınır yönlendiricisine giden yolun tersidir

> 📷 *[Görsel: DODAG ebeveyn ağacı — yakında eklenecek]*

---

## Mantıklı mı?
- IPv4 yerine IPv6'yı seçmek şunlar anlamına gelir:
  - Çok daha büyük veri birimi başlıkları
  - Bir veri birimini MTU boyutunda parçalara ayırmak için 6LoWPAN kullanımı
  - Yavaş bir ağ üzerinden daha fazla veri gönderme
  - RPL yönlendirme protokollerine ihtiyaç
  - Daha büyük bellekler (ve daha düşük pil ömrü)
- IPv6 üzerinden TCP ve HTTP kullanmak şunlar anlamına gelir:
  - İsimleri çözümlemek için DNS kullanımı
  - Gereksiz ek yük (overhead)
  - Gereksiz bellek ayak izi

---

## Dahası Var!
- Akıllı şebeke uygulamaları güvenli olmalıdır, bu nedenle ZigBee IP, TLS dahil olmak üzere güvenlik protokollerini içerir
- IPv6 Komşu Keşfi (Neighbor Discovery) bir örgü ağında (mesh network) çalışmaz, bu nedenle ZigBee IP, 6LoWPAN-ND olarak bilinen bir değişiklik içerir
- IEEE 802.15.4 kısa (16 bit) MAC adreslerine izin verir, bu nedenle ZigBee IP, bir sınır yönlendiricisinin adres çakışmalarını (address collisions) önlemesine izin veren bir mekanizma içerir

---

## Ana Öğeler
- Ortaya çıkan yığın büyüktür
- Tasarım gerekenden daha genel amaçlıdır
- Teknoloji, siyaset ve ekonominin bir zaferi olabilir

> 📷 *[Görsel: ZigBee protokol yığını öğeleri — yakında eklenecek]*

---

<!-- _class: lead -->
# Ağdaki Diğer Eğilimler

---

## Birkaç Temel Teknoloji
- İçerik Önbelleğe Alma (Content Caching)
- Uçtan Uca İletişim (Peer-To-Peer Communication)
- Evrensel Temsil (Universal Representation - XML)
- Hareketliliği (mobility) destekleyen kablosuz ağlar
- Daha yüksek hızlı erişim teknolojileri (1 Gbps)
- Bulut bilişim (Cloud computing) ve bulut veri merkezleri

---

## Yük Dengeleyiciler
- Yük dengeleyici (load balancer), HTTP isteklerini sunucular arasında dağıtır
- Sunuculardan istemciye dönen yol daha yüksek hızlı olabilir

> 📷 *[Görsel: Web yük dengeleyici mimarisi — yakında eklenecek]*

---

## Bindirmeli Ağ
- (a) Bilgisayarların İnternet'e fiziksel bağlantısı
- (b) Bindirmeli yönlendirme (overlay routing) ile dayatılan mantıksal ağ

> 📷 *[Görsel: Fiziksel ağ ve bindirmeli ağ mantığı — yakında eklenecek]*

---

## Diğer Eğilimler
- Dijital telefoni ve dijital videoya geçiş
- Sosyal ağ (social networking) ve sosyal medyanın artan kullanımı
- Dağıtılmış veri merkezleri ve geçiş (migration)
