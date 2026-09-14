class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                sloww = slow
                break
        
        slow = 0

        while True:
            slow = nums[slow]
            sloww = nums[sloww]

            if slow == sloww:
                return slow
        