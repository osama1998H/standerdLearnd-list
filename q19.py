k = [1, 2.3, 5, 88]
m = [1, 6.3, 8, 58]

a = list(set(k).difference(set(m)))
b = list(set(m).difference(set(k)))
c = a + b
print(c)
print()
