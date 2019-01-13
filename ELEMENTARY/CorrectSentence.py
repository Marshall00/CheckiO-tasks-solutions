def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """

    if text[-1]=='.':
        return text[0].upper()+text[1::]
    else:
        return text[0].upper()+text[1::]+'.'
