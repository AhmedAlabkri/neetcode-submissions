class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        my_Adict = {}
        my_Bdict = {}

        for char in s:
            if char not in my_Adict:
                my_Adict[char] = 1
            else:
                my_Adict[char] +=1

        for char in t:
            if char not in my_Bdict:
                my_Bdict[char] = 1
            else:
                my_Bdict[char] += 1

        if my_Adict == my_Bdict:
            return True
        else:
            return False
        