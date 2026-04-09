class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = prices[0]

        for price in prices:
            profit = max(profit, price-left)
            left = min(left, price)
        return profit        