#!/usr/bin/python3
"""module containing find peak module"""


def find_peak_help(nums, start=None, end=None):
    """module containing helper function for  find peak"""
    length = len(nums)
    if not start and not end:
        start, end = 0, length - 1
    mid = (start + end) // 2

    if (mid == 0 or nums[mid - 1]
        <= nums[mid]) and (mid == length - 1
                           or nums[mid + 1] <= nums[mid]):
        if (mid - 1 and
            nums[mid - 1] == nums[mid]) and (mid + 1 and
                                             nums[mid + 1] == nums[mid]):
            if mid + 2 <= length - 1 and nums(mid + 2) >= nums[mid]:
                return find_peak_help(nums, mid + 2, length - 1)
            if mid - 2 >= 0:
                return find_peak_help(nums, 0, mid - 2)
        return mid
    if (mid + 1 <= length - 1 and nums[mid + 1] > nums[mid]):
        return find_peak_help(nums, mid + 1, length - 1)

    return find_peak_help(nums, 0, mid - 1)


def find_peak(list_of_integers):
    """gets the peak integer from a list of integers"""
    if not list_of_integers:
        return None
    index = find_peak_help(list_of_integers)
    return list_of_integers[index]
