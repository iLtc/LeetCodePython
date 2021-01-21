class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        
        self.helper(0, nums, [], results)
        
        return results
    
    def helper(self, index: int, nums, result: List[int], results: List[List[int]]):
        if index >= len(nums):
            results.append(result[:])
        
        else:
            self.helper(index + 1, nums, result, results)
            
            result.append(nums[index])
            
            self.helper(index + 1, nums, result, results)
            
            del result[-1]
        
