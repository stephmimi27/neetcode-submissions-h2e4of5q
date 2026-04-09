class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxp = 0

        minBuy = prices[0]

        for price in prices:
            profit = price - minBuy

            maxp = max(profit, maxp)
            minBuy = min(price, minBuy)

        return maxp