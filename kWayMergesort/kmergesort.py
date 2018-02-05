"""
2. k-way mergesort (the classical mergesort is a special case where k=2).

   >>> kmergesort([4,1,5,2,6,3,7,0], 3) 
   [0,1,2,3,4,5,6,7]

"""
from heapq import *
from math import *
def _kmergehelper(alist):
	heap = []
	res = []
	for idx, item in enumerate(alist):
		heappush(heap, [item[0], 0, idx])
	while heap:
		value, min_idx, item_idx = heappop(heap)
		res.append(value)
		if min_idx+1 < len(alist[item_idx]):
			heappush(heap, [alist[item_idx][min_idx+1], min_idx+1, item_idx])
	return res

def kmergesort(alist, k):
	len_a = len(alist)
	if len_a < 2:
		return alist
	step = int(ceil(float(len_a)/k))
	klist = [kmergesort(alist[i:i+step],k) for i in range(0, len_a, step)]
	return _kmergehelper(klist)

def main():
	print(kmergesort([4,1,5,2,6,3,7,0], 3))

if __name__ == '__main__':
	main()

