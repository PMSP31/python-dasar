# Sets ~ Collection yang tidak terurut, tidak dapat diubah, dan tidak terindex. tidak mengijinkan duplikasi value

# set String
set1 = {"a","b","c"}
print(set1) # saat di run (item nya bisa berpindah-pindah urutannya)
print(type(set1))

# jika adanya duplikasi item
set1 = {"a","b","c","b"}
print(set1) # yang diprint tetap 1

# mencari total item pada set, jika ada duplikasi ttp dihitung 1
print(f"Total item pada set = {len(set1)}")

# set number
numbers = {1,2,3,4}
print(numbers)

# set Boolean
boolean = {False, False, True} # duplikasi 
print(boolean)

# set mix
mix = {1,False,"hai", 10, True}
print(mix)

# set() Constructor
setCons = set(("Ray", "Bob", "Andy"))
print(setCons)