# Looping pada Tuple

tuple1 = ("Sari","Krisna","Teo")

# for loop
print("\nFor Loop")
for name in tuple1 : 
    print(name)

# for & range
print("\nFor Loop & range")
for i in range(len(tuple1)) : 
    print(f"index ke-{i}, data = {tuple1[i]}")

# while
print("\nWhile Loop")
i = 0
while i < len(tuple1) : 
    print(f"index ke-{i}, data = {tuple1[i]}")
    i += 1