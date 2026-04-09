class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxp = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                maxp = max(prices[j] - prices[i], maxp)

        return maxp