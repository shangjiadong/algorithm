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

def buildMaxHeap(alist):
    for i in range(len(alist)//2, -1, -1):
        maxHeapify(alist, len(alist), i)
    return alist

def ksmallest(k, alist):
    # if k < 1: return []
    if k > len(alist):
        k = len(alist)
    blist = alist[:k]
    for i in range(len(blist)//2, -1, -1):
        maxHeapify(blist, k, i)
    for item in alist[k:]:
        if item < blist[0]:
            blist[0] = item
            maxHeapify(blist, k, 0)
    # heapSort(blist)
    for n in range(k-1, -1, -1):
        blist[0], blist[n] = blist[n], blist[0]
        maxHeapify(blist, n, 0)
    return blist


def main():
    print(ksmallest(11, [10, 2, 9, 3, 7, 8, 11, 5, 7]))
    
if __name__ == '__main__':
    main()