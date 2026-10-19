class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) #楼顶的下标index

        # dp[i]：到达位置 i 时，已经支付的最小总费用
        # 楼顶的位置是 n，所以需要下标 0 到 n
        dp = [0] * (n + 1)

        # 可以直接从位置 0 或位置 1 开始
        dp[0] = 0
        dp[1] = 0

        # 从位置 2 开始，计算到楼顶 n
        for i in range(2, n + 1):
            # 从前一个位置爬 1 级过来
            one_step = dp[i - 1] + cost[i - 1]

            # 从前两个位置爬 2 级过来
            two_steps = dp[i - 2] + cost[i - 2]

            # 选择花费较少的方式
            dp[i] = min(one_step, two_steps)
            # dp[i]：到达位置 i 时，已经支付的最小总费用

        return dp[n]

# 中文思路清单
#
# 1. 确定楼顶的位置
#    - n = len(cost)，有费用的台阶下标是 0 到 n - 1。
#    - 楼顶位于下标 n，也就是数组最后一个位置的后面。
#    - 每次可以往上爬 1 级或 2 级。
#
# 2. 创建 dp 数组
#    - dp = [0] * (n + 1)。
#    - dp[i] 表示：到达位置 i 时，已经支付的最小总费用。
#    - 这个费用还没有包含从位置 i 继续往上走的费用。
#    - 数组需要 n + 1 个位置，才能保存楼顶对应的 dp[n]。
#
# 3. 设置初始值
#    - dp[0] = 0，dp[1] = 0。
#    - 因为题目允许直接从位置 0 或位置 1 开始。
#    - 开始站在这两个位置时，还没有支付费用。
#    - 之后从起始位置往上走时，仍然需要支付对应的 cost。
#
# 4. 从位置 2 开始，依次计算到楼顶
#    - 使用 for i in range(2, n + 1)，i 会从 2 遍历到 n。
#    - 到达位置 i，最后一次移动只有两种情况。
#    - 从 i - 1 爬 1 级过来：
#      one_step = dp[i - 1] + cost[i - 1]。
#    - 从 i - 2 爬 2 级过来：
#      two_steps = dp[i - 2] + cost[i - 2]。
#    - one_step 和 two_steps 保存的是两种来源的最小总花费。
#    - 取较小值：dp[i] = min(one_step, two_steps)。
#    - 按下标从小到大计算，确保用到的前两个答案已经算好。
#
# 5. 结束循环并返回答案
#    - 计算完 i = n 后，循环结束。
#    - 此时 dp[n] 就是到达楼顶的最小总花费，直接返回它。
#    - 不返回 dp[n - 1]，因为最后一级有费用的台阶还不是楼顶。
#
# 6. 容易混淆的地方
#    - cost[i] 是从位置 i 往上走的费用。
#    - dp[i] 是到达位置 i 的最小总费用，两者含义不同。
#    - 费用在离开某一级时支付，因此加的是出发位置的 cost。
#    - 爬两级会跳过中间一级，不需要支付被跳过位置的费用。
#    - 计算 dp[n] 时只访问 cost[n - 1] 和 cost[n - 2]，不会越界。
#    - 这里求最小花费，所以比较两种来源后取 min。
#    - 上一道爬楼梯求走法数量，所以把两种来源的数量相加。
#
# 7. 时间和空间复杂度
#    - 时间复杂度 O(n)：每个位置只计算一次。
#    - 空间复杂度 O(n)：使用长度为 n + 1 的 dp 数组。
#
# 快速记忆思路
# - 从 0 或 1 开始，初始花费都是 0。
# - 到达 i，看前一格和前两格。
# - 到达前一格的花费 + 从前一格出发的费用。
# - 到达前两格的花费 + 从前两格出发的费用。
# - 两个总价取最小，一直算到楼顶 n。
#
# 口语讲述思路
#
# I'll use dynamic programming.
# Let n be the length of the cost array. The top is at index n.
#
# I define dp[i] as the minimum total cost to reach position i.
# It doesn't include the cost of leaving that position.
#
# We can start at index zero or index one,
# so I set both dp[0] and dp[1] to zero.
#
# To reach position i, we can come from i minus one or i minus two.
# For each option, I take the minimum cost to reach that earlier position
# and add the cost of leaving it.
# Then I store the smaller total in dp[i].
#
# I calculate these values from index two through index n.
# Finally, I return dp[n], which is the minimum cost to reach the top.
#
# The time complexity is O(n), and the space complexity is O(n).