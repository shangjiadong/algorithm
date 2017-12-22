#!/usr/bin/env python

"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        first = 0
        last = len(nums) - 1
        mid = 0
        if first == last:
            return 0
        while first <= last:
            mid = (first + last) / 2
            if ((mid == 0) or (nums[mid] > nums[mid-1])) and ((mid == last) or (nums[mid] > nums[mid+1])):
                return mid
            else:
                if (mid > 0) and  (nums[mid-1] > nums[mid]):
                    last = mid - 1
                else:
                    first = mid + 1
        return mid 

import main()
sol = Solution()
print sol.findPeakElement([1,2,3,1])