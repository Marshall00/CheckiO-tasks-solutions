def index_power(array: list, n: int) -> int:
    """
        Find Nth power of the element with index N.
    """

    if n>=len(array): #return -1 for the cases when n >= len(array) - to avoid error: index out of range
        return -1
    else:
        return array[n]**n