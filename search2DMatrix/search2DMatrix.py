"""

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

"""

def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """

    if (len(matrix) == 0):
        return False
    else:
        flag = False
        for row_idx in range(len(matrix)):
            if len(matrix[row_idx]) != 0:
                if (target >= matrix[row_idx][0]) and (target <= matrix[row_idx][-1]):
                    first = 0
                    last = len(matrix[row_idx]) - 1
                    while first <= last and not flag:
                        mid = (first + last) // 2
                        if matrix[row_idx][mid] == target:
                            flag = True
                        else:
                            if matrix[row_idx][mid] > target:
                                last = mid - 1
                            else:
                                first = mid + 1                      
        return flag

import unittest

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],3), True)