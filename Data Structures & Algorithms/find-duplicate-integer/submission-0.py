class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        myset = set()

        for i in nums:
            if i not in myset:
                myset.add(i)
            else:
                return i
        
        