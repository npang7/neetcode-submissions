class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        miniBuy = prices[0]
        maxP=0
        for sell in prices:
            if sell >= miniBuy:
                maxP = max(sell-miniBuy,maxP)
            else:
                miniBuy=sell
        return maxP
