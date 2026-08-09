class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        maxConc = 0
        nums_set = set(sorted(nums))

        for i in nums_set:
            
            if i - 1 not in nums_set:
                currConc = 1
                currStart = i
                currMax = i + 1
                while currMax in nums_set:
                    currMax += 1
                    currConc += 1
            else:
                currConc = 1
            maxConc = max(currConc, maxConc)

        return maxConc
            

                










