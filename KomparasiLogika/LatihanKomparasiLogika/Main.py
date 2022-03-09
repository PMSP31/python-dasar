# Latihan komparasi dan logika

# area rentang angka
""" 
# ++++++3---------------10++++++
inputUser = float(input("Masukan Angka bernilai\nkurang dari 3 atau lebih dari 10\n:"))

isCorrect = (inputUser < 3) or (inputUser > 10)
print("Nilai yang anda masukan :", isCorrect)

# -----3++++++++++++10---------
inputUser = float(input("\nMasukan Angka bernilai\nlebih dari 3 dan kurang dari 10\n:"))

isCorrect = (inputUser > 3) and (inputUser < 10)
print("Nilai yang anda masukan :", isCorrect) """

inputUser = float(input("Masukan nilai \nlebih dari 0 dan kurang dari 5 atau lebih dari 8 dan kurang dari 11\n:"))

hasil = (inputUser > 0 and inputUser < 5) or (inputUser > 8 and inputUser < 11)
print(hasil)

inputUser = float(input("\nMasukan nilai \nkurang dari 0 dan lebih dari 5 atau kurang dari 8 dan lebih dari 11\n:"))

hasil = (inputUser < 0 and inputUser > 5) or (inputUser < 8 and inputUser > 11)
print(hasil)