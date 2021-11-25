#!/usr/bin/python3
for nums in range(0, 100):
    for nums2 in range(0, 10):
        if nums == nums2:
            continue
        elif nums > nums2:
            continue
        print("{:d}{:d}".format(nums, nums2), end="")
        if ((nums == 8) and (nums2 == 9)):
            break
        print(", ", end="")
