class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        nums_set = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in nums_set:
                curr_longest = 1
                next_num = nums[i] + 1

                while next_num in nums_set:
                    curr_longest += 1
                    
                    next_num += 1

                longest = max(longest, curr_longest)

        return longest
                        
            
            


