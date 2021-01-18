class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        current = 0

        last = len(nums) - 1

        while current <= furthest < last:
            furthest = max(furthest, current + nums[current])
            current += 1

        return furthest >= last

