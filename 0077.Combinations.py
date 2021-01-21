class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        
        self.helper(1, n, k, [], results)
        
        return results
        
        
    def helper(self, i: int, n: int, k: int, result: List[int], results: List[List[int]]):
        if len(result) == k:
            results.append(result[:])
        else:
            for j in range(i, n + 1):
                result.append(j)
                
                self.helper(j + 1, n, k, result, results)
                
                del result[-1]
        
