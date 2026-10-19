class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if (total % 2 != 0) :
            return False
        target = total // 2
        dp = [False] * (target+1)
        dp[0] = True
        for num in nums:
            for current_sum in range(target, num-1, -1):
                remaining = current_sum - num
                if dp[remaining]:
                    dp[current_sum] = True
        return dp[target]
# 中文思路清单
#
# 1. 计算数组总和，判断是否为奇数
#    - total = sum(nums)。
#    - 如果 total 是奇数，直接返回 False。
#    - 因为两个相等的整数总和，相加一定是偶数。
#
# 2. 确定需要凑出的目标总和
#    - target = total // 2。
#    - 只要选出一些元素，使它们的总和等于 target，就可以返回 True。
#    - 因为剩余全部元素的总和也一定等于 target。
#    - 两组不要求连续，也不要求元素数量相同。
#
# 3. 创建并初始化 dp 数组
#    - dp[x] 表示：使用已经处理过的元素，能否恰好凑出总和 x。
#    - x 表示总和，不是 nums 的下标，也不是元素数量。
#    - 创建 dp = [False] * (target + 1)，记录总和 0 到 target。
#    - 设置 dp[0] = True，因为不选择任何元素，就能凑出 0。
#
# 4. 外层循环，依次处理每个元素 num
#    - 使用 for num in nums。
#    - 每个数组元素最多只能使用一次。
#    - 如果数组中有两个相同的数字，它们是两个独立的元素，可以分别使用。
#
# 5. 内层循环，从 target 倒序计算到 num
#    - 使用 range(target, num - 1, -1)。
#    - current_sum 表示当前正在判断能否凑出的总和。
#    - 循环包含 num，因为单独选择当前元素，就可以凑出 num。
#    - 小于 num 的总和，无法通过加入当前这个正整数得到。
#    - 必须倒序，让后面读取的较小总和还保留本轮更新之前的状态。
#    - 这样，较小总和的组合中不会包含本轮的 num，避免重复使用它。
#
# 6. 判断是否可以加入当前元素，凑出 current_sum
#    - remaining = current_sum - num，表示加入 num 后，还需要的总和。
#    - 如果 dp[remaining] 为 True，说明之前的元素可以凑出 remaining。
#    - 再加上当前 num，就可以凑出 current_sum。
#    - 因此设置 dp[current_sum] = True。
#    - 如果 dp[remaining] 为 False，就保持 dp[current_sum] 原来的值。
#    - 原来已经能凑出的总和，仍然可以通过不选择当前 num 来保留。
#
# 7. 循环结束，返回目标总和是否可达
#    - 每轮内层循环计算到 current_sum = num 后结束。
#    - 所有元素处理完后，返回 dp[target]。
#    - True 表示找到一组总和为 target 的元素，剩下的元素构成另一组。
#    - False 表示无法分成总和相等的两组。
#
# 8. 容易混淆的地方
#    - 本题求能否凑出目标，dp 中保存的是布尔值。
#    - 每个元素最多用一次，所以更新总和时使用倒序。
#    - 如果正序处理一个 1，可能先更新 dp[1]，再用它更新 dp[2]。
#    - 这样相当于把同一个 1 使用了两次，不符合题意。
#    - dp[0] = True 是起始状态，允许单独选择当前元素。
#    - 找到目标子集即可，不需要实际构造两组元素。
#
# 9. 时间和空间复杂度
#    - 设 n 为数组长度，target 为数组总和的一半。
#    - 时间复杂度 O(n * target)：每个元素最多检查 target 个总和。
#    - 空间复杂度 O(target)：使用长度为 target + 1 的 dp 数组。
#
# 快速记忆思路
# - 总和为奇数，直接 False；总和为偶数，目标取一半。
# - dp[x] 表示能否凑出 x，先设置 dp[0] = True。
# - 每个元素只用一次，所以从大总和往小总和更新。
# - 剩余总和能凑出，加入当前元素后，当前总和也能凑出。
# - 最后返回 dp[target]。
#
# 英文面试口语讲解
#
# I'll first calculate the sum of all the numbers.
# If the total is odd, I'll return false.
#
# Otherwise, each subset needs to have half of the total sum.
# So I only need to find one subset with that target sum.
# The remaining numbers will automatically have the same sum.
#
# I'll use a boolean DP array.
# dp[x] tells me whether I can form sum x using the numbers processed so far.
# I set dp[0] to true because choosing no elements gives a sum of zero.
#
# For each number, I check sums from the target down to that number.
# If I could form the current sum minus this number before this update,
# I can now form the current sum by adding this number.
# I also keep any sums that were already possible.
#
# Updating backwards prevents me from using the same element more than once.
# After processing all the numbers, I'll return dp[target].
#
# Let n be the array length.
# The time complexity is O(n * target),
# and the space complexity is O(target).

# 外层执行 n 次，因为每个元素都要处理一次。
# 每次内层最多执行 target 次，因为它从 target 向下遍历到 num。