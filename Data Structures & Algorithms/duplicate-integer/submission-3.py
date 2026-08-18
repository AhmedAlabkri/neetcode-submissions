class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_s = {}

        for i in nums:
            if i not in dict_s:
                dict_s[i] = 1
            else:
                return True
        
        return False