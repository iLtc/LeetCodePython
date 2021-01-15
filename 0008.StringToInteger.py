class Solution:
    def myAtoi(self, s: str) -> int:
        isNegative = False
        result = None
        
        for c in s:
            if '0' <= c <= '9':
                if result is None:
                    result = int(c)
                else:
                    result = result * 10 + int(c)
                    
            else:
                if result is not None:
                    break
                
                if c == ' ':
                    continue
                
                if c == '-' or c == '+':
                    isNegative = c == '-'
                    result = 0
                    continue
                
                break
            
        if result is None:
            result = 0
            
        if isNegative:
            result = - result
            
        if result < - 2 ** 31:
            return - 2 ** 31
        
        if result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        
        return result
