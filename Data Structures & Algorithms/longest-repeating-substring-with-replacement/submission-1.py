class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        hashMap = {}
        best = 0
        while j < len(s):
            if s[j] in hashMap:
                hashMap[s[j]] +=1
            else:
                hashMap[s[j]] = 1
            
            windowLength = j - i + 1
            if (windowLength - max(hashMap.values())) <= k:
                best = max(windowLength, best)
            else:
                hashMap[s[i]] -= 1
                i +=1
            j+=1
        return best





        