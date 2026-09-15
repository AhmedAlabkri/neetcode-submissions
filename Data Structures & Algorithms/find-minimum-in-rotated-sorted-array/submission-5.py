class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,5,6,1,2]
        # [4,5,0,1,2,3]
        i = 0
        j = len(nums) - 1

        result = None

        while i <= j:
            mid = (i+j) // 2

            if nums[mid] >= nums[-1]:
                i = mid + 1
                if result != None:
                    result = min(result, nums[-1])
                else:
                    result = nums[-1]
            else:
                j = mid - 1
                if result != None:
                    result = min(result, nums[mid])
                else:
                    result = nums[mid]
        return result
                



        
        