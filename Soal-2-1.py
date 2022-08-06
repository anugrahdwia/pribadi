#muncul menu
list = ["Selamat Datang!"," ", "--Menu--", "1. Daftar Kontak", "2. Tambah Kontak", "3. Keluar", " "]

for x in list:
    print(x)

a = int(input("Pilih Menu: "))
print()

if a == 1:                                                  #menu 1
    daftar = ["Daftar Kontak:", "Nama: Wahyu", "No Telepon: 08123456789", "Nama: Wardhana", "No Telepon: 08987654321"]
    for z in daftar:
        print(z)
else:
    if a == 2:                                             #menu 2
        nama = []
        telepon = []
        for y in range(1):
            nama.append(input("Nama: "))
            telepon.append(input("No Telepon: "))
        for y in range(1):
            print("Kontak Berhasil Ditambahkan")
    else:
        if a == 3:                                          #menu 3
            print("Program selesai, sampai jumpa!")
        else:
            if a < 1 or a > 3:                              #menu 4
                print("Menu tidak tersedia")
