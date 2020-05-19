#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = int(a) / int(b)
        return result
    except (ZeroDivisionError, ValueError):
        result = None
        return result
    finally:
        print("Inside result: {}".format(result))
