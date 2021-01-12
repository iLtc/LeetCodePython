class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for i in range(numRows)]

        i = 0
        up = True

        for c in s:
            rows[i].append(c)

            if i == 0 or i == numRows - 1:
                up = not up

            i += -1 if up else 1

        result = ""

        for row in rows:
            result += "".join(row)

        return result

