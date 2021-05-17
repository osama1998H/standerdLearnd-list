import random
g = list(range(13))
random.shuffle(g)

for i, j in enumerate(g):
    print(j, "=>", i)
