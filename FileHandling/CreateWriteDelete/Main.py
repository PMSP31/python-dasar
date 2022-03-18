# Create, Write, Delete File

# Append / menambahkan content pada file yang telah ada
""" f = open("FileHandling/coba.txt", 'a')
f.write("\nMenambakan content baru!")
f.close()

# read
f = open("FileHandling/coba.txt",'r')
print(f.read()) """

# Write / menimpa content pada file jika telah ada, jika tidak ada buat file baru
""" f = open("FileHandling/demo.txt", "w")
f.write("Mengganti Contentnya")
f.close()

f = open("FileHandling/demo.txt", "r")
print(f.read()) """

# Create / membuat file, jika file telah ada akan error
# f = open("FileHandling/buat.txt","x") # jika ini dijalankan lagi, akan error karena file buat.txt sudah ada.

# Menghapus file
# menggunakan module
import os
# check file exists?
if os.path.exists("FileHandling/buat.txt"):
    os.remove("FileHandling/buat.txt")
else:
    print("File Tidak ditemukan.")

# membuat folder
# os.mkdir("FileHandling/dirBaru")

# menghapus folder
# os.rmdir("FileHandling/dirBaru")