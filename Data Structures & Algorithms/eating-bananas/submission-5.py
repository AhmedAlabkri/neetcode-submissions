class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        bestRate = R
        while L <= R:
            mid = (L + R) // 2
            result = 0
            for i in piles:
                result += (i + mid - 1) // mid
            
            if result > h:
                # increase rate
                L = mid + 1
            
            elif result <= h:
                # decrese rate
                bestRate = min(bestRate, mid)
                R = mid - 1
            
        return bestRate







                


        