import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):

    counter=0

    text=text.upper()       #whole text should be uppercase as vowels and consonants
    lst=re.split("\W",text) #split the string by any character that is not alphanumeric

    for element in lst:     #if len(element)>1 or element not alphanumeric, go to the next elment
        if len(element)<=1 or not element.isalpha():
            continue

        operator=True       #set operator as True

        for i in range(0,len(element)-1):

            if VOWELS.find(element[i])!=-1 and VOWELS.find(element[i+1])!=-1: #if 2 vowels next to each other - set operator to False and break the loop
                operator=False
                break

            if CONSONANTS.find(element[i])!=-1 and CONSONANTS.find(element[i+1])!=-1: #if 2 consonants next to each other - set operator to False and break
                operator=False
                break

        if operator: #counter+1 only if operator = True (there is no 2 vowels or 2 consonants next to each other)
            counter+=1

    return counter
