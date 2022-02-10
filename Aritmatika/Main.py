# operasi aritmatika

a = 10
b = 3

# penjumlahan
hasil = a + b
print("Hasil dari", a ,"+", b, "=", hasil)

# pengurangan
hasil = a - b
print("Hasil dari", a ,"-", b, "=", hasil)

# perkalian
hasil = a * b
print("Hasil dari", a ,"*", b, "=", hasil)

# pembagian ~hasilnya akan menjadi float
hasil = a / b
print("Hasil dari", a ,"/", b, "=", hasil)

# eksponen(pangkat)
hasil = a ** b
print("Hasil dari", a ,"**" ,b, "=", hasil)

# modulus (Hasil sisa bagi)
hasil = a % b
print("Hasil dari", a ,"%", b, "=", hasil)

# floor division (Pembulatan ke bawah)
hasil = a // b
print("Hasil dari", a ,"//" ,b ,"=", hasil)

# operational precedence

""" 
    urutan prioritas
    - ()
    - eksponen **
    - perkalian, pembagian, floor division, modulus
    - penjumlahan, pengurangan
"""
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=', hasil)