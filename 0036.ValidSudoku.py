class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        boxes = [[] for _ in range(9)]

        for row in range(9):
            for col in range(9):
                num = board[row][col]

                if num == '.':
                    continue

                box = (row // 3) * 3 + col // 3

                if num in rows[row] or num in cols[col] or num in boxes[box]:
                    return False

                rows[row].append(num)
                cols[col].append(num)
                boxes[box].append(num)

        return True

