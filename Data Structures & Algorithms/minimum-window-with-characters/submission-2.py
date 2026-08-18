class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        dict_s = {}
        dict_t = {}


        for char in t:
            if char not in dict_s:
                dict_s[char] = 0
                dict_t[char] = 1
            else:
                dict_t[char] += 1

        resultTracked = None # (j-i, (i, j))
        target = len(dict_t)
        counter = 0
        i = 0
        j = i


        while j < len(s):

            if s[j] not in dict_s:
                pass
            else:
                dict_s[s[j]] += 1

                if dict_s[s[j]] > dict_t[s[j]]:
                    pass
                elif dict_s[s[j]] < dict_t[s[j]]:
                    pass
                elif dict_s[s[j]] == dict_t[s[j]]:
                    counter += 1

                    while counter == target:
                        if resultTracked != None:
                            if (j-i) < resultTracked[0]:
                                resultTracked = (j-i, (i, j))
                        else:
                            resultTracked = (j-i, (i, j))
                        
                        if s[i] in dict_s:
                            dict_s[s[i]] -= 1

                            if dict_s[s[i]] > dict_t[s[i]]:
                                pass
                            elif dict_s[s[i]] < dict_t[s[i]]:
                                counter -= 1
                            elif dict_s[s[i]] == dict_t[s[i]]:
                                pass

                        i += 1
                                
            j += 1

        if resultTracked == None or len(s) < len(t):
            return ""
        else:
            return s[resultTracked[1][0]:resultTracked[1][1]+1]


    






            
