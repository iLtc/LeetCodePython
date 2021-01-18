class Solution:
    def countAndSay(self, n: int) -> str:
        return "".join(self.helper(n))

    def helper(self, n: int) -> [str]:
        if n == 1:
            return ["1"]

        prev_result = self.helper(n - 1)
        result = []

        prev_char = prev_result[0]
        count = 1

        for char in prev_result[1:]:
            if char == prev_char:
                count += 1
            else:
                result.append(str(count))
                result.append(prev_char)
                prev_char = char
                count = 1

        result.append(str(count))
        result.append(prev_char)

        return result
