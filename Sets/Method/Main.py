# Method pada sets

set1 = {"a","b","c"}
set2 = {1,2,3}

# meggabungkan 2 sets menjadi sets baru
# union()
set3 = set1.union(set2)
print(set3)

# update()
set1.update(set2)
print(set1)

x = {"apple","banana","cherry"}
y = {"google","meta","apple"}

# intersection_update() ~ hanya menampilkan item yang duplikat
x.intersection_update(y)
print(x)

# intersection ~ membuat sets baru untuk item yang duplikat
z = x.intersection(y)
print(z)

# symmetric_difference_update() ~ menampilkan item yang tidak duplikat
x.symmetric_difference_update(y)
print(x)

# symmetric_difference() ~ membuat sets baru untuk item yang tidak duplikat
a = x.symmetric_difference(y)
print(a)

# isdisjoint() ~ mengecek apakah item pada 2 set duplikat
mobil = {"Civic", "Lancer", "Avanza","Supra"}
motor = {"Ducati", "Harley", "Supra"}
cek = mobil.isdisjoint(motor)
print(cek) # akan True jika tidak ada duplikasi item

z = mobil.difference_update(motor)
print(z)