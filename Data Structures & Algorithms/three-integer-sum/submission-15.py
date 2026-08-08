class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for c in range(len(nums)):

            if c > 0 and nums[c] == nums[c-1]:
                continue
            #if c > 0:

            target = -nums[c]

            a = c + 1
            b = len(nums) - 1
            while a < b:

                if nums[a] + nums[b] == target:
                    result.append([nums[a], nums[b], -target])
                    a += 1
                    while a < b and nums[a] == nums[a - 1]:
                        a += 1
                    b -= 1
                    while a < b and nums[b] == nums[b + 1]:
                        b -= 1

                elif nums[a] + nums[b] < target:
                    a += 1
                    while a < b and nums[a] == nums[a - 1]:
                        a += 1

                elif nums[a] + nums[b] > target:
                    b -= 1
                    while a < b and nums[b] == nums[b + 1]:
                        b -= 1
            
        return result

                                
                        



                

                    


        