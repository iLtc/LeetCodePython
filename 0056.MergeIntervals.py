class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        results = []

        for i in intervals:
            if len(results) == 0:
                results.append(i)

            else:
                if i[0] <= results[-1][1]:
                    results[-1][1] = max(results[-1][1], i[1])
                else:
                    results.append(i)

        return results
