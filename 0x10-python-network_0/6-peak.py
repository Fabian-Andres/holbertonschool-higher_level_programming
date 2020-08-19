#!/usr/bin/python3
# Find the peak


def find_peak(list_of_integers):
    """ Function peak """

    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
