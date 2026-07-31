---
marp: true
theme: custom-theme
paginate: true
header: 'Bilgisayar Ağları ve İnternet | Modül 2: Uygulama Katmanı'
footer: 'Adapted from D. E. Comer (Prentice-Hall)'
---

<!-- _class: lead -->
# Modül 2: Ağ Programlama ve Uygulama Katmanı

## Uygulama Katmanı Protokolleri, Soket API ve Ağ Mimarileri

**Prof. Douglas E. Comer** ders materyalinden uyarlanmıştır.

---

# Modül 2 Konu Başlıkları

- İnternet Hizmetleri ve İletişim Paradigmaları
- İstemci-Sunucu Modeli ve Alternatifleri
- Basitleştirilmiş Bir API ile Ağ Programlama
- Soket API (The Socket API)
- Uygulama Katmanı Protokolleri
- Standart Uygulama Protokolü Örnekleri

---

<!-- _class: lead -->
# Bölüm 2.1: İnternet Hizmetleri ve İletişim Paradigmaları

---

# Genel İlke: Zekanın Ağ Uçlarında Olması

- İnternet doğrudan hizmet sunmaz; yalnızca iletişim sağlar. Tüm hizmetleri uygulama programları sunar.
- Sonuç:
  - Sesli ve görüntülü telekonferans dahil tüm İnternet iletişimi, uygulama programları arasındaki iletişimden ibarettir.
  - Ağ çekirdeği basit paket iletimi yapar; karmaşık uygulama mantığı uç sistemlerde (host) çalışır.
  - Yeni bir uygulama eklendiğinde ağ altyapısının değiştirilmesi gerekmez.

---

# İletişim Paradigmaları Karşılaştırması

İnternet iki temel iletişim paradigması sunar:

| Özellik | Akış Modeli (Stream - TCP) | Mesaj Modeli (Message - UDP) |
|---|---|---|
| **Bağlantı Yapısı** | Bağlantı Tabanlı (Connection-oriented) | Bağlantısız (Connectionless) |
| **Etkileşim Türü** | Bire-bir İletişim | Bire-bir, Birden-çoğa, Birden-herkese |
| **Veri Birimi** | Bireysel Bayt Dizisi | Bağımsız Mesaj Dizisi |
| **Veri Boyutu** | Değişken / Rastgele Uzunluk | Mesaj Başına Maks. 64 KB |
| **Kullanım Alanı** | Çoğu Standart Uygulama (Web, E-posta) | Çoklu Ortam (Ses/Video, Oyun) |
| **Temel Protokol** | TCP Protokolü | UDP Protokolü |

- **Not**: Her iki paradigmanın da ilk bakışta şaşırtıcı gelen davranış özellikleri vardır.

---

# Akış Modeli (Stream Paradigm - TCP)

- Bir dizi baytı aktarır.
- Bağlantı tabanlıdır: Veri iki uygulama arasında gönderilir.
- İki yönlüdür (her iki yönde birer akış mevcuttur).
- Veriye herhangi bir anlam yüklenmez ve veri içine sınırlar yerleştirilmez.
- **Şaşırtıcı Özellik**:
  - Tüm baytları sırasıyla ulaştırmasına rağmen, akış modeli alıcı uygulamaya teslim edilen bayt bloklarının gönderici uygulama tarafından gönderilen bloklara karşılık geleceğini garanti etmez.

---

# Mesaj Modeli (Message Paradigm - UDP)

- Bağlantısızdır: Ağ, bağımsız mesajları kabul eder ve iletir.
- Gönderici bir mesaja N bayt yerleştirirse, alıcı gelen mesajda tam olarak N bayt bulur.
- Tekli yayın (unicast), çoklu yayın (multicast) veya genel yayın (broadcast) iletimini destekler.
- **Şaşırtıcı Özellik**:
  - Sınırları korumasına rağmen mesaj modeli paketlerin kaybolmasına, yinelenmesine veya sırasız teslim edilmesine izin verir; bu tür hatalar oluştuğunda ne göndericiye ne de alıcıya bilgi verilir.

---

# Akış Taşıma (Stream Transport) ve Veri Blokları (Data Chunks)

- Protokol sistemi şunları yapabilir:
  - Göndericiden gelen veriyi birden fazla segmente bölebilir ve alıcıya her defasında birkaç bayt teslim edebilir.
  - Birden fazla iletimden gelen veriyi tek bir büyük blokta birleştirip alıcıya hepsini tek seferde teslim edebilir.
- **Sonuç**: Alıcı uygulama hangi parçaların gönderildiğini tam olarak bilemez.

---

# Örnek #1

- İki uygulama arasında bir akış bağlantısı olduğunu varsayalım.
- Gönderici:
  - `buf` tamponuna 1000 baytlık mesaj yerleştirir.
  - 1000 baytın tamamını göndermek için tek bir istekte bulunur.
- Alıcı:
  - 1000 baytlık bir `b` tamponu ayırır.
  - Akıştan `b` tamponuna 1000 bayt okuma isteğinde bulunur.
- İşletim sistemi 1 ile 1000 bayt arasında bir miktar döndürebilir.
- Uygulama, 1000 baytın tamamı alınana kadar ard arda çağrılar yapmalıdır.

---

# Örnek #2

- İki uygulama arasında bir akış bağlantısı olduğunu varsayalım.
- Gönderici, her biri 100 bayt uzunluğunda 4 mesajlık bir dizi iletir.
- Alıcı 1000 baytlık büyük bir `b` tamponu ayırır ve akıştan `b` tamponuna 1000 bayta kadar okuma yapılmasını ister.
- İşletim sistemi tek bir okuma isteğinde 4 mesajın tamamını (400 bayt) döndürmeyi seçebilir.
- Alıcı uygulama, gelen veriyi 4 ayrı mesaja kendisi ayırabilmelidir.

---

# Programlama İpuçları

- **Akış Modeli (TCP) Kullanırken**:
  - Alıcının bir mesajın nerede bittiğini anlayacağı bir yöntem geliştirin.
  - Mesajın tamamı alınana kadar soketten okuma yapmaya devam edin.
- **Mesaj Modelini (UDP) Kullanmayı Düşünürken**:
  - Kullanmayın (en azından henüz değil).

---

<!-- _class: compact -->
# Bir Akış İçinde Bireysel Mesajları Belirleme

- **Olasılıklar / Yöntemler**:
  - Tek bir mesaj gönderip ardından dosya sonu (EOF) kapatması yapmak.
  - Her mesajın önüne tamsayı bir uzunluk değeri ekleyerek birden fazla mesaj göndermek.
  - Her mesajın ardına bir sonlandırma karakteri (veya dizisi) ekleyerek birden fazla mesaj göndermek.
- **Notlar**:
  - İki taraf anlaştığı sürece herhangi bir teknik kullanılabilir.
  - Çok baytlı bir uzunluk değeri veya sonlandırma dizisi gönderiliyorsa, tüm baytları almak için uygulamanın birden fazla okuma yapması gerekebileceği unutulmamalıdır.

---

# Gerçekçi Ortamda Mesaj Bölünmesi ve Birleşmesi

- **Sorular (Gerçekçi Bir Senaryoda)**:
  - Tek bir mesajın ağda bölünmesi (parçalanması) olası mıdır?
  - Birden fazla mesajın ağda birleştirilmesi (toplanması) olası mıdır?
- **Yanıtlar**: **Evet, ikisi de oldukça olasıdır!** (Mesaj boyutuna bağlı olarak):
  - **Mesaj Bölünmesi**: 1400 karakterden (bayttan) büyük mesajlar iletim için genellikle birden fazla pakete bölünür; alıcıya birlikte veya ayrı ayrı ulaşabilir.
  - **Mesaj Birleştirilmesi**: Akış hizmeti, toplu veri aktarımını daha verimli kılmak amacıyla küçük mesajları alıcı uygulamaya teslim etmeden önce birleştirecek şekilde tasarlanmıştır.

---

<!-- _class: compact -->
# Akış Modelinde Tamponlama (Buffering)

- Toplu veri aktarımını daha verimli kılan **birleştirme (aggregation)**, gönderici veya alıcı tarafında gerçekleşebilir.
- Akış modeli, uygulamanın verinin iletimini ve teslimini zorlamasını sağlayan bir **itme (push)** işlemi içerir.
- **Unix Geleneği**: Her bireysel `write` çağrısı için otomatik olarak *push* uygulanır.
- **Programlama İpuçları**:
  - Küçük bir mesajın gecikmeden iletilip teslim edilmesini sağlamak için ayrı bir `write` kullanın.
  - *Push* kullanılsa dahi, ağ gecikmeleri nedeniyle uygulamalar birleştirmeyi tolere edecek şekilde yazılmalıdır.
- *(Konunun detayları dersin ilerleyen bölümlerinde açıklanacaktır)*

---

<!-- _class: lead -->
# Bölüm 2.2: İstemci-Sunucu Modeli ve Alternatifleri

---

# İstemci-Sunucu Etkileşim Modeli

- Uygulamalar tarafından iletişim kurmak için kullanılır.
- **Sunucu (Server)** olarak hareket eden uygulama:
  - İlk önce çalışmaya başlar.
  - Bağlantı kurulmasını pasif olarak bekler.
- **İstemci (Client)** olarak hareket eden uygulama:
  - Sunucu çalışmaya başladıktan sonra başlatılır.
  - İletişimi (bağlantıyı) aktif olarak başlatan taraftır.
- **Önemli Kavram**: İletişim bir kez kurulduktan sonra, veri (istekler ve yanıtlar) istemci ile sunucu arasında **her iki yönde de** serbestçe akabilir.

---

# İstemcinin (Client) Özellikleri

- Geçici olarak istemciye dönüşen rastgele bir uygulama programıdır.
- Genellikle doğrudan bir kullanıcı tarafından çağrılır ve genellikle yalnızca tek bir oturum için yürütülür.
- Bir sunucu ile bağlantıyı aktif olarak başlatır, mesaj alışverişinde bulunur ve ardından bağlantıyı sonlandırır.
- Gerektiğinde birden fazla hizmete erişebilir, ancak genellikle aynı anda tek bir uzak sunucuyla bağlantı kurar.
- Kullanıcının kişisel bilgisayarında veya akıllı telefonunda yerel olarak çalışır.
- Özellikle güçlü bir bilgisayar donanımı gerektirmez.

---

# Sunucunun (Server) Özellikleri

- Bir hizmet sunmaya adanmış özel amaçlı, yetkili (privileged) bir programdır.
- Genellikle aynı anda birden fazla uzak istemciyi işleyecek şekilde tasarlanmıştır — **tasarımı karmaşıklaştırır**.
- Bir sistem başlatıldığında (boot) otomatik olarak çağrılır ve birçok istemci oturumu boyunca çalışmaya devam eder.
- Rastgele uzak istemcilerden bağlantı gelmesini pasif olarak bekler ve ardından mesaj alışverişinde bulunur.
- Güçlü donanım ve gelişmiş bir işletim sistemi gerektirir.
- Büyük ve güçlü bir bilgisayarda çalışır.

---

# Sunucu Programları ve Sunucu Sınıfı Bilgisayarlar

- Bilimsel ve pazarlama terminolojisi arasında bir kavram karmaşası bulunmaktadır
- **Bilimsel (Scientific)**: İstemci ve sunucunun her biri birer **programdır**
- **Pazarlama (Marketing)**: Sunucu, güçlü bir **bilgisayardır**

![center height:220px](images/fig_103_server_class.svg)

---

# İstemci-Sunucu Etkileşiminin Özeti

| Sunucu Uygulaması (Server Application) | İstemci Uygulaması (Client Application) |
|---|---|
| İlk olarak başlar | İkinci olarak başlar |
| Hangi istemcinin kendisiyle bağlantı kuracağını bilmesine gerek yoktur | Hangi sunucuyla bağlantı kuracağını bilmek zorundadır |
| Bir istemciden bağlantı gelmesini pasif olarak ve süresiz bekler | İletişim gerektiği her an bir bağlantı başlatır |
| Veri gönderip alarak bir istemciyle iletişim kurar | Veri gönderip alarak bir sunucuyla iletişim kurar |
| Bir istemciye hizmet verdikten sonra çalışmaya devam eder ve diğeri için bekler | Bir sunucuyla etkileşime girdikten sonra sonlanabilir |

---

# İstemci ve Sunucu Tarafından Atılan Adımların Gösterimi

![center height:480px](images/fig_105_client_server_steps.svg)

---

# İstemci-Sunucu Alternatifleri

- **Yayın (Broadcast)**:
  - Gönderici mesajı tüm ağa yayınlar ve tüm istasyonlar mesajı alır.
  - İyi ölçeklenemez (verimsiz hale gelir).
  - Veri erişimini kısıtlamak zordur.
- **Buluşma Noktası (Rendezvous Point)**:
  - İletişim kuran uygulamaları bir aracı (intermediate) bağlar.
  - Esas itibarıyla iki istemci ve bir sunucu mevcuttur.
  - Buluşma noktası bir darboğaz (bottleneck) haline gelir.

---

<!-- _class: compact -->
# İstemci-Sunucu Alternatifleri: Noktadan Noktaya (Peer-to-Peer)

- **Noktadan Noktaya Etkileşim (Peer-to-Peer / P2P)**:
  - Merkezi sunucu darboğazını önlemek için tasarlanmıştır.
  - Veri $N$ adet bilgisayar arasında bölünür.
  - Her bir bilgisayar kendi verisi için **sunucu**, diğer veriler için **istemci** olarak hareket eder.
  - Belirli bir bilgisayar toplam trafiğin yalnızca $1 / N$ kadarını alır.

![center height:200px](images/fig_107_p2p_interaction_cropped.png)

---

<!-- _class: lead -->
# Bölüm 2.3: Basitleştirilmiş API ve Soket API ile Ağ Programlama

---

# Ağ Programlama (Network Programming)

- Ağ üzerinden iletişim kuran istemci ve sunucu uygulamalarının oluşturulmasını ifade eden genel bir terimdir.
- Programcı bir **Uygulama Programlama Arayüzü (API - Application Programming Interface)** kullanır:
  - Fonksiyonlar kümesidir.
  - Veri aktarımının yanı sıra kontrol fonksiyonlarını da içerir (örneğin iletişimi kurma ve sonlandırma).
- İşletim sistemi tarafından tanımlanır; İnternet standartlarının bir parçası değildir.
- **Soket API (Socket API)** fiili bir standart (de facto standard) haline gelmiştir.

---

# Basitleştirilmiş Örnek Bir API

- Konuya başlangıç yapmanıza yardımcı olacaktır.
- **Genel Fikir**:
  - Sunucu `(bilgisayar, uygulama)` ikilisi ile tanımlanır.
  - Sunucu ilk olarak başlar ve bağlantı bekler.
  - İstemci, sunucunun konumunu belirtir.
  - Bir bağlantı kurulduktan sonra istemci ve sunucu veri alışverişinde bulunabilir.
- Basitleştirilmiş API içinde yalnızca yedi fonksiyon bulunmaktadır.

---

# Basitleştirilmiş Örnek API Fonksiyonları

| İşlem (Operation) | Anlamı (Meaning) |
|---|---|
| `await_contact` | Sunucu tarafından bir istemciden bağlantı beklenmesi için kullanılır |
| `make_contact` | İstemci tarafından bir sunucuyla bağlantı kurulması için kullanılır |
| `appname_to_appnum` | Program adını karşılık gelen dahili ikili değere çevirmek için kullanılır |
| `cname_to_comp` | Bilgisayar adını karşılık gelen dahili ikili değere çevirmek için kullanılır |
| `send` | İstemci veya sunucu tarafından veri göndermek için kullanılır |
| `recv` | İstemci veya sunucu tarafından veri almak için kullanılır |
| `send_eof` | Veri gönderimi bittikten sonra hem istemci hem sunucu tarafından kullanılır |

---

# Örnek API İle İstemci ve Sunucu Etkileşimi

- İstemcinin tek bir istek gönderdiği ve sunucunun yanıt verdiği basit bir veri alışverişindeki çağrı dizisi:

![center height:280px](images/fig_114_simplified_api.png)

- İletişim iki yönlü (bidirectional) olduğu için **her iki taraf da `send_eof` çağırmalıdır**.

---

# Örnek API Veri Tipleri

| Tip Adı (Type Name) | Anlamı (Meaning) |
|---|---|
| `appnum` | Bir uygulamayı tanımlamak için kullanılan ikili (binary) değer |
| `computer` | Bir bilgisayarı tanımlamak için kullanılan ikili (binary) değer |
| `connection` | İstemci ile sunucu arasındaki bağlantıyı tanımlamak için kullanılan değer |

---

<!-- _class: compact -->
# Kolaylık Sağlayan Ek Bir Fonksiyon: `recvln`

- Basitleştirilmiş örnek API, kullanım kolaylığı sağlamak amacıyla ek bir `recvln` fonksiyonu içerir.
- Zorunlu değildir, ancak kolaylık sağlar.
- `recv` fonksiyonuna benzer:
  - Bir bağlantıdan veri alır.
  - Alınan veriyi bir tampona (buffer) yerleştirir.
- **Farkı**:
  - Tam olarak istenen miktarda veriyi okur.
  - **Teknik**: Belirtilen uzunlukta veri elde edilene kadar ardışık olarak `recv` fonksiyonunu çağırır.

---

# Örnek API Parametre Tipleri

| Fonksiyon Adı | Dönen Tip | Parametre 1 Tipi | Parametre 2 Tipi | Parametre 3–4 Tipi |
|---|---|---|---|---|
| `await_contact` | `connection` | `appnum` | — | — |
| `make_contact` | `connection` | `computer` | `appnum` | — |
| `appname_to_appnum` | `appnum` | `char *` | — | — |
| `cname_to_comp` | `computer` | `char *` | — | — |
| `send` | `int` | `connection` | `char *` | `int` |
| `recv` | `int` | `connection` | `char *` | `int` |
| `recvln` | `int` | `connection` | `char *` | `int` |
| `send_eof` | `int` | `connection` | — | — |

- *(Detaylar problem çözme saatlerinde / PSO ortamında öğrenilecektir)*

---

# Soket API ve Tarihçesi

- Orijinal olarak **BSD Unix** işletim sisteminin bir parçası olarak geliştirilmiştir (1983).
- Günümüzde endüstride **fiili standart** (de facto standard) haline gelmiştir.
- AT&T, **TLI** (Transport Layer Interface) adında alternatif bir arayüz tanımlamıştı; ancak TLI artık kullanılmamaktadır (extinct).
- Neredeyse tüm işletim sistemleri soket uygulamasını (implementation) içerir.
- Microsoft Windows küçük değişiklikler yapmayı tercih etmiştir (Winsock - rahatsız edici bir ayrıntı).

---

# Soket Özellikleri (Socket Characteristics)

- İşletim sistemi tarafından oluşturulur ve yönetilir.
- İstemci veya sunucu tarafından başlatılabilir:
  - Sunucu bir soket oluşturup **pasif (passive)** dinleme moduna geçer.
  - İstemci bir soket oluşturup **aktif (active)** bağlantı başlatır.
- İşletim sisteminin dosya arayüzüyle entegredir:
  - Uygulama bir soket oluşturduğunda bir **dosya tanımlayıcısı (file descriptor)** elde eder.
  - Okuma (`read`), yazma (`write`) veya kapatma (`close`) işlemleri standart dosya I/O mantığıyla gerçekleştirilebilir.
- Asenkron/zaman uyumsuz (asynchronous / non-blocking) veya senkron/zaman uyumlu (synchronous / blocking) I/O destekler.

---

# TCP İçin Standart Soket API Çağrıları

![center height:240px](images/fig_121_socket_calls.png)

- **Sunucu Tarafı**: `socket()` $\rightarrow$ `bind()` $\rightarrow$ `listen()` $\rightarrow$ `accept()` $\rightarrow$ `recv()`/`send()` $\rightarrow$ `close()`
- **İstemci Tarafı**: `socket()` $\rightarrow$ `connect()` $\rightarrow$ `send()`/`recv()` $\rightarrow$ `close()`
- Bağlantılı (connection-oriented) akış hizmeti (stream service) için etkileşim sırasını gösterir.

---

<!-- _class: lead -->
# Bölüm 2.4: Uygulama Katmanı Protokolleri

---

# Protokol Türleri: Açık ve Kapalı Protokoller

- **Açık Protokol (Open Protocol)**:
  - Spesifikasyonları kamuya açık ve ücretsiz olarak yayımlanmıştır (RFC - Request for Comments).
  - Standartlar **IETF (Internet Engineering Task Force)** tarafından yönetilir.
  - Farklı üreticilerin ve geliştiricilerin yazılımlarının birbiriyle sorunsuz çalışmasını (interoperability) sağlar.
  - Örnekler: HTTP, SMTP, FTP, DNS.
- **Kapalı / Özel Protokol (Closed / Proprietary Protocol)**:
  - Tek bir şirket veya kuruluş tarafından sahiplenilir ve detayları gizli tutulur.
  - Yalnızca ilgili şirketin yazılımları iletişim kurabilir.
  - Örnekler: Skype (orijinal protokol), Skype for Business, Apple FaceTime.

---

# Uygulama Protokolü Tanımı: Temsil ve Aktarım

Bir uygulama katmanı protokolü iki temel bileşeni tanımlar:

1. **Veri Temsili (Data Representation)**:
   - Veri sözdizimi (syntax), mesaj türleri, alan formatları ve karakter kodlaması.
   - İletilen verinin nasıl biçimlendirileceğini ve anlamlandırılacağını (semantics) belirler.
2. **Veri Aktarımı (Data Transfer)**:
   - İstemci ve sunucu arasındaki mesaj alışveriş kuralları ve dizilimi.
   - Bağlantı kurulumu, hata durumu yönetimi, onaylama ve oturum kapatma adımları.

---

# Uygulama Protokollerinde Durum (State)

- **Durumsuz Protokol (Stateless Protocol)**:
  - Sunucu, istemciler hakkında geçmiş etkileşim bilgisini (state) tutmaz.
  - Her bir istek, önceki isteklerden tamamen bağımsızdır.
  - Tasarımı ve uygulaması basittir; sunucu çökse bile toparlanması kolaydır.
  - Örnek: HTTP/1.0 (Çerezler / Cookies kullanılmadığında).
- **Durumlu Protokol (Stateful Protocol)**:
  - Sunucu, istemcinin mevcut durumunu, kimliğini ve oturum geçmişini takip eder.
  - İletişim adımları birbirine bağımlıdır.
  - Örnek: FTP (oturum açma bilgisi ve mevcut çalışma dizini sunucu tarafından tutulur).

---

<!-- _class: lead -->
# Bölüm 2.5: Uygulama Protokolü Örnekleri

- Web Taraması (Web Browsing)
- E-Posta (Email)
- Dosya Aktarımı (File Transfer - FTP)
- Uzaktan Erişim (TELNET / SSH)
- Alan Adı Sistemi (DNS - Domain Name System)

---

# Web Taraması (Web Browsing) ve Temel Standartlar

Web teknolojisi üç temel bileşen üzerine inşa edilmiştir:

- **HTML (HyperText Markup Language)**: Belge içeriğini, bağlantılarını (hyperlinks) ve yapısını tanımlayan biçimlendirme dilidir.
- **URL (Uniform Resource Locator)**: İnternet üzerindeki herhangi bir kaynağın eşsiz adresini ve erişim metodunu belirtir.
- **HTTP (HyperText Transfer Protocol)**: İstemci (web tarayıcı) ile sunucu (web sunucusu) arasındaki veri aktarım protokolüdür.

---

# Tekdüze Kaynak Bulucu (URL - Uniform Resource Locator)

- Web kaynaklarını adreslemek için kullanılan standart sözdizimi:

$$\texttt{protocol://host:port/page\_name}$$

- **`protocol`**: Kullanılacak uygulama protokolü (ör. `http`, `https`, `ftp`).
- **`host`**: Sunucunun etki alanı adı veya IP adresi (ör. `www.cs.purdue.edu`).
- **`port`**: *(Opsiyonel)* Sunucunun dinlediği port numarası (HTTP için varsayılan `80`, HTTPS için `443`).
- **`page_name`**: Sunucudaki dosya veya kaynağın yolu (path) ve adı (ör. `/homes/comer/index.html`).

---

# HTTP Protokolünün Temel Özellikleri

- **Metin Tabanlı (Text-Based)**: İstek ve yanıt başlıkları insan tarafından okunabilir metin formatındadır.
- **İstek / Yanıt Paradigması (Request / Response)**:
  - İstemci sunucuya bir HTTP isteği gönderir.
  - Sunucu durum bilgisi ve talep edilen içerikle yanıt verir.
- **Durumsuz (Stateless)**: Sunucu varsayılan olarak istemci durumunu saklamaz (oturum takibi için çerezler / cookies kullanılır).
- **Önbellekleme (Caching)**: Verimliliği artırmak için yanıtların önbellekte tutulmasını destekler.

---

# Dört Ana HTTP İstek Türü (Request Methods)

| İstek Türü | Açıklama |
|---|---|
| **`GET`** | Sunucudan bir belge ister; sunucu durum bilgisi ve belgenin kopyasını gönderir |
| **`HEAD`** | Sunucudan yalnızca durum/başlık bilgisini ister; belge içeriğini göndermez |
| **`POST`** | Sunucuya veri gönderir; sunucu veriyi belirtilen öğeye ekler (ör. forma ekleme) |
| **`PUT`** | Sunucuya veri gönderir; belirtilen öğenin üzerine tamamen yazar (overwrite) |

- **`GET` İsteği Biçimi**:
  $$\texttt{GET /item HTTP/1.0}\quad\text{veya}\quad\texttt{GET /item HTTP/1.1}$$

---

# HTTP Yanıt Biçimi (Response Header Format)

- Yanıt bir metin başlığı ile başlar ve isteğe bağlı ikili (binary) içerik ile devam eder.
- Başlık formatı:
```http
HTTP/1.0 200 OK
Server: Apache/2.2.11 (Unix)
Last-Modified: Mon, 17 Oct 2011 22:21:41 GMT
Content-Length: 2640
Content-Type: text/html

... [2640 baytlık HTML veri içeriği burada başlar] ...
```
- Başlık kısmı boş bir satır (`CRLF`) ile sonlanır.

---

<!-- _class: compact -->
# HTTP İstek/Yanıt Örneği (Telnet İle Apache Web Sunucusu)

```text
$ telnet www.cs.purdue.edu 80
Trying 128.10.19.20...
Connected to lucan.cs.purdue.edu.
Escape character is '^]'.
GET /homes/comer/ HTTP/1.0

HTTP/1.1 200 OK
Date: Sun, 10 Nov 2013 11:38:27 GMT
Server: Apache/2.2.11 (Unix) mod_ssl/2.2.11 OpenSSL/0.9.8r
Last-Modified: Mon, 17 Oct 2011 22:21:41 GMT
ETag: "bafb0-a50-4af8607f7c740"
Accept-Ranges: bytes
Content-Length: 2640
Connection: close
Content-Type: text/html

... (web sayfasının HTML verisi burada devam eder)
```

---

# Orijinal Uçtan Uca E-Posta Mimarisi

![center height:260px](images/fig_138_original_email.png)

- Her bilgisayar hem e-posta sunucusu hem de e-posta istemcisi çalıştırır.
- Gelen e-postalar doğrudan kullanıcının posta kutusuna (mailbox) bırakılır.
- Giden e-postalar bir kuyruğa (queue) yerleştirilir.
- Alıcının bilgisayarı kapalıysa e-posta iletilemez.

---

# Günümüz E-Posta Mimarisi

![center height:260px](images/fig_139_current_email.png)

- Kullanıcının posta kutusu ayrı bir sunucuda (genellikle ISP veya bulut e-posta sağlayıcısında) tutulur.
- E-posta aktarım uygulaması (MTA) mesajı sunucudaki posta kutusuna bırakır.
- Kullanıcı arayüzü uygulaması (MUA veya Webmail) uzaktaki posta kutusuna erişir.

---

# Basit Posta Aktarım Protokolü (SMTP)

- E-posta aktarımı için standart İnternet protokolüdür.
- **Akış Paradigması (Stream Paradigm)** kullanır ve kontrol mesajları metin tabanlıdır.
- Yalnızca düz metin (plain text) mesajları iletir.
- Mesaj sonunu `<CR><LF>.<CR><LF>` dizilimi ile belirler.
- Göndericinin alıcı adreslerini belirtmesine olanak tanır ve her bir adresi doğrular.
- Aynı bilgisayardaki birden fazla alıcıya tek bir mesaj kopyası göndererek ağ verimliliği sağlar.

---

<!-- _class: compact -->
# Örnek SMTP Oturumu (Example SMTP Session)

```text
S: 220 somewhere.com Simple Mail Transfer Service Ready
C: HELO example.edu
S: 250 OK
C: MAIL FROM:<John_Q_Smith@example.edu>
S: 250 OK
C: RCPT TO:<Mathew_Doe@somewhere.com>
S: 550 No such user here
C: RCPT TO:<Paul_Jones@somewhere.com>
S: 250 OK
C: DATA
S: 354 Start mail input; end with <CR><LF>.<CR><LF>
C: ... mesaj gövdesi iletiliyor ...
C: <CR><LF>.<CR><LF>
S: 250 OK
C: QUIT
S: 221 somewhere.com closing transmission channel
```

---

# Posta Erişim Protokolleri (Mail Access Protocols)

Kullanıcının uzaktaki sunucudaki posta kutusuna erişmesi için iki temel standart protokol bulunur:

- **POP3 (Post Office Protocol version 3)**:
  - Posta kutusundaki e-postaları kullanıcının yerel cihazına indirir.
  - İndirilen mesajlar varsayılan olarak sunucudan silinir.
- **IMAP (Internet Message Access Protocol)**:
  - E-postaları sunucuda saklar ve yönetir.
  - Başlıkları inceleme, klasör oluşturma ve mesajları birden fazla cihaz arasında senkronize etme imkanı sunar.

---

<!-- _class: compact -->
# RFC2822 Posta Mesaj Formatı

- E-posta mesaj yapısını tanımlayan standarttır.
- Mesaj bir metin dosyasından oluşur; başlık (header) ile gövde (body) **boş bir satır** ile ayrılır.
- Başlık satırları `AnahtarKelime: bilgi` biçimindedir.

**Tanımlı Standart Başlıklar:**
- `From:`, `To:`, `Subject:`, `Cc:`

**Genişletme Başlıkları (`X-` ile Başlayanlar):**
- Standardı bozmadan özel bilgiler eklemeye yarar (istemci/sunucu tarafından yok sayılabilir):
```text
X-Best-networking-Course: CS422 at Purdue
X-Spam-Check-Results: bulk spam 90% likely
X-Worst-TV-Shows: any reality show
```

---

# Çoklu Ortam E-Postası (Multimedia Email)

- **Gözlem**:
  - E-posta standartları bilgisayarların yalnızca metin tabanlı arayüzlere sahip olduğu dönemde geliştirilmiştir.
  - SMTP yalnızca düz metin (plain text) iletmeye elverişlidir.
  - Ancak kullanıcılar fotoğraf, tablo, özel yazı tipleri ve renkli içerikler göndermek istemektedir.
- **Soru**: SMTP ikili (binary) verileri aktarmak için kullanılabilir mi?
- **Yanıt**: **Evet**, ikili veriler düz metin karakter dizilerine kodlanarak (encoding) SMTP üzerinden iletilebilir.

---

# Metin Dışı E-Posta ve MIME Standartı

- **MIME (Multipurpose Internet Mail Extensions)**: İkili verileri ve çoklu ortam içeriklerini e-postaya eklemek için standarttır.
- RFC2822 ve SMTP ile tamamen geriye dönük uyumludur (backward compatible).

**Örnek MIME Başlıkları:**
```http
MIME-Version: 1.0
Content-Type: Multipart/Mixed; Boundary=xyz123

--xyz123
Content-Type: image/jpeg
Content-Transfer-Encoding: base64

... [Base64 kodlu resim verisi] ...
--xyz123--
```

---

# Dosya Aktarım Protokolü (FTP - File Transfer Protocol)

- İnternet üzerindeki dosya aktarımı için standart protokoldür.
- Çift bağlantı (two-connection) mimarisine sahiptir:
  - **Kontrol Bağlantısı (Control Connection)**: İstemci tarafından kurulur; komut ve yanıt iletimi için kullanılır.
  - **Veri Bağlantısı (Data Connection)**: Her bir dosya veya dizin aktarımı için sunucu tarafından oluşturulur ve aktarım bitince kapatılır.
- Ayrı bir veri bağlantısı kullanılması her türlü veri tipinin kesintisiz iletilmesini sağlar.

---

<!-- _class: compact -->
# FTP Etkileşim Akışı (Illustration Of FTP Communication)

- İstemci kontrol bağlantısı kurar (`Control Connection`)
- İstemci kontrol bağlantısı üzerinden dizin listesi isteği gönderir
- Sunucu bir veri bağlantısı oluşturur (`Data Connection`)
- Sunucu dizin listesini veri bağlantısı üzerinden gönderir ve veri bağlantısını kapatır
- İstemci kontrol bağlantısından dosya indirme isteği gönderir
- Sunucu yeni bir veri bağlantısı oluşturur ve dosyayı iletir
- Sunucu aktarım tamamlanınca veri bağlantısını kapatır
- İstemci `QUIT` komutu gönderir ve kontrol bağlantısını kapatır

---

# Uzaktan Erişim: TELNET ve SSH

- **TELNET**:
  - Komut satırı arayüzüne (CLI) sahip sistemlere uzaktan erişim sağlar.
  - Tüm iletişim ve şifreler **açık metin (cleartext)** olarak iletilir (güvensizdir).
- **SSH (Secure Shell)**:
  - TELNET'in güvenli alternatifidir. Tüm veri akışını ve kimlik doğrulamasını güçlü kriptografi ile şifreler.
- **Uzaktan Masaüstü (Remote Desktop)**:
  - Grafik Kullanıcı Arayüzüne (GUI) sahip sistemler içindir. İnce istemci (thin client) mimarisiyle yeniden yaygınlaşmıştır.

---

# Alan Adı Sistemi (DNS - Domain Name System)

- İnternet altyapısının en kritik uygulama katmanı servislerinden biridir.
- İnsanlar tarafından kolay hatırlanan isimleri (`www.cs.purdue.edu`), İnternet Protokolünün (IP) kullandığı ikili (binary) adreslere (`128.10.19.20`) dönüştürür.

```text
İnsan Tarafı Adı:  www.cs.purdue.edu
IP Adresi Karşılığı: 128.10.19.20
```

---

# DNS Terminolojisi ve Yapısı

- Alan adları hiyerarşiktir ve noktalarla (`.`) bölümlere ayrılır.
- En önemli bölüm en sağdakidir.
- En sağdaki bölüm **Üst Düzey Alan Adı (TLD - Top-Level Domain)** olarak adlandırılır.
- İstemci tarafında isim sorgulaması yapan yazılıma **Çözümleyici (Resolver)** adı verilir (web tarayıcısı ve e-posta istemcileri tarafından kullanılır).

---

# Üst Düzey Alan Adları (Top-Level Domains - TLD)

| Üst Düzey Alan Adı | Tahsis Edildiği Kuruluş / Amaç |
|---|---|
| **`com`** | Ticari kuruluşlar (Commercial organizations) |
| **`edu`** | Eğitim kurumları (Educational institutions) |
| **`gov`** | ABD Hükümeti (United States government) |
| **`org`** | Kar amacı gütmeyen kuruluşlar (Non-commercial) |
| **`net`** | Büyük ağ destek merkezleri (Network support) |
| **`mil`** | ABD Askeri kurumları (United States military) |
| **Ülke Kodları (`tr`, `de`, `uk`...)** | Egemen devletler (Sovereign nations) |

- ICANN 2014 yılında yüzlerce yeni TLD'ye izin vermiştir.

---

# Alan Adı Kaydı (Domain Registration)

- Kuruluşlar belirli bir TLD altında alan adı başvurusunda bulunur.
- Kendi iç hiyerarşisini belirleyebilir ve bilgisayarlarına isim atayabilir.
- **Coğrafi Kayıt**: `cnri.reston.va.us` biçiminde yapılabilir.
- **Ülke Sözleşmeleri**: İngiltere'deki üniversiteler `.ac.uk` altında kaydolur.

---

# En Çok Barındırıcıya Sahip Alan Adları (Domains With Most Hosts)

| Alan Adı | Açıklama | Alan Adı | Açıklama |
|---|---|---|---|
| **`net`** | Ağlar | **`de`** | Almanya |
| **`com`** | Ticari | **`tr`** | Türkiye |
| **`jp`** | Japonya | **`uk`** | Birleşik Krallık |
| **`edu`** | Eğitim | **`ca`** | Kanada |

---

# Barındırıcı Adları ve Sunulan Hizmetler

- Kuruluşlar genellikle bilgisayar adını sunduğu hizmetle eşleştirir:
  - `mail.foobar.com`
  - `ftp.foobar.com`
  - `www.foobar.com`
- İnsanlar için kolaylık sağlasa da, barındırıcı adı sunucuda hangi servislerin çalıştığını kısıtlamaz (örneğin `mail` isimli bir bilgisayar web sunucusu da çalıştırabilir).

---

# DNS Sunucuları Hiyerarşisi

![center height:260px](images/fig_166_dns_servers.png)

- Sunucu hiyerarşisi: **Kök Sunucular (Root)** $\rightarrow$ **TLD Sunucuları (`com`)** $\rightarrow$ **Yetkili Sunucular (`foobar.com`)**.

---

# Ad Çözümleme ve Önbellekleme (Name Resolution & Caching)

- **Çözümleyici (Resolver)**: Yerel DNS sunucusunun adresiyle yapılandırılır ve ilk sorguyu yerel sunucuya gönderir (Soket kütüphanesindeki karşılığı `gethostbyname`).
- **Önbellekleme (Caching)**:
  - Referans yerelliği (locality of reference) ilkesini izler.
  - Her DNS sunucusu elde ettiği yanıtları önbelleğe alır.
  - Süresi dolan (stale) önbellek kayıtları otomatik temizlenir.

---

<!-- _class: compact -->
# DNS Sunucu Algoritması (DNS Server Algorithm)

```c
/* Giren: DNS çözümleyiciden gelen sorgu mesajı (İsim N) */
/* Çıkan: N için IP adresini içeren yanıt mesajı */

if ( sunucu N için yetkili ise (authority) ) {
    Yetkili yanıt oluştur ve istemciye gönder;
} else if ( N yanıtı önbellekte (cache) mevcut ise ) {
    Yetkisiz (nonauthoritative) yanıt oluştur ve gönder;
} else { /* Yanıt başka bir sunucudan sorgulanmalı */
    if ( N için yetkili sunucu biliniyorsa ) {
        Sorguyu yetkili sunucuya gönder;
    } else {
        Sorguyu Kök (Root) sunucuya gönder;
    }
    Yanıtı al, önbelleğe kaydet ve istemciye ilet;
}
```

---

<!-- _class: lead -->
# Modül 2 Özeti (Summary)

- Tüm İnternet servisleri uygulama katmanı yazılımları tarafından sunulur.
- İletişim akış (stream) veya mesaj (message) paradigması ile gerçekleşir.
- Uygulamaların çoğu **İstemci-Sunucu (Client-Server)** yaklaşımını izler.
- **Soket API (Socket API)** fiili endüstri standardıdır.
- Uygulama protokolleri **Veri Temsili** ve **Veri Aktarımı** kurallarını tanımlar.
- İncelenen protokoller: Web (HTTP), E-Posta (SMTP/MIME), FTP, TELNET/SSH ve DNS.

---

<!-- _class: lead -->
# Sorular?
