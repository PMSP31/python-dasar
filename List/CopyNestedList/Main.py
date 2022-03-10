# Copy pada nested list

data_0 = [1,2,3]
data_1 = [4,5,6]

list_2D = [data_0, data_1]
list_copy = list_2D.copy()
print(f"data = {list_2D}")
print(f"data copy = {list_copy}")

# address list
print(f"addres asli = {hex(id(list_2D))}")
print(f"addres copy = {hex(id(list_copy))}")

# addres member  1 ~ hasilnya sama
print(f"addres-1 asli = {hex(id(list_2D[0]))}")
print(f"addres-1 copy = {hex(id(list_copy[0]))}")

# deep copy
from copy import deepcopy

list_2D = [data_0, data_1]
list_deep = deepcopy(list_2D)

print("\nMenggunakan deep copy\n")
print(f"addres asli = {hex(id(list_2D))}")
print(f"addres deepcopy = {hex(id(list_deep))}")

# addres member  1 ~ hasilnya sama
print(f"addres-1 asli = {hex(id(list_2D[0]))}")
print(f"addres-1 deepcopy = {hex(id(list_deep[0]))}")

print("\nhasil deep copy")
list_2D[0][1] = 20
print(f"data = {list_2D}")
print(f"data copy = {list_copy}")
print(f"data deepcopy = {list_deep}")
# karena menggunakan deepcopy, maka tidak akan mengubah data