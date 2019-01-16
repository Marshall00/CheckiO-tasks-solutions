def checkio(words: str) -> bool:
    counter = 0 #will count whether 3 words are in a row
    x = words.split(' ') #everything in 'words' string is separated by empty space, so we can easily split the results into list

    for word in x:
        if word.isalpha():  #If word contains only letters, add 1 to counter and if during looping counter is >=3,  break the loop as we have success
            counter += 1
            if counter >= 3:
                break
        else:               #every time, the word contains numbers, counter must be reset to 0
            counter = 0
            continue

    return counter >= 3
