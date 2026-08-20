class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        from collections import deque
        q = deque()

        result = []

        i = 0
        j = 0

        while j < len(nums):

            while q and nums[q[-1]] < nums[j]:
                q.pop()
            q.append(j)


            
            if (j - i)+1 >= k:
                result.append(nums[q[0]])

                if i == q[0]:
                    q.popleft()
                i+= 1

            j+= 1
        
        return result




            



            
                