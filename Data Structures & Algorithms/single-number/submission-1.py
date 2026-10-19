class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return list(seen)[0]


# 2. 为什么异或可以找到只出现一次的数字？

# 主要用到三个性质：
# # 性质一：一个数字和自己异或，结果是 0
# a ^ a == 0
# # 例如：5 ^ 5 = 0

# # 性质二：一个数字和 0 异或，结果还是自己
# a ^ 0 == a
# # 例如：5 ^ 0 = 5

# # 性质三：连续异或时，可以调整顺序和分组
# a ^ b ^ a == a ^ a ^ b


# 因此，把数组中的所有数字异或起来：
# 4 ^ 1 ^ 2 ^ 1 ^ 2

# 调整顺序，把相同数字放在一起：
# = 4 ^ (1 ^ 1) ^ (2 ^ 2)
# = 4 ^ 0 ^ 0
# = 4

# 出现两次的数字都会抵消成 0，最后留下只出现一次的数字。