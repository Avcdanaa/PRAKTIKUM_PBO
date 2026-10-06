## Sistem Pemesanan Tiket Wisata Alam dan Manajemen Pengunjung

**Nama:** K DESTIANA  
**NIM:** 2509106001  
**Kelas:** A1'25  

---

## 1. Deskripsi Program

Program ini merupakan implementasi Pemrograman Berorientasi Objek (PBO) dengan judul **Sistem Pemesanan Tiket Wisata Alam dan Manajemen Pengunjung**.

Program digunakan untuk mensimulasikan proses pemesanan tiket wisata alam, pengelolaan data pengunjung, destinasi wisata, pemandu wisata, dan pembayaran.

Konsep PBO yang diterapkan dalam program ini adalah:

- Inheritance
- Superclass dan Subclass
- `super().__init__()`
- Method Overriding
- Protected Attribute
- Private Attribute
- Asosiasi
- Agregasi
- Komposisi
- Polimorfisme

---

# 2. Class yang Digunakan

Program terdiri dari beberapa class, yaitu:

1. `Pengunjung`
2. `PengunjungDomestik`
3. `PengunjungMancanegara`
4. `Pemandu`
5. `DestinasiWisata`
6. `Pembayaran`
7. `Pemesanan`

---

# 3. Inheritance

## 3.1 Superclass

Superclass yang digunakan adalah `Pengunjung`.

```python
class Pengunjung:

Class Pengunjung menjadi parent class untuk dua subclass, yaitu:

PengunjungDomestik
PengunjungMancanegara

Atribut yang terdapat pada superclass:

self._nama
self._no_telepon
self.__pin

Atribut _nama dan _no_telepon merupakan atribut Protected, sedangkan __pin merupakan atribut Private.

Method yang terdapat pada superclass:

verifikasi_pin()
get_nama()
hitung_harga_tiket()
info()
3.2 Subclass PengunjungDomestik

Subclass pertama adalah:

class PengunjungDomestik(Pengunjung):

Subclass ini digunakan untuk data pengunjung dalam negeri.

Pada konstruktor subclass digunakan:

super().__init__(nama, no_telepon, pin)

Atribut khusus yang dimiliki:

self.nik
self.kota_asal

Subclass ini melakukan method overriding pada method hitung_harga_tiket().

Pengunjung domestik mendapatkan diskon sebesar 10% dari harga dasar tiket.

3.3 Subclass PengunjungMancanegara

Subclass kedua adalah:

class PengunjungMancanegara(Pengunjung):

Subclass ini digunakan untuk data pengunjung dari luar negeri.

Pada konstruktor subclass digunakan:

super().__init__(nama, no_telepon, pin)

Atribut khusus yang dimiliki:

self.no_paspor
self.negara_asal

Subclass ini melakukan method overriding pada method hitung_harga_tiket().

Pengunjung mancanegara dikenakan tarif sebesar dua kali harga dasar tiket.

4. Protected dan Private
4.1 Protected

Atribut Protected pada superclass adalah:

self._nama
self._no_telepon

Atribut Protected dapat digunakan oleh subclass.

Contohnya digunakan kembali pada subclass:

self._nama
self._no_telepon
4.2 Private

Atribut Private pada superclass adalah:

self.__pin

Atribut tersebut bersifat rahasia dan tidak dapat diakses secara langsung dari luar class.

Untuk memeriksa PIN digunakan method:

verifikasi_pin()

Contoh:

p1.verifikasi_pin("1234")
p1.verifikasi_pin("0000")

Program juga melakukan pengujian akses langsung terhadap __pin untuk menunjukkan bahwa atribut tersebut bersifat Private.

5. Method Overriding

Method hitung_harga_tiket() terdapat pada superclass:

def hitung_harga_tiket(self, harga_dasar):
    return harga_dasar

Method tersebut kemudian di-override pada PengunjungDomestik:

def hitung_harga_tiket(self, harga_dasar):
    return harga_dasar - (harga_dasar * self.DISKON)

Sedangkan pada PengunjungMancanegara:

def hitung_harga_tiket(self, harga_dasar):
    return harga_dasar * self.PENGALI_TARIF

Dengan demikian, method yang sama memiliki perilaku berbeda sesuai dengan jenis pengunjung.

6. Relasi UML

Program menerapkan tiga jenis relasi UML yang diwajibkan, yaitu:

Asosiasi
Agregasi
Komposisi
6.1 Asosiasi

Relasi Asosiasi diterapkan antara:

Pemesanan -------- Pengunjung
Pemesanan -------- DestinasiWisata

Pada class Pemesanan terdapat:

self.pengunjung = pengunjung
self.destinasi = destinasi

Artinya, sebuah pemesanan memiliki hubungan dengan objek Pengunjung dan DestinasiWisata.

Relasi tersebut merupakan Asosiasi karena Pemesanan menggunakan objek Pengunjung dan DestinasiWisata yang sudah dibuat sebelumnya.

6.2 Agregasi

Relasi Agregasi diterapkan antara:

DestinasiWisata ◇-------- Pemandu

Objek Pemandu dibuat terlebih dahulu di luar class DestinasiWisata.

Contoh:

pemandu1 = Pemandu("Pak Budi", "Pendakian")
pemandu2 = Pemandu("Bu Sari", "Flora & Fauna")

Kemudian pemandu dimasukkan ke dalam destinasi:

destinasi.tambah_pemandu(pemandu1)
destinasi.tambah_pemandu(pemandu2)

Hal tersebut menunjukkan bahwa DestinasiWisata memiliki hubungan dengan beberapa Pemandu, tetapi objek Pemandu dibuat secara terpisah.

Relasi ini merupakan Agregasi.

6.3 Komposisi

Relasi Komposisi diterapkan antara:

Pemesanan ◆-------- Pembayaran

Pada class Pemesanan, objek Pembayaran dibuat langsung di dalam konstruktor:

self.pembayaran = Pembayaran(metode_bayar, total)

Artinya, objek Pembayaran merupakan bagian dari objek Pemesanan.

Relasi ini merupakan Komposisi.

7. Class Pemandu

Class Pemandu digunakan untuk menyimpan data pemandu wisata.

Atribut:

self.nama
self.spesialisasi

Method:

info()

Class Pemandu berhubungan dengan DestinasiWisata menggunakan relasi Agregasi.

8. Class DestinasiWisata

Class DestinasiWisata digunakan untuk menyimpan informasi destinasi wisata.

Atribut:

self.nama
self.lokasi
self.harga_dasar
self.kuota
self.daftar_pemandu

Method:

tambah_pemandu()
kurangi_kuota()
info()

Class ini memiliki relasi Agregasi dengan class Pemandu.

9. Class Pembayaran

Class Pembayaran digunakan untuk menyimpan informasi pembayaran tiket.

Atribut:

self.metode
self.jumlah
self.status

Method:

info()

Objek Pembayaran dibuat di dalam class Pemesanan, sehingga hubungan keduanya menerapkan relasi Komposisi.

10. Class Pemesanan

Class Pemesanan digunakan untuk mengelola proses pemesanan tiket.

Atribut:

self.kode
self.pengunjung
self.destinasi
self.jumlah_tiket
self.tanggal
self.pembayaran

Pada saat pemesanan dibuat, program menghitung harga tiket berdasarkan jenis pengunjung:

harga_satuan = pengunjung.hitung_harga_tiket(destinasi.harga_dasar)

Kemudian total harga dihitung berdasarkan jumlah tiket:

total = harga_satuan * jumlah_tiket

Setelah itu dibuat objek Pembayaran:

self.pembayaran = Pembayaran(metode_bayar, total)

11. Polimorfisme
Polimorfisme diterapkan melalui method:
hitung_harga_tiket()
Program memanggil method yang sama pada dua jenis objek pengunjung:

for p in (p1, p2):
    print(p.info())
    print(f"Harga tiket per orang: Rp{p.hitung_harga_tiket(destinasi.harga_dasar):,.0f}")

Hasilnya berbeda karena method tersebut telah di-override oleh masing-masing subclass.

PengunjungDomestik mendapatkan diskon 10%.
PengunjungMancanegara mendapatkan tarif 2 kali lipat.
12. Data yang Digunakan
Pemandu
Pak Budi
Spesialisasi: Pendakian

Bu Sari
Spesialisasi: Flora & Fauna
Destinasi Wisata
Nama        : Taman Hutan Raya
Lokasi      : Samarinda
Harga Dasar : Rp50.000
Kuota       : 100
Pengunjung Domestik
Nama        : Destiny
No. Telepon : 0812-3456-7890
NIK         : 6472010101010001
Kota Asal   : Samarinda
Pengunjung Mancanegara
Nama        : Kerensensia
No. Telepon : +44-7000-1234
No. Paspor  : X1234567
Negara Asal : Inggris
13. Contoh Pemesanan
Pemesanan 1
Kode         : TKT-001
Pengunjung   : Destiny
Destinasi    : Taman Hutan Raya
Jumlah Tiket : 3
Tanggal      : 10-10-2026
Metode Bayar : QRIS

Harga dasar tiket:

Rp50.000

Karena pengunjung merupakan pengunjung domestik, maka mendapatkan diskon 10%.

Harga setelah diskon:

Rp45.000

Total 3 tiket:

Rp135.000
Pemesanan 2
Kode         : TKT-002
Pengunjung   : Kerensensia
Destinasi    : Taman Hutan Raya
Jumlah Tiket : 2
Tanggal      : 11-10-2026
Metode Bayar : Kartu Kredit

Harga dasar tiket:

Rp50.000

Karena pengunjung merupakan pengunjung mancanegara, maka tarif menjadi dua kali lipat.

Harga tiket per orang:

Rp100.000

Total 2 tiket: Rp200.000

14. Output Program
Program menampilkan:
Data destinasi wisata.
Data pemandu wisata.
Data pengunjung domestik.
Data pengunjung mancanegara.
Harga tiket berdasarkan jenis pengunjung.
Hasil verifikasi PIN.
Data pemesanan tiket.
Informasi pembayaran.
Sisa kuota destinasi wisata.

15. Kesimpulan

Program Sistem Pemesanan Tiket Wisata Alam dan Manajemen Pengunjung telah menerapkan konsep Pemrograman Berorientasi Objek sesuai dengan ketentuan posttest.

Konsep Inheritance diterapkan dengan menggunakan Pengunjung sebagai Superclass dan PengunjungDomestik serta PengunjungMancanegara sebagai Subclass.

Program juga menerapkan penggunaan super().__init__(), atribut Protected, atribut Private, dan Method Overriding.

Selain itu, program menerapkan tiga Relasi UML, yaitu:

Asosiasi antara Pemesanan dengan Pengunjung dan DestinasiWisata.
Agregasi antara DestinasiWisata dengan Pemandu.
Komposisi antara Pemesanan dengan Pembayaran.

Dengan penerapan tersebut, program dapat menunjukkan hubungan antar-class serta penerapan Inheritance dan Polimorfisme pada sistem pemesanan tiket wisata alam.