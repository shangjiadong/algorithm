"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5

All root-to-leaf paths are:
["1->2->5", "1->3"]

input = [1,2,3,null,5]  
output = ["1->2->5","1->3"]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        #root = self.TreeNode()
        if not root: return []
        if not root.left and not root.right: return [str(root.val)]
        return [str(root.val) + '->' + i for i in self.binaryTreePaths(root.left)] + \
            [str(root.val) + '->' + i for i in self.binaryTreePaths(root.right)]
    
