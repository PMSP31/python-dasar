# Operasi Komparasi

""" 
    Hasil dari operasi komparasi adalah boolean
    - <
    - >
    - >=
    - <=
    - ==
    - !=
    - is ~ membandingkan object identity
    - is not
"""

a = 10
b = 2

hasil = a > b
print(a, ">", b, "=", hasil)

hasil = a < b
print(a, "<", b, "=", hasil)

hasil = a >= b
print(a, ">=", b, "=", hasil)

hasil = a <= b
print(a, "<=", b, "=", hasil)

hasil = a == b
print(a, "==", b, "=", hasil)

hasil = a != b
print(a, "!=", b, "=", hasil)

x = 5
y = 5
print("x =", x, "id =", hex(id(x)))
print("y =", y, "id =", hex(id(y)))

hasil = x is y
print("x is y =", hasil)

print("a =", a, "id =", hex(id(a)))
print("b =", b, "id =", hex(id(b)))

hasil = a is not b
print("a is not b =", hasil)