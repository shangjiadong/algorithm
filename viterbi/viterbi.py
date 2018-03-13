"""
3. [WILL BE GRADED]
   Viterbi Algorithm For Longest Path in DAG (see DPV 4.7, [2], CLRS problem 15-1)
   
   Recall that the Viterbi algorithm has just two steps:
   a) get a topological order (use problem 1 above)
   b) follow that order, and do either forward or backtrackward updates

   This algorithm captures all DP problems on DAGs, for example,
   longest path, shortest path, number of paths, etc.

   In this problem, given a DAG (guaranteed acyclic!), output a pair (l, p) 
   where l is the length of the longest path (number of edges), and p is the path. (you can think of each edge being unit cost)

   e.g., for the above example:

   >>> longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
   (5, [0, 2, 3, 4, 5, 6])

   Tie-breaking: arbitrary. any longest path is fine.   
"""
from collections import defaultdict

def order(n, alist):
	topo, degree_in = [], [0]*n
	adj_dict = defaultdict(list)
	# calculated the in degree of a node
	for (i,j) in alist:
		degree_in[j] += 1
		adj_dict[i].append(j) # which node is its neighbor
	# populate the queue with the 0 in-egree nodes
	queue = []
	for k in range(n): 
		if degree_in[k] == 0:
			queue.append(k)
	# give a pointer to the beginning of the queue, while appending, move the pointer down 1
	# continue till the queue is empty
	pointer= 0
	while len(queue) != pointer:
		out = queue[pointer]
		topo.append(out)
		pointer += 1 # move pointer to pop
		neighbor = adj_dict[out]
		for node in neighbor:
			degree_in[node] -= 1
			if degree_in[node] == 0:
				queue.append(node)
	if len(topo) != n: return None
	return topo

def longest(n, alist):
	topo = order(n, alist)
	degree_in = defaultdict(int)
	adj_dict = defaultdict(list)
	for (u, v) in alist:
	    degree_in[v] += 1
	    adj_dict[v].append(u)
	backtrack = defaultdict(int)
	steps = defaultdict(int)
	max_step, end = 0, 0
	for node in topo:
	    if degree_in[node] != 0:
	        neighbor = adj_dict[node]
	        for nn in neighbor:
	            if steps[node] < steps[nn] + 1:
	                steps[node] = steps[nn] + 1
	                backtrack[node] = nn
	        if steps[node] > max_step:
	            max_step = steps[node]
	            end = node
	long_path, vertex = [], end
	long_path.append(vertex)
	while degree_in[vertex] != 0:
	    vertex = backtrack[vertex]
	    long_path = [vertex] + long_path
	return max_step, long_path

def main():
	print(longest(8, [(0, 2), (1, 2), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (5, 6), (5, 7)]))

if __name__ == '__main__':
	main()