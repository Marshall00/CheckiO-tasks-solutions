def checkio(data: list) -> list:

    x=all(data.count(i)==1 for i in data) #first check-if all elements occur only once, x will become True
    list_to_remove=[] #empty list to collect all letters that should be removed after all

    if x==True:
        return [] #If x True, return empty list - each and every element is unique
    else:               #Usin for loop, find all elements that were presented only once, and add them to the list_to_remove
        for i in data:
            if data.count(i) == 1:
                list_to_remove.append(i)
            elif data.count(i) > 1:
                continue

    for element in list_to_remove: #remove all elements using elements from list_to_remove
        data.remove(element)

    return data
