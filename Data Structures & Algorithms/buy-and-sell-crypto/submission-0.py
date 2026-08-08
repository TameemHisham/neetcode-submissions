class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for right in range(1, len(prices)):
            left = min(prices[:right]) 
            if prices[right] > left:
                profit = prices[right]-left
                if maxProfit < profit:
                    maxProfit = profit

        return maxProfit
                
            