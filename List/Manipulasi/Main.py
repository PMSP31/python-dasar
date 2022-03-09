# Manipulasi List

# 1. Mengambil data dari list
# jika dari pertama menggunakan index 0, jika terakhir dimulai index -1
data = ["Paul", "Saka", 'Robert']

data0 = data[0]
print(f"data pertama (index-0) = {data0}")

data_terakhir = data[-1]
print(f"data terakhir (index-(-1)) = {data_terakhir}")

# 2. Mengetahui jumlah/panjang data
panjang_data = len(data)
print(f"Panjang data = {panjang_data}")

# 3. Menambah item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

# list.insert(posisi, item)
data.insert(1, "Charles")
print(f"data setelah ditambah = \n{data}")

# 4. Menambah item di akhir list
data.append("Satria")
print(f"data setelah ditambah = \n{data}")

# 5. Menambah item list dengan list
data2 = ["Rudi", "Yanto"]
# list.extend(listbaru)
data.extend(data2)
print(f"data gabungan = \n{data}")

# 6. Merubah item by index
data[0] = "Dika"
print(f"data ubah = \n{data}")

# 7. Menghapus item ~ case sensitive
# data.remove("yanto") -> error
data.remove("Yanto")
print(f"data remove = \n{data}")

# 8. Menghapus item paling akhir, tapi bisa juga diberi index (default last)
data_akhir = data.pop()
print(data)
print(f"data yang dihapus = {data_akhir}")