class Kalkulator_penjumlahan:
    def __init__(self):
        self.angka1 = 0.0
        self.angka2 = 0.0
        self._hasil_penjumlahan = 0.0 

    def input_angka(self):
        self.angka1 = float(input("Masukkan angka pertama (integer/float): "))
        self.angka2 = float(input("Masukkan angka kedua (integer/float): "))

    def proses_penjumlahan(self):
        self._hasil_penjumlahan = self.angka1 + self.angka2

    def tampilkan_hasil_penjumlahan(self):  
        print("Hasil penjumlahan:", self._hasil_penjumlahan) 

program_penjumlahan = Kalkulator_penjumlahan()
program_penjumlahan.input_angka()
program_penjumlahan.proses_penjumlahan()
program_penjumlahan.tampilkan_hasil_penjumlahan()
