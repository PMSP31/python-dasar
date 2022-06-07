# hellow
# print("Hello World")

# ganjil genap
""" def isGenap(x):
    if x % 2 == 0:
        return True
    else : 
        return False

print(isGenap(12))
print(isGenap(31)) """

list_genap = [i for i in range(21) if i % 2 == 0]
list_ganjil = [x for x in range(21) if x % 2 != 0]

""" for  i in range(21):
    if i % 2 == 0 :
        list_genap.append(i)
    else : 
        list_ganjil.append(i)
        
print(list_ganjil)
print(list_genap)
"""

# FizzBuzz
""" for i in range(1,21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 : 
        print("Fizz")
    elif i % 5 == 0 : 
        print("Buzz")
    else :
        print(i) """

# factorial recursive
# 5x4x3x2x1 = 120
""" def factorial(y):
    if y == 0 :
        return 1
    else :
        return y * factorial(y-1)

print(factorial(5)) """

# factorial looping
""" num = 5
factorial = 1

if num < 0 :
    print("Hanya untuk bilangan positif")
elif num == 0 :
    print(factorial)
else :
    for i in range(1, num + 1):
        factorial = factorial * i
    print(factorial) """

# fibonacci recursive
""" def fibonacci(n):
    if n <= 1 :
        return n
    else : 
        return (fibonacci(n-1) + fibonacci(n-2))

deret = 10

if deret <= 0 :
    print("Hanya Untuk Bilangan positive")
else : 
    print("Deret Fibonacci: ")
    for i in range(deret):
        print(fibonacci(i)) """

# fibonacci looping
""" deret = 10
n1, n2 = 0, 1
count = 0

if deret <= 0 :
    print("Hanya untuk bilangan positive")
elif deret == 1 :
    print(n1)
else :
    while count < deret : 
        print(n1)
        # update value
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1 """

# palindrome
""" def isPalindrome(str) :
    reverse_str = str[::-1]
    if reverse_str == str :
        return True
    else : 
        return False

words = ['ada','topi','kasur rusak']

for word in words:
    print(isPalindrome(word)) """

# simple calculator
def penjumlahan(x, y):
    return x + y

def pengurangan(x, y):
    return x - y

def perkalian(x, y):
    return x * y

def pembagian(x, y):
    return x / y

print('Simple Calculator')
print("""
1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Pembagian""")

while True:
    opt = input('\nPilih Opsi Perhitungan (1/2/3/4) : ')

    if opt in ('1','2','3','4'):
        num1 = float(input("Masukan Angka 1 : "))
        num2 = float(input("Masukan Angka 2 : "))

        if opt == '1' :
            print(f"Hasil Penjumlahan {num1} + {num2} = {penjumlahan(num1,num2)}")
        elif opt == '2' :
            print(f"Hasil Pengurangan {num1} - {num2} = {pengurangan(num1,num2)}")
        elif opt == '3' :
            print(f"Hasil Perkalian {num1} * {num2} = {perkalian(num1,num2)}")
        elif opt == '4' :
            print(f"Hasil Pembagian {num1} / {num2} = {pembagian(num1,num2)}")

        isLanjut = input("\nHitung Ulang? (Y/N): ")
        if isLanjut == 'N' or isLanjut == 'n':
            break
    else : 
        print("Input Yang Anda Masukan Salah! :")