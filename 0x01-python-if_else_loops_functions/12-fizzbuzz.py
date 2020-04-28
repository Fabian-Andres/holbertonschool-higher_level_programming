#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0:
            if n % 5:
                print("{}".format("Fizz"), end=" ")
            else:
                print("{}".format("FizzBuzz"), end=" ")
        elif n % 5 == 0:
            print("{}".format("Buzz"), end="")
            if n != 101:
                print(end=" ")
        else:
            print("{}".format(n), end=" ")
