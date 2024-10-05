#not, or, and, xor

print("=== NOT ===")
a = False
c = not a
print("Boolean Data : ", a)
print("Boolean Data : ", c)

print("=== OR ===")
a = False
b = False
c = a or b
print("Boolean Data : ", a)
print("Boolean Data : ", b)
print(a, 'OR ', b, '=', c)

print("=== AND ===")
a = True
b = False
c = a and b
print("Boolean Data : ", a)
print("Boolean Data : ", b)
print(a, 'AND ', b, '=', c)

print("=== XOR ===")
a = False
b = False
c = a ^ b
print("Boolean Data : ", a)
print("Boolean Data : ", b)
print(a, 'XOR ', b, '=', c)