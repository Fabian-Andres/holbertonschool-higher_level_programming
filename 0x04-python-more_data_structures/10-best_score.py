#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        list_keys = list(a_dictionary.keys())
        max_qty = a_dictionary[list_keys[0]]
        key_max_qty = list_keys[0]
        for k in list_keys:
            if a_dictionary[k] > max_qty:
                key_max_qty = k
                max_qty = a_dictionary[k]
        return key_max_qty
    return None
