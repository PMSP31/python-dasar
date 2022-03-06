# Latihan Percabangan ~ Kalkulator sederhana

# input
print(5*"=" + " KALKULATOR SEDERHANA " + 5*"=")
angka1 = float(input("Masukan angka 1 : "))
angka2 = float(input("Masukan angka 2 : "))

print(f"""
Operasi Penghitungan
1. Penjumlahan
2. Pengurangan
3. Pembagian
4. Perkalian
5. Modulus
6. Pangkat
""")
operasi = input("Pilih operasi penghitungan \n(gunakan angka: 1, 2, 3, dst) : ")

if operasi == "1" :
    hasil = angka1 + angka2
    print(f"\nHasil penjumlahan {angka1} + {angka2} = {hasil}")
elif operasi == "2" :
    hasil = angka1 - angka2
    print(f"\nHasil Pengurangan {angka1} - {angka2} = {hasil}")
elif operasi == "3" :
    hasil = angka1 / angka2
    print(f"\nHasil Pembagian {angka1} / {angka2} = {hasil}")
elif operasi == "4" :
    hasil = angka1 * angka2
    print(f"\nHasil perkalian {angka1} * {angka2} = {hasil}")
elif operasi == "5" :
    hasil = angka1 % angka2
    print(f"\nHasil Modulus {angka1} % {angka2} = {hasil}")
elif operasi == "6" :
    hasil = angka1 ** angka2
    print(f"\nHasil perpangkatan {angka1} ** {angka2} = {hasil}")
else :
    print("Input yang anda masukan salah !!!")

print("\nTerimakasih telah mencoba program ini :)")