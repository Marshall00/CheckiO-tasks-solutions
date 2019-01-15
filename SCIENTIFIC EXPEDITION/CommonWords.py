def checkio(first, second):

    lst=[] #In this list we will keep common words for both sets
    x=first.split(',') #Create list of all words in x string
    y=second.split(',')#Create list of all words in y string

    x_set=set(x) #Create set based on x list
    y_set=set(y) #Create set based on y list

    s=x_set.intersection(y_set) #set of all common words

    for element in s:
        lst.append(element) #list of all common words created based on s-set

    return ','.join(sorted(lst))#Create alpah. ordered string with all words separated by comma
