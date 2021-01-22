# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root: TreeNode):
            if root is None:
                return
    
            helper(root.left)
            helper(root.right)
            results.append(root.val)
    
        results = []
        helper(root)
        return results
