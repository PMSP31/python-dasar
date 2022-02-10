# Casting tipe Data
# merubah dari satu tipe ke tipe lain

# Integer
print("====Integer====")
data_int = 9
print(data_int, type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan False jika nilai int 0, selain itu akan True
print(data_float, type(data_float))
print(data_str, type(data_str))
print(data_bool, type(data_bool))

# Float
print("====Float====")
data_float = 4.5
print(data_float, type(data_float))

data_int = int(data_float) # pembulatan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)

print(data_int, type(data_int))
print(data_str, type(data_str))
print(data_bool, type(data_bool))

# Boolean
print("====Boolean====")
data_bool = True
print(data_bool, type(data_bool))

data_int = int(data_bool) # pembulatan ke bawah
data_str = str(data_bool)
data_float = float(data_bool)

print(data_int, type(data_int))
print(data_str, type(data_str))
print(data_float, type(data_float))

# String
print("====String====")
data_str = "10"
print(data_str, type(data_str))

data_int = int(data_str) # string tidak bisa diubah integer, jika bukan angka
data_bool = bool(data_str) # false jika string kosong ""
data_float = float(data_str) # string harus angka

print(data_int, type(data_int))
print(data_bool, type(data_bool))
print(data_float, type(data_float))