class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 当前维护的连续子数组的和
        current_sum = 0

        # 遍历过程中发现的最大子数组和
        max_sum = nums[0]

        for num in nums:
            # 前面的累积和为负，会拖累当前数字，因此舍弃
            if current_sum < 0:
                current_sum = 0

            # 加入当前数字
            current_sum += num

            # 更新全局最大值
            max_sum = max(max_sum, current_sum)

        return max_sum        



# Subarray（子数组）与 Subsequence（子序列）的区别：
#
# 1. Subarray：必须连续，并且保持原来的顺序。
#    - 从原数组中取出连续的一段。
#    - 不能跳过中间的元素。
#
# 2. Subsequence：可以不连续，但必须保持原来的相对顺序。
#    - 可以删除一些元素，也可以不删除任何元素。
#    - 不能改变剩余元素的顺序。
#
# 两者都按原数组中的位置选择元素，不能重复使用同一个位置。

# 是否允许为空，需要看具体题目的要求。
# 快速记忆：
#    Subarray：连续，顺序不变。
#    Subsequence：可以跳，顺序不变。
#    每个子数组都是子序列，但子序列不一定是子数组。