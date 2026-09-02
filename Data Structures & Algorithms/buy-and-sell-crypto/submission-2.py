class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left = 0
        for right in range(1, len(prices)):
            while prices[left] > prices[right]:
                left += 1
            profit = prices[right]-prices[left]
            maxProfit = max(maxProfit, profit)

        return maxProfit