class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        dictS = {}
        dictT = {}

        for char in t:
            if char not in dictS:
                dictS[char] = 0
                dictT[char] = 1
            else:
                dictT[char] += 1


        target = len(dictT)
        counter = 0
        resultTracker = None # (Length, (indexi, indexj))
        i = 0
        j = 0

        while j < len(s):
            if s[j] not in dictS:
                pass
            else:
                dictS[s[j]] += 1

                if dictS[s[j]] == dictT[s[j]]:
                    counter += 1


            # reverse until counter is not valid
            while counter == target:
                if resultTracker == None:
                    resultTracker = (j - i, (i, j))
                elif resultTracker[0] > j - i:
                    resultTracker = (j - i, (i, j))

                if s[i] in dictS:
                    dictS[s[i]] -= 1

                    if dictS[s[i]] >= dictT[s[i]]:
                        pass
                    else:
                        counter -= 1
                i += 1
            j += 1
        if resultTracker != None:
            result = s[resultTracker[1][0]:resultTracker[1][1] + 1]
            return result
        else:
            return ""
            

            
            






        

