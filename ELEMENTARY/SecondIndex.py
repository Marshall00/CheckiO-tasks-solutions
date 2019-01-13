def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """

    counter=0
    index=0
    if symbol not in text:
        return None
    else:
        counter+=1
        index=text.index(symbol)
        for i in range(index+1,len(text)):
            if text[i]==symbol:
                return i
            else:
                continue
