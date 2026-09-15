class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i = 0
        j = 0
        results = 0

        while j < len(prices):

            if prices[j] < prices[i]:
                i = j
                j +=1
            else:
                results = max(results, prices[j] - prices[i])
                j+=1
        return results
        