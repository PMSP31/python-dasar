# Operasi Assignment

a = 5
print("nilai a =", a)

# +=
a += 1 # a = a + 1
print("nilai a += 1, a =", a)

# -=
a -= 2 # a = a - 2
print("nilai a -= 2, a =", a)

# *=
a *= 5 # a = a * 5
print("nilai a *= 4, a =", a)

# /=
a /= 2 # a = a / 2
print("nilai a /= 2, a =", a)

b = 10
print("\nnilai b =", b)

# %=
b %= 3 # b = b % 3
print("nilai b /= 3, b =", b)

# //=
b = 10
b //= 3
print("nilai b //= 3, b =", b)

# **=
a = 5
a **= 3
print("nilai a **= 3, a =", a)

# Bitwise
# |= OR
c = True
print("\nnilai c =",c)
c |= False
print("nilai c |= False, c =", c)
c = False
print("nilai c =",c)
c |= False
print("nilai c |= False, c =", c)

# &= AND
c = True
print("\nnilai c =",c)
c &= False
print("nilai c &= False, c =", c)
c = True
print("nilai c =",c)
c &= True
print("nilai c &= False, c =", c)

# ^= XOR
c = True
print("\nnilai c =",c)
c ^= False
print("nilai c ^= False, c =", c)
c = True
print("nilai c =",c)
c ^= True
print("nilai c ^= False, c =", c)

# shifting
d = 0b0100
print('\nnilai d =', d,"||",format(d, '04b'))
d >>= 2
print("nilai d >>= 2, d =", format(d, '04b'))
d <<= 1
print("nilai d <<= 1, d =", format(d, '04b'))