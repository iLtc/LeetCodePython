class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        self.helper(nums, 0, len(nums), results)

        return results

    def helper(self, nums: List[int], start: int, length: int, results: List[List[int]]):
        if start == length:
            results.append(nums[:])
            return

        for i in range(start, length):
            nums[start], nums[i] = nums[i], nums[start]

            self.helper(nums, start + 1, length, results)

            nums[start], nums[i] = nums[i], nums[start]

