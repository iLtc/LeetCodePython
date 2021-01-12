class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        seen = {}

        i = 0
        j = 0

        while i < len(s) and j < len(s):
            if s[j] in seen:
                i = max(i, seen[s[j]] + 1)

            seen[s[j]] = j

            result = max(result, j - i + 1)

            j += 1

        return result
