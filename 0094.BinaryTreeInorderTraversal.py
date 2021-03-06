# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root: TreeNode):
            if root is None:
                return
            
            helper(root.left)
            results.append(root.val)
            helper(root.right)
            
        results = []
        helper(root)
        return results
