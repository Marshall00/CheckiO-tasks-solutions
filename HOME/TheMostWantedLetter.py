import collections
from string import ascii_lowercase as alphabet #importing alphabet

def checkio(text: str) -> str:

    text=text.lower() #all letters should be lowercase
    new_text='' #this will be our new text


    for element in text: #for each element, if the element is in alphabet, add it to the newly creted string
        if element in alphabet:
            new_text+=element
        else:
            continue


    new_text=''.join(sorted(new_text)) #sort new_text in alphabetical order

    x=collections.Counter(new_text) #use counter to get pairs: element : count i.e 'a' : 5

    return x.most_common()[0][0] #result should be only a letter so we need to get first element from the first element from previously defined x
