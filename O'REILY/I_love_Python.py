def i_love_python():
    """
        Let's explain why do we love Python.
    """
    x=['I','love','you','dear']
    x.pop()

    string=''
    for word in x:
        string+=word+' '

    string=string.replace('you','Python!')

    return string.rstrip()
