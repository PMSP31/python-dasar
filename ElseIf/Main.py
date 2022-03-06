# ELIF = else if Statement
umur = int(input("Masukan usia anda = "))

if umur < 5 :
    print("Usia anda masuk ke golongan balita")
elif umur <= 10 :
    print("Usia anda masuk ke golongan anak-anak")
elif umur <= 17 :
    print("Usia anda masuk ke golongan remaja")
else :
    print("Usia anda masuk ke golongan dewasa")