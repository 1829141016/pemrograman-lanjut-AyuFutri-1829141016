from abc import ABCMeta, abstractmethod

class FakultasBahasa(metaclass=ABCMeta):
    @abstractmethod
    def cetakData(self):
        pass

class Binggris(FakultasBahasa):
    def __init__(self, fak, tahun_ajar, jumlah_mahasiswa):
        self.fak = fak
        self.tahun_ajar = tahun_ajar
        self.jumlah_mahasiswa = jumlah_mahasiswa

    def cetakData(self):
        print("Fakultas\t\t :", self.fak)
        print("Tahun Ajar\t\t :", self.tahun_ajar)
        print("jumlah mahasiswa\t :", self.jumlah_mahasiswa)

class sasing(FakultasBahasa):
    def __init__(self, fak, tahun_ajar, jumlah_mahasiswa, jurusan):
        self.fak = fak
        self.tahun_ajar = tahun_ajar
        self.jumlah_mahasiswa = jumlah_mahasiswa
        self.jurusan = jurusan
    def cetakData(self):
        print("Fakultas\t\t :", self.fak)
        print("Tahun Ajar\t\t :", self.tahun_ajar)
        print("Jumlah mahasiswa\t :", self.jumlah_mahasiswa)
        print("jurusan\t\t\t :", self.jurusan)

def main():
    obj = Binggris('FakultasBahasa', '2019', '85')
    print("BAHASA INGGRIS")
    obj.cetakData()

    del obj

    obj = sasing('FakultasBahasa', '2019', '90', 'mipa')
    print("\nSASTRA INGGRIS")
    obj.cetakData()

if __name__ == "__main__":
    main()
