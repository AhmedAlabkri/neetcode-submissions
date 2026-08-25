class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [9, 1, 2, 3, 4, 5]    # target = 9
        i = 0
        j = len(nums) - 1

        while i < j:
            mid = (i+j) // 2     


            if nums[mid] == target:
                return mid


            if nums[mid] > nums[j]:
                if nums[i] <= target <= nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1

            elif nums[mid] < nums[j]:
                if nums[mid] <= target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1

        if nums[j] == target:
            return j
        else:
            return -1



