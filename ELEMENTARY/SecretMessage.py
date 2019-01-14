def find_message(text: str) -> str:
    """Find a secret message"""
    secret_message='' #so far empty string - it will be our final message

    text=text.replace(' ','') #concatenate text - removing all the spaces and create one, long string

    for element in text:      #if element is a uppercase letterm assign it to the secret_message
        if element.isupper():
            secret_message+=element
        else:
            continue

    return secret_message
