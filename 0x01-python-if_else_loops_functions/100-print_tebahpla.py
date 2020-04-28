#!/usr/bin/python3
for item in range(122, 96, -1):
    if item % 2 == 0:
        print("{:s}".format(chr(item)), end="")
    else:
        item -= 32
        print("{:s}".format(chr(item)), end="")
