# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(0, len(nums) - 1, nums)
        
        
    def helper(self, start: index, end: index, nums: List[int]) -> TreeNode:
        if start > end:
            return None
        
        mid = (start + end) // 2
        
        node = TreeNode(val=nums[mid])
        
        node.left = self.helper(start, mid - 1, nums)
        node.right = self.helper(mid + 1, end, nums)
        
        return node
        
