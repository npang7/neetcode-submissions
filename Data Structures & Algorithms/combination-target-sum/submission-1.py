
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(i, total):
            # 1. 当前组合的和刚好达到目标，保存答案
            if total == target:
                result.append(path.copy())
                return
            # 2. 没有数字可以继续考虑，或者总和已经超过目标
            if i == len(nums) or total > target:
                return

            # 3. 第一种选择：再选一个当前数字
            path.append(nums[i])
            # 仍然考虑 nums[i]，因为同一个数字可以重复使用
            backtrack(i, total + nums[i])

            # 4. 第二种选择:撤销这一层加入的数字
            path.pop()
            # 不再选当前数字，考虑下一个数字
            backtrack(i + 1, total)

        backtrack(0, 0)
        return result

# Combination Sum — 思路清单
#
# 1. 理解题意：
#    - nums 中的数字互不相同，而且都是正数。
#    - 找出所有数字之和等于 target 的组合。
#    - 同一个数字可以重复使用任意多次。
#    - 不能返回重复组合。
#    - [2, 2, 5] 和 [2, 5, 2] 算同一个组合。
#
# 2. 核心思路：
#    - 使用回溯，逐个考虑候选数字。
#    - 每一步有两种选择：
#      ① 再选一个当前数字。
#      ② 不再选当前数字，转向下一个数字。
#
# 3. 创建列表：
#    - result 保存所有符合要求的组合。
#    - path 保存当前正在构造的组合。
#
# 4. 定义递归函数 backtrack(i, total)：
#    - i：当前正在考虑的候选数字下标。
#    - total：当前 path 中所有数字的和。
#    - 下标小于 i 的数字，不能再继续加入当前组合。
#    - 但前面已经加入 path 的数字仍然保留。
#
# 5. 先判断是否找到答案：
#    - 如果 total == target，当前组合符合要求。
#    - 执行 result.append(path.copy()) 保存组合。
#    - return 结束当前递归调用，返回上一层。
#    - 因为所有数字都是正数，再加入数字就会超过目标。
#
# 6. 再判断是否需要停止：
#    - 如果 i == len(nums)，没有候选数字可以继续考虑。
#    - 如果 total > target，总和已经超过目标。
#    - 这两种情况都直接 return，不保存答案。
#    - 超过目标可以剪枝，因为加入正数只会让总和更大。
#
# 7. 探索“再选一个当前数字”的分支：
#    - 执行 path.append(nums[i])。
#    - 调用 backtrack(i, total + nums[i])。
#    - i 保持不变，允许下一层继续选择同一个数字。
#    - total 增加，表示当前组合加入了一个 nums[i]。
#
# 8. 撤销选择：
#    - 执行 path.pop()，删除这一层加入的末尾元素。
#    - 将 path 恢复到加入当前数字之前的状态。
#    - 直接写 pop()，不写 pop(nums[i])。
#    - pop 的参数是下标，不是要删除的元素值。
#
# 9. 探索“不再选当前数字”的分支：
#    - 调用 backtrack(i + 1, total)。
#    - i 加一，转向下一个候选数字。
#    - total 不变，因为这个分支没有加入新的数字。
#    - 前面已经选好的数字仍然保留在 path 中。
#
# 10. 启动递归并返回：
#     - 调用 backtrack(0, 0)。
#     - 从第一个候选数字开始，初始总和为 0。
#     - 所有分支探索结束后，返回 result。
#
# 11. 为什么不会产生重复组合：
#     - 下标只能保持不变或者增加，不能往回走。
#     - 例如从 2 转向 5 之后，就不能再加入 2。
#     - 因此可以生成 [2, 2, 5]，不会再生成 [2, 5, 2]。
#     - 按数组下标的固定顺序选择，不需要额外使用集合去重。
#
# 12. 容易混淆的地方：
#     - 选当前数字：递归时使用 i，允许重复选择。
#     - 不再选当前数字：递归时使用 i + 1。
#     - Subsets 中选完用 i + 1，因为数字不能重复使用。
#     - 保存答案时使用 path.copy()，避免后续修改影响答案。
#     - total 是整数，每层递归有自己的参数值。
#     - 下一层的 total 增加，不会修改当前层的 total。
#     - 因此返回后只需要恢复 path，不需要手动减少 total。
#
# 13. 复杂度：
#     - n：候选数字数量。
#     - d = target // min(nums)：合法组合的最大可能长度。
#     - V：实际递归调用的总次数。
#     - K：找到的合法组合数量。
#     - 时间：O(V + K * d)，包括搜索和复制答案。
#     - 一个包含复制成本的宽松上界是 O((d + 1) * 2^(n + d))。
#     - 额外空间：O(n + d)，不包含答案。
#     - 原因：递归路径既可能重复选数字，也可能跳过候选数字。
#     - 答案空间：O(K * d)。


# 快速记忆思路
#
# 和刚才的 Subsets 一样：选 → 探索 → 撤销 → 不选。
# 区别是：选完还留在 i，才能重复使用当前数字。
#
# 达标：保存副本。
# 超标或用完候选数字：返回。
# 选：path.append(nums[i])，递归 (i, total + nums[i])。
# 撤销：path.pop()。
# 不再选：递归 (i + 1, total)。
#
# 口诀：选就留，不选走；达标存，超标停。


# 口语讲述思路
#
# I use backtracking to build all combinations whose sum equals the target.
# I keep a list called path for the current combination,
# and track its sum and the index of the current candidate.
#
# At each step, I explore two choices.
#
# First, I include the current number and recurse with the same index.
# Keeping the same index allows me to use that number again.
#
# After the call returns, I pop the last element to undo the choice.
# Then I explore the other branch by moving to the next index
# without adding the current number.
#
# When the sum equals the target, I save a copy of path.
# If the sum exceeds the target, or there are no candidates left,
# I stop exploring that branch.
#
# Since all numbers are positive, a sum that is too large
# can never become valid by adding more numbers.
#
# Moving only forward through the candidates prevents duplicate combinations.
#
# The search is exponential in the worst case,
# and saving each answer takes time proportional to its length.
# The extra space is O(n + d), excluding the output,
# where d is the maximum possible length of a valid combination.