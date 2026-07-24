class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [-1,0,2,4,6,8] , t = 1
        right = (len(nums) - 1)
        left = 0

        while not left > right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                left = mid + 1
            
            elif nums[mid] > target:
                right = mid - 1

        return -1




