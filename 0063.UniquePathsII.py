class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        d = [[0] * n for _ in range(m)]

        d[0][0] = 1

        for i in range(1, n):
            if obstacleGrid[0][i] != 1 and d[0][i - 1] == 1:
                d[0][i] = 1

        for i in range(1, m):
            if obstacleGrid[i][0] != 1 and d[i - 1][0] == 1:
                d[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue

                d[i][j] = d[i][j - 1] + d[i - 1][j]

        return d[m - 1][n - 1]
