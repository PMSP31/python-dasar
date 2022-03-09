#  If Else Statement

name = input("Masukan nama anda : ")

# if inline
""" if name == "Paul" : print("Si ganteng!")
print(f"Hello {name}") """

# if Indentation
""" if name == "Paul" :
    print("Si ganteng!!")
    print("Asli dah")
print(f"Terimakasih {name}") """

# if else
umur = int(input("Masukan umur anda : "))
if umur >= 17 : 
    print(f"Selamat datang {name}!")
else :
    print(f"Maaf {name}, kamu belum cukup umur.")
