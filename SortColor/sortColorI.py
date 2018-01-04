class Solution(object):
    def partition(self, alist, start, end):
        pivot = alist[start]
        left = start + 1
        right = end
        done = False
        while not done:
            while left <= right and alist[left] <= pivot:
                left += 1
            while left <= right and alist[right] >= pivot:
                right -= 1
            if left > right:
                done = True
            else:
                temp = alist[left]
                alist[left] = alist[right]
                alist[right] = temp
        temp = pivot
        alist[start] = alist[right]
        alist[right] = pivot
        return right
    def quickSort(self, alist, start, end):
        if start < end:
            split = self.partition(alist, start, end)
            self.quickSort(alist, start, split-1)
            self.quickSort(alist, split+1, end)
        
        
    def sortColors(self, nums):
        from collections import defaultdict
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.quickSort(nums, 0, len(nums)-1)
        
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