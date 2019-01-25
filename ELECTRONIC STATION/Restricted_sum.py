def checkio(data):
    if len(data)==0:
        return 0
    else:
        return data[0]+checkio(data[1:]) #This is quite smart hidden loop that can launch the same function using next and next items
