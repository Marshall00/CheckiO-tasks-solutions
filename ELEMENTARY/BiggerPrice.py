def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    return sorted(data, key=lambda k: k['price'],reverse=True)[:limit] #sort the elements in