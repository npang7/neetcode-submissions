class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        # used[i] 表示 nums[i] 是否已在当前排列中
        used = [False] * len(nums)  #不要忘记False左右的[ 、]

        def backtrack():
            # 当前排列已经包含所有数字，保存答案
            if len(path) == len(nums):
                result.append(path.copy())
                return

            # 尝试把每个尚未使用的数字放到下一个位置
            for i in range(len(nums)):
                if used[i]:
                    continue

                # 第一种：选择 nums[i]
                path.append(nums[i])
                used[i] = True
                backtrack()

                # 第二种：不选，撤销选择，恢复状态
                path.pop()
                used[i] = False


        backtrack()
        return result

# Permutations — 思路清单
#
# 1. 理解题意：
#    - nums 中的数字互不相同。
#    - 返回所有可能的排列。
#    - 每个排列必须包含全部数字，每个数字恰好使用一次。
#    - 顺序不同就是不同答案，例如 [1, 2] 和 [2, 1]。
#
# 2. 核心思路：
#    - 使用回溯，从左到右构造排列。
#    - 每一层决定：下一个位置放哪个尚未使用的数字？
#    - 尝试所有未使用的数字，就能得到所有排列。
#
# 3. 初始化变量：
#    - result 保存所有完整排列。
#    - path 保存当前正在构造的排列。
#    - used = [False] * len(nums)。
#    - used[i] 表示 nums[i] 是否已经在当前 path 中。
#    - used 只记录当前排列的使用情况，不是永久标记。
#
# 4. 定义递归函数 backtrack()：
#    - 不需要传入下标，因为每一层都要检查整个 nums。
#    - len(path) 表示已经填好了多少个位置。
#    - 每次递归调用，继续填写下一个位置。
#
# 5. 判断结束条件：
#    - 如果 len(path) == len(nums)，当前排列已经完整。
#    - 执行 result.append(path.copy())，保存排列的副本。
#    - return 结束当前调用，返回上一层。
#    - 注意写 path.copy()，带括号才会执行复制。
#
# 6. 遍历所有候选数字：
#    - 使用 for i in range(len(nums))。
#    - i 是候选数字在 nums 中的下标。
#    - i 不是当前正在填写的排列位置。
#    - 每一层都从 i = 0 开始，因为前面下标的数字也可能尚未使用。
#
# 7. 跳过已经使用的数字：
#    - 如果 used[i] 为 True，执行 continue。
#    - continue 只跳过本次循环，继续检查下一个候选数字。
#    - 这样保证同一个数字不会在当前排列中使用两次。
#
# 8. 选择当前数字：
#    - 执行 path.append(nums[i])，加入当前排列。
#    - 执行 used[i] = True，标记这个数字已经使用。
#    - 调用 backtrack()，继续填写下一个位置。
#
# 9. 理解递归过程：
#    - 遇到 backtrack() 时，本层的循环暂停。
#    - 下一层拥有自己的 for 循环和自己的 i。
#    - 下一层完成后，返回本层调用 backtrack() 的地方。
#    - 本层继续执行后面的撤销操作，不会重新从 i = 0 开始。
#    - 各层的 i 相互独立，但共享同一个 path 和 used。
#
# 10. 撤销选择：
#     - 执行 path.pop()，删除当前层加入的末尾元素。
#     - 执行 used[i] = False，让这个数字可以被其他分支使用。
#     - 两个状态都必须恢复。
#     - 恢复后，本层的 for 循环继续考虑下一个候选数字。
#     - 本层循环结束时，函数自然返回上一层。
#
# 11. 启动并返回：
#     - 调用 backtrack()，从空排列开始搜索。
#     - 所有递归调用完成后，返回 result。
#     - nums 中数字互不相同，不需要额外去重。
#
# 12. 复杂度：
#     - n：数组长度。
#     - 第一个位置有 n 种选择，第二个有 n - 1 种，依此类推。
#     - 一共有 n! 个排列。
#     - 每个排列包含 n 个数字，保存时需要复制。
#     - 时间：O(n * n!)。
#     - 额外空间：O(n)，用于 path、used 和递归栈，不包含答案。
#     - 答案空间：O(n * n!)。


# 快速记忆代码结构思路
#
# 满了存，用过跳；选择并标记，递归后恢复。
#
# result = []
# path = []
# used = [False] * len(nums)
#
# def backtrack():
#     if len(path) == len(nums):
#         result.append(path.copy())
#         return
#
#     for i in range(len(nums)):
#         if used[i]:
#             continue
#
#         path.append(nums[i])     # 选择
#         used[i] = True           # 标记使用
#
#         backtrack()              # 填下一个位置
#
#         path.pop()               # 撤销选择
#         used[i] = False          # 恢复为未使用
#
# backtrack()
# return result


# 口语讲述思路
#
# I use backtracking to build the permutations one position at a time.
# At each position, I try every number that has not been used yet.
#
# I keep a list called path for the current permutation,
# and a boolean array called used to track which numbers are in it.
#
# For each unused number, I add it to path and mark it as used.
# Then I recurse to fill the next position.
#
# When that recursive call returns, I remove the number from path
# and mark it as unused, so other branches can use it.
# The current loop then continues to the next candidate.
#
# Once path contains all the numbers, I save a copy of it.
# I need a copy because path will change during backtracking.
#
# Since the input numbers are unique, this generates each permutation once.
#
# There are n factorial permutations, and each one takes O(n) time to copy.
# The time complexity is O(n times n factorial).
# The extra space is O(n), excluding the output.
