class Solution(object):
	def sortColors(self, nums):
	        from collections import defaultdict
	        """
	        :type nums: List[int]
	        :rtype: void Do not return anything, modify nums in-place instead.
	        """
	        numElement = defaultdict(int)
	        for item in nums:
	            if item in numElement:
	                numElement[item] += 1
	            else:
	                numElement[item] = 1
	                
	        for idx in range(len(nums)):
	            if idx < numElement[0]:
	                nums[idx] = 0 
	            elif idx < numElement[1] + numElement[0]:
	                nums[idx] = 1
	            else:
	                nums[idx] = 2

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
            nums = stringToIntegerList(line)
            
            ret = Solution().sortColors(nums)

            out = integerListToString(nums)
            if ret is not None:
                print "Do not return anything, modify nums in-place instead."
            else:
                print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()