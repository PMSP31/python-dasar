data = "Ini adalah string"
print(data, type(data))

# Pembuatan String
""" 
1.menngunakan single quote ''
2.menggunakan double quote ""
"""
data = 'ini single quote'
print(data)

data = "ini double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini hari jum'at")

# \

# 1. tanda ' menjadi string
print('kemarin adalah hari jum\'at')

# 2. tanda \ menjadi string
print('home:\\User\\PmsP')

# 3. tab
print("tulisan ini di\ttab")

# 4. backspace
print("Paul \bMahardika")

# 5. newline
print("ini baris 1.\nini baris 2.")

# String Literal atau raw

# menggunakan raw string ~ mengubah semua elemen menjadi string
print(r'C:\\new folder')

# multiline literal string
print(""" 
Nama: Paul Mahardika,
Umur: 17
""")

# mulitiline literal string dan RAW
print(r""" 
Nama: Paul
Umur: 17\tahun
""")