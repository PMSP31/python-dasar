# File Handling Python

# open() ~ function yang digunakan untuk file handling
# memiliki 2 paramater open(filename, mode)
""" 
    mode :
    * "r" ~ Read - Default Value = Membuka file untuk dibaca, error jika file tidak ditemukan
    * "a" ~ Append = Membuka File untuk menambahkan, buat file baru jika tidak ada
    * "w" ~ Write = Membuka file untuk ditulis, buat file baru jika tidak ada
    * "x" ~ Create = Membuat file yang ditentukan, error jika file sudah ada
"""

# membuka file
# jika ini dijalankan di Terminal biasa akan error, tetapi jika dijalankan di VSCode akan jalan.
f = open("FileHandling/coba.txt", "r")
# read() ~ digunakan untuk membaca content dari file
# print(f.read())
# membaca beberapa char saja
# print(f.read(5))

# readline()
""" print(f.readline())
print(f.readline()) """

# Loop
for x in f :
    print(x)

# close() ~ digunakan untuk menutup file
f.close()