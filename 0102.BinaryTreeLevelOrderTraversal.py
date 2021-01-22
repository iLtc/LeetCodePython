# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        results = [[]]
        queue = [root, None]
        
        while queue:
            node = queue.pop(0)
            
            if node is None:
                if queue:
                    queue.append(None)
                    results.append([])
                    
            else:
                results[-1].append(node.val)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
        return results
