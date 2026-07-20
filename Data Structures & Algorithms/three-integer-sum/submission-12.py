class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        res = []

        for c in range(len(nums)):
            if c > 0 and nums[c] == nums[c - 1]:
                continue

            a = c + 1
            b = len(nums) - 1

            if nums[c] > 0:
                return res

            target = -nums[c]
            
            while a < b:

                while a < b and nums[a] + nums[b] == target:
                    res.append([nums[a], nums[b], nums[c]])

                    a += 1
                    while a < b and nums[a] == nums[a - 1]:
                        a += 1
                    b -= 1
                    while a < b and nums[b] == nums[b + 1]:
                        b -= 1
                

                while a < b and nums[a] + nums[b] > target:
                    b -= 1

                while a < b and nums[a] + nums[b] < target:
                    a += 1
        
        return res
                
                

            




        