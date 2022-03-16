""" Dictionaries 
    ~ collection yang terurut dan dapat diubah tetapi tidak mengijinkan duplikasi item.
    jika ada duplikasi item, maka duplikasi nya kana menimpa value sebelumnya

    Dictionaries menyimpan data menggunakan key
"""

car = {
    "brand" : "Toyota",
    "model" : "Supra",
    "color" : "White"
}
print(car)
print(type(car))

# mengakses item menggunakan key
print(car["model"])

# menghitung item pada dictionary
print(len(car))

# memasukan semua tipe data (hanya di value, key wajib string!)
car2 = {
    "brand" : "Mitsubishi",
    "type" : "Evo Lancer XI",
    "stock" : True,
    "year" : 2005,
    "color" : "Blue"
}
print(car2)