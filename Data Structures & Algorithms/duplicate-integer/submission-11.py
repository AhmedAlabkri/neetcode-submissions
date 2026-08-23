class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        myset = set()

        for i in nums:
            if i not in myset:
                myset.add(i)
            else:
                return True
        return False
        