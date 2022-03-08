# For Loop

# menggunakan list
""" angka = [0,1,2,3,4]
print(angka)

for i in angka:
    print(f"i adalah = {i}")

print("akhir program 1 \n") """

# menggunakan range, range dimulai index ke 0
""" for i in range(6) :
    print(f"i adalah = {i}")

print("akhir program 2 \n") """

# range merubah index pertama
""" for i in range(1,10) : 
    print(f"i adalah = {i}")

print("akhir program 3 \n") """

# menggunakan string
""" data_str = "Paul mahardika"

for huruf in data_str : 
    print(huruf)

print("akhir program 4 \n") """

# While Loop
""" angka = 0 

while angka < 5 :
    print(angka)
    angka += 1
    # di python tidak bisa melakukan 'angka++'

print("end of program") """

# pass -> berfungsi sebagai dummy, tidak akan dieksekusi
""" angka = 0

while angka < 5 : 
    angka += 1
    if angka == 2 : 
        pass # ini tidak akan dieksekusi
    print(angka) """

# continue
""" angka = 0

while angka < 5 :
    angka += 1 # aksi 1

    if angka % 2 == 0 : 
        print("Buzz")
        continue # akan membuat loop loncat ke aksi 1

    print("Fizz") # aksi 2, karena ada continue diatas, maka langsung kembali ke aksi 1 'angka += 1' """

# break
angka = 0

while angka < 10 : 
    angka += 1

    if angka == 7 :
        print("KETEMU!!")
        break # akan menghentikan loop jika True

    print(angka)
