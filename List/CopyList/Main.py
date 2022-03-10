# Teknik Duplikasi List

a = ['Dika', 'Putra', 'Samsul']
print(f"a = {a}")

b = a # pass by reference 
print(f"b = {b}")

# akan merubah kedua list
a[0] = "Jack"
print(f"a = {a}")
print(f"b = {b}")

# addres kedua list sama
print(f"addres a = {hex(id(a))}")
print(f"addres b = {hex(id(b))}")

# duplikasi data yang Benar
print("\nDuplikasi dengan copy()")
c = a.copy() # full duplikat / data baru
print(f"addres a = {hex(id(a))}")
print(f"addres b = {hex(id(b))}")
print(f"addres c = {hex(id(c))}")

# karena menggunakan copy, maka data c tidak akan merubah data a
c[1] = "Mike"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
a[1] = "Edward"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")