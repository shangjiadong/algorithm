"""
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""

def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if (len(needle) == 0) or (haystack == needle):
        return 0
    elif (len(needle) > len(haystack)) or (len(haystack) == 0):
        return -1
    elif (len(haystack) == len(needle)) and (haystack != needle):
        return -1
    elif (len(needle) == 1):
         for i in range(len(haystack)):
            if i < len(haystack) - len(needle):
                if haystack[i:i+len(needle)] == needle:
                    return i
            else:
                return -1
    elif len(needle) < len(haystack):
        for i in range(len(haystack)):
            if i <= len(haystack) - len(needle):
                if haystack[i:i+len(needle)] == needle:
                    return i
            else:
                return -1


import unittest

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(strStr("hello", "ll"), 2)