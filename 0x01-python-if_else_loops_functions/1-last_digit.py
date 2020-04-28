#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
text1 = "Last digit of "
text2 = ["and is greater than 5", "and is 0", "and is less than 6 and not 0"]
if number < 0:
    lastDigit *= -1
if lastDigit > 5 and lastDigit > 6:
    print("{0}{1:1d} is {2:1d} {3}".format(text1, number, lastDigit, text2[0]))
elif lastDigit == 0:
    print("{0}{1:1d} is {2:1d} {3}".format(text1, number, lastDigit, text2[1]))
elif lastDigit < 6:
    print("{0}{1:1d} is {2:1d} {3}".format(text1, number, lastDigit, text2[2]))
