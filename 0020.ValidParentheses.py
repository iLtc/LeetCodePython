class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for x in list(s):
            if x in ['(', '[', '{']:
                stack.append(x)
                
            else:
                if len(stack) == 0:
                    return False
                
                if stack[-1] != mapping[x]:
                    return False
                
                del stack[-1]
                
        if len(stack) > 0:
            return False
        else:
            return True
                
                
