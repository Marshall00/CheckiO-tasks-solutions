def checkio(data: str) -> bool:


    if len(data)>9: #Len is the basic requirement, then rest requirements are condensed to one line with connector 'and'
        if any(x.isupper() for x in data) and any(x.islower() for x in data) and any(x.isdigit() for x in data):
            return True
        else:
            return False
    else:
        return False
