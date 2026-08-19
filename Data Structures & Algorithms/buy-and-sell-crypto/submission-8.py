class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i = 0
        j = 0

        result = 0
        while j < len(prices):

            if prices[j] < prices[i]:
                i = j
            elif prices[j] > prices[i]:
                result = max(result, prices[j] - prices[i])
                j += 1
            else:
                j += 1
        
        return result

