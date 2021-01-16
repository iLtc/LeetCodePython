class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == "" or s.isspace():
            return 0

        return len(s.split()[-1])

