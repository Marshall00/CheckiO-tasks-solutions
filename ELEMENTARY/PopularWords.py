def popular_words(text: str, words: list) -> dict:

    splt_lst = text.split() #divide text into small parts
    dct = {} #create empty dict to collect occurences

    splt_lst=[x.lower() for x in splt_lst] #splt_lst in lower-case version

    for word in words:
        dct[word.lower()] = 0 #adding all provided words to the dict

    for word in splt_lst:       #loop that counts occurences
        if word in dct.keys():
            dct[word] += 1
    return dct
