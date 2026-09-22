# Sistem Pemesanan Tiket Wisata Alam dan Manajemen Pengunjung
K Destiana  2509106001 A1'25 Praktikum Pemrograman Berorientasi Objek

## Deskripsi
Program ini dibuat menggunakan Python dengan konsep OOP untuk mengelola data wisata, pengunjung, dan pemesanan tiket wisata alam.

## Class yang Digunakan
Program memiliki 3 class utama:

1. **Wisata**  
   Menyimpan nama wisata, lokasi, dan harga tiket.

2. **Pengunjung**  
   Menyimpan nama, umur, dan nomor telepon pengunjung.

3. **Pemesanan**  
   Mengatur kode pemesanan, data pengunjung, wisata, jumlah tiket, dan status pemesanan.

## Penerapan OOP
Program menerapkan beberapa materi OOP, yaitu:

- **Class dan Object** untuk membuat dan mengelola data.
- **Atribut dan Method** untuk menyimpan data dan menjalankan fungsi.
- **Class Attribute** untuk data yang digunakan bersama.
- **Instance Attribute** untuk data masing-masing object.
- **Instance Method** menggunakan `self`.
- **Class Method** menggunakan `@classmethod` dan `cls`.
- **Static Method** menggunakan `@staticmethod`.
- **Encapsulation** menggunakan private attribute seperti `__harga_tiket`, `__nomor_telepon`, dan `__jumlah_tiket`.
- **Property dan Setter** digunakan untuk mengakses serta mengubah data private dengan validasi.

## Pengujian
Program melakukan pengujian untuk:

- Membuat object dari setiap class.
- Menampilkan data wisata, pengunjung, dan pemesanan.
- Menggunakan class method dan static method.
- Mengubah data menggunakan setter dengan nilai yang valid.
- Menguji data yang tidak valid, seperti harga negatif, jumlah tiket 0, dan nomor telepon yang salah.

Contoh:

```python
wisata1.harga_tiket = -10000
```

Data tersebut akan ditolak karena harga tiket tidak boleh negatif.