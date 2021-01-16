class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        number2letters = {'2': ['a', 'b', 'c'],
                          '3': ['d', 'e', 'f'],
                          '4': ['g', 'h', 'i'],
                          '5': ['j', 'k', 'l'],
                          '6': ['m', 'n', 'o'],
                          '7': ['p', 'q', 'r', 's'],
                          '8': ['t', 'u', 'v'],
                          '9': ['w', 'x', 'y', 'z']}
                        
        results = [""]
        old_results = None
        
        for digit in digits:
            old_results = results
            results = []
            
            for result in old_results:
                for letter in number2letters[digit]:
                    results.append(result + letter)
                    
        return results

