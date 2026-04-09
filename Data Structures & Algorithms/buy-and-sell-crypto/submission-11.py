class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minBuy = prices[0]
        
        for p in prices:
            maxp = max(maxp, p - minBuy)

            minBuy = min(minBuy, p)

        return maxp