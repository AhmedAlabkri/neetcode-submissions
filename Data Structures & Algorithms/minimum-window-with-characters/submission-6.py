class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""
        d_s = {}
        d_t = {}

        for char in t:
            if char not in d_t:
                d_t[char] = 1
            else:
                d_t[char]+=1
        
        matches = len(d_t)

        i = 0
        j = len(t)
        counter = 0
        result = None # (i,j, j-i)
        for c in range(j):
            if s[c] not in d_s:
                d_s[s[c]] = 1
                if s[c] in d_t and d_s[s[c]] == d_t[s[c]]:
                    counter +=1
            else:
                d_s[s[c]] += 1
                if s[c] in d_t and d_s[s[c]] == d_t[s[c]]:
                    counter +=1
        if counter == matches:
            return s[i:j]
        
        while j < len(s):

            if s[j] not in d_s:
                d_s[s[j]] = 1
            else:
                d_s[s[j]] += 1
            if s[j] in d_t:
                if d_s[s[j]] == d_t[s[j]]:
                    counter+=1
                else:
                    pass
            
            while counter == matches:
                if result == None:
                    result = (i, j, j-i)
                else:
                    if result[2] > j-i:
                        result = (i, j, j-i)
                d_s[s[i]] -=1
                if s[i] in d_t:
                    if d_s[s[i]] >= d_t[s[i]]:
                        pass
                    else:
                        counter-=1
                
                i+=1
            j+=1
        
        if result:
            return s[result[0]:result[1]+1]
        
        return ""




            
        

        

