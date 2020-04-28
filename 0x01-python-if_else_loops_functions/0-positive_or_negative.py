#!/usr/bin/python3
import random
number = random.randint(-10, 10)
text = ["is positive", "is zero", "is negative"]
if number > 0:
    print("{:1d} {}".format(number, text[0]))
elif number == 0:
    print("{:1d} {}".format(number, text[1]))
else:
    print("{:1d} {}".format(number, text[2]))
