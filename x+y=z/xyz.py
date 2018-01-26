"""
For a given array A of n *distinct* numbers, find all triples (x,y,z) 
   s.t. x + y = z. (x, y, z are distinct numbers)

   e.g.,
   
   find([1, 4, 2, 3, 5]) returns [(1,3,4), (1,2,3), (1,4,5), (2,3,5)]

   Note that:
   1) no duplicates in the input array
   2) you can choose any arbitrary order for triples in the returned list.

   Filename: xyz.py
   Must run in O(n^2) time.

   Hint: you can use any built-in sort in Python.
"""

def find(alist):
    alist.sort()
    res = []
    for i in range(2, len(alist)):
        left = 0
        right = i-1
        while left < right:
            if alist[left] + alist[right] == alist[i]:
                res.append((alist[left], alist[right], alist[i]))
            left += 1
            right -= 1
    return res

def main():
    print(find([1, 4, 2, 3, 5]))
    
if __name__ == "__main__":
    main()