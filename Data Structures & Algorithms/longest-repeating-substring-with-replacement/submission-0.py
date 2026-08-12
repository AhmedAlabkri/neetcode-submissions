class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        my_dict = {} # "A" : int

        i = 0
        j = i
        my_dict[s[i]] = 1

        while j != len(s) and i <= j:

            window_length = j - i + 1

            # 
            most_common = float("-inf")
            for x in my_dict: # 26
                most_common = max(my_dict.get(x), most_common)

            if (window_length - most_common) <= k:
                result = max(result, window_length)
                # moving j
                j += 1
                if j < len(s) and s[j] not in my_dict:
                    my_dict[s[j]] = 1
                elif j < len(s) and s[j] in my_dict:
                    my_dict[s[j]] += 1
            else:
                my_dict[s[i]] -= 1
                i += 1
        return result



            
            
