class Solution:
    def simplifyPath(self, path: str) -> str:
        results = []
        
        for dir in path.split('/'):
            if dir == "" or dir == ".":
                continue
            
            elif dir == "..":
                if len(results) > 0:
                    del results[-1]
                    
            else:
                results.append(dir)
                
        return "/" + "/".join(results)
