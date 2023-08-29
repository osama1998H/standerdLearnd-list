n = [1,2,3,4,5,6]

l = 0
sl = 0

for i0, i in enumerate(n):
    if i > l:
        n = l
    sl = i if i0 in [0, len(n)] else n[i-1]
print(l, sl)