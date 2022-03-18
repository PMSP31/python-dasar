# Python Modules

# import modul buatan sendiri
# import myModule

# rename module
import myModule as mx

# penggunaan module
mx.salam("Paul","Sore")

# akses Dictionary dari album
a = mx.person1["name"]
print(a)

# built-in modules dari python
import platform
x = platform.system()
print(x)

# dir() ~ built-in function untuk list semua function/nama variable dari module
x = dir(platform)
# print(x)

# import from module
from myModule import person1
print(person1)