# Nested List ~ List bersarang

# list biasa
angka0 = [1,2]
angka1 = [3,4,5]

list_biasa = [1,2,3,4,5]
print(list_biasa)

# nested list
list_2D = [angka0, angka1, 6, 7]
print(list_2D)

# pengaksesan data nested list
data = list_2D[1][2]
print(f"data index ke [1][2] = {data}")

# contoh penggunaan
peserta1 = ["Yanto", 18, "Laki-laki"]
peserta2 = ["Rahmad", 25, "Laki-laki"]
peserta3 = ["Sari", 23, "Perempuan"]

list_peserta = [peserta1, peserta2, peserta3]
print(f"\nList Peserta = {list_peserta}")

for peserta in list_peserta :
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"gender\t: {peserta[2]}\n")