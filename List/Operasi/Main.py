# Operasi List

data = [3,1,8,4,2,1,0,8,4,5,9,3,2,1]
print(data)

# 1. count ~ menghitung total duplikasi data
data_1 = data.count(1)
data_4 = data.count(4)
print(f"total angka 1 pada data = {data_1}")
print(f"total angka 4 pada data = {data_4}")

# 2. mencari index data ~ Case Sensitive
siswa = ["Dika", "Herman", "Ricky", "Rudi", "Ahmad"]
print(siswa)
index_herman = siswa.index("Herman")
print(f"index Herman = {index_herman}")

# 3. sort data
data.sort()
print(f"data sort = \n{data}")
siswa.sort()
print(f"siswa sort = \n{siswa}")

# 4. reverse
data.reverse()
print(f"data reverse = \n{data}")
siswa.reverse()
print(f"siswa reverse = \n{siswa}")