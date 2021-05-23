def concatnate(n):
    result = []
    for i in range(1, n+1):
        result.append(f"p{i}")
        result.append(f"q{i}")
    return result


print(concatnate(5))
