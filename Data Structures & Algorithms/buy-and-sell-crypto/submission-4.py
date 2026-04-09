class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxp = 0

        for l in range(len(prices)-1):
            for j in range(l, len(prices)):
                maxp = max(prices[j] - prices[l], maxp)
                print(maxp, prices[l], prices[j])
            
        return maxp