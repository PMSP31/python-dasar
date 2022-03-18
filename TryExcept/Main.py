# Try Except ~ Error Handling

""" 
    terdapat beberapa block untuk Try Except
    ~ block try = untuk mengetest error pada code
    ~ block except = untuk menghandle error
    ~ block else = untuk mengeksekusi kode jika tidak ada error
    ~ block finally = untuk mengeksekusi kode tapi tidak tergantung dari block try & except
"""
# print(x) # tanpa block try except akan membuat crash / tidak akan dijalankan lagi dan menyebabkan error, 

# simple try except block
""" try:
    print(x) # karena ini error
except:
    print("an exception occured") # maka ini yang diprint """

# mendefinisikan exception
""" try :
    print(x)
except NameError : # ini yang akan dijalankan jika terjadi NameError
    print("Tidak dapat menemukan variable x")
except : # ini akan dijalankan jika terdapat error lain selain block except diatas
    print("Ada kesalahan lainnya") """

# block else
""" try : 
    print("Hallo") # karena tidak error ini akan diprint
except : # karena block try tidak error maka block except tidak dijalankan
    print("Terjadi kesalahan program")
else: # ini dijalankan jika pada block try tidak ada error
    print("Tidak ada kesalahan program")
 """
# block finally
""" try : 
    print(x)
except :
    print("Terjadi Kesalahan")
finally : # apapun hasilnya block finally akan dijalankan
    print("Try Except sudah dijalankan") """

# Latihan
""" try: 
    f = open("TryExcept/demofile.txt")
    try :
        f.write("tes halo 123")
    except : 
        print("Terjadi kesalahan saat penulisan pada file")
    finally :
        f.close()
except :
    print("Terjadi kesalahan saat membuka file") """

# raise keyword 
# digunakan untuk melempar exception / pengecualian
x = -1
if x < 0 :
    raise Exception("Maaf number tidak boleh dibawah 0!")