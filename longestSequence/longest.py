"""
>>> longest([[], 1, []])
0

>>> longest([[[], 1, []], 2, [[], 3, []]])
2

>>> longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]])
5
"""
# def height(tree):
#     if len(tree) == 0:
#         return 0
#     else:
#         return 1 + max(height(tree[0]), height(tree[2]))

# def longest(tree):
    
#     else:
#         l_left = longest(tree[0])
#         l_right = longest(tree[2])
#         return max(l_left, l_right, height(tree[0]) + height(tree[2]))
def _longest_helper(tree):
    if not tree:
        return 0, 0
    l_left, h_left = _longest_helper(tree[0])
    l_right, h_right = _longest_helper(tree[2])
    return max(l_left, l_right, h_left + h_right), 1 + max(h_left, h_right)

def longest(tree):
    return _longest_helper(tree)[0]
    
if __name__ == "__main__":
    print(longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]))
    