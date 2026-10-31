class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minibuy = prices[0]
        maxP = 0
        for price in prices:
            P = price - minibuy
            minibuy = min(price, minibuy)
            maxP = max(P, maxP)
        return maxP