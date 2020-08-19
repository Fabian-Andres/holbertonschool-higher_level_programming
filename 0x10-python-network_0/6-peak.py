#!/usr/bin/python3
# Find the peak

def find_peak(list_of_integers):
    peak = 0

    if not list_of_integers:
        return None

    for i in range(0, len(list_of_integers)):
        try:
            next_num = list_of_integers[i+1]
        except:
            next_num = 0
        try:
            prev_num = list_of_integers[i-1]
        except:
            next_num = 0

        current = list_of_integers[i]

        if current > next_num and current > prev_num:
            peak = current

    return peak
