# Kalkulator Suhu

# konversi Celcius ke suhu lainnya

from math import floor


print("\nProgram Kalkulator Suhu\n")

celcius = float(input("Masukan Suhu dalam Celcius: "))
print("Suhu", celcius, 'C')

cel_reamur = (4/5) * celcius
print("Suhu dalam Reamur", cel_reamur, "R")

cel_fahren = ((9/5)* celcius) + 32
print("Suhu dalam Fahrenheit", cel_fahren, "F")

cel_kelvin = celcius + 273
print("Suhu dalam Kelvin", cel_kelvin, "K")

# Konversi Reamur ke suhu lain
reamur = float(input("\nMasukan Suhu dalam Reamur: "))
print("Suhu", reamur, "R")

reamur_cel = (5/4) * reamur
print("Suhu dalam Celcius", reamur_cel, "C")

reamur_fahren = ((9/4) * reamur) + 32
print("Suhu dalam Fahrenheit", reamur_fahren, "F")

reamur_kelvin = ((5/4) * reamur) + 273
print("Suhu dalam Kelvin", reamur_kelvin, "K")

# Konversi Fahrenheit ke suhu lain
fahrenheit = float(input("\nMasukan Suhu dalam Fahrenheit: "))
print("Suhu", fahrenheit, "F")

fahren_cel = 5/9 * (fahrenheit-32)
print("Suhu dalam Celcius", fahren_cel, "C")

fahren_reamur = 4/9 * (fahrenheit - 32)
print("Suhu dalam Reamur", fahren_reamur, "R")

fahren_kelvin = fahren_cel + 273
print("Suhu dalam Kelvin", fahren_kelvin, "K")

# Konversi Kelvin ke suhu lain
kelvin = float(input("\nMasukan Suhu dalam Kelvin: "))
print("Suhu", kelvin, "K")

kelvin_cel = kelvin - 273
print("Suhu dalam Celcius", kelvin_cel, "C")

kelvin_ream = 4/5 * (kelvin - 273)
print("Suhu dalam Reamur", kelvin_ream, "R")

kelvin_fahren = ((9/5) * kelvin_cel) + 32
print("Suhu dalam Fahrenheit", kelvin_fahren, "F")