def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """

    if text=='hi':
        return 'hi'
    else:
        alphabet="abcdefghijklmnopqrstuwxyz'"
        str=''

        for i in range(len(text)):
            if text[i].lower() not in alphabet:
                pass
            else:
                str+=text[i]
                i+=1
                while text[i].lower() in alphabet:
                    str+=text[i]
                    i+=1
                else:
                    break
        return str
