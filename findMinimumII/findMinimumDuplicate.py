#!/usr/bin/env python
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""
class Solution(object):
	def findMin(self, nums):
	    """
	    :type nums: List[int]
	    :rtype: int
	    """
	    first = 0
	    last = len(nums) - 1
	    if first == last:
	        return nums[first]
	    else:
	        if nums[first] < nums[last]:
	            return nums[first]
	        else:
	            mid = (first + last) / 2
	            minLeft = self.findMin(nums[first:mid+1])
	            minRight = self.findMin(nums[mid+1:last+1])
	            return min(minLeft, minRight)

def main():
	nums = [3,3,3,1,2,3]
	sol = Solution()
	print sol.findMin(nums)      