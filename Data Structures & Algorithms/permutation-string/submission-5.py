class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        import string

        if len(s1) > len(s2):
            return False
        
        dict_s1 = {}
        dict_s2 = {}

        for char in string.ascii_lowercase:
            dict_s1[char] = 0
            dict_s2[char] = 0

        for char in s1:
            dict_s1[char] += 1
        
        i = 0
        j = len(s1)
        for k in range(i, j):
            dict_s2[s2[k]] += 1

        matches = 26
        for key in dict_s1:
            if dict_s1[key] == dict_s2[key]:
                continue
            else:
                matches -= 1
        if matches == 26:
            return True
      
        i += 1
        while j < len(s2):

            if dict_s2[s2[i - 1]] == dict_s1[s2[i - 1]]:
                matches -= 1

            dict_s2[s2[i - 1]] -= 1 #

            if dict_s2[s2[i - 1]] == dict_s1[s2[i - 1]]:
                matches += 1

            if dict_s2[s2[j]] == dict_s1[s2[j]]:
                matches -= 1

            dict_s2[s2[j]] += 1 #

            if dict_s2[s2[j]] == dict_s1[s2[j]]:
                matches += 1
            
            if matches == 26:
                return True
            i += 1
            j += 1
            
        return False

            


        