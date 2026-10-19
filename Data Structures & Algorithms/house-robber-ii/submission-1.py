class Solution: # circle限定：第一间和最后一间，最多只能偷一间，也可以两间都不偷。
    def rob(self, nums: List[int]) -> int:
        # 只有一间房子时，直接拿走这间房子的钱
        if len(nums) == 1:
            return nums[0]

        # 计算一组直线排列的房子的最大金额 
        # 和上一题的主干相同！
        def rob_linear(houses):
            m = len(houses)

            # dp[i]：考虑前 i 间房子，最多能偷到的钱
            dp = [0] * (m + 1)

            dp[0] = 0
            dp[1] = houses[0]

            for i in range(2, m + 1):
                # 不偷当前这间
                skip = dp[i - 1]

                # 偷当前这间
                take = dp[i - 2] + houses[i - 1]

                dp[i] = max(skip, take)

            return dp[m]

        # 情况一：排除最后一间 ， 这是截断list操作！
        without_last = rob_linear(nums[:-1])
        #表示从开头取到最后一个元素之前，也就是去掉最后一个元素。

        # 情况二：排除第一间
        without_first = rob_linear(nums[1:])
        #表示从下标 1 一直取到末尾，也就是去掉第一个元素。


        # 返回两种情况中的最大金额
        return max(without_last, without_first)


# 中文思路清单
#
# 1. 先处理只有一间房子的情况
#    - 如果 len(nums) == 1，直接返回 nums[0]。
#    - 因为只有一间房子时，可以直接偷它。
#    - 如果直接排除首尾，两次切片都会得到空数组，漏掉唯一的房子。
#
# 2. 定义处理直线房子的辅助函数 rob_linear(houses)
#    - houses 表示这次要考虑的一段直线排列的房子。
#    - 辅助函数返回：这些房子中，不偷相邻房子时能得到的最大金额。
#    - 函数被调用时，先设置 m = len(houses)，表示这段房子的数量。
#    - 外面已经处理了只有一间房子的情况，所以传入的 houses 至少有一间。
#
# 3. 在辅助函数中创建 dp 数组，并设置初始值
#    - 创建 dp = [0] * (m + 1)。
#    - dp[i] 表示：考虑 houses 中的前 i 间房子，最多能偷到的钱。
#    - dp[0] = 0：没有房子时，金额为 0。
#    - dp[1] = houses[0]：只有第一间房子时，最大金额就是它的钱。
#    - i 表示房子数量，所以前 i 间中的最后一间下标是 i - 1。
#
# 4. 在辅助函数中，依次计算考虑前 2 间到前 m 间的最大金额
#    - 使用 for i in range(2, m + 1)。
#    - 不偷当前这间：skip = dp[i - 1]。
#    - 偷当前这间：take = dp[i - 2] + houses[i - 1]。
#    - 偷当前这间时，必须跳过紧挨着它的前一间。
#    - 比较两种选择：dp[i] = max(skip, take)。
#    - 计算完 i = m 后，循环结束，返回 dp[m]。
#    - 如果 houses 只有一间，循环不执行，直接返回 dp[1]。
#
# 5. 调用辅助函数，计算排除最后一间的情况
#    - without_last = rob_linear(nums[:-1])。
#    - nums[:-1] 表示去掉最后一个元素，保留前面的房子。
#    - 排除最后一间后，剩下的房子可以按照直线处理。
#    - without_last 保存这种情况下的最大金额。
#
# 6. 再次调用辅助函数，计算排除第一间的情况
#    - without_first = rob_linear(nums[1:])。
#    - nums[1:] 表示从下标 1 取到末尾，去掉第一间房子。
#    - without_first 保存这种情况下的最大金额。
#
# 7. 返回两种情况中的较大值
#    - 返回 max(without_last, without_first)。
#    - 因为首尾相邻，任何合法方案至少要放弃首尾中的一间。
#    - 两种情况覆盖了所有合法方案，也包含首尾都不偷的方案。
#
# 8. 容易混淆的地方
#    - 排除最后一间，不代表必须偷第一间；剩下的房子仍然自由选择。
#    - 排除第一间，也不代表必须偷最后一间。
#    - dp[i] 不要求偷当前这间，它是考虑前 i 间时的整体最大金额。
#    - dp 的下标表示房子数量，houses 的下标从 0 开始，所以使用 houses[i - 1]。
#    - 必须先排除房子，再重新计算，不能直接从原来的最大金额里减去首尾金额。
#    - 因为排除某间房子后，最优方案可能需要重新选择其他房子。
#
# 9. 时间和空间复杂度
#    - 时间复杂度 O(n)：对长度为 n - 1 的房子分别计算两次。
#    - 两次切片也需要 O(n) 时间，总时间仍然是 O(n)。
#    - 空间复杂度 O(n)：切片和辅助函数中的 dp 数组都需要额外空间。
#
# 快速记忆思路
# - 首尾相邻，至少放弃一端。
# - 排除尾，做一次 House Robber；排除头，再做一次 House Robber。
# - 每次都比较：不偷当前这间，或者偷当前这间并跳过前一间。
# - 两次结果取最大，只有一间时单独返回。
#
# 口语讲述思路
#
# The first and last houses are neighbors,
# so we can't rob both of them.
#
# I'll split the problem into two cases.
# In the first case, I exclude the last house.
# In the second case, I exclude the first house.
# Each case becomes a regular House Robber problem.
#
# I'll write a helper function for a line of houses.
# It uses a DP array, where dp[i] is the maximum amount
# we can rob from the first i houses.
#
# For each house, we can either skip it or rob it.
# If we skip it, we keep the best result from the first i minus one houses.
# If we rob it, we add its money to the best result
# from the first i minus two houses, so we avoid its neighbor.
# Then we take the larger amount.
#
# I run this helper once for each case and return the larger result.
# If there's only one house, I simply return its value.
#
# The time complexity is O(n), and the space complexity is O(n).
