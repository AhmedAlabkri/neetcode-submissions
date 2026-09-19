class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = j = result = 0
        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
                j+=1
            else:
                result = max(prices[j]-prices[i], result)
                j+=1
        return result
        