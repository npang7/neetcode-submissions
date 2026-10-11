class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        # 决定是否选择 nums[i]
        def backtrack(i):
            # 所有数字都已经考虑完，记录当前子集
            if i == len(nums):
                result.append(path.copy())
                return

            # 第一种选择：选 nums[i]
            path.append(nums[i])
            # 继续决定后面的数字
            backtrack(i + 1)

            # 第二种选择：不选 nums[i]
            # 撤销刚才的选择，恢复原来的 path
            path.pop()
            # 当前数字不加入 path，直接考虑下一个数字
            backtrack(i + 1)

        #函数开始
        # 从第一个数字开始做决定
        backtrack(0)
        return result

# Subsets — 思路清单
#
# 1. 理解题意：
#    - nums 中的数字互不相同。
#    - 返回所有可能的子集，包括空集和数组本身。
#    - 每个数字在一个子集中最多使用一次。
#    - 不能包含重复子集，答案顺序不限。
#
# 2. 核心思路：
#    - 使用回溯，依次考虑每个数字。
#    - 每个数字都有两种选择：选它，或者不选它。
#    - 探索所有选择组合，就能得到所有子集。
#
# 3. 创建列表：
#    - result 保存所有找到的子集。
#    - path 保存当前正在构造的子集。
#
# 4. 定义递归函数 backtrack(i)：
#    - i 表示接下来要考虑的数字下标。
#    - 下标小于 i 的数字，都已经决定选或不选。
#    - i 不是 path 的长度。
#
# 5. 判断结束条件：
#    - 如果 i == len(nums)，说明所有数字都考虑完了。
#    - 无论选了几个数字，此时都得到一个完整子集。
#    - 执行 result.append(path.copy()) 保存当前子集。
#    - return 结束当前调用，回到上一层继续探索。
#
# 6. 探索“选当前数字”的分支：
#    - 执行 path.append(nums[i])，加入当前数字。
#    - 调用 backtrack(i + 1)，继续考虑下一个数字。
#    - 这个调用会探索所有包含当前数字的后续情况。
#
# 7. 撤销选择：
#    - 执行 path.pop()，删除这一层加入的数字。
#    - 将 path 恢复到选择当前数字之前的状态。
#    - 递归返回不会自动撤销对列表的修改，需要手动 pop。
#
# 8. 探索“不选当前数字”的分支：
#    - 不将 nums[i] 加入 path。
#    - 再次调用 backtrack(i + 1)，继续考虑下一个数字。
#    - 两个递归调用的 i 相同，但调用时的 path 不同。
#
# 9. 启动递归：
#    - 调用 backtrack(0)，从第一个数字开始考虑。
#    - 所有分支探索结束后，返回 result。
#
# 10. 为什么使用 path.copy()：
#     - path 会不断被 append 和 pop 修改。
#     - 需要复制当前子集，使保存的答案不受后续修改影响。
#     - 直接保存 path，会让所有答案引用同一个列表。
#
# 11. 为什么不会产生重复子集：
#     - 输入数字互不相同。
#     - 每个数字按固定的下标顺序被考虑一次。
#     - 每个子集对应唯一的一套“选 / 不选”决定。
#
# 12. 复杂度：
#     - n：数组长度。
#     - 每个数字有两种选择，共有 2^n 个子集。
#     - 复制一个子集最多需要 O(n) 时间。
#     - 时间：O(n * 2^n)。
#     - 额外空间：O(n)，用于递归栈和 path，不包含答案。
#     - 答案空间：O(n * 2^n)。


# 面试口语讲述思路
#
# I use backtracking to generate all possible subsets.
# For each number, I explore two choices: include it or skip it.
#
# I keep a list called path to store the current subset.
# The recursive function takes an index, which tells me
# which number to consider next.
#
# First, I add the current number to path and recurse
# to the next index.
#
# After that call returns, I remove the number from path
# to undo the choice. Then I recurse again without including it.
#
# When the index reaches the length of nums, I have considered
# every number, so I save a copy of the current subset.
# I need a copy because path will change as I explore other branches.
#
# Since the numbers are unique, each subset corresponds
# to one unique combination of include-or-skip decisions.
#
# There are 2^n subsets, and copying each subset takes up to O(n) time.
# The time complexity is O(n * 2^n).
# The extra space is O(n), excluding the output.