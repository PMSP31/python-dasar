# Manipulasi item Dictionaries

car = {
    "brand" : "Honda",
    "model" : "Civic Type R",
    "year" : 1997
}
# mengakses item dengan key
x = car["model"]
print(x)

# get() 
x = car.get("year")
print(x)

# keys() ~ menampilkan semua key
x = car.keys()
print(x)

# items() ~ menampilkan semua item
x = car.items()
print(x)

# values() ~ menampilkan semua value
x = car.values()
print(x)

# mengecek key apakah terdaftar
if "model" in car :
    print(car["model"])

# method update() ~ mengupdate value
car.update({"year" : 2010})
print(car)

# menambah item baru
car["stock"] = True
print(car) 

# update() juga dapat menambah item baru
car.update({"color" : "Red"})
print(car)

# pop() ~ menghapus item dengan key
car.pop("stock")
print(car)

# popitem() ~ menghapus item yang ditambahkan terakhir 
car.popitem()
print(car)

# setdefault() ~ menjadikan default value untuk key,jika tidak terdapat key maka akan ditambahkan key baru
x = car.setdefault("model", "Civic")
print(x)

# clear() ~ mengkosongkan Dictionaries
car.clear()
print(car)

# del ~ menghapus dictionaries
# del car
# print(car) # akan error jika diprint