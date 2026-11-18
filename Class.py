class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, jurusan):
        self.__nama = nama
        self.nim = nim
        self.jurusan = jurusan
        Mahasiswa.jumlah_mahasiswa += 1

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, nama_baru):
        self.__nama = nama_baru

    def tampil_data(self):
        print(f"Nama    : {self.__nama}")
        print(f"NIM     : {self.nim}")
        print(f"Jurusan : {self.jurusan}")

    @classmethod
    def total_mahasiswa(cls):
        print(f"Jumlah Mahasiswa: {cls.jumlah_mahasiswa}")

    @staticmethod
    def info():
        print("Program Sistem Data Mahasiswa")


class Kampus:
    def __init__(self, nama_kampus):
        self.nama_kampus = nama_kampus
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)

    def tampil_semua(self):
        print(f"\nDaftar Mahasiswa {self.nama_kampus}")
        for mhs in self.daftar_mahasiswa:
            mhs.tampil_data()
            print("-" * 20)


Mahasiswa.info()

mhs1 = Mahasiswa("Budi", "231001", "Informatika")
mhs2 = Mahasiswa("Siti", "231002", "Sistem Informasi")
mhs3 = Mahasiswa("Asep", "231003", "Teknik Industri")
mhs4 = Mahasiswa("Joko", "231005", "Teknik Sipil")
mhs5 = Mahasiswa("Bowo", "231004", "Teknik Sawit")

kampus = Kampus("Universitas Bina Bangsa")

kampus.tambah_mahasiswa(mhs1)
kampus.tambah_mahasiswa(mhs2)
kampus.tambah_mahasiswa(mhs3)
kampus.tambah_mahasiswa(mhs4)
kampus.tambah_mahasiswa(mhs5)

kampus.tampil_semua()

Mahasiswa.total_mahasiswa()