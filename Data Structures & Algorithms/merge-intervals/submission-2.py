class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)): #第一个区间已经放进 res，循环可以跳过它
            start, end = intervals[i]
            if start <= res[-1][1]:
                res[-1] = [res[-1][0],max(end,res[-1][1])]
            else:
                res.append([start,end])
        return res


# Merge Intervals（合并区间）
#
# 一、所属知识点 / 关键词
#
# - Intervals：区间问题。
# - Array / List：用二维列表存储区间。
# - Sorting：按区间起点排序。
# - Linear Scan：从左往右扫描。
# - Greedy：与最后一个已合并区间比较，重叠就立即合并。
# - 不需要 DP、堆或双重循环。
#
#
# 二、记忆思路
#
# 1. 按起点从小到大排序。
#    - 让可能重叠的区间连续出现，方便依次处理。
#
# 2. 把第一个区间放进结果列表 res。
#    - 题目保证至少有一个区间，可以直接访问 intervals[0]。
#
# 3. 遍历剩余区间，与 res 中“最后一个区间”比较。！！！
#    - res[-1] 是当前最右侧的合并结果。
#
# 4. 如果 start <= res[-1][1]，说明重叠。
#    - 左端点保持 res[-1][0]。
#    - 右端点取 max(end, res[-1][1])。
#
# 5. 否则不重叠，把新区间加入 res。
#
# 6. 返回 res。
#
# 快速记忆：
# 起点排序，看最后一段；
# 重叠取最大终点，不重叠就追加。


# 三、为什么只比较 res 的最后一个区间？
#
# - res 中的区间已经按起点排序，并且互不重叠。
# - 当前新区间的起点，不小于前面已处理区间的起点。
# - res 中更早的区间已经与最后一段分开，不可能再和当前区间重叠。
# - 所以只需要检查 res[-1]，不需要遍历整个 res。
#
#
# 四、易错点
#
# 1. 端点相等也算重叠。
#    - 本题条件是 start <= res[-1][1]。
#    - Meeting Rooms 中端点相等不算冲突，使用的是 <。
#    - 比较符号要根据具体题意决定。
#
# 2. 合并时不能直接使用当前区间的 end。
#    - 当前区间可能被已有区间完全包含。
#    - 直接赋值可能缩小范围，必须取两个终点的最大值。
#
# 3. 比较的是 res[-1]，不是原数组中的前一个区间。
#    - res[-1] 保存累计合并后的完整范围。
#    - 原数组的前一个区间不一定包含完整的合并信息。
#
# 4. 第一个区间已经加入 res，可以从下标 1 开始遍历。
#    - 遍历全部区间也正确，只是会多做一次自己与自己的合并。
#
# 5. 没有重叠时，要追加完整区间 [start, end]。
#    - res.append([start, end])。
#
# 6. sort() 会修改输入列表的顺序。
#    - 如果需要保留输入顺序，可以先使用 sorted() 创建新列表。
#
#
# 五、相关 Python 基础
#
# 1. 二维列表取值
#
# intervals[i]     ：第 i 个区间。
# intervals[i][0]  ：第 i 个区间的起点。
# intervals[i][1]  ：第 i 个区间的终点。
#
# 2. 负数下标
#
# res[-1]     ：结果列表中的最后一个区间。
# res[-1][0]  ：最后一个区间的起点。
# res[-1][1]  ：最后一个区间的终点。
#
# 3. 解包
#
# start, end = intervals[i]
#
# 等价于：
#
# start = intervals[i][0]
# end = intervals[i][1]
#
# 4. sort 与 lambda
#
# intervals.sort(key=lambda x: x[0])
#
# - sort()：原地排序，返回 None。
# - key：指定排序依据。
# - lambda x: x[0]：接收一个区间，返回它的起点。
# - 默认从小到大排序。
# - 不要写 intervals = intervals.sort(...)，否则会得到 None。
#
# 5. append 与替换
#
# res.append([start, end])
# - 在末尾增加一个新区间，res 的长度加 1。
#
# res[-1] = [res[-1][0], max(end, res[-1][1])]
# - 替换最后一个区间，res 的长度不变。
#
# 6. 列表引用
#
# res = [intervals[0]]
# - 此时 res[0] 和 intervals[0] 引用同一个内部列表。
# - 本代码合并时替换整个 res[-1]，不会修改原区间内部的端点。
# - 如果改成 res[-1][1] = ...，则可能同时修改原输入中的区间。
#
#
# 六、复杂度
#
# 时间复杂度：O(n log n)。
# - 排序 O(n log n)。
# - 扫描 O(n)。
#
# 空间复杂度：O(n)。
# - 返回结果最多包含 n 个区间。
# - 即使不计返回结果，Python 的 sort 最坏也需要 O(n) 辅助空间。
#
#
# 七、英文面试口述
#
# I'll sort the intervals by their start times.
# Then I'll scan them and compare each interval with the last merged interval.
#
# If they overlap, I'll keep the existing start
# and update the end to the larger of the two end points.
# Otherwise, I'll append the current interval as a separate interval.
#
# Since the intervals are sorted, I only need to check the last merged interval.
# The time complexity is O(n log n), and the space complexity is O(n).