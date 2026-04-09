class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxp = 0

        for l in range(len(prices)-1):
            for i in range(l, len(prices)):
                maxp = max(prices[i] - prices[l], maxp)

        return maxp