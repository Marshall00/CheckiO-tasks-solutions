def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """

    if line == "":
        return 0

    counter = 0
    lst = []

    for i in range(0, len(line) - 1):

        if line[i] == line[i + 1]:
            counter += 1
            lst.append(counter)

        else:
            counter = 0

    return (max(lst, default=0)) + 1