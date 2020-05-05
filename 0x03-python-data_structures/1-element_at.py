#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None
    index = my_list.index(idx)
    if my_list[index] == idx:
        return (my_list[idx])
    else:
        return None
