"""
For a given array A of n *distinct* numbers, find all triples (x,y,z) 
   s.t. x + y = z. (x, y, z are distinct numbers)

   e.g.,
   
   find([1, 4, 2, 3, 5]) returns [(1,3,4), (1,2,3), (1,4,5), (2,3,5)]

   Note that:
   1) no duplicates in the input array
   2) you can choose any arbitrary order for triples in the returned list.

"""

import bisect
def find(alist, q, k):
    if k > len(alist):
        return alist
    if k < 1:
        return []
    idx = bisect.bisect_left(alist, q)
    l, r = idx-1, idx
    while k > 0:
        if (r >= len(alist)) or ((l > 0) and (abs(alist[l]-q) <= abs(alist[r]-q))):
            l -= 1
        else:
            r += 1
        k -= 1
    return alist[l+1:r]
def main():
    print(find([1,2,3,4,4,7], 5.2, 2))
    print(find([1,2,3,4,4,7], 6.5, 3))
    print(find([1,2,3,4,4,6,6], 5, 3))
    print(find([1,2,3,4,4,5,6], 4, 5))
if __name__ == "__main__":
    main()