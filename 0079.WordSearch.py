class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m, self.n = len(board), len(board[0])
        self.len = len(word)
        
        for row in range(self.m):
            for col in range(self.n):
                if board[row][col] == word[0] and self.helper(row, col, 0, board, word):
                    return True
                
        return False
        
    def helper(self, row: int, col: int, index: int, board: List[List[str]], word: str) -> bool:
        if index == self.len:
            return True
        
        if row < 0 or row >= self.m or col < 0 or col >= self.n:
            return False
        
        if board[row][col] != word[index]:
            return False
        
        char = board[row][col]
        board[row][col] = '.'
        
        for r, c in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            result = self.helper(row + r, col + c, index + 1, board, word)
            
            if result:
                return True
                
        board[row][col] = char
                
        return False
