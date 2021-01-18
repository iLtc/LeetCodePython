class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[0] * n for _ in range(m)]

        for i in range(n):
            d[0][i] = 1

        for i in range(1, m):
            d[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = d[i][j - 1] + d[i - 1][j]

        return d[m - 1][n - 1]
