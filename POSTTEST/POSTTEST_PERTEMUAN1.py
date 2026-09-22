class Wisata:
    nama_sistem = "Sistem Wisata Alam"
    jumlah_wisata = 0
    mata_uang = "Rupiah"

    def __init__(self, nama, lokasi, harga_tiket):
        self.nama = nama
        self.lokasi = lokasi
        self.__harga_tiket = 0
        self.harga_tiket = harga_tiket
        Wisata.jumlah_wisata += 1

    @property
    def harga_tiket(self):
        return self.__harga_tiket

    @harga_tiket.setter
    def harga_tiket(self, harga):
        if harga < 0:
            raise ValueError("Harga tiket tidak boleh negatif.")
        self.__harga_tiket = harga

    def tampilkan_info(self):
        print(f"{self.nama} - {self.lokasi} - Rp{self.harga_tiket:,}")

    @classmethod
    def tambah_wisata(cls, data):
        return cls(data["nama"], data["lokasi"], data["harga_tiket"])

    @staticmethod
    def format_harga(harga):
        return f"Rp{harga:,}".replace(",", ".")

class Pengunjung:
    nama_sistem = "Manajemen Pengunjung"
    jumlah_pengunjung = 0
    status_default = "Aktif"

    def __init__(self, nama, umur, nomor_telepon):
        self.nama = nama
        self.umur = umur
        self.__nomor_telepon = ""
        self.nomor_telepon = nomor_telepon
        Pengunjung.jumlah_pengunjung += 1

    @property
    def nomor_telepon(self):
        return self.__nomor_telepon

    @nomor_telepon.setter
    def nomor_telepon(self, nomor):
        if not Pengunjung.validasi_nomor(nomor):
            raise ValueError("Nomor telepon harus 10-13 digit.")
        self.__nomor_telepon = nomor

    def tampilkan_data(self):
        print(f"{self.nama} - {self.umur} tahun - {self.nomor_telepon}")

    @classmethod
    def dari_data(cls, data):
        return cls(
            data["nama"],
            data["umur"],
            data["nomor_telepon"]
        )

    @staticmethod
    def validasi_nomor(nomor):
        return nomor.isdigit() and 10 <= len(nomor) <= 13


class Pemesanan:
    nama_sistem = "Sistem Pemesanan Tiket"
    jumlah_pemesanan = 0
    status_default = "Diproses"

    def __init__(self, kode, pengunjung, wisata, jumlah_tiket):
        self.kode = kode
        self.pengunjung = pengunjung
        self.wisata = wisata
        self.__jumlah_tiket = 0
        self.jumlah_tiket = jumlah_tiket
        self.status = "Diproses"
        Pemesanan.jumlah_pemesanan += 1

    @property
    def jumlah_tiket(self):
        return self.__jumlah_tiket

    @jumlah_tiket.setter
    def jumlah_tiket(self, jumlah):
        if jumlah < 1:
            raise ValueError("Jumlah tiket minimal 1.")
        self.__jumlah_tiket = jumlah

    def hitung_total(self):
        return self.wisata.harga_tiket * self.jumlah_tiket

    def tampilkan_pemesanan(self):
        print(f"Kode     : {self.kode}")
        print(f"Pengunjung: {self.pengunjung.nama}")
        print(f"Wisata   : {self.wisata.nama}")
        print(f"Tiket    : {self.jumlah_tiket}")
        print(f"Total    : {Wisata.format_harga(self.hitung_total())}")
        print(f"Status   : {self.status}")

    @classmethod
    def buat_pemesanan(cls, kode, pengunjung, wisata, jumlah):
        return cls(kode, pengunjung, wisata, jumlah)

    @staticmethod
    def cek_jumlah_tiket(jumlah):
        return jumlah >= 1

wisata1 = Wisata("Gunung S", "Kutai Barat", 25000)
wisata2 = Wisata("Pulau Kelapa", "Kutai barat", 50000)

wisata1.tampilkan_info()
wisata2.tampilkan_info()

wisata3 = Wisata.tambah_wisata({
    "nama": "Danau Jempang",
    "lokasi": "Kutai Barat",
    "harga_tiket": 30000
})

pengunjung1 = Pengunjung("Destiana", 20, "081234567890")
pengunjung2 = Pengunjung("Kerensensia", 21, "082345678901")

pengunjung1.tampilkan_data()
pengunjung2.tampilkan_data()

pengunjung3 = Pengunjung.dari_data({
    "nama": "Billie Eilish",
    "umur": 20,
    "nomor_telepon": "083456789012"
})

pesanan1 = Pemesanan("PSN001", pengunjung1, wisata1, 2)
pesanan2 = Pemesanan("PSN002", pengunjung2, wisata2, 3)

pesanan1.tampilkan_pemesanan()
pesanan2.tampilkan_pemesanan()

pesanan3 = Pemesanan.buat_pemesanan(
    "PSN003", pengunjung3, wisata3, 1
)

pesanan3.tampilkan_pemesanan()


print("\n--- STATIC METHOD ---")
print(Pengunjung.validasi_nomor("081234567890"))
print(Pemesanan.cek_jumlah_tiket(2))
print(Wisata.format_harga(50000))

print("\n--- SETTER VALID ---")

pesanan1.jumlah_tiket = 4
print("Jumlah tiket:", pesanan1.jumlah_tiket)

wisata1.harga_tiket = 30000
print("Harga tiket:", Wisata.format_harga(wisata1.harga_tiket))

print("\n--- SETTER TIDAK VALID ---")

try:
    wisata1.harga_tiket = -10000
except ValueError as e:
    print(e)

try:
    pesanan1.jumlah_tiket = 0
except ValueError as e:
    print(e)

try:
    pengunjung1.nomor_telepon = "abc"
except ValueError as e:
    print(e)

print("\n--- CLASS ATTRIBUTE ---")
print("Jumlah wisata:", Wisata.jumlah_wisata)
print("Jumlah pengunjung:", Pengunjung.jumlah_pengunjung)
print("Jumlah pemesanan:", Pemesanan.jumlah_pemesanan)