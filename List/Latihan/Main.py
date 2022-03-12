# Latihan List

print(10*"="," Program Data Buku ", 10*"=")

list_buku = []

while True : 
    print('\nMasukan Data Buku')
    print("="*20)

    judul = input("Judul Buku = ")
    penulis = input("Penulis Buku = ")

    buku = [judul, penulis]
    list_buku.append(buku)

    print("\nBuku Berhasil ditambahkan!\n")

    isLanjut = input("Tambah Data Lagi? (y/n) ")

    if isLanjut == "n" :
        break

print("\n",10*"="," List Data Buku ", 10*"=")
for index,buku in enumerate(list_buku) :
    print(f"{index + 1}. {buku[0]} | {buku[1]}")