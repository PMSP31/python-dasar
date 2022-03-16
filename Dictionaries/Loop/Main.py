# Loop pada Dictionary

siswa = {
    "nama" : "Rio Saputra",
    "kelas" : 12,
    "jurusan" : "Teknik Otomotif"
}

for x in siswa : 
    print(siswa[x])

# for loop values
print("\n")
for x in siswa.values():
    print(x)

# for loop keys
print("\n")
for x in siswa.keys():
    print(x)

# for loop items
print("\n")
for x,y in siswa.items():
    print(x,y)

x = 0
while x < len(siswa): 
    print(x)
    x += 1