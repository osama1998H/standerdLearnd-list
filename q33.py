from itertools import combinations

x = list(range(10))
a = combinations(x, 2)
print(a)
b = [list(i) for i in a]
print(b)
