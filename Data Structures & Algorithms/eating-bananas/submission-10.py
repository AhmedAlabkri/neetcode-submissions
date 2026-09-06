class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        i = 1
        j = max(piles)
        bestValid = 0

        while i <= j:
            mid = (i+j) // 2
            counter = 0
            for b in piles:
                x = (b + mid - 1) // mid
                counter+=x

            if counter <= h:
                bestValid = mid
                j = mid - 1
            else:
                i = mid + 1
        return bestValid

        # [1,4,3,2] , h = 9
        # i = 1 , j = 4 , bestValid = 0 ,, mid = 2 , counter = 6
        # bestValid = 6

            


        