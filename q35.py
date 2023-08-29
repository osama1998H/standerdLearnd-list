def concatnate(n):
    result = []
    for i in range(1, n+1):
        result.extend((f"p{i}", f"q{i}"))
    return result


print(concatnate(5))
