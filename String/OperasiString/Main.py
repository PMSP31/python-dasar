# Operasi dan Manipulasi String

# 1. Menyambung String (concat)
""" awal = "Paul"
akhir = "Mahardika"

nama = awal + " " + akhir
print(nama) """

# 2. Menghitung panjang string / length
""" panjang = len(nama)
print("Panjang dari nama =" ,panjang) """

# Operator untuk string

# Cek char/string pada string, yang dicari harus sama persis
""" ul = "ul"
status = ul in nama
print(ul + " berada di nama = " + str(status))

pehul = "pehul"
status = pehul not in nama
print(pehul + " tidak berada di nama = " + str(status)) """

# perkalian string
""" print("paul"*4)
print(2*"gans") """

# indexing
""" print("index ke-0 : " + nama[0])
print("index ke-7 : " + nama[7]) """
# jika minus, maka diambil dari belakang
""" print("index ke-(-1) : " + nama[-1])
print("index ke-(-3) : " + nama[-3]) """
# pengambilan string dari index tertentu
""" print("index ke-[0:3] : " + nama[0:4])
print("index ke-[6:14] : " + nama[5:15])
print("index ke-[0,2,4,6] : " + nama[0:7:2]) """

# item
# mencari item terkecil
# print("item terkecil dari nama adalah = " + min(nama))
# mencari item terbesar
# print("item terbesar dari nama adalah = " + max(nama))

# cek ascii
""" ascii = ord('u')
print("ASCII code untuk u adalah " + str(ascii)) """

# method bawaan dari string
# count ~ menghitung panjang string
""" data = "ada panda disana ya"
jumlah = data.count("a")
print("jumlah a dari " + data + " adalah " + str(jumlah)) """

# Merubah case string
# Uppercase
salam = "ooyy!"
print(salam)
print(salam.upper())

# lowecase
salam = "HElllo!"
print(salam)
print(salam.lower())

# check isX method
salam = "haaii"
lower = salam.islower()
print(salam + " apakah lower? = " + str(lower))
upper = salam.isupper()
print(salam + " apakah upper? = " + str(upper))

# pengecheckan string
""" 
    isalpha -> mengecek semuanya huruf
    isalnum -> mengecek huruf dan angka
    isdecimal -> mengecek angka saja
    isspace -> mengecek spasi, tab, newline 
    istitle -> mengecek semua kata harus dimulai huruf besar
"""
judul = '"Belajar Python"'
cek_judul = judul.istitle()
print(judul + " apakah istitle? " + str(cek_judul))

huruf = 'abcdEFG' # tidak boleh ada spasi
cek_huruf = huruf.isalpha()
print(huruf + " apakah isalpha? " + str(cek_huruf))

alnum = 'paul123'
cek_alnum = alnum.isalnum()
print(alnum + " apakah isalnum? " + str(cek_alnum))

deci = '123'
cek_deci = deci.isdecimal()
print(deci + " apakah isdecimal? " + str(cek_deci))

space = "    "
cek_space = space.isspace()
print(space + " apakah isspace? " + str(cek_space))

# cek kata awal dan akhir string
cek_start = "Paul mahardika".startswith("Paul")
print("start = ", cek_start)
cek_end = "Paul mahardika".endswith("mahardika")
print("start = ", cek_end)

# join -> menggabungkan komponen string pada list
arr = ['Paul', 'Mahardika', '31']
print(arr)
hasil = ' '.join(arr)
print(hasil)

# split -> mengubah string menjadi list
str = "Kaki Kura-kura Kiri"
print(str)
print(str.split(' '))

# alokasi karakter
# rjust()
kanan = "KANAN".rjust(10,"#")
print("'"+kanan+"'")

# ljust
kiri = "KIRI".ljust(10,"*")
print("'"+kiri+"'")

# center
center = "TENGAH".center(20,'-')
print("'"+center+"'")

# strip
strip = center.strip("-") # -> menghilangkan karakter -
print("'"+strip+"'")
