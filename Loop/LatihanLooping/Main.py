# Latihan Looping membuat segitiga

# 1. Menggunakan for
sisi = 10
# dummy variable
count = 1
for i in range(sisi) : 
    print("*" * count)
    count += 1

print("Segitiga For \n")

# 2. Menggunakan while - break
count = 1
while True :
    print("*" * count)
    count += 1

    if count >= sisi: 
        break

print("Segitiga While \n")

# 3. Segitiga ganjil
count = 1
while True :
    # akan print * jika ganjil
    if count % 2 == 1: 
        print("*" * count)
        count += 1
    else : 
        # akan di skip jika genap
        count += 1
        continue

    if count >= sisi: 
        break

print("Segitiga Ganjil \n")

# 4. Segitiga sama kaki
count = 1
spasi = int(sisi / 2)
while True :
    if count % 2 == 1: 
        print(" "*spasi,"+" * count)
        spasi -= 1
        count += 1
    else : 
        count += 1
        continue

    if count >= sisi: 
        break

print("Segitiga sama kaki \n")

# 5. Belah ketupat
for i in range(0, 5):
    print(" " * (5 - i), end = "")
    for x in range(i):
        print("+ ", end = "")

    print()
for i in range(5, 0, -1):
    print(" "*(5-i), end='')
    for x in range(i):
        print("+ ", end='')
    print()