a = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1), (2, 1)]

b = []

for i in a:
    if i not in b:
        b.append(i)
print(a)
print(b)
