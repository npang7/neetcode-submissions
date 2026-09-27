class Solution: # 2 pointers
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP=0
        while r < len(prices):
            if prices[l] <= prices[r]:
                maxP = max(maxP, prices[r]-prices[l])
            else:
                l = r
            r +=1
        return maxP

#I use two pointers. The left pointer starts at index zero and represents the buying day. The right pointer starts at index one and represents the selling day. I move the right pointer through the array. If the selling price is higher than the buying price, I calculate the profit and update the maximum profit. Otherwise, I move the left pointer to the right pointer, because that day has a lower or equal buying price. After each iteration, I move the right pointer one step forward. Finally, I return the maximum profit.