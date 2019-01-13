def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    import re

    try:
        if begin in text and end in text:
            result = re.search('{}(.*){}'.format(begin, end), text)
            return (result.group(1))

        elif begin in text and end not in text:
            start = text.index(begin) + len(begin)
            return (text[start::])

        elif begin not in text and end in text:
            end_marker = text.index(end[0])
            return (text[0:end_marker])

        else :
            return text
    except:
        return ''
