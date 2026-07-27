class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        R = max(piles)
        L = 1
        betterResult = max(piles)
        while L <= R:
            result = 0
            mid = (L + R) // 2

            for i in piles: # [1, 2, 3, 4]
                result += (i + mid - 1) // mid
            
            if result > h:
                L = mid + 1
            
            elif result <= h:
                R = mid - 1
                betterResult = min(mid, betterResult)

        return betterResult






