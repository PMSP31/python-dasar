# Format String

# String
nama = "Paul"
salam = f"Hello saya {nama}"
print(salam)

# Boolean
boolean = True
format_bol = f"Cukup Umur ? {boolean}"
print(format_bol)

# integer
umur = 17
salam =  f"Umur saya {umur} tahun."
print(salam)

# pembulatan integer
angka = 15
pembulatan = f"pembulatan = {angka:d}"
print(pembulatan)

# format ribuan, jutaan, dst
ribuan = 1500
format_rb = f"ribuan = {ribuan:,}"
print(format_rb)

jutaan = 1500000
format_jt = f"jutaan = {jutaan:,}"
print(format_jt)

# float
decimal = 12345.54321
format_fl = f"Decimal = {decimal:.3f}"
print(format_fl)

# leading zero
decimal = 12345.54321
format_fl = f"Decimal = {decimal:010.3f}"
print(format_fl)

# menampilkan tanda + dan -
angka_min = -23
angka_pls = 10
format_min = f"minus = {angka_min:+d}"
format_pls = f"plus = {angka_pls:+d}"
print(format_min)
print(format_pls)

# aritmatika
harga = 12000
jumlah = 6
total = f"Harga Total = Rp. {harga * jumlah:,}"
print(total)

# binary, octal, hex
angka = 123
format_binary = f"Binary = {bin(angka)}"
format_octal = f"Octal = {oct(angka)}"
format_hex = f"Hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)