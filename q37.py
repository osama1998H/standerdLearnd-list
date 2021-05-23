def common(a: list, b: list) -> list:
    """[summary]

    Args:
        a (list): [description]
        b (list): [description]

    Returns:
        list: [description]
    """
    result = []

    for i in a:
        if i in b:
            result.append(i)
    return result


print(common([i for i in range(11)], [i for i in range(6, 15)]))
