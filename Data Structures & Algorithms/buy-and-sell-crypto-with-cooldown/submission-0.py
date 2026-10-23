class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = float("-inf")
        sold = float("-inf")
        rest = 0

        for price in prices:
            new_hold = max(hold, rest - price)
            new_sold = hold + price
            new_rest = max(rest, sold)

            hold, sold, rest = new_hold, new_sold, new_rest

        # 最后手里不持有币，利润才完成结算
        return max(sold, rest)