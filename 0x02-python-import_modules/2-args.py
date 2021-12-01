#!/usr/bin/python3
import sys


def main(*argv):
    i = 0
    count = len(sys.argv) - 1
    if count == 1:
        print("{:d} argument:".format(count))
    elif count == 0:
        print("{:d} arguments.".format(count))
    else:
        print("{:d} arguments:".format(count))
    for args in sys.argv:
        if (i != 0):
            print("{}: {}".format(i, args))
        i += 1


if __name__ == "__main__":
    main()
