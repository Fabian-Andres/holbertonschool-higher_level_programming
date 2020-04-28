#!/usr/bin/python3
for n1 in range(0, 8):
    for n2 in range(0, 10):
        if n1 < n2:
            print("{}{}".format(n1, n2), end=", ")
print("{}".format(89))
