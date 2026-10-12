class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def backtrack(start):
            # 所有字符都已经分割完，保存当前方案
            if start == len(s):
                result.append(path.copy())
                return

            # 尝试下一段子串的不同结束位置
            for end in range(start, len(s)):
                part = s[start:end + 1] #end+1: Python 切片不包含右边界。要包含下标 end 的字符

                # 当前子串不是回文，跳过
                if part != part[::-1]:
                    continue

                # 1. 选择当前回文子串
                path.append(part)
                # 从这一段后面的字符继续分割
                backtrack(end + 1)

                # 2. 撤销这一层选择的子串
                path.pop()

        backtrack(0)
        return result
# Palindrome Partitioning — 思路清单
#
# 1. 理解题意：
#    - 将整个字符串 s 分割成若干个连续子串。
#    - 每个子串都必须是回文：正着读和反着读相同。
#    - 返回所有合法的分割方案。
#    - 不能漏掉、重复使用或重新排列原字符串中的字符。
#
# 2. 核心思路：
#    - 使用回溯，从左到右构造分割方案。
#    - 每一层决定：下一段子串在哪里结束？
#    - 如果这一段是回文，就选择它，递归分割剩余字符串。
#
# 3. 初始化变量：
#    - result 保存所有完整的分割方案。
#    - path 保存当前已经选择的回文子串。
#    - part 是当前正在检查的候选子串。
#
# 4. 定义递归函数 backtrack(start)：
#    - start 表示下一段子串的开始下标。
#    - start 前面的字符已经分割好，保存在 path 中。
#    - 当前调用负责探索剩余字符串 s[start:] 的所有合法分割。
#
# 5. 判断结束条件：
#    - 如果 start == len(s)，说明所有字符都已经分割完。
#    - 执行 result.append(path.copy())，保存当前方案。
#    - return 结束当前调用，回到上一层继续探索。
#    - 不能用 len(path) == len(s)，因为一段可能包含多个字符。
#    - 例如 ["aa", "b"] 只有两段，却已经覆盖 "aab" 的全部字符。
#
# 6. 枚举下一段的结束位置：
#    - 使用 for end in range(start, len(s))。
#    - 当前层的 start 不变，end 逐渐往后移动。
#    - 当前子串为 part = s[start:end + 1]。
#    - Python 切片不包含右边界，因此需要 end + 1。
#    - end 从 start 开始，保证每个候选子串都非空。
#
# 7. 检查当前子串是不是回文：
#    - part[::-1] 得到反转后的字符串。
#    - 如果 part != part[::-1]，执行 continue。
#    - continue 跳过当前选项，继续尝试下一个结束位置。
#    - 不能用 break：短子串不是回文，更长的子串仍可能是回文。
#    - 例如 "ab" 不是回文，但 "aba" 是回文。
#
# 8. 选择当前回文子串：
#    - 执行 path.append(part)。
#    - 表示当前方案决定把这一段切下来。
#
# 9. 递归处理剩余字符串：
#    - 调用 backtrack(end + 1)。
#    - 当前子串已经覆盖到 end，下一段必须从 end + 1 开始。
#    - 不能固定使用 start + 1，因为当前子串可能包含多个字符。
#    - 下一层会探索所有后续方案，并撤销它自己做出的选择。
#
# 10. 撤销当前层的选择：
#     - 下一层返回后，执行 path.pop()。
#     - 删除当前层加入的 part，恢复选择之前的 path。
#     - 然后当前层的 for 循环继续，尝试下一个 end。
#     - 所有递归共享同一个 path，所以换分支前必须恢复它。
#     - 例如第一段可以选 "a" 或 "aa"，这两种选择不能同时留下。
#     - pop 只修改当前 path，不会删除 result 中保存的副本。
#
# 11. 启动并返回：
#     - 调用 backtrack(0)，从字符串开头开始分割。
#     - 搜索过程中，完整方案直接加入共享的 result。
#     - 所有搜索完成后，partition 函数返回 result。
#
# 12. 复杂度：
#     - n：字符串长度。
#     - n - 1 个字符间隙，每个间隙都可以选择切或不切。
#     - 最坏情况下有 2^(n - 1) 种合法分割。
#     - 考虑子串检查和保存方案，时间为 O(n * 2^n)。
#     - 长度为 k 的子串，切片和反转检查需要 O(k) 时间。
#     - 额外空间：O(n)，用于递归栈、当前路径和临时字符串。
#     - 答案空间最多为 O(n * 2^n)。


# 快速记忆思路
#
# start 决定从哪里开始，end 决定在哪里结束。
#
# ① start 到达末尾：保存 path.copy()，返回。
# ② for end：尝试不同长度的下一段。
# ③ part = s[start:end + 1]。
# ④ 不是回文：continue。
# ⑤ 是回文：append → backtrack(end + 1) → pop。
#
# 口诀：枚举结束点，回文才选；递归后半段，返回撤销。


# 口语讲述思路
#
# I use backtracking to build each partition from left to right.
# I keep a list called path to store the palindromic substrings
# I have chosen so far.
#
# The recursive function takes a start index.
# Everything before that index has already been partitioned.
#
# From start, I try every possible ending position for the next substring.
# I check whether the substring is a palindrome
# by comparing it with its reversed version.
#
# If it is not a palindrome, I skip it.
# Otherwise, I add it to path and recurse from the next character
# after the substring.
#
# When that call returns, I pop the substring to restore the previous state.
# This lets me try a different ending position without keeping
# the previous choice in path.
#
# When start reaches the end of the string, the partition is complete.
# I save a copy of path because it will change during backtracking.
#
# The worst-case time complexity is O(n times two to the power of n),
# including palindrome checks and saving the partitions.
# The extra space is O(n), excluding the output.
