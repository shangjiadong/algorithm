"""
1. [WILL BE GRADED]
   Dijkstra (see CLRS 24.3 and DPV 4.4)
   
   Given an undirected graph, find the shortest path from source (node 0)
   to target (node n-1). 
   
   Edge weights are guaranteed to be non-negative, since Dijkstra doesn't work
   with negative weights, e.g.
 
       3
   0 ------ 1   
     \    /
    2 \  / -2
       \/
       2
   
   in this example, Dijkstra would return length 2 (path 0-2), 
   but path 0-1-2 is better (length 1).

   For example (return a pair of shortest-distance and shortest-path):
   
       1
   0 ------ 1   
     \    /  \
    5 \  /1   \6
       \/   2  \
       2 ------ 3
            
   >>> shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)])
   (4, [0,1,2,3])

   [UPDATE] Tiebreaking: arbitrary. Any shortest path would do.

"""
from collections import defaultdict
from heapq import *
from heapdict import heapdict

def shortest(n, edge):
	g = defaultdict(set)
	for l, r, c in edge:
		g[l].add((r, c))
		g[r].add((l, c))

	queue, visited = [(0, 0, ())], set()
	while queue:
		(cost, v1, path) = heappop(queue)
		if v1 not in visited:
			visited.add(v1)
			path = (v1, path)
			if v1 == n-1: 
				seq = []
				return cost, solution(path, seq)
			for v2, c in g.get(v1, ()):
				if v2 not in visited:
					heappush(queue, (cost+c, v2, path))
	def solution(path, seq):
		while len(path) > 1:
			seq.append(path[0])
			path = path[1]
		seq.reverse()
		return seq
	return float("inf")

def shortest1(n, edge):
	g = defaultdict(set)
	for l, r, c in edge:
		g[l].add((r, c))
		g[r].add((l, c))
	queue = heapdict()
	for i in range(n):
		queue[i] = float("inf")
	queue[0] = 0
	backtrack = defaultdict(int)
	while queue:
		v1, p = queue.popitem()
		length = p
		if v1 == n-1:
			d, path = n-1, [n-1]
			while backtrack[d] != 0:
				path = [backtrack[d]] + path
				d = backtrack[d]
			return length, [0] + path
		for v2, cost in g.get(v1, ()):
			if (v2 in queue) and (queue[v2] > p + cost):
				queue[v2] = p+cost
				backtrack[v2] = v1
	return float("inf")

def main():
	print(shortest1(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))

if __name__ == '__main__':
	main()


