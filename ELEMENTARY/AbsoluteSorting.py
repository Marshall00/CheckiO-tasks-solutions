def checkio(numbers_array: tuple) -> list:

    return sorted(numbers_array, key=lambda i: abs(i)) #sort an array using key abs for each element of array