#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for k in list(a_dictionary.keys()):
        del a_dictionary[k]
    return a_dictionary
