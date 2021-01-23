# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodes = []
        self.helper(root)
        
    def helper(self, node: TreeNode):
        if node:
            self.helper(node.left)
            self.nodes.append(node)
            self.helper(node.right)
        
    def next(self) -> int:
        return self.nodes.pop(0).val
        
    def hasNext(self) -> bool:
        return len(self.nodes) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
