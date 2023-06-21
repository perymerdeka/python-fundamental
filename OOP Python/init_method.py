class PersegiPanjang:
    def __init__(self, p, l):
        self.p = p
        self.l = l

    def hitung_luas(self):
        return self.p * self.l

    def info(self):
        print(f"Hasil Perhitungan dari {self.p} dan {self.l} adalah {self.hitung_luas()}")


# definisi class
p1 = PersegiPanjang(10, 15)

# panggil method
p1.info()