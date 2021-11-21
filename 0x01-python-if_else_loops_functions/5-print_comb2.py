#!/usr/bin/python3
for nums in renge(0, 100):
    print("{:02d}".format(nums), end="")
    if nums == 99:
        break
    print(", ", end="")
