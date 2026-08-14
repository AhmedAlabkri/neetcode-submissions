class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mydict1 = {}
        mydict2 = {}

        if len(s1) > len(s2):
            return False
            
        import string
        for char in string.ascii_lowercase:
            mydict1[char] = 0
            mydict2[char] = 0
        
        for char in s1:
            if char in mydict1:
                mydict1[char] +=1

        
        i = 0
        j = len(s1)
        for k in range(i,j):
            mydict2[s2[k]] += 1

            # compare matches
        matches = 26
        for key in mydict1:
            if mydict1[key] == mydict2[key]:
                continue
            elif mydict1[key] != mydict2[key]:
                matches -= 1
        if matches == 26:
            return True
        i += 1

        while j < len(s2):
            if mydict1[s2[i - 1]] == mydict2[s2[i - 1]]:
                matches -= 1

            mydict2[s2[i - 1]] -= 1

            if mydict1[s2[i - 1]] == mydict2[s2[i - 1]]:
                matches += 1


            if mydict1[s2[j]] == mydict2[s2[j]]:
                matches -= 1
            mydict2[s2[j]] += 1
            if mydict1[s2[j]] == mydict2[s2[j]]:
                matches += 1

            if matches == 26:
                return True

            i += 1
            j += 1
            
        return False

            
            




    