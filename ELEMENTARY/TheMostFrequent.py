import collections

def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    x = collections.Counter(data) #collections.Counter will create a dictionary with key-values pairs where value=number of occurrences of the data element

    return max(x, key=lambda k: x[k])
