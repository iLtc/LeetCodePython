class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1

        negative = False

        if dividend < 0:
            negative = not negative
            dividend = - dividend

        if divisor < 0:
            negative = not negative
            divisor = - divisor

        memory = {}

        count = 1
        total = divisor

        while total <= dividend:
            memory[count] = total

            total += total
            count += count

        result = 0

        for count, total in reversed(memory.items()):
            if total <= dividend:
                result += count
                dividend -= total

        return - result if negative else result
