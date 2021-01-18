class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = None
        nums.sort()

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                temp = nums[i] + nums[left] + nums[right]

                if temp == target:
                    return target

                if result is None or abs(temp - target) < abs(result - target):
                    result = temp

                if temp < target:
                    left += 1
                else:
                    right -= 1

        return result
