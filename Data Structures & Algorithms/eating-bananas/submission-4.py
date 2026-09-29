class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            k = (left + right) // 2

            hours = 0
            for pile in piles:
                #hours += (pile + k - 1) // k  #用整数运算计算向上取整
                            # k - 1 有余数时多算一小时，恰好整除时不多算 
                hours += math.ceil(pile / k) #向上取整
            if hours <= h:
                right = k #不是k-1，必须保留 k，因为它可能就是答案
            else:
                left = k + 1

        return left

# / 是普通除法，结果是浮点数（float）。
# // 是向下取整除法，结果会向负无穷方向取整。

# 任何正整数 pile 都可以写成：
# pile = h × k + r
# 其中 h 是完整吃掉 k 根的小时数，r 是剩余香蕉数，且 0 ≤ r < k。
# - 如果 r = 0：刚好吃完，需要 h 小时。
# - 如果 r > 0：剩下的香蕉还要占用一小时，需要 h + 1 小时。
# 公式 (pile + k - 1) // k 正好同时处理这两种情况。
# (pile - 1) // k + 1 算出的就是最后一根香蕉所在的小时编号。

# I use binary search to find the minimum eating speed. The search range is from 1 to the size of the largest pile, since eating faster than that would not reduce the time needed for any pile.
# For each candidate speed k, I go through the piles and calculate the total time. Each pile takes the ceiling of its size divided by k hours.
# If the total time is at most h, k works, but there may be a smaller speed that also works. So I move the right bound to k. Otherwise, k is too slow, so I move the left bound to k + 1.
# When the bounds meet, that speed is the minimum speed that works.