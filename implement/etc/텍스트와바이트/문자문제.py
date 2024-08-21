s = 'cafe'
print(len(s))

b = s.encode('utf8')
print(s.encode('utf8'))

print(b.decode('utf8'))

cafe = bytes('cafe', encoding = 'utf_8')
print(cafe)
print(cafe[0])

cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:]) 