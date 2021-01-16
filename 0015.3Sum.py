class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        results = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    results.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif nums[left] + nums[right] < -nums[i]:
                    left += 1

                else:
                    right -= 1

        return results
