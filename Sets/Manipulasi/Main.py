# Memanipulasi item pada sets

# Mengakses / mengambil item
# set tidak memiliki index atau key, maka untuk mengambil datanya harus di looping
buah = {"Apel","Pisang","Durian"}
for x in buah : 
    print(x)
# mengecek apakah item terdapat pada sets
print("Pisang" in buah)

# Menambah item ~ method add()
buah.add("Jeruk")
print(buah)

# Menggabungkan set ~ method update()
buah2 = {"Nanas","Semangka","Bengkoang"}
buah.update(buah2)
print(buah)

# update() tidak harus sets, bisa juga iterable object lainnya(list,tuples,dictionaries,dll)
buah3 = ["Kiwi","Rambutan"]
buah.update(buah3)
print(buah)

# menghapus item ~ method remove()
buah.remove("Rambutan") # jika item tidak ada di sets, akan error
print(buah)

# method discard()
buah.discard("Semangka") # jika tidak ada item di sets, tidak akan error
print(buah)

# method pop(), pop akan menghapus item terakhir tetapi karena sets ini unordered, maka yang dihapus akan acak/random
x = buah.pop()
print(x)
print(buah)

# mengosongkan sets ~ method clear()
buah2.clear()
print(buah2)

# delete set ~ del
# del buah 
print(buah) # akan error jika di print, karena sudah langsung terhapus