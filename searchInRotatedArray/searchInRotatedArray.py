"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

"""


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # if target not in nums:
    #     return -1
    # else: 
    #     return nums.index(target)
    

    first = 0
    last = len(nums) - 1

    while (first <= last):
        mid = (first + last)//2
        if target == nums[mid]: return mid

        if nums[first] <= nums[mid]:
            if nums[first] <= target < nums[mid]:
                last = mid - 1
            else:
                first = mid + 1
        else:
            if nums[mid] < target <= nums[last]:
                first = mid + 1
            else:
                last= mid - 1
    return -1

import unittest

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(search([], 5), -1)