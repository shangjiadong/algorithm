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

def maxHeapify(alist, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if (l < n) and alist[l] > alist[largest]:
        largest = l
    if (r < n) and alist[r] > alist[largest]:
        largest = r
    if largest != i:
        alist[i], alist[largest] = alist[largest], alist[i]
        maxHeapify(alist, n, largest)
def heapSort(aHeap):
    len_heap = len(aHeap)-1
    for n in range(len_heap, -1, -1):
        aHeap[0], aHeap[n] = aHeap[n], aHeap[0]
        maxHeapify(aHeap, n, 0)

def ksmallest(k, alist):
    blist = list(alist[:k])
    for item in list(alist[k:]):
        if item < blist[0]:
            blist[0] = item
            for j in range(k-1, -1, -1):
                maxHeapify(blist, len(blist), j)
    heapSort(blist)
    return blist

def main():
	print(ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7]))


if __name__ == '__main__':
	main()

