def checkio(number: int) -> int:
    x = str(number)
    counter = 1

    for i in x:
        if int(i) > 0:
            counter *= int(i)
        else:
            continue

    return counter