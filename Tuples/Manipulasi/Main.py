# Manipulasi Tuple

# Mengakses item
# 1. berdasarkan index
tuple1 = ("Toyota","BMW","Mercedes-Benz","Chevrolet","Yamaha","Suzuki")
print(tuple1)
print(f"item index ke-0 = {tuple1[0]}")

# 2. Negative indexing
print(f"item index ke-(-1) = {tuple1[-1]}")

# 3. Range index
# [dimulai dari index : sebelum index]
# dimulai dari index 2 sampai sebelum index 5, jadi datanya 2,3,4
print(f"item dari index ke-(2-4) = {tuple1[2:5]}")
print(f"item berakhir sebelum index ke-4 = {tuple1[:4]}")
print(f"item dari index ke-3 = {tuple1[3:]}")
# range of negative index
print(f"item dari index ke-((-5)-(-2)) = {tuple1[-5:-2]}")

# 4. Check item pada tuple 
if "Toyota" in tuple1 : 
    print("Yeah, Toyota ada di tuple!")


# Mengubah item pada tuple
# convert tuple ke list untuk mengubah itemnya, lalu convert lagi ke tuple
print("\nMengubah data tuple")
tuple1 = ("Toyota","BMW","Mercedes-Benz","Chevrolet","Yamaha","Suzuki")
print(f"sebelum = {tuple1}")
x = list(tuple1)
x[3] = "Porsche"
y = tuple(x)

print(f"setelah = {y}")

# Menambah item
buah = ("Apel","Pisang","Pepaya")
print(f"sebelum = {buah}")
b = list(buah)
b.append("Jeruk")
buah = tuple(b)
print(f"sesudah = {buah}")

# menambah item tanpa mengconvert ke list
z = ("Salak",)
buah += z
print(f"tanpa convert ke list = {buah}")

# menghapus item
b = list(buah)
b.remove("Salak")
buah = tuple(b)
print(f"menghapus item = {buah}")

# menghapus seluruh tuple 
# del buah
# print(buah) # -> akan error jika di print

# JOIN & MULTIPLY TUPLE
# Join ~ menggabungkan 2 tuple
tuple1 = ("a","b","c")
tuple2 = (1,2,3)

# menggunakan +
tupleJoin = tuple1 + tuple2
print(tupleJoin)

# Multiply ~ Mengkalikan item pada tuple
multiTuple = tuple1 * 3
print(multiTuple)

# METHODS
# count ~ menghitung total duplikasi item pada tuple
angka = (1,4,1,3,1,5,6,7,4)
print(angka)
print(f"count 1 pada angka = {angka.count(1)} ")
# index ~ mencari index item yang sesuai pada tuple
print(f"index item 4 pada angka = {angka.index(4)}")