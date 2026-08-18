class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        result = 0

        i = 0
        j = 1

        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
                j += 1
            elif prices[j] > prices[i]:
                result = max(prices[j] - prices[i], result)
                j += 1
            else:
                j+=1

            
        
        return result



