#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None or isinstance(roman_string, str) == 0 or
            len(roman_string) == 0):
        return 0

    integer = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    length = len(roman_string)

    i = 0
    num_convert = 0
    while i < length:
        if i == length - 1:
            num_convert += integer[roman_string[i]]
        elif integer[roman_string[i]] < integer[roman_string[i + 1]]:
            num_convert += integer[roman_string[i + 1]] - integer[roman_string[i]]
            i += 1
        else:
            num_convert += integer[roman_string[i]]
        i += 1

    return num_convert
