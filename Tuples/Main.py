# Tuple ~ collection yang urut dan unchangeable / tidak dapat diubah setelah dibuat.

# tuple string
tuple1 = ("apel", "bengkoang", "ceri")
print(f"ini tuple string = {tuple1}")

# tuple number
tuple2 = (1,4,2,6)
print(f"ini tuple number = {tuple2}")

# tuple boolean
tuple3 = (True, False, False)
print(f"ini tuple boolean = {tuple3}")

# tuple mix-data
tupleMix = ("Satu", 2, False)
print(f"ini tuple mix = {tupleMix}")

# sama dengan list, tuple juga menggunakan index untuk setiap datanya
print(f"Index ke-1 dari tuple = {tuple1[1]}")

# mengetahui banyak item pada tuple
print(f"Banyak item pada tuple = {len(tuple1)}")

# Tuple one item ~ jika item hanya satu, pastikan diberi tanda koma
# ini benar
oneTuple = ("Apel",)
print(type(oneTuple))

# ini akan dianggap string
oneTuple = ("Apel")
print(type(oneTuple))