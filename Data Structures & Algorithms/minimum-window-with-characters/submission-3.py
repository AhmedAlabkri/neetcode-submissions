class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        d_t = {}
        d_s = {}

        for char in t:
            if char not in d_t:
                d_t[char] = 1
            else:
                d_t[char] +=1
        
        i = 0
        j = 0
        matches = len(d_t)
        count = 0
        result = None # (i, j, j-i)
        while j < len(s):
            
            if s[j] not in d_s:
                d_s[s[j]] = 1
            else:
                d_s[s[j]] += 1
            if s[j] in d_t:
                if d_s[s[j]] == d_t[s[j]]:
                    count +=1

                
            while count == matches:
                if result and result[2] > j-i:
                    result = (i, j, j-i) 
                if not result:
                    result = (i, j, j-i)

                d_s[s[i]] -= 1
                if s[i] in d_t:
                    if d_s[s[i]] < d_t[s[i]]:
                        count-=1
                i +=1
            j+=1
        
        if result:
            return s[result[0]:result[1]+1]
        return ""



            



