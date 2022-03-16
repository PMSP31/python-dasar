# Copy Dictionaries

motor = {
    "brand" : "Honda",
    "model" : "CBR",
    "year" : 2012
}
# copy()
copy = motor.copy()
print(copy)

# dict()
dict = dict(motor)
print(dict)

# NESTED COPY
siswa = {
    "siswa1" : {
        "nama" : "Toni",
        "kelas" : 10
    },
    "siswa2" : {
        "nama" : "Yogi",
        "kelas" : 12
    },
    "siswa3" : {
        "nama" : "Beni",
        "kelas" : 10
    }
}
print(siswa)

# cara lain nested copy
siswa4 = {
    "name" : "Mia",
    "kelas" : 9
}

siswa5 = {
    "name" : "Vico",
    "kelas" : 11
}

siswa = {
    "siswa4" : siswa4,
    "siswa5" : siswa5
}
print(siswa)
