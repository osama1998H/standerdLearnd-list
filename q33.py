from itertools import combinations

x = list(range(10))
b = []
a = combinations(x, 2)
print(a)
for i in a:
    # print(i)
    b.append(list(i))

print(b)
