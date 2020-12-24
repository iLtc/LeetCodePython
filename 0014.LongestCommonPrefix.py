class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        strs.sort()
        
        result = ""
        
        for i, j in zip(strs[0], strs[-1]):
            if i == j:
                result += i
            else:
                break
                
        return result
