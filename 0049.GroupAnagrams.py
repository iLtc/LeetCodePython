class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}

        for s in strs:
            key = tuple(sorted(s))

            if key not in results:
                results[key] = []

            results[key].append(s)

        return results.values()
