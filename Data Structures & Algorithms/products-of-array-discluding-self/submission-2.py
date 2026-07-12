class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [None] * len(nums)

        # [48, 24, 12, 8], postfix = 48
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix = prefix * nums[i]
        
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            output[i] *= postfix
            postfix = postfix * nums[i]

        return output


            