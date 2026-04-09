class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxp = 0

        minp = prices[0]


        for p in prices:
            profit = p - minp

            maxp = max(profit, maxp)

            minp = min(minp, p)

        return maxp