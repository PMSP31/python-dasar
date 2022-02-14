# Operasi Bitwise

a = 10
b = 7

# bitwise OR |
c = a | b
print("\n==========OR==========")
print('nilai :', a, ' ,binary :', format(a,'08b'))
print('nilai :', b, '  ,binary :', format(b,'08b'))
print('----------------------------------(|)')
print('nilai :', c, ' ,binary :', format(c,'08b'))

# bitwise AND &
c = a & b
print("\n==========AND==========")
print('nilai :', a, ' ,binary :', format(a,'08b'))
print('nilai :', b, '  ,binary :', format(b,'08b'))
print('----------------------------------(&)')
print('nilai :', c, '  ,binary :', format(c,'08b'))

# bitwise XOR ^
c = a ^ b
print("\n==========XOR==========")
print('nilai :', a, ' ,binary :', format(a,'08b'))
print('nilai :', b, '  ,binary :', format(b,'08b'))
print('----------------------------------(^)')
print('nilai :', c, ' ,binary :', format(c,'08b'))

# bitwise NOT ~
c = ~a
print("\n==========NOT==========")
print('nilai :', a, ' ,binary :', format(a,'08b'))
print('----------------------------------(~)')
print('nilai :', c, ' ,binary :', format(c,'08b'))

# Shifting
# shift right >>
c = b >> 2
print("\n==========>>==========")
print('nilai :', b, '  ,binary :', format(b,'08b'))
print('----------------------------------(>>)')
print('nilai :', c, ' ,binary :', format(c,'08b'))

# shift left <<
c = b << 2
print("\n==========<<==========")
print('nilai :', b, '  ,binary :', format(b,'08b'))
print('----------------------------------(<<)')
print('nilai :', c, ' ,binary :', format(c,'08b'))