import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Panduan", 
    page_icon="📑",
    layout="wide",
    initial_sidebar_state="collapsed")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles/main.css")

tab1, tab2, tab3 = st.tabs([":memo: Produksi Akuakultur", ":gear: Tahapan Produksi Pembesaran", ":books: Cara Budidaya Ikan yang Baik (CBIB)"])


# TAB 1
with tab1:

   col1, col2 = st.columns([3,1], gap='small')
   
   with col1:

      st.markdown(
    """
    **Produksi Budidaya Perikanan _(Akuakultur)_** adalah kegiatan menghasilkan komoditas ikan konsumsi untuk tujuan komersial, mencakup 3 segmentasi kegiatan:

    - :small_blue_diamond: **Segmentasi _Pembenihan_** : menghasilkan dan memperbanyak bibit komoditas ikan
    - :small_blue_diamond: **Segmentasi _Pendederan_** : membesarkan bibit komoditas ikan hingga ukuran tertentu
    - :small_blue_diamond: **Segmentasi _Pembesaran_** : membesarkan ikan hingga ukuran konsumsi atau ukuran bahan baku pengolahan
    
"""
)


   with col2:
      i1 = Image.open('assets/tab_1a.jpg')
      st.image(i1, caption='Gambar 1. Pembesaran ikan lele')

      st.write(
      """
      <style>[data-testid="stHorizontalBlock"] {align-items: center;}</style>
      """, unsafe_allow_html=True)

   st.write("---")


   col1, col2 = st.columns([3,1])
   with col1:

      st.markdown(
         """
**Kegiatan pembesaran ikan bertujuan** untuk menyediakan komoditas ikan ukuran konsumsi 
sesuai permintaan pasar (lokal dan ekspor), 
baik untuk konsumsi langsung maupun sebagai bahan baku olahan.

Untuk dapat melakukan segmen pembesaran ikan secara menguntungkan
dan berkelanjutan, maka pada segmen ini juga harus didukung oleh **penyediaan
benih unggul**. Selain itu, **teknologi budidaya** terkini juga perlu diterapkan
secara tepat, terutama teknologi ramah lingkungan atau teknologi maju yang
lebih efisien dalam sub sistem pembesaran ikan.

Perencanaan kegiatan produksi juga harus memperhitungkan **faktor-faktor pembatas**.
Faktor-faktor tersebut jika dapat dikelola dengan baik akan memberi dampak langsung
pada peningkatan keuntungan yang ditandai dengan **peningkatan volume produksi** dan 
**periode produksi yang lebih singkat**.
    
"""
)


   with col2:
      i1 = Image.open('assets/tab_1b.jpg')
      st.image(i1, caption='Gambar 2. Faktor-faktor pembatas produksi pembesaran')

      st.write(
      """
      <style>[data-testid="stHorizontalBlock"] {align-items: center;}</style>
      """, unsafe_allow_html=True)

   st.write("---")

   container = st.container()
   container.markdown(
         """
Fasilitas utama pada kegiatan pembesaran ikan adalah wadah, 
yang meliputi bak, kolam, tambak, maupun Keramba Jaring Apung (KJA).
Pemilihan jenis wadah disesuaikan dengan **ketersediaan lahan, air dan dana**.
"""
)
   
   col1, col2, col3, col4, col5 = st.columns(5)
   with col1:
      i1 = Image.open('assets/tab_1e.jpg')
      st.image(i1, caption='Gambar 3. Kolam tanah')

      st.write(
      """
      <style>[data-testid="stHorizontalBlock"] {align-items: center;}</style>
      """, unsafe_allow_html=True)

   with col2:
      i2 = Image.open('assets/tab_1c.png')
      st.image(i2, caption='Gambar 4. Kolam beton')

      st.write(
      """
      <style>[data-testid="stHorizontalBlock"] {align-items: center;}</style>
      """, unsafe_allow_html=True)

   with col3:
      i2 = Image.open('assets/tab_1d.png')
      st.image(i2, caption='Gambar 5. Kolam terpal')

      st.write(
      """
      <style>[data-testid="stHorizontalBlock"] {align-items: center;}</style>
      """, unsafe_allow_html=True)

   with col4:
      i2 = Image.open('assets/tab_1f.jpg')
      st.image(i2, caption='Gambar 6. KJA')

      st.write(
      """
      <style>[data-testid="stHorizontalBlock"] {align-items: center;}</style>
      """, unsafe_allow_html=True)

   with col5:
      i2 = Image.open('assets/tab_1g.jpg')
      st.image(i2, caption='Gambar 7. Bak fiber')

      st.write(
      """
      <style>[data-testid="stHorizontalBlock"] {align-items: center;}</style>
      """, unsafe_allow_html=True)






# TAB 2
with tab2:

   # -- 2a
   col1, col2, col3 = st.columns([3,1,1])
   with col1:

      st.markdown(
    """
    **1. Persiapan wadah dan air**

    Persiapan wadah dan air merupakan tahap krusial dalam kegiatan budidaya. Menurut pengalaman penulis,
    50% resiko sudah teratasi melalui persiapan wadah dan air yang tepat. Persiapan wadah menyesuaikan 
    dengan jenis wadah. Secara umum meliputi: 
    
    - (a). ***pembersihan, desinfeksi, $*$pengapuran dan pengeringan wadah***, 
    
    - (b). ***pengisian dan persiapan air.***
    
    Tinggi air disesuaikan dengan ukuran benih. Benih yang berukuran kecil biasanya **ketinggian air 40-50 cm**, bertujuan
    agar benih dapat dengan mudah menjangkau pakan dan bernafas di permukaan. Ketinggian air dinaikkan secara
    bertahap seiring dengan bertambahnya ukuran ikan yang dipelihara. Persiapan air dilakukan dengan pemberian pupuk organik 
    (pupuk kandang, dosis 250-500 g/m$^2$) atau anorganik (Urea dosis 15 g/m$^2$ dan TSP dosis 10g/m$^2$) sumber nitrogen dan fosfor
    untuk menumbuhkan plankton. Proses persiapan air dapat berlangsung selama **5-7 hari** ditandai dengan tumbuhnya
    plankton (warna air kehijauan-hijauan). Plankton sengaja ditumbuhkan dalam air kolam untuk menstabilkan
    kondisi air sehingga benih yang masih rentan dapat bertahan hidup dengan lebih baik. Benih yang baru ditebar 
    sebaiknya dipuasakan selama 12-24 jam bertujuan untuk adaptasi lingkungan baru serta mengosongkan lambung agar 
    benih respon terhadap pakan yang akan diberikan.

    
"""
)
      

   with col2:
      i2 = Image.open('assets/tab_2a.png')
      st.image(i2, caption='Gambar 1. Persiapan wadah')

      st.write(
      """
      <style>[data-testid="stHorizontalBlock"] {align-items: center;}</style>
      """, unsafe_allow_html=True)
   
   with col3:
      i2 = Image.open('assets/tab_2b.jpg')
      st.image(i2, caption='Gambar 2. Pemupukan air')

      st.write(
      """
      <style>[data-testid="stHorizontalBlock"] {align-items: center;}</style>
      """, unsafe_allow_html=True)

   st.write("---")

   # -- 2b
   col1, col2 = st.columns([3,1])
   with col1:

      st.markdown(
    """
    **2. Penebaran benih**

    Pemilihan benih tidak boleh asal. Pilihlah benih ikan yang unggul,
    tahan penyakit, lincah dan sehat. Benih unggul dapat diperoleh di
    balai-balai perikanan Kementerian Kelautan dan Perikanan atau di 
    pembenih yang memiliki sertifikat CPIB (Cara Pembenihan Ikan yang 
    Baik). Sebelum benih dilepas, lakukan proses aklimatisasi dengan 
    ketentuan mengacu pada SNI (01-6484.2-2000) dengan membiarkan wadah/
    kantong plastik berisi benih di kolam selama **15-30 menit** sampai berembun 
    dan selanjutnya benih dilepas secara perlahan dan bertahap. Aklimatisasi 
    bertujuan untuk memberi kesempatan benih ikan beradaptasi dengan 
    lingkungan air kolam. Padat tebar adalah jumlah ikan yang dimasukkan ke 
    wadah budidaya per meter perseginya. Padat tebar adalah faktor pembatas
    budidaya sehingga perlu ditentukan dengan baik. Acuan padat tebar sesuai 
    SNI dapat diakses di [Standar Nasional Indonesia](https://akses-sni.bsn.go.id/).
    
"""
)
      

   with col2:
      i2 = Image.open('assets/tab_2c.jpg')
      st.image(i2, caption='Gambar 3. Penebaran benih')

      st.write(
      """
      <style>[data-testid="stHorizontalBlock"] {align-items: center;}</style>
      """, unsafe_allow_html=True)

   st.write("---")

# -- 2c
   col1, col2 = st.columns([3,1])
   with col1:

      st.markdown(
    """
    **3. Pengelolaan pakan**

    Pengelolaan pakan meliputi **frekuensi, waktu dan jumlah pemberian pakan**.
    Frekuensi adalah jumlah pemberian pakan dalam satu hari.
    Waktu pemberian pakan disesuaikan dengan frekuensi pemberian pakan dengan
    jarak antar pemberian harus memperhitungkan laju pengosongan lambung ikan.
    Umumnya interval waktu antar pemberian pakan berkisar 3-6 jam untuk ikan 
    air tawar. Pakan yang diberikan harus sesuai kebutuhan ikan. Secara umum
    jumlah pakan yang diberikan berkisar **3-6% dari bobot tubuhnya**, disesuaikan
    dengan komoditas yang dipelihara. Kemudian setiap 7-10 hari jumlah pemberian
    pakan harus disesuaikan karena ikan bertambah bobot tubuhnya, dengan cara
    melakukan sampling bobot ikan secara acak sejumlah minimal 30 ekor dan 
    dimasukkan kedalam perhitungan jumlah pemberian pakan.
    
"""
)
      

   with col2:
      i2 = Image.open('assets/tab_2d.webp')
      st.image(i2, caption='Gambar 4. Pemberian pakan')

      st.write(
      """
      <style>[data-testid="stHorizontalBlock"] {align-items: center;}</style>
      """, unsafe_allow_html=True)

   st.write("---")

# -- 2d
   col1, col2 = st.columns([3,1])
   with col1:

      st.markdown(
    """
    **4. Pengelolaan air, hama dan penyakit**

    Pengelolaan air adalah esensi utama dalam kegiatan budidaya perikanan.
    Kualitas air yang baik dan sesuai dengan ikan, akan membuat ikan nyaman 
    sehingga nutrisi dari pakan yang dicerna digunakan untuk tumbuh. Sebaliknya, 
    kualitas air yang jelek akan membuat ikan stress sehingga nutrisi dari pakan 
    diubah menjadi energi untuk mengatasi stress yang berakibat ikan tidak akan
    bertambah besar. Kualitas air yang jelek paling sering terjadi karena jumlah 
    dan frekuensi pemberian pakan yang berlebihan. Sisa pakan di dasar wadah
    jika dibiarkan akan membusuk menjadi _ammonia_ yang merupakan racun bagi ikan.
    Maka sebaiknya jika dirasa sudah banyak sisa pakan di dasar wadah, sepertiga air harus dibuang dan
    diganti dengan air baru. Jika pengelolaan air dilakukan dengan benar, 
    ikan akan terhindar dari stres dan meminimalisir infeksi atau masuknya 
    agen penyakit ke dalam tubuhnya. Agen penyakit dan hama dalam wadah budidaya
    tidak muncul dengan sendirinya. Biasanya keduanya berasal dari sumber air yang
    terkontaminasi atau ada kontaminasi silang dari manusia atau hewan yang masuk 
    ke dalam wadah budidaya. Maka disarankan untuk memastikan sumber air yang 
    dipakai bebas atau minim agen penyakit atau hama.

    Selain penyakit infeksi, terdapat penyakit non-infeksi yang berhubungan 
    dengan kekurangan zat-zat mikro (vitamin, mineral, zat aktif) yang dibutuhkan ikan. Penyakit
    ini jarang terjadi, namun pembudidaya tetap harus memperhatikan kebutuhan
    zat-zat mikro yang dibutuhkan ikan.

    
"""
)
      

   with col2:
      i2 = Image.open('assets/tab_2e.jpg')
      st.image(i2, caption='Gambar 5. Pengelolaan air')

      st.write(
      """
      <style>[data-testid="stHorizontalBlock"] {align-items: center;}</style>
      """, unsafe_allow_html=True)

   st.write("---")

# -- 2e
   col1, col2 = st.columns([3,1])
   with col1:

      st.markdown(
    """
    **5. Pemanenan**

    Panen dilakukan saat ikan yang dipelihara sudah mencapai ukuran jual per kilogramnya.
    Ukuran tersebut bervariasi tergantung komoditas. Ukuran konsumsi ikan lele umumnya 
    dimulai dari 12 ekor/kg sampai 8 ekor/kg. Ukuran konsumsi ikan nila 3 ekor/kg sampai
    1 ekor/kg. Ukuran size dicapai dalam tempo yang berbeda-beda tergantung jenis ikan,
    sistem dan teknologi yang digunakan dan beberapa faktor lainnya. Sehari sebelum 
    pemanenan, ikan dipuasakan agar tidak mengotori air saat proses pengangkutan. Selain
    itu saat panen juga ikan yang tidak masuk ukuran akan dipisahkan.
    
"""
)
      

   with col2:
      i2 = Image.open('assets/tab_2f.jpeg')
      st.image(i2, caption='Gambar 6. Pemanenan')

      st.write(
      """
      <style>[data-testid="stHorizontalBlock"] {align-items: center;}</style>
      """, unsafe_allow_html=True)


# TAB 3
with tab3:
   

   col1, col2 = st.columns([3,1])
   with col1:
      st.markdown(
         """
Kualitas produk menjadi salah satu hal yang paling diperhatikan oleh konsumen 
untuk membeli suatu produk. Produk yang bersertifikasi memiliki nilai jual 
lebih di pasaran dibandingkan produk yang belum bersertifikasi. 
Dalam hal produksi perikanan, pembudidaya wajib menjaga kualitas produk 
perikanan untuk menjaga kepercayaan konsumen dan meningkatkan keinginan 
konsumen untuk membeli produk perikanan. Direktorat Jenderal Perikanan Budidaya 
terus berupaya mewujudkan peningkatan performa pelaku usaha budidaya ikan 
sesuai persyaratan internasional. Persyaratan budidaya ikan sebagaimana 
ditetapkan dalam [Keputusan Menteri Kelautan dan Perikanan Nomor 02/KEP/2007 
tentang Cara Budidaya Ikan yang Baik](https://empangqq.files.wordpress.com/2013/07/kep-02-men-2007-tentang-cara-budidaya-ikan-yang-baik.pdf) 
merupakan penekanan keamanan pangan yang 
selanjutnya diharmonisasikan dengan FAO Technical Guidelines for Aquaculture 
Certification yang tidak hanya mensyaratkan keamanan pangan tetapi juga 3 (tiga) 
aspek lain yaitu integritas lingkungan, kesehatan dan kesejahteraan ikan serta 
sosial ekonomi. Proses harmonisasi tersebut menghasilkan 5 (lima) 
SNI Cara Budidaya Ikan yang Baik pada tahun 2015 yaitu:
""")
   with col2:
      i2 = Image.open('assets/tab_3a.jpg')
      st.image(i2, caption='Gambar 1. Logo IndoGAP-Akuakultur')

      st.write(
      """
      <style>[data-testid="stHorizontalBlock"] {align-items: center;}</style>
      """, unsafe_allow_html=True)

   container = st.container()
   container.markdown(
         """
- ✔️ [SNI 8228.1, Cara budidaya ikan yang baik (CBIB) Bagian 1: Udang](https://akses-sni.bsn.go.id/viewsni/baca/6370)
- ✔️ [SNI 8228.2, Cara budidaya ikan yang baik (CBIB) Bagian 2: Rumput laut](https://akses-sni.bsn.go.id/viewsni/baca/6371)
- ✔️ [SNI 8228.3, Cara budidaya ikan yang baik (CBIB) Bagian 3: Ikan hias](https://akses-sni.bsn.go.id/viewsni/baca/6372)
- ✔️ [SNI 8228.4, Cara budidaya ikan yang baik (CBIB) Bagian 4: Ikan air tawar](https://akses-sni.bsn.go.id/viewsni/baca/6373)
- ✔️ [SNI 8228.5, Cara budidaya ikan yang baik (CBIB) Bagian 5: Ikan laut di karamba jaring apung](https://akses-sni.bsn.go.id/viewsni/baca/6374)

Salah satu cara yang dilakukan untuk meningkatkan kepercayaan konsumen terhadap 
produk perikanan adalah dengan sertifikasi. Sertifikasi dalam bidang budidaya 
perikanan disebut sertifikat CBIB (Cara Budidaya Ikan yang Baik). CBIB adalah 
penerapan cara memelihara dan/atau membesarkan ikan serta memanen hasilnya 
dalam lingkungan yang terkontrol sehingga memberikan jaminan pangan dari 
pembudidayaan dengan memperhatikan sanitasi, pakan, obat ikan dan bahan kimia 
serta bahan biologis. Lebih lanjut dalam sertifikasi produk perikanan untuk 
produk ekspor dapat mengajukan sertifikasi IndoGAP _(Indonesia Good Aquaculture 
Practice)_.

Sertifikasi CBIB bagi pembudidaya memiliki beberapa manfaat, diantaranya adalah 
meningkatkan kepercayaan konsumen, melindungi konsumen, produk bersertifikasi, 
keamanan pangan, pencatatan proses/ produk budidaya, dan peningkatan daya saing. 
Ada beberapa aspek yang perlu diperhatikan dalam sertifikasi CBIB bagi pembudidaya. 
Aspek tersebut meliputi pembangunan wadah budidaya; lokasi budidaya yang jauh 
dari limbah industri, pertanian, peternakan, dan mck; penggunaan benih 
bersertifikat; volume air cukup untuk budidaya; kualitas air yang baik; 
penggunaan pakan sesuai rekomendasi KKP; penggunaan obat dan antibiotik sesuai 
dengan peraturan yang berlaku; penanganan panen dalam rantai dingin; penggunaan 
alat-alat dalam proses budidaya tidak mengganggu mutu ikan; kebersihan lokasi 
budidaya; pelatihan pekerja; serta kesejahteraan pekerja.

Usaha budidaya perikanan diklasifikasikan menjadi usaha mikro, usaha kecil, 
usaha menengah, dan usaha besar. Pengklasifikasian ini berdasarkan jumlah 
modal usaha selain tanah dan bangunan dalam rupiah. Secara berturut-turut, 
usaha mikro memiliki modal <1 M, usaha kecil memiliki modal 1 - 5 M, usaha 
menengah memiliki modal 5 - 10 M, dan usaha besar memiliki modal >10 M. 
Pengajuan sertifikasi CBIB untuk usaha mikro dan kecil cukup sampai memiliki 
Surat Pemenuhan Pelaksanaan Prinsip-prinsip CBIB. Sedangkan usaha menengah 
dan besar harus mengajukan sertifikasi CBIB berbasis IndoGAP. Persyaratan 
yang dibutuhkan meliputi NIB, KTP, Data Unit Usaha, email, nomor kartu KUSUKA, 
dan mengisi _self-check_ CBIB pada halaman www.cbib.kkp.go.id. Alur pengajuan 
sertifikasi CBIB dimulai dari pembudidaya harus sudah mendaftarkan unit 
usahanya sehingga memiliki NIB. Kemudian pembudidaya mendaftar pada halaman 
www.cbib.kkp.go.id , mengisi verifikasi _self-check_, melaksanakan verifikasi 
CBIB, dan penerbitan surat pemenuhan prinsip-prinsip CBIB. Untuk unit usaha 
skala menengah dan besar dilanjutkan ke permohonan sertifikasi CBIB ke LSPro 
sehingga mendapatkan sertifikasi CBIB dan penggunaan logo IndoGAP pada hasil 
produknya. Pentingnya penerapan Cara Budidaya Ikan yang Baik pada setiap unit 
usaha budidaya akan memberikan manfaat yang baik kepada pembudidaya dan 
konsumen. Oleh karena itu, mari terapkan prinsip-prinsip CBIB dalam unit 
usaha budidaya agar menghasilkan produk perikanan yang berkualitas dan 
berkelanjutan*.
"""
)
container.caption(
         """
*sumber: dislautkan.jogjaprov.go.id
""")