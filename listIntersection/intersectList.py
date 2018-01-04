"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
"""


class Solution(object):

	def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        elemDict = {}
        for num in nums1:
            if num in elemDict:
                elemDict[num] += 1
            else:
                elemDict[num] = 1
        intersectList = []
        for num in nums2:
            if num in elemDict:
                elemDict[num] -= 1
                if elemDict[num] == 0:
                    del elemDict[num]
                intersectList.append(num)
        return intersectList

def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            nums1 = stringToIntegerList(line)
            line = lines.next()
            nums2 = stringToIntegerList(line)
            
            ret = Solution().intersect(nums1, nums2)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()