#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for k in list(a_dictionary.keys()):
        del a_dictionary[k]
    return a_dictionary
