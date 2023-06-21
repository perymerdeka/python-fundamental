"""
self: object pada class

"""

class PersegiPanjang:
    def __init__(self, p, l):
        self.p = p
        self.l = l


    def hitung_luas(self):
        return f"Luas Persegi Panjang: {self.p * self.l}"


    def info(self):
        print(f"Hasil Perhitungan dari {self.p} dan {self.l} adalah {self.hitung_luas()}")

class Segitiga:
    def __init__(self, a, t):
        self.a = a
        self.t = t

    def hitung_luas(self):
        luas = self.a * self.t / 2
        return f"Luas Segitiga: {luas}"

    def info(self):
        print(f'Luas Dari Segitiga yang Alasnya {self.a} dan Tinggi {self.t} adalah {self.hitung_luas()}')



# p1 = PersegiPanjang()

# cetak info

# p1.info()

## hitung luas
# p1.hitung_persegi_panjang(10, 15)