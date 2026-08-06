---
marp: true
theme: custom-theme
paginate: true
header: 'Bilgisayar Ağları ve İnternet | Modül 6: Diğer Konular'
footer: 'Adapted from D. E. Comer (Prentice-Hall)'
---

<!-- _class: lead -->
# Modül 6: Ağ Güvenliği, Yönetim ve Diğer Konular

**Prof. Douglas E. Comer** ders materyalinden uyarlanmıştır.


---

## MODÜL VI

Diğer Konular


---

## Konular

- Ağ performansının ölçülmesi
- Hizmet Kalitesi (QoS) ve provizyon
- Multimedya ve IP telefonu
- Ağ güvenliği
- Trafik mühendisliği ve MPLS
- Ağ yönetimi (SNMP)


---

## Ölçme

Ağ Performansı


---

## Ağ Performansını Neden Ölçmeliyiz?

- Optimizasyon
- Planlama (gelecekteki ihtiyaçları öngörmek)
- Trafiği değerlendirme ve anlama
  - Uygulamalardaki ve ağ kullanımındaki eğilimler
  - Anormal trafik düzenlerini tespit etme
- Sözleşmenin (SLA) uygulanması
- Övünme hakları
  - Bir kuruluştaki BT personeli
  - Bir ekipman satıcısında pazarlama departmanı


---

## Niteliksel Terminoloji ve Pazarlama

- Pazarlama niteliksel terimleri seviyor gibi görünüyor
  - Yüksek hızlı
  - Hızlı
  - Güçlü
  - Yüksek bant genişliği (bandwidth)
- Ne yazık ki
  - Niteliksel terminoloji belirsizdir
  - Ağ teknolojileri hızla değişiyor


---

## Solmuş Nitel Terminoloji

- Yüksek hızlı kiralık hat
  - Bir zamanlar 9,6 Kbps'de çalışacak şekilde tanımlanmıştı
- İnternetin Çok Yüksek Hızlı Omurga Ağ Sistemi
(VBNS)
  - Artık pek dikkate alınmayan kullanılmış OC-12 bağlantıları
yüksek hız
- Hızlı Ethernet
  - 100 Mbps'de çalışır ve yalnızca onda biri kadar hızlıdır
Gigabit Ethernet teknolojisi
- Geniş bant
  - Bir zamanlar FCC tarafından 128 Kbps'den başlayacak şekilde tanımlanmıştı


---

## Nicel Ölçüler

- Ölçülebilir ölçüm şaşırtıcı derecede zordur
- Rotalar ve veri hızları asimetrik olabilir, bu da
bir yöndeki ölçümler, bir yöndeki ölçümlerden farklıdır
diğeri
- Ölçüm problarının takılması performansı etkileyebilir
ölçülen sistem
- Koşullar hızla değişebilir


---

## Toplu Trafik Analizi

- Kısa vadeli değişim
  - Paketler patlama adı verilen kümeler halinde ulaşma eğilimindedir
- Uzun vadeli değişim
  - Günlük ve yıllık modeller mevcuttur
- İlginçtir ki veri trafiği ses trafiğine benzemez
  - Sesli telefon aramalarının toplamı düzgün bir ortalamadır
  - Veri trafiğinin toplamı patlamalı


---

## Kendine Benzerlik

Sesli telefon trafiğinin aksine veri trafiği yoğundur. Veri
veri kümeleri nedeniyle trafiğin kendine benzer olduğu söylenir
trafik istatistiksel olarak benzer bir patlama modeli sergiliyor
tek bir bağlantıdaki patlamaya.
Önemli olan nokta: veri trafiğini analiz etmek kolay değil


---

## Ağ Performansının Pratik Ölçüleri

- Üç temel niceliksel ölçü
Ölçü
Açıklama
1 Bir biti 1'e aktarmak için gereken süre
gecikme (delay/latency) (gecikme (delay/latency))
bir
ağ
itibaren
bir
son
için
başka biri
1 Verim (kapasite) 1 Aktarılabilecek veri miktarı 1
Bir ağ üzerinden birim zamanda 1
Titreşim
(değişkenlik)

değişiklikler
içinde
gecikme (delay/latency)
bu
meydana gelmek
ve
the
1 değişiklik süresi
- Üçünün tamamen bağımsız olmadığını göreceğiz


---

## Gecikme veya Gecikme

- Verilerin bir ağ üzerinden "geçmesi" için gereken süre
- Gecikmeyi tek bir bitin çalışması için gereken süre olarak düşünün.
bir ağdan geçmek
- bağlıdır
  - Evrenin fiziksel özellikleri (ışık hızı)
  - Ağdaki trafik


---

## Gecikme Süresi ve Algılanan Yanıt Süresi

- Kullanıcılar yanıt süresiyle ilgileniyor
- Gecikmenin çeşitli bileşenleri genel müdahaleye katkıda bulunur
kullanıcının algıladığı zaman
Tür
Açıklama
21 222222222222222222222222222222222222222222222222222222222222222
1 Erişim Gecikmesi
1 Bir erişim elde etmek için gereken süre
1 iletim ortamı (örneğin bir kablo)
Yayılma
gecikme (delay/latency)

zaman
gerekli
için
bir
sinyal
için
seyahat
karşısında
bir
iletim
orta
1 Anahtarlama Gecikmesi
1 Bir paketi iletmek için gereken süre
21 222222222222222222222222222222222222222222222222222222222222222
1 Kuyruk Gecikmesi
1 Bir paketin 1 paketin hafızasında geçirdiği süre
1 anahtar veya yönlendirici (router) seçilmeyi bekliyor
iletim
1 Sunucu Gecikmesi
1 Sunucunun bir soruya yanıt vermesi için gereken süre 1
1 istek ve bir yanıt gönderin


---

## Darboğazlar

- İletişim sisteminin herhangi bir parçası darboğaz olabilir
en fazla gecikmeye neden olan
- Örnekler
  - Erişim gecikmesi: kablosuz bir kanal edinme
  - Yayılma gecikmesi: bir uydu iletimi
  - Anahtarlama gecikmesi: derin paket incelemesi
  - Sunucu gecikmesi: Bir haber ajansının web sitesi sırasında aşırı yükleme
bir kriz
  - Kuyruk gecikmesi: Paketlerin yola çıktıklarından daha hızlı ulaşması


---

## Gecikmenin Değerlendirilmesi

- Bir aralıkta birden fazla ölçüm yapın
- Minimum, maksimum, ortalama ve standart sapmayı raporlayın
- Mümkünse gecikmeyi kurucu bileşenlere bölün
- Tekrarlanan kalıpları aramak için küçük aralıkları seçin


---

## Verim

- Bir ağın birim başına taşıyabileceği maksimum veri miktarı
zaman
- Saniye başına bit cinsinden veri hızı olarak ifade edilir (ör. 100 megabit)
saniyede)
- Yanlışlıkla ağ "hızı" olarak anılıyor, ancak aslında bir ölçü
ağ kapasitesi
- Performansa ilişkin bir üst sınır verir, garanti vermez


---

## Verimin Değerlendirilmesi

- Çeşitli olası önlemler
  - Tek bir iletişim kanalının kapasitesi
  - Ağ boyunca bir yol boyunca kapasite
  - Tüm kanalların toplam kapasitesi
  - Giriş ve çıkış noktası çiftleri arasındaki kapasite
aynı anda kullanılan


---

## Goodput Kavramı

- Ağın anlamlı değerlendirmesini sağlamak için icat edildi
performans
- Bir başvurunun alındığı efektif oran olarak tanımlanır
veri
- Aşağıdaki nedenlerden herhangi biri nedeniyle verimden farklı olabilir
  - Uygulama protokolü ek yükü
  - Kanal kodlama ek yükü
  - Paket başlığı ek yükü
  - Alıcı arabellek sınırlamaları
  - Tıkanıklığı önleme mekanizmaları
  - Paket yeniden iletimi


---

## İyi Verimin Değerlendirilmesi

- Başarılı bir şekilde gelen verileri ölçün ve hesaplayın
birim zaman başına düşen veri miktarı
- İyi çıktı ölçümleri aynı zamanda ortaya çıkan genel giderleri de içerir
tarafından
  - İşletim sistemi
  - Taşıma protokolü
  - Alt katman kodlamaları ve protokolleri
  - Uygulama protokolü ve uygulaması
- Not: Her ne kadar verim terimini kullansalar da çoğu
ölçüm araçları iyi girdi raporu


---

## Titreşim

- Ağ performansının bir diğer önemli ölçüsü
- Ses akışının iletiminde özellikle önemlidir ve
video
- Gecikmedeki değişimi ölçer
- Örnek
  - Ağın ortalama gecikme (delay/latency) D'ye sahip olduğunu varsayalım
  - Eğer her paketin geçmesi tam olarak D zaman birimini alıyorsa
ağ, titreşim sıfır
  - Paketler D+ε ve D – ε gecikmeleri arasında değişiyorsa,
ortalama gecikme (delay/latency) D olarak kalır ancak titreşim artar


---

## Temel Gözlem

İnternetteki tıkanıklık (congestion) en önemli sorundur
paket kaybının, yüksek titreşimin ve uzun gecikmelerin nedenidir.


---

## Jitter'ı Yönetme

- İnterneti eş zamanlı bir ağla değiştirin
  - Orijinal telefon ağında kullanılan yaklaşım
  - Tüm paralel yollar tam olarak aynı gecikmeye sahiptir
- Kapasiteyi ayırmak için İnternet'i değiştirin
  - Modülün ilerleyen kısımlarında tartışılacaktır
- Mevcut İnternet tasarımını koruyun ve aşağıdaki protokolleri ekleyin
titreşimi telafi etmek
  - Temel teknik titreşim tamponudur
  - Modülün ilerleyen kısımlarında tartışılacaktır


---

## Verim ve Gecikmeyi Anlamak

(devam)
- Analoji ağ ölçümlerini anlamamıza yardımcı olur
Yayılma gecikmesi, tek bir bitin içinde kaldığı süreyi belirtir
bir ağda geçiş. Verim (kaç tane olduğunu belirtir)
bitler birim zamanda ağa girebilir, ağı ölçer
kapasite.
- Temel sonuç bir aforizmaya dahil edilmiştir
Her zaman daha fazla verim satın alabilirsiniz, ancak satın alamazsınız
daha düşük gecikme (delay/latency).


---

## Gecikme Verimliliği Ürünü

- "Hareket halindeki" maksimum veri miktarını belirtir
Bir ağda bulunan bitler = D × T
nerede
  - D saniye cinsinden ölçülen gecikmedir
  - T, saniye başına bit cinsinden ölçülen verimdir
- İlkinden önce kaç bitin iletilebileceğini belirtir
bit alıcıya ulaşır
- gecikme (delay/latency) bant genişliği (bandwidth) ürününün sıklıkla yanlış etiketlenmesi


---

## Gecikme Verimi Terminolojisi ve Örnekler

- Ethernet
  - Verimi yüksek olmasına rağmen gecikme (delay/latency) limitleri kısadır
gecikme (delay/latency)-geçiş ürünü
- Uydu bağlantısı
  *Genellikle yüksek gecikmeli bir ürüne sahiptir çünkü
gecikme (delay/latency) uzun ve verim yüksek
- Gayri resmi olarak bir benzetme kullanıyoruz
  - Uzun gecikmeli bir ağa uzun boru denir
  - Yüksek verimliliğe sahip bir ağa yağ borusu denir
  - Uydu, uzun, kalın bir boru olarak bilinir


---

## Gecikme, Verim,

ve Kullanım


---

## Gecikme ve Verim Arasındaki İlişki

- Teorik olarak gecikme (delay/latency) ve verim bağımsızdır
- Uygulamada birbirleriyle ilişkilidirler
- Sebep
  - Verim, trafiğin geçebileceği hızı belirler
bir iletişim bağlantısı üzerinden
  - Bir anahtar veya yönlendirici (router), paketleri gönderilinceye kadar sıraya koyar
  - Veri bir anahtara veya yönlendiriciye ayrıldığından daha hızlı ulaşıyorsa,
kuyruk uzunluğu artar, bu da gecikmenin artması anlamına gelir
(tıkanıklık (congestion))


---

## Tıkanıklığın Nasıl Oluştuğunu Gösteren Resim

- Üç adet 1 Gbps bağlantıya sahip bir yönlendirici (router) düşünün ve
trafiğin iki bağlantı üzerinden geldiğini varsayalım
üçüncü için
giriş 1 (1 Gbps)
yönlendirici (router)
çıkış (1 Gb/sn)
giriş 2 (1 Gb/sn)
- Kırmızı bağlantının kapasitesi iki katına çıkarıldığında tüm bağlantılar kullanılabilir.
daha fazla tıkanıklık (congestion) yaşarsınız, bu da gecikmeyi artırır


---

## Kullanım

- Bir ağ bağlantısındaki mevcut yükün ölçümü
- Kullanılan kapasitenin yüzdesi olarak verilir ve ifade edilir
0,0 ile 1,0 arasında gerçek bir değer olarak
- Örnek: 1 Gbps kapasiteli bir bağlantının trafiği 500 ise
Mbps, bağlantı kullanımı 0,5
- Kullanım zamanla değiştiği için belirli bir süre boyunca raporlanır.
vererek aralık
  - Tepe (yani maksimum)
  - Ortalama (yani ortalama)


---

## Gecikme Tahmini Olarak Kullanım

- Paket trafiği patlamalı
- Anahtar keşif: etkin kuyruk gecikmesi tahmin edilebilir
kullanımdan şu şekilde:
D0
D =
(1 - U)
- Nerede
  - D 0 ağ boştayken gecikmedir
  - U, 0 ile 1 arasındaki mevcut kullanımdır


---

## Kullanımın Bir Fonksiyonu Olarak Gecikme

akraba
gecikme (delay/latency)
rölanti gecikmesi
%25
%50
%75
%100
kullanım

> 📷 *[Görsel: Diyagram/Grafik — yakında eklenecek]*


---

## Kullanımın Pratik Yorumu

- Kullanım arttıkça gecikme (delay/latency) hızla artar
- Kullanım %50'ye ulaştığında gecikme (delay/latency) iki katına çıkar
- Kullanım %80'e ulaştığında gecikme (delay/latency) beş kat artar
ortalamadan


---

## 50-80 Kuralı

- Sezgisel yöneticiler takip eder
  - Kullanım %50'ye ulaştığında yükseltme planlayın
  - Kullanım %80'e ulaştığında yükseltmenin zamanı geçmiş demektir
- Not: alternatif bir ağın bölümlendirilmesinden oluşur (örn.
VLAN'ları ayırma)


---

## Hat Hızı ve Saniyedeki Paket Sayısı

- Ağ ekipmanının hat hızında çalıştığı söylenir
ekipman bir dizi arka arkaya paketi işleyebilir
- Gözlemle
  - Paket başına ek yük genellikle ekipmandaki darboğazdır
  - Belirli bir veri hızı için ekipman süreçleri
*
Paketler büyükse saniyede daha az paket
*
Paketler küçükse saniyede daha fazla paket
- Sonuç: Hat hızı,
paket boyutunun belirtilmesi


---

## Hizmet Kalitesi (QoS)

- Hizmet sağlamak için kullanılabilecek teknolojiler seti
garantiler
  - Gecikmeye bağlı
  - Verim garantisi
  - Titreşime bağlı
- Pazarlama
  - QoS ile “kaliteyi” eşitlemeye çalışır
  - QoS eksikliğinin kalite eksikliği anlamına geldiğini ima eder


---

## İnternette QoS

- Motivasyon
  - Akış gibi uygulamaları çalıştırmayı mümkün kılın
kesintisiz video
  - Servis sağlayıcıların (çok) daha fazla ücret almasına izin verin
daha iyi hizmet
- Üç yaklaşım önerildi ve incelendi
  - Öncelik
  - İnce taneli QoS
  - İri taneli QoS


---

## Öncelikli Yaklaşım

- Her pakete bir öncelik atanır ve çoğullama seçilir
öncelik sırasına göre paketler
- İSS'ler arasında popülerdir ve bazı şirketler tarafından
ses ve video trafiği önceliği
- Avantajlar
  - Uygulaması kolay
  - Bir müşteri yerine bir “müşteriye” öncelik atayabilir
belirli veri türü
- Dezavantajları
  - Kantitatif garanti yok
  - Açlığa yol açabilir


---

## İnce Taneli QoS Yaklaşımı

- IETF tarafından Entegre Hizmetler adı altında takip edilmektedir
(IntServ) ve ATM ağlarında benimsenmiştir
- Her akış için görüşülen QoS parametreleri (örneğin, her TCP
bağlantı)
  - Maksimum gecikme (delay/latency)
  - Minimum verim
  - Maksimum titreşim
- Uygulanması zor/imkansız
Uzun yıllar süren araştırma ve standart çalışmalarından sonra, QoS'ye yönelik ince taneli yaklaşım birkaç özel alana havale edildi.
vakalar.


---

## Hayatta Kalan QoS Terminolojisi

- ATM'den türetilmiştir
1 Kısaltma 1
Genişleme
Anlamı
21 222222222222222222222222222222222222222222222222222222222222222222222
1 Veri akışa sabit bir hızla girer, 1
1 dijitalleştirilmiş bir sesten alınan veriler gibi 1
CBR
Sabit Bit Hızı
çağrı
girme
en
kesinlikle
Kbps
1 Veri akışa bir değişkenle giriyor
1 Değişken Bit Hızı
Belirtilen istatistik dahilinde 1 oran
VBR
1 sınır

akış
katılıyorum
için
kullanmak
her neyse
ABR
Mevcut
Bit
Oran
veri
oran
öyle
mevcut
en
bir
verildi
1 kez
21 222222222222222222222222222222222222222222222222222222222222222222222
1 Akış için herhangi bir bit hızı belirtilmemiştir; 1
UBR
belirtilmemiş
Bit
Oran
the
uygulama
öyle
memnun
ile
en iyi çabayı gösteren hizmet
- İstatistiksel olarak belirlenen sınırlar (örn. ortalama ve zirve)
verim ve patlama boyutu)


---

## İri taneli QoS Yaklaşımı

- IETF adı altında onaylanan güncel yaklaşım
Farklılaştırılmış Hizmetler (DiffServ)
- Trafiği sınıflara ayırır
- Akış başına değil, her sınıf için garantili hizmet
- Uygulaması ince taneli yaklaşıma göre daha kolaydır
- Genellikle orantılı bir garanti olarak uygulanır.
mutlak miktarlar
- Örnek politika
Temel ağın en az %10'u
kapasite ses trafiği için ayrılmıştır


---

## Bir Yönlendiricinin QoS'yi Uygulamak İçin Attığı Adımlar

paketler
varmak
paketler
ayrılmak
QoS uygulayan yönlendirici (router)
sınıflandırma
ve Polislik
Yönlendirme
hesaplama
Çıkış
Sıraya girme
Trafik
Planlama
- Polis gelen trafiğe kuralları uygular
- Yönlendirme birden fazla yol arasından seçim yapabilir (yönlendirici (router)
çok sayıda çıktı kuyruğu var)
- Sıralamada Rastgele Erken Atma (KIRMIZI) kullanılabilir


---

## Trafik Planlama

- Kuyruklardan paketleri seçmek için kullanılan algoritma
- Başlıca türleri
1 Algoritma
Açıklama
21 222222222222222222222222222222222222222222222222222222222222222222
1 Sızdıran Kova 1 Bir kuyruğun paketleri sabit bir hızda göndermesine izin verir.
1 paket sayacını periyodik olarak artırmak ve kullanmak
the
sayaç
için
kontrol
iletim
1 Token Kovası 1 Bir kuyruğun sabit bir hızda veri göndermesine izin verir.
1 bayt sayacını periyodik olarak artırmak ve 1'i kullanmak
İletimi kontrol etmek için 1 sayaç
Ağırlıklı
Seçer
paketler
itibaren
bir
ayarlamak
arasında
kuyruklar
göre
için
bir
Yuvarlak
Robin
ayarlamak
arasında
ağırlıklar
bu
bölmek
the
kapasite
içine
sabit
Tek tip paket boyutu varsayılarak yüzde 1
21 222222222222222222222222222222222222222222222222222222222222222222
1 Round-robin yaklaşımının 1'i hesaba katan bir çeşidi
Açık
1 Round Robin Aktarılan paketler yerine 1 bayt gönderilir ve 1 bayt gönderilir
büyük bir paketin neden olduğu geçici açık


---

## Trafik Mühendisliği

- Bir yöneticinin şunları yapmasına olanak tanıyan bir ağ oluşturma yaklaşımı
bir ağ üzerinden rotaları oluşturup kontrol edin ve atayın
her birine belirli veri türleri
- ima ediyor
  - Standart dışı yönlendirme mekanizması
  - Belirli bir yol boyunca gönderilen belirli bir türdeki tüm trafik
- En popüler teknoloji: MPLS


---

## Çoklu Protokol Etiket Değiştirme (MPLS)

- Seviye 1 ISP'ler arasında yaygın olarak dağıtılır
- Katılımcı yönlendiricilerin MPLS modülüne sahip olmasını gerektirir
- Yönlendiricilerin bir yol boyunca yapılandırılmasıyla oluşturulan MPLS tüneli
- yönlendirici (router), yöneticinin bağlantının bir kısmını atamasına izin verebilir
Her tünelin kapasitesi
  - Çoklu protokol terimi ortaya çıkar çünkü bir MPLS paketi
keyfi içerik barındırıyor


---

## Etiket Yeniden Yazma

- Konsept ATM'den geldi ve MPLS'de kullanıldı
- Yoldaki her bağlantının farklı tam sayı etiketi vardır
- yönlendirici (router), iletmeden önce MPLS veri birimindeki etiketi yeniden yazar
sonraki atlamaya
- Etiket değiştirme olarak bilinir
- Motivasyon: küresel koordinasyondan kaçının ve yerele izin verin
etiketlerin atanması
- Dezavantajları:
  - MPLS'yi yapılandırmak için genel bir protokol mevcut değildir
yol
  - Hata ayıklamak zor olabilir


---

## MPLS Nasıl Çalışır?

- yönlendirici (router) tarafından MPLS başlığında kapsüllenen datagram
bir tünelin başlangıcı
- Üzerinde çalışılacağı yolun etiketiyle etiketlenmiş MPLS datagramı
geçmeli
- Yol boyunca her yönlendirici (router)
  - Yönlendirme kararı vermek için etiketi kullanır
  - Etiketi bir sonraki atlamada kullanılan değerle değiştirir
- Datagram sona ulaştığında MPLS kapsülleme kaldırıldı
tünelin


---

## Etiket Yeniden Yazma İllüstrasyonu

bir
H1
R4
Ç
Ç
B
bir
bir
H2
etiket 4'e gönder
B
bir
R1
32 B
B
bir
R2
B
Ç
bir
gelen
etiket 3
R3
32 12 B
- Yol üzerindeki etiketler şunlardır: 4, 32, 12, 3


---

## Multimedya




---

## Birkaç Tanım

(devam)
- Oynatma, belirli bir süre için gerçek zamanlı bilgilerin çıktısını ifade eder.
kullanıcı (örn. video ekranı veya ses çıkışı)
- Örnekleme hızı, gerçek zamanlı bilgilerin alınma hızını ifade eder.
dijital forma dönüştürülmüştür (örneğin ses örneklenmiş 8000)
saniyede kez)
- Senkronizasyon, oynatmanın koordinasyonunu ifade eder
birden fazla kaynaktan gelen bilgiler (örneğin bir film gerektirir)
ses ve video arasındaki senkronizasyon)


---

## Gerçek Zamanlı Örnek Oranları

- Her gerçek zamanlı veri kaynağı bir örnekleme hızı seçebilir ve
kodlama
- Örnekler
  - Bir video akışı saniyede 30 kare içerebilir,
sıkıştırmayı kullanan bir kodlamayla
  - Bir ses akışı başına 8000 ses örneği içerebilir
PCM kodlamasını kullanarak ikinci
- Önemli kavram
Çünkü her gerçek zamanlı bilgi kaynağı bir seçim yapabilir.
örnekleme hızı, oynatma ve senkronizasyonun bilinmesi gerekir
örnekleme hızı ve seçilen kodlama.


---

## Akışlı Gerçek Zamanlı Verilerin Aktarımı

- Kaynak
  - Düzenli aralıklarla bilgi örnekleri
  - Sürekli veri üretir
  - Verileri iletime hazırlar
- İdeal iletim kanalı
  - Kaynağın ürettiği oranda girişi kabul eder
  - Çıktıyı girdiyle aynı oranda sağlar


---

## Kantitatif Ağ Performansı

Gerçek Zamanlı Akış İçin Gerekli
- QoS türü: Sabit Bit Hızı (CBR)
- Gönderenin veri hızına uyum sağlamaya yeterli verim
(önceden bilinir)
- Belirli bir sınır dahilinde gecikme (delay/latency), genellikle 200 msn
- Sıfır veya sıfıra yakın titreşim


---

## Tamponlama

- Paket iletim sisteminde özellikle önemlidir
- Birden fazla örneği tek bir iletimde birleştirir
- Avantaj
  - İletim verimliliğini artırır
- Dezavantaj
  - Gecikmeyi tanıtır


---

## Tamponlama Örneği

- PCM sesini düşünün
- Her 125 µsaniyede bir alınan sekiz bitlik bir ses örneği
- Ethernet'in 1500 oktetlik yükü vardır
- Çerçevenin tamamını doldurmayı beklemek zaman alıyor
125 × 10−6 saniye/bayt × 1500 bayt = 0,188 saniye
- Bir paketin doldurulması kaynakta gecikmeye neden olur


---

## Arabelleğe Alma Uzlaşması

- Uygulamaya göre tampon boyutunu seçin
- Örnek: her pakette 128 ses örneği gönderin
- Takaslar
  - Paket boyutu paket başına bir örnekten daha büyüktür, ancak
kesinlikle gerekenden daha fazla paket üretir
  - Başlık ek yükü, toplam bitlerin daha küçük bir yüzdesidir
paket başına bir numuneden daha fazla, ancak daha büyük
daha büyük paketlere göre yüzde
  - gecikme (delay/latency), paket başına çok sayıda örnek kullanılmasından daha iyidir, ancak
paket başına bir numune kadar iyi değil


---

## Titreşim Tamponları




---

## Gerçek Zamanlı Veri Akışı

İnternet genelinde
- Üstesinden gelmeli
  - Kayıp paketler
  - Çoğaltılmış paketler
  - Paketler sipariş dışı teslim edildi
  - Gecikmedeki sapma (jitter)
- Temel gerçekler
  - Geleneksel yeniden iletim işe yaramaz
  - Titreme kaçınılmazdır


---

## İki Faydalı Teknik

- Zaman damgaları
  - Gönderen tarafından sağlanmıştır
  - Her veri parçasına atanır
  - Alıcının verinin ne zaman oynatılması gerektiğini bilmesine izin ver
  - Saat ihtiyacını ortadan kaldırmak için göreceli değerleri kullanın
senkronizasyon
- Titreşim tamponu
  - Alıcı tarafından kullanılır
  - Gecikmedeki küçük farklılıklara uyum sağlar


---

## Titreşim Arabelleği

- Alıcı tarafından gelen gerçek zamanlı verileri birleştirmek için kullanılır
- Bir öğenin üzerindeki zaman damgası, öğenin nereye yerleştirileceğini belirler
oynatma sırası
- Genel prensip: bilgilerin mevcut olmasını sağlayın
gecikmeden oynama zamanı
- İpucu: d'nin maksimum titreşimini telafi etmek için gecikme (delay/latency)
- zaman birimleri için oynatma
- Sonuç: titreşim arabelleği, oynatmanın yapılabilmesi için yeterli veriyi tutar
kesintisiz devam et


---

## Bir Jitter Arabelleğinin Çizimi

paketler geliyor
patlamalar halinde
çıkarılan paketler
tekdüze bir oranda
titreşim tamponu
oynatma
süreç
- ekran
bağlantı
internete
- Normal çalışma sırasında oynatma d süresi boyunca devam edebilir
Geciken paketleri beklerken birimler


---

## Gerçek Zamanlı Aktarım Protokolü (RTP)

- Ses ve video için yaygın olarak kullanılır
- İsmine rağmen aslında bir aktarım protokolü değil
- Titreşim tamponu içermez ve kontrol etmez
oynatma
- Üç temel mekanizma sağlar
  - Her paket üzerinde alıcıya izin veren sıra numarası
kayıp ve sipariş dışı teslimatla başa çıkmak
  - Verilerin oynatılması için kullanılan zaman damgası
  - Alıcıya durumu bildiren kaynak tanımlayıcılar dizisi
Verilerin kaynağı/kaynağı


---

## RTP Ayrıntıları

- Gönderenin ve alıcının örnekleme hızını seçmesine olanak tanır ve
kodlama
- Aktarılan her mesaj için bir başlık belirtir
- Taşıma için UDP'yi kullanır
- Zaman damgasını paket sıra numarasından ayırır
- Bazı çerçevelerin işaretlenmesine olanak tanıyan bir işaretleyici bit içerir
- Tamamlayıcı protokol, alıcıların göndericiyi
aktarma


---

## RTP Tasarımı İçin Motivasyon

- İşaretleme
  - Tam çerçeve takip edilerek diferansiyel kodlamaya izin verir
artan değişikliklerle
  - Örnek kullanım: video I-frame ve ardından B-frame'ler
- Zaman damgası ve paket sırasının ayrılması
  - Zaman damgalarının doğrusal olarak ilişkili olması gerekmediği anlamına gelir
paketler
  - Hızı değiştiren sıkıştırma şemalarına izin verir
veri gönderildi


---

## RTP Başlık Formatı

VER
P
X
CC
M
ÖDEME TÜRÜ
SIRA NUMARASI
ZAMAN DAMGASI
SENKRONİZASYON KAYNAĞI TANIMLAYICI
KATKIDA BULUNAN KAYNAK TANIMLAYICI
...
- TIMESTAMP gönderen ve alıcı tarafından yorumlanır
- PAYTYPE, yük türünü belirtir
- Rastgele seçilen ilk SIRA NUMARASI
- KATKIDA BULUNAN KAYNAK TANIMLAYICILARI gönderenin şunları yapmasına olanak tanır:
birden fazla kaynaktan gelen akışları karıştırın


---

## RTP Kapsülleme

- Üç seviyeli kapsülleme
RTP HDR
RTP Yükü
UDP HDR
UDP Yükü
IP Başlığı
IP Yükü
Çerçeve Başlığı
Çerçeve Yükü
- UDP kullanımı, yerine tek bir çoklu yayın gönderilmesine izin verir
çoklu tek noktaya yayın kopyaları


---

## IP Telefon (VoIP)




---

## IP Telefon

- IP Üzerinden Ses (VoIP) olarak bilinir
- İki grup standartlar oluşturdu
  - Uluslararası Telekomünikasyon Birliği (ITU)
  - İnternet Mühendisliği Görev Gücü (IETF)
- Standartlar iki temel noktada hemfikirdir
  - Darbe Kodu Modülasyonu (PCM) kullanılarak kodlanmış ses
  - Dijitalleştirilmiş sesi aktarmak için kullanılan RTP
- Standartlar aynı fikirde değil
  - Sinyal verme
  - Kamu Anahtarlamalı Telefon Ağı (PSTN) etkileşimi


---

## Sinyalizasyon

- Telco'nun kurulması ve sona erdirilmesi süreci için kullanılan terim
çağrı
- İçerir
  - Bir telefon numarasını bir konumla eşleme
  - Aranan tarafa rota bulma
  - Muhasebe ve faturalandırma için kullanılan bilgilerin kaydedilmesi
  - Çağrı yönlendirme gibi işlevlerin kullanılması
- Geleneksel için standart çağrı yönetimi olanağı
telefon sistemi Sinyal Sistemi 7 (SS7) olarak bilinir


---

## IETF Yaklaşımı

- Oturum Başlatma Protokolü (SIP) olarak bilinir
- Bir telefon numarasını eşlemek için kullanılan Alan Adı Sistemi
bir IP adresi
- SIP sinyalizasyon sistemi
  - Kullanıcı aracısı arama yapar veya sonlandırır (örn. IP telefonu)
  - Konum sunucusu, kullanıcılardan ve hizmetlerden oluşan bir veritabanına danışır.
abone oldukları yerler ve tercihler
  - Proxy sunucusu istekleri iletir ve yönlendirmeyi optimize eder
  - Yönlendirme sunucusu çağrı yönlendirme gibi görevleri yerine getirir
ve 800 numaralı bağlantılar
  - Kayıt şirketi sunucusu kullanıcıların hizmete kaydolmasına olanak tanır


---

## İTÜ Yaklaşımı

- Standart H.323'tür
- SIP tarafından kullanılan terminolojiden önemli ölçüde farklıdır
- Terminal IP telefon işlevlerini sağlar ve ayrıca
video ve veri iletimi için olanaklar içerir
- Gatekeeper konum ve sinyal verme işlevlerini sağlar ve
PSTN'ye bağlantılar kurar
- Ağ geçidi, IP telefon sistemi ile PSTN'yi birbirine bağlar ve
hem sinyallemeyi hem de medya çevirisini yönetir
- Çok Noktalı Kontrol Ünitesi (MCU) aşağıdaki hizmetleri sağlar:
çok noktalı konferans


---

## Uluslararası Softswitch Konsorsiyumu (ISC)

- Terminolojiyi birleştirmek için satıcılar tarafından oluşturulmuştur
birden fazla standart ve tek bir kavramsal model oluşturun
- Açıklamaya yeterli 10 fonksiyondan oluşan bir liste tanımlandı
diğerleri
- Her işlev için yeni terimler icat edildi


---

## VoIP Protokollerinin ve Katmanlamanın Özeti

Katman
Ara
Süreç.
Kullanıcı
multimedya
Kullanıcı
Veri
Destek
Yönlendirme
Sinyal
Taşıma
H.323
Megako
MGCP
SIP
RTP
T.120
RTCP
RTSP
NTP
SDP
SAYI
GEZİ
SİGTRAN
TCP
UDP
UDP
TCP
TCP
UDP
SCTP
IP, RSVP ve IGMP
- Her protokol karmaşık olabilir
- H.323 bir şemsiyedir


---

## H.323

- Bir araya toplanan geniş protokol seti
- Ses, video ve veri aktarımı sağlar
- Ana protokollerin özeti
Katman
Sinyalizasyon
Kayıt
Ses
video
Veri
Güvenlik
H.225.0-Q.931
H.250-Ek G
H.245
H.250
H.225.9-RAS
G.711
H.263
G.722
G.723
G.728
H.261
H.323
T.120
H.235
TCP
TCP, UDP
RTP, RTCP
TCP, UDP
UDP
IP, RSVP ve IGMP


---

## Telefon Numarası Eşleme ve Yönlendirme

- IETF tarafından önerilen iki standart
  - TRIP bilgi alışverişi için konum sunucularına güvenir
  - ENUM (E.164 NUMbers), arpa üst düzey alanını kullanır
Alan Adı Sistemi
- ENUM örneği
  - Telefon numarası 1-800-555-1234
  - Alan adı dize olarak oluşturulmuştur
4.3.2.1.5.5.5.0.0.8.1.e164.arpa


---

## Ağ Güvenliği

- Birçok yönü olan geniş konu
- Başlıca sorunlar şunları içerir:
2 222222222222222222222222222222222222222222222222222222222222222222
Sorun
Açıklama
1 Banka gibi tanınmış bir site gibi görünmek 1
Kimlik avı
Bir kullanıcının kişisel bilgilerini elde etmek için 1, genellikle 1
hesap
sayı
ve
erişim
kod
12 222222222222222222222222222222222222222222222222222222222222222222
Yanlış beyan
Yapımı
yanlış
veya
abartılı
iddialar
hakkında
mallar
veya
1 hizmet veya sahte veya kalitesiz ürünler sunmak
21 222222222222222222222222222222222222222222222222222222222222222222
1 Safları kandırmayı amaçlayan çeşitli hile türleri 1
Dolandırıcılıklar
12 222222222222222222222222222222222222222222222222222222222222222222
1 kullanıcı para yatırıyor veya suça yataklık ediyor
İnkar
arasında
Hizmet
Kasıtlı olarak
engelleme
bir
özel
internet
site
için
1 ticari faaliyetleri ve ticareti önlemek veya engellemek 1
21 222222222222222222222222222222222222222222222222222222222222222222
1 Kontrol Kaybı 1 Davetsiz misafir bilgisayar sisteminin kontrolünü ele geçirir
1 ve sistemi suç işlemek için kullanıyor
Kayıp
arasında
Veri
Kayıp
arasında
entelektüel
mülk
veya
diğer
değerli
tescilli
iş
bilgi


---

## Saldırganların Kullandığı Tekniklere Örnekler

Teknik
Açıklama
Telefon dinleme
Paketlerin kopyasını oluşturma
1 Önceki oturumdan yakalanan paketleri gönderme 1
Tekrar oynat
1 Arabellek Taşması
1 Değerlerin üzerine yazmak için bellek arabelleğinin taşması
Adres
Sahtecilik
Sahtecilik
the
IP
kaynak
adres
içinde
bir
paket
İsim
Sahtecilik
Kullanma
bir
yazım hatası
arasında
bir
tanınmış
isim
DoS
ve
DDoS
Sel
bir
site
ile
paketler
için
önlemek
erişim
1 2222222222222222222222222222222222222222222222222222222222222222222
1 Rastgele TCP SYN segmentlerinden oluşan bir akış gönderme
SYN Flood
1 Şifre çözme anahtarını veya şifreyi tahmin etme
Anahtar Kırma
1 Güvenlik açığı bulunan bir uygulamayı bulmak için bağlantı noktalarını araştırmak
Bağlantı Noktası Tarama
İnternetten paket kaldırma
112Paket Ele Geçirme 11


---

## Dolaylı Saldırılar

- Saldırgan farkında olmadan kullanıcıların bilgisayarlarına el koyar
- El konulan bilgisayarlarda çalışan botlar saldırı başlatır
- Örnek: Dağıtılmış Hizmet Reddi (DDoS)
saldırgan komutanlar
birden fazla bilgisayar
ve paketleri aktarır
hedeflemek
toplam trafik
sunucuyu bunaltıyor
internet


---

## Paket Ele Geçirme

- Aşırı güvenlik açığı
- Birçok saldırı için kullanılabilir
- Ortadaki adam saldırılarına izin verir
- Örnek saldırılar
bir ana bilgisayarın kimliğine bürünebilir veya
değiştirilmiş paketleri ilet
herhangi bir İnternet hedefi
sunucu
Telefon dinleyebilir, tekrar oynatabilir, sahtekarlık yapabilir,
Anahtarları kırın, bağlantı noktalarını tarayın ve
bir sunucuyu taklit etmek
ortadaki adam
kaynak


---

## Güvenlik Politikası

- Kesinlikle güvenli bir ağ mevcut değil
- Güvenlik mekanizmaları anlamlı hale gelmeden önce organizasyon
bir güvenlik politikası tanımlamanız gerekir
  - Veri bütünlüğü (izinsiz değişiklik yok)
  - Veri kullanılabilirliği (hizmet kesintisi yok)
  - Veri gizliliği (izinsiz erişim yok)
  - Gizlilik (gönderenin kimliği açıklanmaz)
  - Sorumluluk (kayıt tutma ve denetim takibi)
  - Yetkilendirme (kimlerin bilgiye erişmesine izin verilir)


---

## Yetkilendirme ve Kimlik Doğrulama

- Yetkilendirme, kimlik doğrulamayla iç içedir
  - Kimlik doğrulama olmadan yetkilendirme anlamsızdır
  - Talep edenin kimliğini bilmeli
- Gerçekleştirilemeyecek bir güvenlik politikası tanımlamanın hiçbir anlamı yoktur.
zorunlu


---

## Yaptırım Mekanizmaları

2 22222222222222222222222222222222222222222222222222222222222222222
Teknik
Amaç
21 22222222222222222222222222222222222222222222222222222222222222222
1 Karma
1 Veri bütünlüğü
21 22222222222222222222222222222222222222222222222222222222222222222
1 Şifreleme
1 Gizlilik
21 22222222222222222222222222222222222222222222222222222222222222222
1 Dijital İmza
1 Mesaj kimlik doğrulaması 1
12 22222222222222222222222222222222222222222222222222222222222222222
Dijital
Sertifikalar
Gönderen
kimlik doğrulama
12 22222222222222222222222222222222222222222222222222222222222222222
Güvenlik duvarları
sitesi
bütünlük
12 22222222222222222222222222222222222222222222222222222222222222222
İzinsiz giriş
Algılama
Sistemler
sitesi
bütünlük
21 22222222222222222222222222222222222222222222222222222222222222222
1 Derin Paket İncelemesi ve İçerik Taraması 1 Site bütünlüğü
21 22222222222222222222222222222222222222222222222222222222222222222
1 Sanal Özel Ağ (VPN'ler)
1 Veri gizliliği ve 1
1 güvenilir erişim
12 22222222222222222222222222222222222222222222222222222222222222222

> 📷 *[Görsel: Diyagram/Grafik — yakında eklenecek]*


---

## Doğramak

- Mesajın hayır olmadan ulaşmasını garanti etmek için kullanılır
  - Değişiklikler
  - Eklemeler
- Gönderen ve alıcı bir anahtarı paylaşır
- Gönderici, H adı verilen küçük bir değeri hesaplamak için anahtarı kullanır.
  - Mesaj Kimlik Doğrulama Kodu (MAC)
  - Mesajın karması
- Gönderici H mesajını iletir
- Alıcı, alınan hash değerini hesaplamak için aynı anahtarı kullanır
mesaj verir ve H ile karşılaştırır


---

## Şifreleme

- Temel güvenlik tekniği
- Bilgisayarlardan ve bilgisayar ağlarından önce ortaya çıkar
- Kapsamlı matematiksel analiz
- Tanımlar
  - Düz metin: orijinal, şifrelenmemiş mesaj
  - Şifreli metin: şifrelemeden sonra mesaj
  - Şifreleme anahtarı: şifreleme için kullanılan kısa bit dizisi
  - Şifre çözme anahtarı: şifre çözme için kullanılan kısa bit dizisi
- Not: Bazı şemalarda şifreleme ve şifre çözme anahtarları
farklı; diğerlerinde ise aynıdırlar


---

## Şifrelemenin Matematiği

- Şifreleme ve şifre çözme işlevler olarak görülüyor
- Şifreleme, K1 anahtarını ve M düz metin mesajını alır.
argümanları kullanır ve sonuç olarak şifreli metin C'yi üretir
C = şifrelemek ( K1 , M )
- Şifre çözme, argüman olarak bir anahtar (K2) ve şifreli metin (C) alır,
ve bunun sonucunda M adında bir düz metin mesajı üretir
M = şifre çözme ( K2 , C )
- Matematiksel olarak şifre çözme, şifrelemenin tersidir
M = şifre çözme ( K2 , şifreleme ( K1 , M ))


---

## İki Ana Şifreleme Türü

- Özel veya gizli anahtar şifrelemesi (simetrik)
  - Şifreleme ve şifre çözme aynı anahtarı kullanır
  - Anahtar paylaşılan bir sırdır
M = şifre çözme ( K , şifreleme ( K , M ))
- Genel anahtar şifrelemesi (asimetrik)
  - Şifreleme ve şifre çözme farklı anahtarlar kullanır
  - Genel anahtar geniş çapta dağıtılır
  - Özel anahtar yalnızca bir tarafça bilinir
  - Bir kullanıcının genel anahtarını bilmek, kişinin anahtarı tahmin etmesine yardımcı olmaz.
karşılık gelen özel anahtar


---

## Dijital İmzalarla Kimlik Doğrulama

(devam)
- Garanti etmek için ek düzeyde şifreleme kullanabilir
gizlilik
- Bob mesajı imzalar ve Alice'in genel anahtarını kullanarak şifreler
X = şifrelemek ( alice_pub , şifrelemek ( bob_priv, M ))
- Alice özel anahtarıyla mesajın şifresini çözer ve ardından
Bob'un herkese açık şifresini çözerek gönderenin kimliğini doğrular
anahtar
M = şifreyi çöz ( bob_pub , şifreyi çöz ( alice_priv , X ))


---

## Anahtar Dağıtımı

- Herkesin, her kullanıcının ortak anahtarının bir kopyasını alması gerekir
- Saldırganın yanlış bir anahtar dağıtması durumunda tüm sistem
şifreleme düzeni tehlikeye girdi
- Soru: Genel anahtarlar nasıl dağıtılabilir?
her kopyanın doğru olduğunu garanti ediyor mu?
- Çeşitli çözümler önerildi; çoğu anahtara güveniyor
Genel anahtarları dağıtan yetkili kuruluşlar
- Tanınmış otorite tarafından imzalanmış anahtarları içeren mesaj
dijital sertifika
- Not: Bir otoritenin genel anahtarını bilmek onu
diğer ortak anahtarları güvenli bir şekilde elde etmek mümkün


---

## Güvenlik Duvarı Teknolojisi

- Site ile İnternet arasına eklendi
- Paketleri politikaya göre filtreler
- Hem gelen hem de giden trafiği kontrol eder
- Genel yaklaşım: aksi durumlar dışında tüm iletişimin engellenmesi
politika tarafından açıkça izin veriliyor


---

## Güvenlik Duvarı Örneği

(devam)
- Site için güvenlik duvarı kurallarına örnek:
1 Yön 1 Çerçeve Türü 1
1 IP Hedefi 1 IP Tipi 1 Kaynak Bağlantı Noktası 1 Dst Bağlantı Noktası 1
IP Kaynağı
1'i 1 arada
1 192.5.48.1 1
*
TCP
*
1'i 1 arada
1 192.5.48.2 1
*
TCP
*
içinde
*
192.5.48.3
TCP
*
1'de
*
*
1 192.5.48.3 1 UDP 1
dışarı
192.5.48.1
*
TCP
*
1 dışarı 1
1 192.5.48.2 1
*
TCP
*
1 dışarı 1
1 192.5.48.3 1
*
TCP
*
1 dışarı 1
1 192.5.48.3 1
1 UDP1
*
*


---

## Diğer Ağ Güvenlik Sistemleri

- Saldırı Tespit Sistemi (IDS)
  - Gelen paket akışını izler
  - Olağandışı aktiviteyi belirlemeye çalışır
- Derin Paket Denetimi (DPI)
  - Başlığın ötesinde paket içeriğine bakar
  - Önemli düzeyde işlem gerektirir
- Dosya inceleme sistemleri
  - Tüm veri dosyasını inceleyin (ör. e-posta)
  - İnceleyen sistemlerden daha fazla sorunu tespit edebilir
bireysel paketler


---

## Sanal Özel Ağ (VPN)

- Özel bir ağ bağlantısını taklit eder
- Trafiği emtia interneti üzerinden gönderir
- Gizliliği garanti etmek için şifreleme kullanır
- Tünel açma olarak bilinen teknik
- Kullanılabilir
  - Bir kuruluşun siteleri arasında
  - Birey ve organizasyon arasında


---

## VPN'lerde Kullanılan Şifreleme ve Tünel Açma

- Kullanılan üç temel yaklaşım
  - Yük şifreleme
  - IP-in-IP tünelleme
  *TCP'de IP tünelleme
- Orijinal veriler üçünde de şifrelenir
- Ek güvenlik için ped datagram uzunluğu


---

## IP-in-IP Tünelinin Gösterimi

Güvenli Bir VPN İçin Kullanılır
kaynak = X
varış = Y
Orijinal (Şifrelenmemiş) Yük
şifrelemek
Orijinal Datagramın Şifrelenmiş Versiyonu
kaynak = R1
varış = R2
İletim İçin Kapsüllenmiş Şifrelenmiş Datagram


---

## Güvenlik Teknolojilerine Örnekler

-PGP (Oldukça İyi Gizlilik)
- SSH (Güvenli Kabuk)
- SSL (Güvenli Soket Katmanı)
- TLS (Aktarım Katmanı Güvenliği)
- HTTPS (HTTP Güvenliği)
- IPsec (IP güvenliği)
- RADIUS (Uzaktan Kimlik Doğrulama Çevirmeli Kullanıcı Hizmeti)
- WEP (Kabloluya Eşdeğer Gizlilik)
-WPA (Wi-Fi Korumalı Erişim)


---

## Ağ Yönetimi




---

## Terminoloji

- Ağ yöneticisi veya ağ yöneticisi bir kişidir
ağdan sorumlu
  - Planlama
  - Kurulum
  - Operasyon
  - İzleme
- Ağ intraneti ifade eder
  - Tek bir kuruluş tarafından sahip olunan ve işletilen
  - Yönlendiriciler, anahtarlar gibi birçok yönetilen öğeyi içerir,
sunucular ve ana bilgisayarlar
  - Birden fazla siteye yayılabilir


---

## İlginç Bir Sorun

- Üstesinden gelmek için birçok protokol mekanizması oluşturuldu
sorunlar otomatik olarak
  - İleri hata düzeltme
  - Yeniden iletim
  - Yönlendirme protokolleri
- Sonuç: protokoller sorunları yöneticiden gizleyebilir!


---

## Endüstri Standardı Modeli

- ITU tavsiyesi M.3400'den türetilmiştir
- Kısaltmayla bilinir, FCAPS
- Kısaltma yönetimin beş yönünü ifade eder
2 22222222222222222222222222222222222222222222222222222
1 Kısaltma 1
Anlamı
21 22222222222222222222222222222222222222222222222222222
1 Arıza tespiti ve düzeltme
F
21 22222222222222222222222222222222222222222222222222222
1 Yapılandırma ve çalıştırma
Ç
1 Muhasebe ve faturalandırma
bir
P
12 22222222222222222222222222222222222222222222222222222
1 Performans değerlendirmesi ve optimizasyonu 1
S
Güvenlik
güvence
ve
koruma


---

## Arıza İzolasyonu ve Kök Neden Analizi

- Kullanıcılar yüksek düzeyde semptomlar bildiriyor
  - Örnek: Paylaşılan bir dosya sistemine erişimimi kaybettim
- Yönetici semptomları altta yatan nedene bağlamalıdır
  - Kablo kesilmesi
  - Güç kaynağı arızalandı veya disk çöktü
  - Yazılım yapılandırması değiştirildi (ör. dosya sistemi yeniden adlandırıldı)
veya taşındı)
  - Güvenlik değiştirildi (ör. şifrenin süresi doldu)


---

## Ağ Öğesi

- Yönetilen bir varlık için genel terim
  - Fiziksel cihaz
  - Hizmet (ör. DNS)
- Örnekler
Yönetilebilir Ağ Öğeleri
1 Katman 2 Anahtar
IP yönlendirici (router)
1 VLAN Anahtarı
Güvenlik duvarı
1 Kablosuz Erişim Noktası 1 Dijital Devre (CSU/DSU) 1
Baş-Uç
DSL
modem
DSLAM
DHCP
Sunucu
DNS
Sunucu
Yük Dengeleyici
1 Web Sunucusu


---

## Eleman Yönetim Sistemi

- Her seferinde bir öğeyi yönetebilen yönetim aracı
- Genellikle ağ öğesinin satıcısı tarafından sağlanır
- Eleman yönetim sistemlerinin sınırlandırılması
  - MPLS tünelini birden fazla yönlendiricide yapılandırırken,
eleman yönetim sistemi yalnızca yöneticinin şunları yapmasına izin verir:
aynı anda bir yönlendirici (router) yapılandırın
  - Yönlendiriciler birden fazla satıcı tarafından satılıyorsa, her satıcının
kendi eleman yönetim sistemi
- Ne yazık ki çoğu ağda yalnızca öğe yönetimi bulunur


---

## Ağ Yönetim Aracı Türleri

Fiziksel Katman Testi
Performans İzleme
Erişilebilirlik ve Bağlantı Akış Analizi
Paket Analizi
Yönlendirme ve Trafik Mühendisliği
Ağ Keşfi
Yapılandırma
Cihaz Sorgulama
Güvenlik Uygulaması
Olay İzleme
Ağ Planlama

> 📷 *[Görsel: Diyagram/Grafik — yakında eklenecek]*


---

## Yönetim Sistemleri Nasıl Çalışmalıdır?

- Bazı olasılıklar
  - Paralel bir fiziksel ağ kullanın
  - Paralel mantıksal ağ kullanın
  - Özel bir bağlantı katmanı protokolü kullanın
  - Verilerle aynı bağlantıları, ekipmanı ve protokolleri kullanın
- Sürpriz: modern ağ yönetimi sonuncuyu takip ediyor
yaklaşma


---

## Basit Ağ Yönetimi Protokolü (SNMP)

- İnternet standardı
- Yöneticinin bilgisayarındaki (yönetici) yazılımın etkileşime girmesini sağlar
bir öğede (aracı) çalışan yazılımla
- Değiştirilen mesajların biçimini ve anlamını belirtir
- TCP veya UDP üzerinden uygulama protokolü olarak çalışır
- Mağaza getir paradigmasını kullanır


---

## SNMP Getir-Mağaza Paradigması

- Tanımlanan kavramsal değişkenler kümesi
- Her değişkene bir ad verilir
- Yönetim Bilgi Tabanı olarak bilinen değişkenler kümesi
(MIB)
- SNMP iki temel işlem sunar
  - GET bir değişkenin değerini okumak için
  - PUT, bir değeri değişkene depolamak için
- Tüm yönetim fonksiyonları GET'in yan etkileri olarak tanımlanır veya
MIB değişkenine PUT
- Örnek: PUT'un yan etkisi olarak tanımlanan yeniden başlatma


---

## SNMP Kodlaması

- SNMP, Soyut Sözdizimi Gösterimi olarak bilinen bir standart kullanır.1
(ASN.1)
- Değişken uzunluklu kodlama
- Örnek: uzunluk ve değer olarak kodlanmış tamsayı
2 22222222222222222222222222222222222222222222222222
1 Ondalık 1 Onaltılık 1 Uzunluk 1 Bayt Değeri 1
Tamsayı
Eşdeğer
Bayt
(içinde
altıgen)
21 22222222222222222222222222222222222222222222222222
27 1
1B
1B
12 22222222222222222222222222222222222222222222222222
24.567
5FF7
5F
F7
12 22222222222222222222222222222222222222222222222222
2E789
02 E7 89
1 190.345 1


---

## MIB Değişken Adları

- Hiyerarşiktir
- Standart önekle başlayın
- Belirli bir protokolü ve değişkeni tanımlayın
- Örnek: alınan IP paketlerinin sayacının adı var
iso.org.dod.internet.mgmt.mib.ip.ipInReceives
- Ad tamsayı olarak kodlanmıştır:
1.3.6.1.2.1.4.3


---

## MIB'deki Diziler

- ASN.1 bir dizi tipini tanımlamaz
- Birçok MIB değişkeni kavramsal diziye karşılık gelir
  - Yönlendirme tablosu
  - ARP önbelleği
  - Ağ arayüzleri seti
- Hile
  - Değişken ismine “index” eklenir
  - Yönetici yazılımı, taşımak için GET-NEXT işlemini kullanır
dizi aracılığıyla


---

## İndeksleme Örneği

- IP yönlendirme tablosuna atanan değişken adı
standart-prefix.ip.ipRoutingTable
- Her alanın bir adı vardır
- GET_NEXT işlemini gerçekleştiren ilk yönlendirme tablosu girişini alır
- Örneğin, hedef adres alanı değişkeninin adı:
standart-prefix.ip.ipRoutingTable.ipRouteEntry.field.IPdestaddr


---

## Çok sayıda MIB

- Başlangıçta
  - Bir MIB
  - IP, TCP, UDP, ICMP için tanımlanmış değişkenler
- Şimdi
  - Birçok MIB
  - Yönlendiriciler, anahtarlar, modemler, yazıcılar, ana bilgisayarlar için değişkenler,
ve diğer ağ öğeleri


---

## Özet

(devam)
- Ağ güvenliği karmaşık ve zordur
- Hiçbir ağ tamamen güvenli değildir
- Hayat yine de devam ediyor
- Ağ yönetimi karmaşık ve zordur
- Mevcut araçlar oldukça ilkel
- Hayat yine de devam ediyor


---

## Sorunuz mu var?


