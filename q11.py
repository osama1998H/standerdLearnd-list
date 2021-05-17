l1 = [1, 25, 4, 7]
l2 = [6, 12, 55, 10]


def common_item(l1, l2):
    b = []
    for i in l1:
        for n in l2:
            if i == n:
                b.append(True)
            else:
                b.append(False)
    return any(b)


print(common_item(l1, l2))
