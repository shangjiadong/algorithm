"""
   Number of n-node BSTs

   input: n
   output: number of n-node BSTs

   >>> bsts(2)
   2
   >>> bsts(3)
   5
   >>> bsts(5)
   42

   [HINT] there are two 2-node BSTs:
      2    1
     /      \
    1        2
"""

def bsts(n):
    tree_dict = {0: 1, 1: 1}
    if n in tree_dict:
        return tree_dict[n]
    else:
        total = 0
        for i in range(n):
            total += bsts(i) * bsts(n-1-i)
        tree_dict[n] = total
        return tree_dict[n]

def main():
	print(bsts(1))
	print(bsts(2))
	print(bsts(3))
	print(bsts(4))
	print(bsts(5))
	print(bsts(6))

if __name__ == '__main__':
	main()
