# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.helper(root, root)
    
    def helper(self, first: TreeNode, second: TreeNode) -> bool:
        if first == None and second == None:
            return True
        
        if first == None or second == None:
            return False
        
        return first.val == second.val and self.helper(first.left, second.right) and self.helper(first.right, second.left)
        
