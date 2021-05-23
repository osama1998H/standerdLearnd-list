n = [1,2,3,4,5,6]

l = 0 
sl = 0

for i0, i in enumerate(n):
    if i > l:
        n = l
    if i0 == 0:
        sl = i
    elif i0 == len(n):
        sl = i
    else:
        sl = n[i-1]

print(l, sl)