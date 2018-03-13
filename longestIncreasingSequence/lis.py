"""
1. Longest (Strictly) Increasing Subsequence
   
   input/output are lower-case strings:

   >>> lis("aebbcg")
   "abcg"

   >>> lis("zyx")
   "z"

   tiebreaking: arbitrary. any optimal solution is ok.

   Q: What are the time and space complexities?
"""

"""
L(i) = 1 + max( L(j) ) where 0 < j < i and arr[j] < arr[i]; or
L(i) = 1, if no such j exists.
To find the LIS for a given array, we need to return max(L(i)) where 0 < i < n.
"""

def lis(astring):
	len_s = len(astring)
	longseq = []
	longseq.append([0, astring[0]])
	for i in range(1, len_s):
		lis_max, pos_max = -1, -1
		for j in range(i):
			if (astring[j] < astring[i]) and (longseq[j][0] > lis_max):
				lis_max, pos_max = longseq[j][0], j
		if lis_max == -1:
			longseq.append([0, astring[i]])
		else:
			longseq.append([lis_max+1, longseq[pos_max][1]+astring[i]])
	return longseq[len_s-1][1]


def main():
	print(lis("aebbcg"))
	print(lis("zyx"))

if __name__ == '__main__':
	main()



