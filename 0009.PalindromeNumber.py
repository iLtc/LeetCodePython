class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        x = str(x)
        length = len(x)
        
        for i in range(length):
            if x[i] != x[length - 1 - i]:
                return False
            
        return True
