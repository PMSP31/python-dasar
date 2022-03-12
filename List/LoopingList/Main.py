# Looping pada List

# for loop
print("For Loop")
numbers = [8,6,3,5,2,1,7]

# for variable in list
for number in numbers :
    print(f"number = {number}")

# for loop & range
print("\nFor Loop & Range")
numbers = [2,5,6,4,7,1]
panjang = len(numbers)

for i in range(panjang) : 
    print(f"angka-[{i}] = {numbers[i]}")

# While loop
print("\nWhile Loop")

numbers = [2,5,6,4,7,1]
panjang = len(numbers)
i = 0

while i < panjang :
    print(f"angka-[{i}] = {numbers[i]}")
    i += 1

# List Comprehension
print("\nList Comprehension")
data = ['Rio',4,6,2,"Toni"]
[print(f"data = {i}") for i in data]

angka = [2,4,6,8]
kuadrat = [i**2 for i in angka]
print(kuadrat)

# Enumerate
print("\nEnumerate")
list = ['Rio',4,6,2,"Toni"]

for index,data in enumerate(list) :
    print(f"index ke-{index} memiliki data = {data}")

# dengan enumerate dapat mengganti kegunaan while & for loop range pada loop list