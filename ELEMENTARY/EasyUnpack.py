def easy_unpack(elements: tuple) -> tuple:
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    # your code here
    lst = []
    lst.append(elements[0])
    lst.append(elements[2])
    lst.append(elements[-2])

    return tuple(lst)