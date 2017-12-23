#!/usr/bin/env python
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

"""

def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    first = 0
    last = len(nums) - 1
    
    while first <= last:
        mid = (first + last) / 2
        if len(nums) == 1:
            return nums[0]
        if (nums[last] < nums[last-1]):
            return nums[last]
        if (nums[mid-1] >= nums[mid]) and (nums[mid] <= nums[mid+1]):
            return nums[mid]
        if (nums[first] < nums[mid]) and (nums[first] > nums[last]):
            first = mid
        else:
            last = mid

import unittest

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(findMin([2,1]), 1)