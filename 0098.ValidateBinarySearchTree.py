# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root: TreeNode, left: int, right: int) -> bool:
            if root is None:
                return True
            
            if root.val <= left or root.val >= right:
                return False
            
            return helper(root.left, left, root.val) and helper(root.right, root.val, right)
        
        return helper(root, -math.inf, math.inf)
