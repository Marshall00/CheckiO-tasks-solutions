def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    sum = 0 #variable to sum up our values

    if len(array)==0: #first check - if len is 0 or not
        return 0
    else:            #if index is divisible by 2, let's count the values under such indexes
        for i in range(0, len(array)):
            if i % 2 == 0:
                sum += array[i]
            else:
                continue

    return sum*array[-1] #final result  - sum * last element of the array
