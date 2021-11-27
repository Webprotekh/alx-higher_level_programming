#!/usr/bin/python3
for n in reversed(range(97, 123)):
    print("{}".format(chr(n)) if (n % 2 == 0)
          else "{}".format(chr(n - 32)), end='')
