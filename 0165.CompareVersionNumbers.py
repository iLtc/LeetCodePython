class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split(".")]
        v2 = [int(x) for x in version2.split(".")]
        
        min_length = min(len(v1), len(v2))
        
        for i in range(min_length):
            if v1[i] < v2[i]:
                return -1
            
            if v1[i] > v2[i]:
                return 1
            
        for i in range(min_length, len(v1)):
            if v1[i] > 0:
                return 1
            
        for i in range(min_length, len(v2)):
            if v2[i] > 0:
                return -1
            
        return 0
