#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        my_list = list(dict.fromkeys(my_list))
        add = 0
        for i in my_list:
            add += i
        return add
