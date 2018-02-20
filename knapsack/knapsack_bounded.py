"""

   Bounded Knapsack

   You have n items, each with weight w_i and value v_i, and has c_i copies.
   **All numbers are positive integers.**
   What's the best value for a bag of W?

   >>> best(3, [(2, 4, 2), (3, 5, 3)])
   (5, [0, 1])

   the input to the best() function is W and a list of triples (w_i, v_i, c_i).

   tie-breaking: same as in p1:

   >>> best(3, [(1, 5, 2), (1, 5, 3)])
   (15, [2, 1])

   >>> best(3, [(1, 5, 1), (1, 5, 3)])
   (15, [1, 2])

   >>> best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)])
   (130, [6, 4, 1])

   >>> best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)])
   (236, [6, 7, 3, 7, 2])

   Q: What are the time and space complexities?

   filename: knapsack_bounded.py

"""
def best(cap, item):
    opt = [[0 for i in range(len(item)+1)] for j in range(cap+1)]
    back = [[0 for j in range(len(item)+1)] for j in range(cap+1)]
    for i, (wt, val, cp) in enumerate(item):
        i += 1
        for weight in range(1,cap+1):
            for j in range(min(cp, weight//wt)+1):
                if weight >= j*wt and opt[weight][i] < opt[weight-j*wt][i-1] + j*val:
                    opt[weight][i] = opt[weight-j*wt][i-1] + j*val
                    back[weight][i-1] = j
    return opt[cap][len(item)], backtrack(len(item)-1, back, cap, item)

def backtrack(i, back, cap, item):
    	if i < 0:
        	return []
        return backtrack(i-1, back, cap-item[i][0]*back[cap][i], item) + [back[cap][i]]    

def main():
	print(best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]) == (236, [6, 7, 3, 7, 2]))
	print(best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)]) == (130, [6, 4, 1]))
	print(best(3, [(1, 5, 1), (1, 5, 3)]) == (15, [1, 2]))
	print(best(3, [(1, 5, 2), (1, 5, 3)]) == (15, [2, 1]))

if __name__ == '__main__':
	main()