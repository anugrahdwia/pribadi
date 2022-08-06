# a = float(input("Nilai Ujian Teori: "))
# b = float(input("Nilai Ujian Praktek: "))
# c = 70
# print()
# if c > a:
#     print("Anda harus mengulang ujian teori")
# if c > b:
#     print("Anda harus mengulang ujian praktek")
# else:
#     print("Selamat, anda lulus")

a = float(input("Nilai Ujian Teori: "))
b = float(input("Nilai Ujian Praktek: "))
c = 70
print()
if c > a and c > b:
    print("Anda harus mengulang ujian teori dan praktek")
else:
    if c <= a and c > b:
        print("Anda harus mengulang ujian praktek")
    else:
        if c <= b and c > a:
            print("Anda harus mengulang ujian teori")
        else:
            print("Selamat, anda lulus")