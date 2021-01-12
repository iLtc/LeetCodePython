class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        l = len(s)

        for i in range(l):
            if len(result) < 1:
                result = s[i]

            for j in range(1, l):
                if i - j < 0 or i + j >= l:
                    break

                if s[i - j] == s[i + j]:
                    if 2 * j + 1 > len(result):
                        result = s[i - j : i + j + 1]
                else:
                    break

            if i < l - 1 and s[i] == s[i + 1]:
                if len(result) < 2:
                    result = s[i : i + 2]

                for j in range(1, l):
                    if i - j < 0 or i + 1 + j >= l:
                        break

                    if s[i - j] == s[i + 1 + j]:
                        if 2 * j + 2 > len(result):
                            result = s[i - j : i + j + 2]
                    else:
                        break

        return result

