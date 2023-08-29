def common(a: list, b: list) -> list:
    """[summary]

    Args:
        a (list): [description]
        b (list): [description]

    Returns:
        list: [description]
    """
    return [i for i in a if i in b]


print(common(list(range(11)), list(range(6, 15))))
