"""
1. (taken from my first paper: see "Algorithm 1" in Huang and Chiang (2005).)

Given two lists A and B, each with n integers, return
a sorted list C that contains the smallest n elements from AxB:

AxB = { (x, y) | x in A, y in B }

i.e., AxB is the Cartesian Product of A and B.

ordering:  (x,y) < (x',y') iff. x+y < x'+y' or (x+y==x'+y' and y<y')

You need to implement three algorithms and compare:

(a) enumerate all n^2 pairs, sort, and take top n.
(b) enumerate all n^2 pairs, but use qselect from hw1.
(c) Dijkstra-style best-first, only enumerate O(n) (at most 2n) pairs.
  Hint: you can use Python's heapq module for priority queue.

Q: What are the time complexities of these algorithms? 

>>> a, b = [4, 1, 5, 3], [2, 6, 3, 4]
>>> nbesta(a, b)   # algorithm (a), slowest
[(1, 2), (1, 3), (3, 2), (1, 4)]
>>> nbestb(a, b)   # algorithm (b), slow
[(1, 2), (1, 3), (3, 2), (1, 4)]
>>> nbestc(a, b)   # algorithm (c), fast
[(1, 2), (1, 3), (3, 2), (1, 4 )]

"""

def nbesta(a, b):
    c = []
    for b_num in b:
        for a_num in a:
            c.append([(a_num, b_num), a_num + b_num])
    c.sort(key=lambda x: x[1])
    best = [item[0] for item in c]
    return best[:len(a)]

from random import randint
def qselect(alist, k):
    if k > len(alist) or k < 1 or alist == []:
        return []
    else:
        rand_idx = randint(0, len(alist)-1)
        alist[0], alist[rand_idx] = alist[rand_idx], alist[0]
        pivot = alist[0][2]
        left = [x for x in alist if x[2] < pivot]
        if k-1 == len(left):
            return (alist[0][0], alist[0][1])
        elif k-1 < len(left):
            return qselect(left, k)
        else:
            right = [x for x in alist[1:] if x[2] >= pivot]
            return qselect(right, k-1-len(left))  

def nbestb(a, b):
    c = []
    res = []
    for b_num in b:
        for a_num in a:
            c.append((a_num, b_num, a_num + b_num))
    for k in range(1, len(a)+1):
        res.append(qselect(c, k))
    return res

from heapq import *
def nbestc(a, b):
    a.sort()
    b.sort()
    k = len(a)
    res = []
    heap = []
    occu = set()
    heappush(heap, ((a[0]+b[0], b[0], a[0]), 0, 0))
    occu.add((0, 0))
    while len(res) < k:
        comb, i, j = heappop(heap)
        res.append((comb[2], comb[1]))
        if i+1 < len(a) and (i+1, j) not in occu:
            heappush(heap, ((a[i+1]+b[j], b[j], a[i+1]), i+1, j))
            occu.add((i+1, j))
        if j+1 < len(b) and (i, j+1) not in occu:
            heappush(heap, ((a[i]+b[j+1], b[j+1], a[i]), i, j+1))
            occu.add((i+1, j))
    return res
            

def main():
	a, b = [4, 1, 5, 3], [2, 6, 3, 4]
	print(nbesta(a, b))
	a, b = [4, 1, 5, 3], [2, 6, 3, 4]
	print(nbestb(a, b))
	a, b = [4, 1, 5, 3], [2, 6, 3, 4]
	print(nbestc(a, b))

if __name__ == '__main__':
	main()