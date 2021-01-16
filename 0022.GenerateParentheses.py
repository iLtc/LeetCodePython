class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']

        results = []
        self.helper('', n, 0, 0, results)

        return results

    def helper(self, s: str, n: int, left: int, right: int, results: List[str]):
        if len(s) == 2 * n:
            results.append(s)
            return

        if left < n:
            self.helper(s + '(', n, left + 1, right, results)

        if right < left:
            self.helper(s + ')', n, left, right + 1, results)

