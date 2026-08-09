class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = i + 1
        maxProfit = 0
        while i < j and i < (len(prices) - 1) and j < len(prices):
            if prices[j] - prices[i] <= 0:
                i += 1
                j = i + 1

            else:
                maxProfit = max(maxProfit, prices[j] - prices[i])
                j+=1
        
        return maxProfit

            
            
        




