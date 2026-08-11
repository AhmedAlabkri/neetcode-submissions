class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 0 - 9 & a - z / A - Z

        my_dict = {}
        
        i = 0
        j = i
        maxSeq = 0
        while j < len(s):
            if s[j] not in my_dict:
                my_dict[s[j]] = j
                j += 1

            else:
                index = my_dict[s[j]]
                my_dict[s[j]] = j
                maxSeq = max(j - i, maxSeq)
                # restarting
                i = max(i, index + 1)
                j += 1
                
        maxSeq = max(j - i, maxSeq)

        return maxSeq




        