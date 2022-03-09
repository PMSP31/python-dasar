# Operasi Logika atau Boolean

""" 
    - not
    - or
    - and
    - xor
"""

# Not Kebalikan data awal
print("==== NOT ====")
a = True
c = not a
print("Data boolean a =", a)
print("--------------- NOT")
print("Data boolean c =", c)

# OR jika salah satu True maka hasilnya True
print("==== OR ====")
a = False
b = False
c = a or b
print(a, "OR" , b, "=", c)
a = False
b = True
c = a or b
print(a, "OR" , b, " =", c)
a = True
b = False
c = a or b
print(a, " OR" , b, "=", c)
a = True
b = True
c = a or b
print(a, " OR" , b, " =", c)

# AND jika salah satu False maka hasilnya False, jika 2 True maka hasilnya True
print("==== AND ====")
a = False
b = False
c = a and b
print(a, "AND" , b, "=", c)
a = False
b = True
c = a and b
print(a, "AND" , b, " =", c)
a = True
b = False
c = a and b
print(a, " AND" , b, "=", c)
a = True
b = True
c = a and b
print(a, " AND" , b, " =", c)

# XOR jika salah satu True maka hasilnya True, sisanya False
print("==== XOR ====")
a = False
b = False
c = a ^ b
print(a, "XOR" , b, "=", c)
a = False
b = True
c = a ^ b
print(a, "XOR" , b, " =", c)
a = True
b = False
c = a ^ b
print(a, " XOR" , b, "=", c)
a = True
b = True
c = a ^ b
print(a, " XOR" , b, " =", c)