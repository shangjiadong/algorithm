"""
Find the k smallest numbers in a data stream of length n (k<<n),
using only O(k) space (the stream itself might be too big to fit in memory).

>>> ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7])
[2, 3, 5, 7]
>>> ksmallest(3, range(1000000, 0, -1))
[1, 2, 3]

Note: 
a) it should work with both lists and lazy lists
b) the output list should be sorted
"""

from heapq import *
def ksmallest(k, alist):
    # if k < 1: return []
    if k > len(alist):
        k = len(alist)
    heap = []
    for idx, val in enumerate(alist):
        if idx < k:
            heappush(heap, -val)
        else:
            if -val > heap[0]:
                heapreplace(heap, -val)
    res = [-heappop(heap) for i in range(len(heap))] 
    return res[::-1]

def main():
    print(ksmallest(11, [10, 2, 9, 3, 7, 8, 11, 5, 7]))

if __name__ == '__main__':
    main()
