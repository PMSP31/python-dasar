# Width & Multiline

nama = "Paul Mahardika"
umur = 17
tinggi = 172.5

# standard
data = f"nama = {nama}, umur = {umur}, tinggi badan = {tinggi}."
print(5*"="+ " Data Diri "+ 5*"=")
print(data)

# newline \n
data = f"nama = {nama}, \numur = {umur}, \ntinggi badan = {tinggi}."
print("\n" + 5*"="+ " Data Diri "+ 5*"=")
print(data)

# triple double quote
data = f"""nama = {nama}
umur = {umur}
tinggi badan = {tinggi}."""
print("\n" + 5*"="+ " Data Diri "+ 5*"=")
print(data)

# mengatur lebar
nama = "Paul"
data = f"""
nama    = {nama:>5}
umur    = {umur:>5}
tinggi  = {tinggi:>5}"""
print("\n" + 5*"="+ " Data Diri "+ 5*"=")
print(data)