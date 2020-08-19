#!/usr/bin/python3
# Find the peak


def find_peak(list_of_integers):
    """ Function peak """

    if not list_of_integers:
        return None

    len_list = len(list_of_integers)

    if len_list == 1:
        return list_of_integers[0]
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[len_list - 1] >= list_of_integers[len_list - 2]:
        return list_of_integers[len_list - 1]

    for i in range(1, len(list_of_integers) - 1):
        next_num = list_of_integers[i + 1]
        prev_num = list_of_integers[i - 1]
        current = list_of_integers[i]

        if current > next_num and current > prev_num:
            return current
