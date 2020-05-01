#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argc = len(sys.argv)
    if argc - 1 == 0:
        print("{:d} arguments.".format(argc - 1))
    elif argc - 1 == 1:
        print("{:d} argument:".format(argc - 1))
    else:
        print("{:d} arguments:".format(argc - 1))

    for i in range(1, argc):
        print("{:d}: {:s}".format(i, sys.agv[i]))
