class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n #我们自己加的
        for i in range(n):
            xorr ^= i ^ nums[i]
        return xorr

# 因为后面的循环：
# for i in range(n):
# 只会提供下标：
# 0, 1, 2, ..., n - 1
# 但是完整范围应该是：
# 0, 1, 2, ..., n
# 循环下标里没有 n，所以提前把 n 放进 xorr。
# 这样，n 加上循环中的所有 i，就覆盖了所有应该出现的数字。