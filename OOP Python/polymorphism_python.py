from rumus import Segitiga, PersegiPanjang

# definisikan class
s1 = Segitiga(10, 15)
p1 = PersegiPanjang(10, 15)
daftar_bangun_ruang = []

# tambah item
daftar_bangun_ruang.append(s1)
daftar_bangun_ruang.append(p1)

print('Contoh Polomorphism')

for data in daftar_bangun_ruang:
    print(f'Luas:  {data.hitung_luas()}')