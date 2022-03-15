# Unpack / membongkar item dari tuple

sayur = ("cabe","paprika","wortel")

# memasukan itemnya ke variable, item yang dimasukan sesuai urutannya
(merah, hijau, orange) = sayur
print(merah)
print(hijau)
print(orange)

# menggunakan *, memasukan banyak item pada 1 variable
print("\n")
sayur2 = ("cabe","paprika","wortel","tomat")
(merah, hijau, *orange) = sayur2 # penggunaannya tidak harus diakhir, bisa ditengah / diawal
print(merah)
print(hijau)
print(orange) #akan menjadi list
# print(type(orange))