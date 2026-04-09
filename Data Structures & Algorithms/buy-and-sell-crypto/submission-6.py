class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxp = 0

        for p in range(len(prices)):
            for i in range(p, len(prices)):
                maxp = max(prices[i]-prices[p], maxp)

        return maxp