#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for w in my_string:
        if w != 'c' and w != 'C':
            new_string += w
    return (new_string)
