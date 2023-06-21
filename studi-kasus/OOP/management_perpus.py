class Perpustakaan:
    def __init__(self, Judul,no_buku):
        self.judul = str(judul)
        self.nomor = str(no_buku)

    def getJudul(self):
        return self.judul
    def getNomor(self):
        return self.nomor
    def setJudul(self, judul):
        self.judul = judul
    def setNomor(self, no_buku):
        self.nomor = no_buku

Daftar_buku = {}
loop = True

print("====================================")
print("             Daftar Perpustakaan                    ")
print("====================================")
print("                 MENU          ")
print("1. Tambah Buku      =")
print("2. Hapus Buku       =")
print("3. Tampilkan Daftar Buku     =")
print("4. Cari Buku                 =")
print("5. Edit Judul Buku           =")
print("6. Edit Nomor Buku           =")
print("7. Jumlah Total Buku         =")
print("0. Exit/Keluar               =")
print("=====================================")

while(loop):
    print("\n\n")
    menu = input("Masukan Menu : ")

    if menu == "1":
        judul = input("Masukan judul : ")
        nomor = input("Masukan Nomor Buku : ")
        book = Perpustakaan(judul, nomor)
        Daftar_buku[nomor] = book
    elif menu == "2":
        nomor = input("Masukan Nomor Buku : ")
        if(nomor in Daftar_buku):
            del Daftar_buku[nomor]
        else:
                print("Data Tidak Ditemukan")
    elif menu == "3":
        for x in Daftar_buku:
            print("Judul Buku : ", Daftar_buku[x].getJudul())
            print("Nomor Buku : ", Daftar_buku[x].getNomor())
    elif menu == "4":
        nomor = input("Masukan Nomor Buku : ")
        if (nomor in Daftar_buku):
            print("Judul Buku : ", Daftar_buku[nomor].getJudul())
            print("Nomor Buku : ", Daftar_buku[nomor].getNomor())
        else:
            print("Data Tidak Ditemukan")
    elif menu == "5":
        nomor = input("Masukan Nomor Buku : ")
        if(nomor in Daftar_buku):
            judulBaru = input("Masukan Judul Baru : ")
            Daftar_buku[nomor].setJudul(judulBaru)
        else:
            print("Data Tidak Ditemukan")
    elif menu == "6":
        nomor = input("Masukan Nomor Buku : ")
        if(nomor in Daftar_buku):
            nomorBaru = input("Masukan Nomor Buku Baru : ")
            Daftar_buku[nomor].setNomor(nomorBaru)
        else:
            print("Data Tidak Ditemukan")
    elif menu == "7":
        print("Jumlah Total Buku : ", len(Daftar_buku))
    elif menu == "0":
        loop = False
    else:
        print("Perintah Tidak Ditemukan ( Aplication By Feri Lukmansyah)")
