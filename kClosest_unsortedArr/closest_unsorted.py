"""
Given an array A of n numbers, a query x, and a number k,
   find the k numbers in A that are closest (in value) to x.
   For example:

   find([4,1,3,2,7,4], 5.2, 2)  returns   [4,4]
   find([4,1,3,2,7,4], 6.5, 3)  returns   [4,7,4]
   find([5,3,4,1,6,3], 3.5, 2)  returns   [3,4]


   Filename: closest_unsorted.py
   Must run in O(n) time. 
   The elements in the returned list must be in the original order.
   In case two numbers are equally close to x, choose the earlier one.
"""

from random import randint
def qselect(alist, k):
    if k > len(alist) or alist == [] or k < 1:
        return []
    pivot_idx = randint(0, len(alist)-1)
    alist[0], alist[pivot_idx] = alist[pivot_idx], alist[0]
    pivot = alist[0]
    left = [x for x in alist if x < pivot]
    if len(left) == k-1:
        return pivot
    elif len(left) > k-1:
        return qselect(left, k)
    else:
        right = [x for x in alist[1:] if x >= pivot]
        return qselect(right, k-1-len(left))
def find(alist, q, k):
    if k > len(alist):
        return alist
    if k < 1:
        return []
    blist = [abs(x-q) for x in alist]
    min_k_val = qselect(blist, k)
    res = []
    count = 0
    for n in alist:
        if abs(n-q) <= min_k_val and count < k:
            res.append(n)
            count += 1
    return res
def main():
    print(find([4,1,3,2,7,4], 5.2, 2))
    print(find([4,1,3,2,7,4], 6.5, 3))
    print(find([5,3,4,1,6,3], 3.5, 2))
    
if __name__=="__main__":
    main()