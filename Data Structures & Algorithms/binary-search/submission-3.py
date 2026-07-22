class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            # [0, 1, 2, 3, 4, 5]
            # [-1, 0, 2, 4, 6, 8] 
            if nums[mid] > target:
                right = mid - 1
                mid = (left + right) // 2
    
            elif nums[mid] < target:
                left = mid + 1
                mid = (left + right) // 2

        
        return -1