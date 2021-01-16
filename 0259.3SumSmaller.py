class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()

        results = 0

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] + nums[i] < target:
                    results += right - left

                    left += 1

                else:
                    right -= 1

        return results
