# LIST (Array dalam bhs pemrograman lain) 

# Kumpulan data numbers
data_angka = [3, 1, 8, 4]
print(data_angka)

# String
data_str = ["Paul", "Mahardika", "Putro"]
print(data_str)

# Boolean
data_bool = [True, False, False, True]
print(data_bool)

# mix ~ campuran tipe data
data_mix = [4, "Mobil", True, "Paul", False]
print(data_mix)

# Cara lain membuat List 
# 1. menggunakan keyword list
data_range = range(0, 10, 2) # range(start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)

# 2. menggunakan for loop ~ list comprehension
list_for = [i*2 for i in range(0, 10)]
print(list_for)

# 3. menggunakan for if loop
list_for_if = [i for i in range(0, 10) if i % 2 == 0]
print(list_for_if)

list_for_if = [i for i in range(0, 10) if i % 2 != 0]
print(list_for_if)

# 4. list() Constructor
listCons = list((1,2,3,4))
print(listCons)