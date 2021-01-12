class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0

        result = int("".join(reversed(list(str(abs(x))))))

        if negative:
            result = - result

        if -2 ** 31 <= result <= 2 ** 31 - 1:
            return result

        return 0

