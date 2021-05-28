# a = ["black", "blue", "red", "viber"]
# print(a)
# for i in range(len(a)):
#     if i != 0:
#         # a.insert(i-1, "b")
#         a[i-1] = i


# print(a)

color = ['Red', 'Green', 'Black']
print("Original List: ", color)
color = [v for elt in color for v in ('c', elt)]
print("Original List: ", color)
