---
marp: true
theme: custom-theme
paginate: true
header: 'Bilgisayar Ağları ve İnternet | Modül 3: Fiziksel Katman'
footer: 'Adapted from D. E. Comer (Prentice-Hall)'
---

<!-- _class: lead -->
# Modül 3: Veri İletişimi Temelleri ve Fiziksel Katman

**Prof. Douglas E. Comer** ders materyalinden uyarlanmıştır.

---

# Modül 3 Konu Başlıkları

- Motivasyon ve model
- Bilgi kaynakları ve sinyaller
- İletim ortamları
- Güvenilirlik ve kanal kodlaması
- İletim modları
- Modülasyon ve demodülasyon
- Çoklama ve tekleme (kanallaştırma)

---

<!-- _class: lead -->
# Bölüm 3.1: Motivasyon ve Model

---
<!-- _class: compact -->
# Veri İletişimi Nedir?

- Geniş bir çalışma alanıdır.
- Genellikle Fiziksel Katman ile ilişkilendirilir.
- Şu alanlara değinir:
  - Fizik
  - Matematik
  - Mühendislik
- Şunları kapsar:
  - Sinyal iletimi
  - Veri kodlama
  - Modülasyon ve çoklama

---

# Motivasyon

- Analog ve dijital bilgiyi iletmenin yollarını bulmak:
  - Doğal fenomenler kullanarak (ör. elektromanyetik radyasyon)
  - Birden fazla göndericinin bir iletim ortamını paylaşmasına izin vererek
- Veri iletişimi şunları sağlar:
  - Kavramsal bir çerçeve
  - Matematiksel temel

---

# Temel Kavram

> Analog ve dijital iletişimi ayrı düşünsek de, sonuçta tüm iletişim aynı fiziksel fenomenleri — genellikle elektromanyetik enerjiyi — kullanır.

- Farklar, fiziksel fenomenlerin kullanım biçiminde yatar:
  - **Analog**: Sürekli bir aralıktaki tüm değerleri kullanır.
  - **Dijital**: Sabit bir değer kümesiyle sınırlı kalır, genellikle iki değer.
- Veri iletişimi hem analog hem dijitali kapsar.

---

# Veri İletişimi Kavramsal Çerçevesi

<!-- Görsel: PDF sayfa 179 — Bilgi kaynağından hedefe uzanan blok diyagramı (kaynak kodlayıcı, kanal kodlayıcı, çoklayıcı, modülatör, fiziksel kanal, demodülatör, tekleyici, kanal çözücü, kaynak çözücü) -->

> 📷 *[Görsel: Kavramsal çerçeve blok diyagramı — yakında eklenecek]*

---

<!-- _class: lead -->
# Bölüm 3.2: Bilgi Kaynakları ve Sinyaller

---

# Bilgi Kaynakları

- Bir giriş sinyali şu kaynaklardan gelebilir:
  - Mikrofon gibi bir dönüştürücü (transducer)
  - Ethernet arayüzü gibi bir alıcı (receiver)
- Sinyallerin tanınması ve dönüştürülmesini tanımlamak için **sinyal işleme (signal processing)** terimini kullanırız.

---

# Sinüs Dalgaları (Sine Waves)

<!-- Görsel: PDF sayfa 182 — Sinüs dalgası grafiği -->

> 📷 *[Görsel: Sinüs dalgası — yakında eklenecek]*

---

# Sinüs Dalgaları (Sine Waves)

- Pek çok doğal fenomeni karakterize ettikleri için temel önem taşırlar.
- Örnekler:
  - İşitilebilir sesler (audible tones)
  - Radyo dalgaları
  - Işık enerjisi

---

# Fourier Analizi (Fourier Analysis)

- Birden fazla sinüs dalgası bir araya getirilebilir:
  - Sonuca **bileşik dalga (composite wave)** adı verilir.
  - Birden fazla sinyalin birleştirilmesine karşılık gelir (ör. aynı anda iki müzik notası çalmak).
- Fourier adlı matematikçi, rastgele bir bileşik dalgayı ayrı sinüs dalgalarına ayrıştırmanın yolunu keşfetti.
- Fourier analizi, sinyal işleme için matematiksel temeli sağlar.
- Kötü haber: Fourier'e göre dijital bir dalga, sonsuz sayıda sinüs dalgasına ayrışır.

---

<!-- _class: compact -->
# Sinüs Dalgası Özellikleri

- Ağlarda kullanılan üç önemli özellik: **frekans**, **genlik** ve **faz**

<!-- Görsel: PDF sayfa 185-188 — Dört farklı sinüs dalgası karşılaştırması: orijinal, yüksek frekanslı, düşük genlikli, yeni fazlı -->

> 📷 *[Görsel: Sinüs dalgası özellikleri karşılaştırması — yakında eklenecek]*

---

# Analog Bant Genişliğinin Tanımı

- Bir sinyali sinüs dalgası kümesine ayrıştır ve en yüksek ile en düşük frekans arasındaki farkı al.
- Frekans alanı grafiğinden kolayca hesaplanabilir.

<!-- Görsel: PDF sayfa 189 — 4 KHz bant genişliğine sahip örnek sinyal frekans grafiği -->

> 📷 *[Görsel: Bant genişliği frekans grafiği — yakında eklenecek]*

---

# Dijital Sinyaller ve Sinyal Seviyeleri

- Bir dijital sinyal seviyesi birden fazla bit temsil edebilir.

<!-- Görsel: PDF sayfa 190-192 — İki seviyeli ve dört seviyeli sinyal karşılaştırması -->

> 📷 *[Görsel: Dijital sinyal seviyeleri — yakında eklenecek]*

- **Baud hızı**: Sinyalin saniyede kaç kez değiştiğidir.
- **Bit hızı** (bps) = baud × ⌊log₂(seviye sayısı)⌋

---

# Dijitalden Analoga Dönüştürme

- Dijital sinyal, sinüs dalgaları bileşiğiyle yaklaşık olarak ifade edilir.
- Matematiksel olarak dijital bir sinyalin bant genişliği sonsuzdur.

<!-- Görsel: PDF sayfa 193 — Dijital sinyalin giderek artan sinüs dalgası toplamıyla yaklaşımı -->

> 📷 *[Görsel: Dijitalden analoga dönüşüm — yakında eklenecek]*

---

# Analogdan Dijitale Dönüştürme

- Dönüştürme sırasında üç adım uygulanır:
  1. **Örnekleme (Sampling)**
  2. **Nicemleme (Quantization)**
  3. **Kodlama (Encoding)**

<!-- Görsel: PDF sayfa 194-196 — PCM kodlayıcı blok diyagramı ve sekiz seviyeli örnekleme grafiği -->

> 📷 *[Görsel: Analogdan dijitale dönüşüm — yakında eklenecek]*

---

# Örnekleme Hızı ve Nyquist Teoremi

- Saniyede kaç örnek alınmalıdır?
- Nyquist adlı matematikçi yanıtı keşfetti:

$$\text{örnekleme hızı} = 2 \times f_{\max}$$

*($f_{\max}$: bileşik sinyaldeki en yüksek frekans)*

- **Örnek**: 4000 Hz'e kadar ses frekanslarını yakalamak için dijital telefon sistemi saniyede 8000 örnek alır.
- Tek bir dijitalleştirilmiş ses görüşmesinin veri hızı:

$$8000 \frac{\text{örnek}}{\text{sn}} \times 8 \frac{\text{bit}}{\text{örnek}} = 64.000 \frac{\text{bit}}{\text{sn}}$$

---

# Doğrusal Olmayan Kodlama

- Doğrusal örnekleme ses için iyi çalışmaz.
- Araştırmacılar, insan kulağının duyarlı olduğu sesleri yeniden üretmek için dinamik aralığı değiştiren doğrusal olmayan örnekleme yöntemleri geliştirdi.
- **Mu-law (µ-law)**:
  - Kuzey Amerika ve Japonya'da kullanılır.
  - Daha geniş dinamik aralık, ancak gürültüye daha duyarlı.
- **A-law**:
  - Avrupa'da kullanılır.
  - Gürültüye daha az duyarlı, ancak daha dar dinamik aralık.

---

# Senkronizasyon Hataları ve Hat Kodlaması

- Senkronizasyon hatası, alıcı ve göndericinin bit sınırları konusunda anlaşamaması durumunda (saatler farklılaştığında) ortaya çıkar.

<!-- Görsel: PDF sayfa 201 — Gönderilen ve alınan bit dizisinin kayması diyagramı -->

> 📷 *[Görsel: Senkronizasyon hatası — yakında eklenecek]*

- Hat kodlama teknikleri senkronizasyon hatalarını önler.

---

# Örnek Hat Kodlaması: Manchester Kodlaması (Manchester Encoding)

- Ethernet'te kullanılır.
- Alıcıyı göndericiye senkronize eder (geçiş, biti temsil eder).
- (a) Manchester Kodlaması ve (b) Diferansiyel Manchester Kodlaması örnekleri:

<!-- Görsel: PDF sayfa 202 — Manchester ve diferansiyel Manchester kodlama diyagramları -->

> 📷 *[Görsel: Manchester kodlaması — yakında eklenecek]*

---

<!-- _class: lead -->
# Bölüm 3.3: İletim Ortamları

---
<!-- _class: compact -->
# İletim Ortamlarının Sınıflandırması

- **Elektriksel**:
  - Bükümlü çift (twisted pair)
  - Koaksiyel kablo (coaxial cable)
- **Işık**:
  - Optik fiber
  - Kızılötesi (InfraRed)
  - Lazer
- **Elektromanyetik (Radyo)**:
  - Karasal radyo (terrestrial)
  - Uydu (satellite)

---

# Gerçek Dünyadan Kötü Haberler

- Gerçek dünyada entropi hüküm sürer.
- İletim pek çok sorunla karşı karşıyadır.

---

# Kayıp, Girişim ve Elektriksel Gürültü

- Elektriksel ve elektromanyetik dünyadaki sorunlar:
  - **Direnç (Resistance)**: Kayıba yol açar.
  - **Kapasite (Capacitance)**: Bozulmaya yol açar.
  - **Endüktans (Inductance)**: Girişime yol açar.
- Rastgele elektromanyetik radyasyona **gürültü (noise)** adı verilir:
  - Elektrik motoru gibi belirli kaynaklardan üretilebilir.
  - Arka plan radyasyonu, evrenin kaçınılmaz bir özelliğidir.

---

# Örnekler

- Elektriksel sinyaller bir tel boyunca yayıldığında elektromanyetik enerji yayılır (tel anten gibi davranır).
- Elektromanyetik radyasyon metalle karşılaştığında, tel üzerindeki sinyallere girişim yapabilecek küçük bir elektrik akımı oluşur.
- Sonlandırılmamış bir tele elektriksel bir darbe gönderildiğinde, yansıma geri gelir.
- Bir sinyal iki tel arasındaki bağlantıdan geçtiğinde yansıma ve kayıp meydana gelir.
- Not: Bir ağ tanılama aracı, yansımayı kullanarak kablonun kesildiği noktaya olan mesafeyi bulur.

---

# Bakır Kablolarda Gürültü Etkisi Nasıl Azaltılır?

- Çeşitli teknikler geliştirilmiştir:
  - Korumasız bükümlü çift (UTP - Unshielded Twisted Pair)
  - Koaksiyel kablo (Coaxial cable)
  - Korumalı bükümlü çift (STP - Shielded Twisted Pair)
- Tümü bilgisayar ağlarında kullanılır.

---

# Bükümlü Çiftin Avantajı

<!-- Görsel: PDF sayfa 209-211 — Bükülmemiş ve bükümlü çift karşılaştırması, radyasyon kaynağı ve fark voltajı diyagramları -->

> 📷 *[Görsel: Bükümlü çift çalışma prensibi — yakında eklenecek]*

- Bükülmemiş bir tel çiftinde, radyasyonun önce çarptığı telde daha fazla akım oluşur.
- Bükmek her teli eşit şekilde etkiye maruz bırakır; fark sıfıra yaklaşır.

---

# Koaksiyel Kablo ve Koruma

- Daha iyi koruma: Tel etrafına metal bir kalkan sarılır.
  - Dış plastik kaplama
  - Örgülü metal kalkan
  - Plastik yalıtım
  - Sinyal için iç tel
- Bükümlü çifte de kalkan eklenebilir:
  - Birden fazla çifti içeren kablonun tamamı etrafına
  - Her çiftin etrafına ve kablonun tamamı etrafına
- Kalkan, maksimum veri hızını belirler.

---

<!-- _class: compact -->
# Kablolama Standartları ve Veri Hızları (Wiring Standards And Data Rates)

| Kategori | Açıklama | Veri Hızı |
|---|---|---|
| **CAT 1** | Telefon için korumasız bükümlü çift | < 0,1 Mbps |
| **CAT 2** | T1 verisi için korumasız bükümlü çift | 2 Mbps |
| **CAT 3** | Bilgisayar ağları için geliştirilmiş CAT2 | 10 Mbps |
| **CAT 4** | Token Ring ağlar için geliştirilmiş CAT3 | 20 Mbps |
| **CAT 5** | Ağlar için korumasız bükümlü çift | 100 Mbps |
| **CAT 5E** | Daha fazla gürültü bağışıklığı için genişletilmiş CAT5 | 125 Mbps |
| **CAT 6** | 200 Mbps için test edilmiş korumasız bükümlü çift | 200 Mbps |
| **CAT 7** | Tüm kablo ve her çift etrafında folyo kalkanlı bükümlü çift | 600 Mbps |

- Listede hangi yaygın veri hızı eksik?

---

# Işık Enerjisi Kullanan Ortamlar

- **Kızılötesi (InfraRed)** iletim: kısa menzil ve düşük veri hızı.
- **Noktadan noktaya lazerler**: binalar arası bağlantı için kullanışlı.
- **Optik fiber**: yüksek veri hızı ve uzun mesafe.
- Işığın fiberde neden kaldığı:

<!-- Görsel: PDF sayfa 215 — Kırılma, soğurulma ve yansıma diyagramları -->

> 📷 *[Görsel: Optik fiber iç yansıma — yakında eklenecek]*

---

<!-- _class: compact -->
# Elektromanyetik Spektrum ve Özellikleri

<!-- Görsel: PDF sayfa 216 — Frekans ekseni üzerinde spektrum diyagramı -->

> 📷 *[Görsel: Elektromanyetik spektrum — yakında eklenecek]*

| Sınıf | Frekans Aralığı | Yayılım Türü |
|---|---|---|
| **Düşük Frekans** | < 2 MHz | Dalga yeryüzü eğrisini izler, ancak engebeli arazi tarafından engellenebilir. |
| **Orta Frekans** | 2 - 30 MHz | Dalga atmosfer katmanlarından (özellikle iyonosferden) yansıyabilir. |
| **Yüksek Frekans** | > 30 MHz | Dalga düz bir çizgide ilerler ve engellerle bloke edilir. |

---

# Uydu İletişimi

- Üç tür iletişim uydusu:

| Yörünge Türü | Açıklama |
|---|---|
| **LEO** (Alçak Dünya Yörüngesi) | Düşük gecikme avantajı, ancak gözlemci açısından uydu gökyüzünde hareket ediyor gibi görünür. |
| **MEO** (Orta Dünya Yörüngesi) | Kuzey ve Güney Kutuplarında iletişim sağlamak için kullanılan eliptik yörünge. |
| **GEO** (Jeostasyoner Yörünge) | Uydu, yeryüzündeki bir konuma göre sabit kalır; ancak daha uzakta olma dezavantajı vardır. |

---

# GEO Uyduları

- Atmosfer ile birlikte çizilmiş Dünya şekli — GEO uydusu şekilde nerede olurdu?

<!-- Görsel: PDF sayfa 218 — Dünya ve atmosfer ölçekli çizimi -->

> 📷 *[Görsel: GEO uydusu ve Dünya — yakında eklenecek]*

---

# GEO Uyduları (devam)

- GEO uydusuna mesafe: **35.785 km** (22.236 mil).
- Yaklaşık olarak Dünya'nın çapının 3 katı veya Ay'a olan mesafenin onda biri.
- Başka bir deyişle: uydu sayfanın çok dışında!
- Ağ açısından sonucu: ışık hızında bile uzun bir gidiş-dönüş süresi:

$$\text{Gidiş-dönüş süresi} = \frac{2 \times 35.8 \times 10^6 \text{ m}}{3 \times 10^8 \text{ m/s}} \approx 0{,}238 \text{ sn}$$

---

# İletim Ortamlarının Ölçütleri

- **Yayılım gecikmesi (Propagation delay)**: Bir sinyalin ortamı geçmesi için gereken süre.
- **Kanal kapasitesi (Channel capacity)**: Maksimum veri hızı.

---

# Kanal Kapasitesi (Channel Capacity)

- **Nyquist Teoremi**: $B$ bant genişliği ve $K$ sinyal seviyesi için teorik maksimum veri hızı:

$$D = 2B \log_2 K$$

- **Shannon Teoremi**: Gürültü varlığında maksimum kanal kapasitesi $C$:

$$C = B \log_2 (1 + S/N)$$

- $S/N$ miktarı **sinyal-gürültü oranı** olarak bilinir.

---

# Değerlendirme

- **Nyquist Teoremi** bize umut verir: daha fazla sinyal seviyesi kullanmak veri hızını artırabilir.
- **Shannon Teoremi** ayıltıcıdır: evrendeki elektriksel gürültü, herhangi bir pratik iletişim sisteminin etkin kanal kapasitesini sınırlar.

---

<!-- _class: lead -->
# Bölüm 3.4: Güvenilirlik ve Kanal Kodlaması

---

# Hata Kaynakları ve Türleri

- Hata kaynakları: girişim, bozulma ve zayıflama (attenuation).
- Ortaya çıkan hata türleri:

| Hata Türü | Açıklama |
|---|---|
| **Tek Bit Hatası** | Bir bit bloğundaki tek bir bit değişir, diğerleri değişmez (genellikle çok kısa süreli girişimden kaynaklanır). |
| **Patlama Hatası** (Burst Error) | Bir bit bloğundaki birden fazla bit değişir (genellikle uzun süreli girişimden kaynaklanır). |
| **Silme (Belirsizlik)** | Alıcıya ulaşan sinyal belirsizdir — açıkça 0 veya 1'e karşılık gelmez (bozulma veya girişimden kaynaklanabilir). |

- Hataları saptamak ve düzeltmek için **kanal kodlaması** kullanılır.

---

# İleri Hata Düzeltme Kavramı (Concept Of Forward Error Correction - FEC)

- Gönderici orijinal mesajı bir kodlayıcıdan geçirir: koruma için fazladan bitler eklenir.
- Alıcı bir kod sözcüğü alır: kontrol eder ve isteğe bağlı olarak düzeltir.
- Örnekler:
  - Tek eşlik biti (single parity bit)
  - Satır ve Sütun kodu (RAC - Row And Column)
  - Döngüsel Artıklık Denetimi (CRC - Cyclic Redundancy Check)

<!-- Görsel: PDF sayfa 227 — FEC gönderici-alıcı blok diyagramı -->

> 📷 *[Görsel: İleri hata düzeltme şeması — yakında eklenecek]*

---

# Örnek: Satır ve Sütun Kodu

- 12 bit göndermek için bitler bir matrise dizilir, her satır ve sütun için eşlik hesaplanır ve 20 bit gönderilir.

<!-- Görsel: PDF sayfa 228-229 — Bit matrisi, eşlik bitleri ve hata tespiti diyagramı -->

> 📷 *[Görsel: Satır ve sütun kodu — yakında eklenecek]*

- Alıcı, 12 bit için aynı eşliği hesaplar ve alınan eşlik bitleriyle karşılaştırır.

---

# Hamming Mesafesi (Hamming Distance)

- Bir kodun hatalara karşı direncini değerlendirmek için kullanılır.
- $S_1$ bit dizisini $S_2$ bit dizisine dönüştürmek için gereken bit değişikliği sayısı olarak tanımlanır.
- $S_1$ ve $S_2$'nin özel veya (XOR) işlemindeki 1 bitlerinin sayısı olarak hesaplanabilir.
- Bir kodun gücünü değerlendirmek için: tüm olası kod sözcüğü çiftleri arasındaki Hamming mesafesini hesapla ve minimumu al.
- Minimum Hamming mesafesi $n$ ise, $n$'den az bit değiştiren hata saptanabilir.

---

# İnternet Sağlama Toplamı Hesabı (Internet Checksum Computation)

```
Verilen:  Rastgele uzunlukta bir M mesajı
Hesapla:  16-bit 1'ler tümleyeni sağlama toplamı C

Yöntem:
  M'yi 16'nın tam katına tamamla;
  32-bit sağlama toplamı tamsayısı C'yi sıfıra ayarla;
  for ( M'deki her 16-bit grup ) {
      16 biti tamsayı olarak ele al ve C'ye ekle;
  }
  C'nin yüksek düzey 16 bitini çıkar ve C'ye ekle;
  Sağlama toplamı, düşük düzey 16 bitin tersidir;
  Sağlama toplamı sıfırsa tümü 1 olarak değiştir;
```

---

# Döngüsel Artıklık Kodu (CRC - Cyclic Redundancy Code)

- Ethernet ve diğer yüksek hızlı ağlarda kullanılır.
- Özellikleri:

| Özellik | Açıklama |
|---|---|
| **Rastgele Uzunluk** | Sağlama toplamı gibi, veri sözcüğü boyutu sabit değildir; CRC rastgele uzunluktaki mesajlara uygulanabilir. |
| **Mükemmel Hata Tespiti** | Hesaplanan değer mesajdaki bit dizisine bağlı olduğundan CRC mükemmel hata tespit kapasitesi sağlar. |
| **Hızlı Donanım Uygulaması** | Sofistike matematiksel temeline rağmen, CRC hesabı donanım tarafından son derece hızlı gerçekleştirilebilir. |

---

# CRC'nin Açıklaması (Explanation Of CRC)

- **Matematikçiler**: CRC hesabını polinom bölmesinin kalanı olarak açıklar.
- **Teorik bilgisayar bilimciler**: İkili sayıların bölmesinden kalan olarak açıklar.
- **Kriptograflar**: Derecesi 2 olan Galois alanındaki bir işlem olarak açıklar.
- **Bilgisayar programcıları**: Mesaj üzerinde yineleyen ve tablo araması kullanan bir algoritma olarak açıklar.
- **Donanım mimarları**: Özel veya (XOR) kullanan küçük bir donanım boru hattı birimi olarak açıklar.

---

# Soru

- Aşağıdakileri açıklayabilir misiniz?
  - **Gerçek 1**: Ethernet ile kullanılan 32 bitlik CRC'yi hesaplayan bir fonksiyon yazmak mümkündür.
  - **Gerçek 2**: Ticari Ethernet ürünleri CRC hesaplamak için yazılım yerine donanım kullanır.

---

<!-- _class: lead -->
# Bölüm 3.5: İletim Modları

---

# Terminoloji

- **Seri (Serial)**: Bir seferde bir bit.
- **Paralel (Parallel)**: Bir seferde birden fazla bit.
- İletim yöntemlerinin sınıflandırması:
  - **Paralel**
  - **Seri**:
    - Eşzamansız (Asynchronous)
    - Eşzamanlı (Synchronous)
    - İzokronöz (Isochronous)

---

# Bitlerin ve Baytların Seri Sıralaması

- Her iki taraf da bitlerin iletildiği sıra üzerinde anlaşmalıdır.
- **Büyük-endian (big-endian)** ve **küçük-endian (little-endian)** olarak bilinen iki yaklaşım vardır.
- Örnek: Ethernet, bayt için büyük-endian ve bit için küçük-endian sıralaması kullanır.

<!-- Görsel: PDF sayfa 238 — Byte/bit sıralama diyagramı -->

> 📷 *[Görsel: Büyük/küçük-endian sıralama — yakında eklenecek]*

---

# Eşzamansız ve Eşzamanlı İletim

- **Eşzamansız**: Kullanılmadığında hat boştadır; veri rastgele bir zamanda başlar.
- **Eşzamanlı**: Her bit yuvası kullanılır; alıcı bitleri baytlara nasıl gruplandıracağını bilmelidir.

<!-- Görsel: PDF sayfa 239 — Eşzamansız ve eşzamanlı iletim voltaj diyagramları -->

> 📷 *[Görsel: Eşzamansız ve eşzamanlı iletim — yakında eklenecek]*

---

# Simpleks ve Dupleks Modların Gösterimi

<!-- Görsel: PDF sayfa 240 — Simpleks, tam dupleks ve yarı dupleks diyagramları -->

> 📷 *[Görsel: Simpleks/dupleks iletim modları — yakında eklenecek]*

- **(a) Simpleks**: Tek yönlü iletim.
- **(b) Tam Dupleks (Full-Duplex)**: Her iki yönde eş zamanlı iletim.
- **(c) Yarı Dupleks (Half-Duplex)**: Her iki yönde iletim, ancak aynı anda değil.

---

<!-- _class: lead -->
# Bölüm 3.6: Modülasyon ve Demodülasyon

---

# Genlik Modülasyonu Gösterimi

<!-- Görsel: PDF sayfa 242-245 — Taşıyıcı, sinyal ve modüle edilmiş taşıyıcı diyagramları (kademeli) -->

> 📷 *[Görsel: Genlik modülasyonu — yakında eklenecek]*

---

# Frekans Modülasyonu Gösterimi

<!-- Görsel: PDF sayfa 246 — Sinyal ve modüle edilmiş taşıyıcı diyagramı -->

> 📷 *[Görsel: Frekans modülasyonu — yakında eklenecek]*

---

# Kaydırmalı Anahtarlama (Shift Keying)

- Modülasyona benzer, ancak sinyal dijitaldir.

<!-- Görsel: PDF sayfa 247 — Taşıyıcı, dijital sinyal ve genlik kaydırmalı anahtarlama diyagramı -->

> 📷 *[Görsel: Genlik kaydırmalı anahtarlama (ASK) — yakında eklenecek]*

---

# Bir Meydan Okuma

Girdi olarak bir sinyali tanımlayan nokta serisi alan ve önceki diyagramlardaki gibi genlik ve frekans modülasyonunu gösteren sinüs dalgası grafikleri üreten bir bilgisayar programı yazın.

---

# Diğer Modülasyon Konuları

- Faz kayması modülasyonu (phase shift modulation)
- Genlik ve faz kayması birleştirilerek saniyedeki bit artırma (QAM teknikleri)
- Kombinasyonları temsil etmek için takımyıldızı diyagramları (constellation diagrams)
- Modemler (modülatör / demodülatör)

---

<!-- _class: lead -->
# Bölüm 3.7: Çoklama ve Tekleme (Kanallaştırma)

---

# Çoklama Kavramı ve Türleri (Concept Of Multiplexing And Types)

<!-- Görsel: PDF sayfa 251-252 — Çoklayıcı, paylaşılan ortam ve tekleyici diyagramı -->

> 📷 *[Görsel: Çoklama kavramı — yakında eklenecek]*

- Türler:
  - Frekans bölmeli çoklama (FDM - Frequency Division Multiplexing)
  - Dalga boyu bölmeli çoklama (WDM - Wavelength Division Multiplexing)
  - Zaman bölmeli çoklama (TDM - Time Division Multiplexing)
  - Kod bölmeli çoklama (CDM - Code Division Multiplexing)

---

# Frekans Bölmeli Çoklama (FDM - Frequency Division Multiplexing)

- Yayın radyosu ve kablo TV'de kullanılır.
- Tekleme, filtre kümeleriyle gerçekleştirilir.

<!-- Görsel: PDF sayfa 253 — FDM çoklayıcı/tekleyici diyagramı ve kanal filtreleri -->

> 📷 *[Görsel: FDM şeması — yakında eklenecek]*

---

<!-- _class: compact -->
# FDM Uygulamada

- Her kanala bir frekans aralığı atanır.

| Kanal | Kullanılan Frekanslar |
|---|---|
| 1 | 100 KHz - 300 KHz |
| 2 | 320 KHz - 520 KHz |
| 3 | 540 KHz - 740 KHz |
| 4 | 760 KHz - 960 KHz |
| 5 | 980 KHz - 1180 KHz |
| 6 | 1200 KHz - 1400 KHz |

- Bitişik kanalları ayırmak için bir **koruma bandı (guard band)** kullanılır.

---

# Dalga Boyu Bölmeli Çoklama (WDM - Wavelength Division Multiplexing)

- Işıkla kullanılan (optik fiber üzerinde) bir FDM biçimidir.
- Ayrı frekanslar **renkler** veya **lambdalar** olarak adlandırılır.
- Frekansları ayırmak için prizmalar kullanılır.
- Güncel teknoloji Yoğun WDM'dir (DWDM); tek bir kanal 10 Gbps sağlayabilir.

---

# Zaman Bölmeli Çoklama (TDM - Time Division Multiplexing)

- Gönderenler sırayla iletim yapar.

<!-- Görsel: PDF sayfa 256 — TDM çoklayıcı/tekleyici veri akışı diyagramı -->

> 📷 *[Görsel: TDM şeması — yakında eklenecek]*

- **Eşzamanlı TDM (Synchronous TDM)**:
  - Her gönderene bir yuva atanır (genellikle döngüsel sırayla).
  - Telefon şirketleri tarafından kullanılır.
- **İstatistiksel TDM (Statistical TDM)**:
  - Gönderen yalnızca hazır olduğunda iletir (ör. Ethernet).

---

# Kod Bölmeli Çoklama (CDM - Code Division Multiplexing)

- Cep telefonlarında kullanılan matematiksel çoklama biçimidir.
- Algoritma:
  - Her gönderici/alıcı çiftine **chip dizisi** adı verilen benzersiz bir sayı atanır.
  - Gönderenler veri değerini chip dizisiyle çarpar (ortogonal vektör uzayları).
  - İletilen değer tüm göndericilerin toplamıdır.
  - Her alıcı, veriyi çıkarmak için gelen değeri kendi chip dizisiyle çarpar.
- İstatistiksel TDM'ye göre avantaj: ağ yoğun olduğunda daha düşük gecikme.

---

# Hiyerarşik Çoklama

- Hiyerarşiler, birden fazla düşük kapasiteli kanalı birleştirmek için FDM ve TDM ile kullanılır.
- Telefon sistemi tarafından kullanılan TDM hiyerarşisi örneği:

| Düzey | Hız |
|---|---|
| DS-0 | 64 Kbps (tek ses kanalı) |
| DS-1 | 1,544 Mbps (24 × DS-0) |
| DS-2 | 6,312 Mbps (4 × DS-1) |
| DS-3 | 44,736 Mbps (7 × DS-2) |
| DS-4 | 274,176 Mbps (6 × DS-3) |

---

# Ters Çoklama

- Tek bir kanaldan gelen veriyi birkaç düşük hızlı kanala böler.
- Yüksek hızlı kanal mevcut olmadığında veya çok pahalı olduğunda kullanılır.
- Bazı İSS'ler birkaç 10 Gbps kanalını daha yüksek hızlı bir kanalla birleştirmek için ters çoklama kullanır.

---

# Modül 3 Özeti

- Veri iletişimi Fiziksel Katman ve veri aktarımıyla ilgilenir.
- Kavramlar şunları içerir:
  - Sinyaller ve dijital ile analog arasındaki dönüşüm
  - İletim ortamları
  - Güvenilirlik ve kanal kodlaması
  - Modülasyon ve demodülasyon
  - Çoklama ve tekleme

---

<!-- _class: lead -->
# Sorular?
