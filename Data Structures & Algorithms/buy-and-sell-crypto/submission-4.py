class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        miniBuy = prices[0]
        maxP = 0
        for sell in prices:
            maxP = max(sell-miniBuy, maxP)
            if sell <= miniBuy:
                miniBuy = sell
        return maxP
