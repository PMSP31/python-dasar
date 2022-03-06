# Date & Time
import datetime as dt

""" today = dt.date.today()
print(today)
print(f"today is {today:%A}") """

# latihan
print("Masukan Tanggal, \nBulan, dan Tahun kelahiran anda.\n")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(tanggal_lahir)
print(f"Hari kelahiran anda adalah : {tanggal_lahir:%A} \n")

# menghitung umur
today = dt.date.today()
print(f"Saat ini : {today}")
umur_hari = today - tanggal_lahir
umur_bulan = (umur_hari.days % 365) // 30
umur_tahun = umur_hari.days // 365

print(f"Umur anda saat ini : {umur_tahun} tahun, {umur_bulan} bulan, {umur_hari.days} hari.")