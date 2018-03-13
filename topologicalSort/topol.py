"""
2. Topological Sort
   
   For a given directed graph, output a topological order if it exists.
   
   Tie-breaking: ARBITRARY tie-breaking. This will make the code 
   and time complexity analysis a lot easier. 

   e.g., for the following example:

     0 --> 2 --> 3 --> 5 --> 6
        /    \   |  /    \
       /      \  v /      \
     1         > 4         > 7

   >>> order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
   [0, 1, 2, 3, 4, 5, 6, 7]

   If we flip the (3,4) edge:

   >>> order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])
   [0, 1, 2, 4, 3, 5, 6, 7]

   If there is a cycle, output None

   >>> order(4, [(0,1), (1,2), (2,1), (2,3)])
   None

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

def main():
	print(order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
	print(order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)]))
	print(order(4, [(0,1), (1,2), (2,1), (2,3)]))


if __name__ == '__main__':
	main()

