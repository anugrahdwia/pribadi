# Nama = "Lian"
# Umur = 22
# Tinggi = 170.5

# x = f"Nama saya {Nama}, umur saya {Umur} tahun dan tinggi saya {Tinggi} cm."
# print(x)

nama = []
umur = []
tinggi = []

for x in range(1):
    nama.append(input("Nama: "))
    umur.append(input("Umur: "))
    tinggi.append(input("Tinggi: "))
    print()
for x in range(1):
    print ("Nama saya", nama[x] + ", umur saya", umur[x], "tahun dan tinggi saya", tinggi[x], "cm.")