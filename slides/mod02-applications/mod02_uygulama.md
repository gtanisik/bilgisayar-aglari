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

# Soket API (The Socket API)

- **Soket (Socket)**: Uygulama katmanı ile Taşıma katmanı (TCP/UDP) arasındaki fiili standart işletim sistemi arayüzüdür.
- 1983 yılında BSD Unix işletim sisteminde tanıtılmıştır (BSD Sockets API).
- Bir soket, uygulamanın ağa açılan kapısıdır ve işletim sistemi tarafından bir dosya tanımlayıcısı (file descriptor) gibi yönetilir.

---

# TCP İçin Standart Soket API Çağrıları

![center height:300px](images/fig_121_socket_calls.png)

- Sunucu Tarafı: `socket()` -> `bind()` -> `listen()` -> `accept()` -> `recv()`/`send()` -> `close()`
- İstemci Tarafı: `socket()` -> `connect()` -> `send()`/`recv()` -> `close()`

---

<!-- _class: lead -->
# Bölüm 2.4: Uygulama Katmanı Protokolleri

---

# Uygulama Katmanı Protokolü Nedir?

- İki uç uygulamanın birbiriyle nasıl mesajlaşacağını belirleyen kurallar bütünüdür.
- Şunları tanımlar:
  - Mesaj türleri (ör. İstek / Yanıt).
  - Mesajların sözdizimi (syntax) ve alan yapıları.
  - Alanların anlamı (semantics).
  - Yanıt verme ve iletişim kuralları.

---

# Uygulama Protokollerinde Durum (State)

- **Durumsuz Protokol (Stateless Protocol)**:
  - Sunucu istemciler hakkında geçmiş etkileşim bilgisini tutmaz (ör. HTTP/1.0). Her istek bağımsızdır. Tasarımı basittir, sunucu çökse bile kolay toparlanır.
- **Durumlu Protokol (Stateful Protocol)**:
  - Sunucu istemcinin oturum durumunu ve geçmişini hatırlar (ör. FTP). İletişim karmaşıklaşır ancak daha zengin etkileşim sağlar.

---

<!-- _class: lead -->
# Bölüm 2.5: Standart Uygulama Protokolü Örnekleri

---

# Web Teknolojileri ve HTTP

Web üç temel standart üzerine inşa edilmiştir:

1. **HTML (HyperText Markup Language)**: Belge içeriğini ve yapısını biçimlendirir.
2. **URL (Uniform Resource Locator)**: İnternet üzerindeki kaynağın adresini belirtir (`http://host:port/path`).
3. **HTTP (HyperText Transfer Protocol)**: İstemci (tarayıcı) ile sunucu arasındaki aktarım protokolüdür.

---

# HTTP İstek Türleri ve Yanıt Kodu Sınıfları

- **HTTP İstek Metotları**:
  - `GET`: Sunucudan kaynak ister.
  - `POST`: Sunucuya veri formları iletir.
  - `HEAD`: Yalnızca başlık bilgisini ister.
  - `PUT`: Sunucuya dosya yükler.
- **HTTP Durum Kodları**:
  - `200 OK`: Başarılı.
  - `301 Moved Permanently`: Kalıcı yönlendirme.
  - `404 Not Found`: Kaynak bulunamadı.
  - `500 Internal Server Error`: Sunucu içi hata.

---

# Orijinal vs Günümüz E-Posta Mimarisi

![center height:300px](images/fig_138_original_email.png)

- **Orijinal Model**: Gönderenin bilgisayarı doğrudan alıcının bilgisayarına bağlanıp e-postayı iletir (Alıcının bilgisayarı kapalıysa iletişim başarısız olur).

---

# Günümüz E-Posta Mimarisi

![center height:300px](images/fig_139_current_email.png)

- **Posta Sunucuları (Mail Servers / MTA)**: E-postalar sunucular arasında SMTP ile kesintisiz aktarılır ve alıcı kutusunda saklanır.
- **Posta Erişim Protokolleri**: Kullanıcı cihazından e-postalarını POP3 veya IMAP ile çeker.

---

<!-- _class: compact -->
# E-Posta Protokolleri ve Standartları

- **SMTP (Simple Mail Transfer Protocol - Port 25/587)**:
  - E-postaları iletmek için kullanılır (Push Protokolü).
- **POP3 (Post Office Protocol v3 - Port 110/995)**:
  - E-postaları sunucudan cihaza indirir, varsayılan olarak sunucudan siler.
- **IMAP (Internet Message Access Protocol - Port 143/993)**:
  - E-postaları sunucuda tutar, klasörleri cihazlar arasında senkronize eder.
- **RFC2822 & MIME (Multipurpose Internet Mail Extensions)**:
  - E-posta mesaj başlık formatı ve metin dışı (resim, ses, dosya) içeriklerin eklenmesini sağlayan standarttır.

---

# Dosya Aktarım Protokolü (FTP)

![center height:300px](images/fig_154_ftp_architecture.png)

- FTP çift bağlantı (two-connection) kullanır:
  - **Kontrol Bağlantısı (Port 21)**: Komutlar ve yanıtlar için (TCP).
  - **Veri Bağlantısı (Port 20)**: Dosya içeriğinin aktarımı için (TCP).

---

# Uzaktan Erişim Protokolleri (Telnet & SSH)

- **Telnet (Port 23)**:
  - Uzaktaki bir komut satırına erişim sağlar.
  - Güvensizdir; tüm kullanıcı adı, parola ve veriler açık metin (cleartext) olarak iletilir.
- **SSH (Secure Shell - Port 22)**:
  - Telnet'in güvenli alternatifidir.
  - Tüm iletişim ve kimlik doğrulama güçlü kriptografi ile şifrelenir.
  - Günümüzün standart uzaktan yönetim aracıdır.

---

# Alan Adı Sistemi (DNS - Domain Name System)

- İnsanlar isimleri hatırlar (`www.google.com`), bilgisayarlar IP adreslerini kullanır (`142.250.185.78`).
- **DNS**: İsimler ile IP adresleri arasında dönüşüm yapan dağıtık (distributed) bir veritabanı sistemidir. UDP ve TCP Port `53` üzerinde çalışır.

---

# Hiyerarşik İsim Alanı ve Kök Sunucular

![center height:300px](images/fig_166_dns_servers.png)

- **Kök Sunucular (Root Servers)**: Hiyerarşinin en tepesindedir (Dünyada 13 kök IP adresi).
- **Üst Düzey Alan Adı Sunucuları (TLD Servers)**: `.com`, `.org`, `.net`, `.tr` gibi uzantıları yönetir.
- **Yetkili Sunucular (Authoritative Servers)**: Kurumların kendi domain kayıtlarını tutar.

---

# DNS Adres Çözümleme ve Önbellekleme

![center height:300px](images/fig_167_dns_resolution.png)

1. İstemci yerel DNS sunucusuna (Local DNS) başvurur.
2. Yerel DNS sırasıyla Kök -> TLD -> Yetkili sunucuya sorgu gönderir.
3. Sonuç yerel DNS'te önbelleğe (cache) alınır ve istemciye döndürülür.

---

<!-- _class: lead -->
# Bölüm 2.6: Özet

---

# Modül 2 Özeti

- Uygulama katmanı İnternet mimarisinin en üst katmanıdır ve zeka ağın uçlarındadır.
- **Akış (TCP)** ve **Mesaj (UDP)** olmak üzere iki temel iletişim modeli vardır.
- **Soket API**, uygulamaların TCP/IP protokol yığınına erişmesini sağlar.
- Web uygulamaları **HTTP**, **HTML** ve **URL** üzerine kuruludur.
- E-Posta **SMTP**, **POP3/IMAP** ve **MIME** standartlarını kullanır.
- **FTP** kontrol ve veri kanallarını birbirinden ayırır.
- **DNS**, İnternet üzerindeki isim-IP dönüşümünü sağlayan dağıtık bir sistemdir.
