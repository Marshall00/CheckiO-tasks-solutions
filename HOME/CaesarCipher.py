from string import ascii_lowercase as alphabet #alphabet imported from string


def to_encrypt(text, delta):
    alpha_lst=[]  #alphabet in list form
    new_text = '' #this will be a result

    for y in range(0,3):        #additional 'for loop' using for making alphabet repetitive in list(useful when delta>len(alphabet))
        for i in alphabet:      #to avoid an ERROR that says about exceeding len of list
            alpha_lst.append(i)


    for element in text:    #If element is a letter, add a letter that is placed 'delta' far from the letter
        if element.isalpha():
            new_text += alpha_lst[alpha_lst.index(element) + delta]
        else:
            new_text+=element

    return new_text
