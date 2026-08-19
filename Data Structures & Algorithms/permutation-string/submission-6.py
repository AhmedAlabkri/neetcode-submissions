class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        
        mydicts1 = {}
        mydicts2 = {}
        import string
        for char in string.ascii_lowercase:
            if char not in mydicts1:
                mydicts1[char] = 0
                mydicts2[char] = 0

        for char in s1:
            if char in mydicts1:
                mydicts1[char] += 1
        

        i = 0
        j = len(s1)

        for c in range(i, j):
            if s2[c] in mydicts2:
                mydicts2[s2[c]] += 1
        

        matches = 26

        for key in mydicts1:
            if mydicts1[key] != mydicts2[key]:
                matches -= 1
            
        if matches == 26:
            return True
        
        i += 1
        while j < len(s2):

            if mydicts1[s2[i - 1]] == mydicts2[s2[i - 1]]:
                matches -= 1
            
            mydicts2[s2[i - 1]] -= 1

            if mydicts1[s2[i - 1]] == mydicts2[s2[i - 1]]:
                matches += 1
            

            if mydicts1[s2[j]] == mydicts2[s2[j]]:
                matches -= 1
            
            mydicts2[s2[j]] += 1

            if mydicts1[s2[j]] == mydicts2[s2[j]]:
                matches += 1
            
            if matches == 26:
                return True

            i += 1
            j += 1
        
        return False










        
        