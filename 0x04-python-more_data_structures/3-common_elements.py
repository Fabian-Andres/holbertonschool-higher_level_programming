#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 and set_2:
        a = set(set_1)
        b = set(set_2)
        return (a & b)
