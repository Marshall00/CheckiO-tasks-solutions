def count_words(text: str, words: set) -> int:
    counter = 0 #will count words that we can find in text

    for word in words:          #loop through every word in words and check if it is available in given text
        if word in text.lower():
            counter += 1
        else:
            continue

    return counter