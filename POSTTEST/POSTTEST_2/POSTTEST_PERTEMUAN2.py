# ============================================================
# POSTTEST PBO
# Sistem Pemesanan Tiket Wisata Alam dan Manajemen Pengunjung
# ============================================================


# ============================================================
# SUPERCLASS
# ============================================================

class Pengunjung:
    """
    Superclass (Parent Class) untuk semua jenis pengunjung.
    """

    def __init__(self, nama, no_telepon, pin):
        # Protected attribute
        self._nama = nama
        self._no_telepon = no_telepon

        # Private attribute
        self.__pin = pin

    def verifikasi_pin(self, pin):
        """
        Memeriksa PIN pengunjung.
        Atribut __pin bersifat private sehingga
        tidak dapat diakses langsung dari luar class.
        """
        return self.__pin == pin

    def get_nama(self):
        return self._nama

    def hitung_harga_tiket(self, harga_dasar):
        """
        Method yang akan di-override oleh subclass.
        """
        return harga_dasar

    def info(self):
        return (
            f"Pengunjung: {self._nama} | "
            f"Telp: {self._no_telepon}"
        )


# ============================================================
# SUBCLASS 1
# ============================================================

class PengunjungDomestik(Pengunjung):
    """
    Subclass untuk pengunjung dalam negeri.
    Mendapatkan diskon 10%.
    """

    DISKON = 0.10

    def __init__(self, nama, no_telepon, pin, nik, kota_asal):

        # Memanggil constructor superclass
        super().__init__(nama, no_telepon, pin)

        # Atribut unik subclass
        self.nik = nik
        self.kota_asal = kota_asal

    def hitung_harga_tiket(self, harga_dasar):
        """
        Overriding method hitung_harga_tiket().
        Pengunjung domestik mendapatkan diskon 10%.
        """
        return harga_dasar - (harga_dasar * self.DISKON)

    def info(self):
        """
        Overriding method info().
        """
        return (
            f"[Domestik] {self._nama} | "
            f"Telp: {self._no_telepon} | "
            f"NIK: {self.nik} | "
            f"Asal: {self.kota_asal}"
        )


# ============================================================
# SUBCLASS 2
# ============================================================

class PengunjungMancanegara(Pengunjung):
    """
    Subclass untuk pengunjung mancanegara.
    Tarif tiket adalah 2x harga dasar.
    """

    PENGALI_TARIF = 2

    def __init__(
        self,
        nama,
        no_telepon,
        pin,
        no_paspor,
        negara_asal
    ):

        # Memanggil constructor superclass
        super().__init__(nama, no_telepon, pin)

        # Atribut unik subclass
        self.no_paspor = no_paspor
        self.negara_asal = negara_asal

    def hitung_harga_tiket(self, harga_dasar):
        """
        Overriding method hitung_harga_tiket().
        Pengunjung mancanegara membayar 2x harga dasar.
        """
        return harga_dasar * self.PENGALI_TARIF

    def info(self):
        """
        Overriding method info().
        """
        return (
            f"[Mancanegara] {self._nama} | "
            f"Telp: {self._no_telepon} | "
            f"Paspor: {self.no_paspor} | "
            f"Negara: {self.negara_asal}"
        )


# ============================================================
# CLASS PEMANDU
# ============================================================

class Pemandu:
    """
    Class Pemandu.

    Pemandu dibuat secara terpisah dari DestinasiWisata,
    kemudian dimasukkan ke dalam objek destinasi.
    Hal ini menunjukkan hubungan AGREGASI.
    """

    def __init__(self, nama, spesialisasi):
        self.nama = nama
        self.spesialisasi = spesialisasi

    def info(self):
        return f"{self.nama} ({self.spesialisasi})"


# ============================================================
# CLASS DESTINASI WISATA
# ============================================================

class DestinasiWisata:
    """
    Class untuk menyimpan informasi destinasi wisata.
    """

    def __init__(self, nama, lokasi, harga_dasar, kuota):
        self.nama = nama
        self.lokasi = lokasi
        self.harga_dasar = harga_dasar
        self.kuota = kuota

        # Menyimpan objek Pemandu
        self.daftar_pemandu = []

    def tambah_pemandu(self, pemandu):
        """
        Menambahkan objek Pemandu ke destinasi.

        Hubungan dengan Pemandu merupakan AGREGASI
        karena objek Pemandu dibuat di luar class ini.
        """
        self.daftar_pemandu.append(pemandu)

    def kurangi_kuota(self, jumlah):
        """
        Mengurangi kuota destinasi berdasarkan
        jumlah tiket yang dipesan.
        """
        if jumlah <= self.kuota:
            self.kuota -= jumlah
            return True

        return False

    def info(self):
        """
        Menampilkan informasi destinasi.
        """

        if self.daftar_pemandu:
            pemandu = ", ".join(
                p.info() for p in self.daftar_pemandu
            )
        else:
            pemandu = "-"

        return (
            f"{self.nama} - {self.lokasi} | "
            f"Harga dasar: Rp{self.harga_dasar:,.0f} | "
            f"Sisa kuota: {self.kuota} | "
            f"Pemandu: {pemandu}"
        )


# ============================================================
# CLASS PEMBAYARAN
# ============================================================

class Pembayaran:
    """
    Class Pembayaran.

    Objek Pembayaran dibuat langsung di dalam Pemesanan.
    Hubungan ini merupakan KOMPOSISI.
    """

    def __init__(self, metode, jumlah):
        self.metode = metode
        self.jumlah = jumlah
        self.status = "Lunas"

    def info(self):
        return (
            f"{self.metode} - "
            f"Rp{self.jumlah:,.0f} "
            f"({self.status})"
        )


# ============================================================
# CLASS PEMESANAN
# ============================================================

class Pemesanan:
    """
    Class untuk mengelola pemesanan tiket.

    Hubungan:
    - Asosiasi dengan Pengunjung
    - Asosiasi dengan DestinasiWisata
    - Komposisi dengan Pembayaran
    """

    def __init__(
        self,
        kode,
        pengunjung,
        destinasi,
        jumlah_tiket,
        tanggal,
        metode_bayar
    ):

        self.kode = kode

        # ====================================================
        # ASOSIASI
        # ====================================================
        # Pemesanan berhubungan dengan Pengunjung
        # dan DestinasiWisata.
        self.pengunjung = pengunjung
        self.destinasi = destinasi

        self.jumlah_tiket = jumlah_tiket
        self.tanggal = tanggal

        # ====================================================
        # POLIMORFISME
        # ====================================================
        # Method hitung_harga_tiket() akan menjalankan
        # versi sesuai subclass pengunjung.
        harga_satuan = pengunjung.hitung_harga_tiket(
            destinasi.harga_dasar
        )

        total = harga_satuan * jumlah_tiket

        # ====================================================
        # KOMPOSISI
        # ====================================================
        # Objek Pembayaran dibuat langsung di dalam
        # objek Pemesanan.
        self.pembayaran = Pembayaran(
            metode_bayar,
            total
        )

    def cetak_tiket(self):
        """
        Menampilkan detail tiket pemesanan.
        """

        print("=" * 60)
        print("                 TIKET WISATA")
        print("=" * 60)

        print(f"Kode tiket : {self.kode}")
        print(f"Atas nama  : {self.pengunjung.get_nama()}")
        print(
            f"Destinasi  : {self.destinasi.nama} "
            f"({self.destinasi.lokasi})"
        )
        print(f"Tanggal    : {self.tanggal}")
        print(f"Jumlah     : {self.jumlah_tiket} tiket")
        print(f"Pembayaran : {self.pembayaran.info()}")

        print("=" * 60)


# ============================================================
# PROGRAM UTAMA
# ============================================================

if __name__ == "__main__":

    # ========================================================
    # AGREGASI
    # ========================================================
    # Objek Pemandu dibuat secara terpisah.
    # Setelah itu dimasukkan ke DestinasiWisata.

    pemandu1 = Pemandu(
        "Pak Budi",
        "Pendakian"
    )

    pemandu2 = Pemandu(
        "Bu Sari",
        "Flora & Fauna"
    )

    # ========================================================
    # OBJECT DESTINASI
    # ========================================================

    destinasi = DestinasiWisata(
        "Taman Hutan Raya",
        "Samarinda",
        50000,
        100
    )

    # Menambahkan pemandu ke destinasi
    destinasi.tambah_pemandu(pemandu1)
    destinasi.tambah_pemandu(pemandu2)

    # ========================================================
    # MENAMPILKAN DATA DESTINASI
    # ========================================================

    print()
    print("=== DATA DESTINASI ===")
    print(destinasi.info())

    # ========================================================
    # INHERITANCE
    # ========================================================
    # Membuat object dari dua subclass.

    p1 = PengunjungDomestik(
        "Destiny",
        "0812-3456-7890",
        "1234",
        "6472010101010001",
        "Samarinda"
    )

    p2 = PengunjungMancanegara(
        "Kerensensia",
        "+44-7000-1234",
        "9999",
        "X1234567",
        "Inggris"
    )

    # ========================================================
    # POLIMORFISME
    # ========================================================
    # Object p1 dan p2 sama-sama memanggil method info()
    # dan hitung_harga_tiket(), tetapi hasilnya berbeda
    # sesuai subclass masing-masing.

    print()
    print("=== DATA PENGUNJUNG ===")

    for p in (p1, p2):

        print(p.info())

        harga = p.hitung_harga_tiket(
            destinasi.harga_dasar
        )

        print(
            f"Harga tiket per orang: "
            f"Rp{harga:,.0f}"
        )

    # ========================================================
    # ENCAPSULATION
    # ========================================================
    # __pin merupakan atribut private.
    # Akses langsung dari luar class akan gagal.

    print()
    print("=== UJI ATRIBUT PRIVATE ===")

    try:
        print(p1.__pin)

    except AttributeError as e:
        print(
            "Akses langsung ke __pin gagal:"
        )
        print(e)

    # Verifikasi menggunakan method khusus
    print(
        "Verifikasi PIN benar :",
        p1.verifikasi_pin("1234")
    )

    print(
        "Verifikasi PIN salah :",
        p1.verifikasi_pin("0000")
    )

    # ========================================================
    # PEMESANAN 1
    # ========================================================
    # ASOSIASI:
    # Pemesanan berhubungan dengan Pengunjung dan Destinasi.

    pesanan1 = Pemesanan(
        "TKT-001",
        p1,
        destinasi,
        3,
        "10-10-2026",
        "QRIS"
    )

    # Mengurangi kuota destinasi
    destinasi.kurangi_kuota(
        pesanan1.jumlah_tiket
    )

    print()
    print("=== PEMESANAN 1 ===")
    pesanan1.cetak_tiket()

    # ========================================================
    # PEMESANAN 2
    # ========================================================

    pesanan2 = Pemesanan(
        "TKT-002",
        p2,
        destinasi,
        2,
        "11-10-2026",
        "Kartu Kredit"
    )

    # Mengurangi kuota destinasi
    destinasi.kurangi_kuota(
        pesanan2.jumlah_tiket
    )

    print()
    print("=== PEMESANAN 2 ===")
    pesanan2.cetak_tiket()

    # ========================================================
    # SISA KUOTA
    # ========================================================

    print()
    print(
        f"Sisa kuota {destinasi.nama}: "
        f"{destinasi.kuota}"
    )

    # ========================================================
    # BUKTI AGREGASI
    # ========================================================
    # Pemandu dibuat secara terpisah dari destinasi.
    # Oleh karena itu objek Pemandu tetap dapat digunakan
    # secara independen.

    print()
    print("=== BUKTI AGREGASI ===")
    print(
        "Pemandu tetap dapat digunakan "
        "secara independen:"
    )

    print(pemandu1.info())
    print(pemandu2.info())