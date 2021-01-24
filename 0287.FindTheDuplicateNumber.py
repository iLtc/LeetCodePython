class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        memory = set()
        
        for num in nums:
            if num in memory:
                return num
            
            memory.add(num)
