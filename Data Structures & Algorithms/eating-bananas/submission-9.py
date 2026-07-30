class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        while L < R:

            k = (L + R) // 2
            result = 0
            for i in piles:
                result += (i + k - 1) // k

            if result > h:
                L = k + 1
            elif result <= h:
                R = k
            
        return R

            
            
            









        