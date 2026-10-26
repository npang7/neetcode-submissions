"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True

# Meeting Rooms（会议室）
#
# 一、所属知识点 / 关键词
#
# - Intervals：区间问题。
# - Array / List：使用列表存储会议。
# - Sorting：按开始时间排序。
# - Linear Scan：排序后线性扫描，比较相邻会议。
# - 本题不需要 DP、堆或复杂的贪心选择。
#
#
# 二、题目与解题思路
#  从下标 1 开始遍历。因为要用到i-1
#    - intervals[i]：当前会议。
#    - intervals[i - 1]：前一场会议。
# 快速记忆：按开始时间排序，当前开始 < 前场结束，就冲突。


# 三、对象和列表的取值区别
# 对应排序：
# intervals.sort(key=lambda meeting: meeting[0])
#
# 对应冲突判断：
# intervals[i][0] < intervals[i - 1][1]
#
#
# 四、sort 基础
#
# 1. 默认从小到大排序，直接修改原列表。
#
# nums.sort()
#
# 2. 从大到小排序。
#
# nums.sort(reverse=True)
#
# 3. sort() 返回 None，不要把返回值赋给原列表。
#
# 正确：nums.sort()
# 错误：nums = nums.sort()
#
# 4. key 指定排序依据。
#    - 对每个元素计算一个 key，按 key 的大小排列原来的元素。
#    - 不会把元素替换成 key。
#
# words.sort(key=len)                       # 按字符串长度
# intervals.sort(key=lambda x: x.start)     # 按对象的开始时间
# intervals.sort(key=lambda x: x[0])        # 按列表的第一个元素
#
# 5. 多条件排序。
#    - 先按开始时间排序。
#    - 开始时间相同时，再按结束时间排序。
#
# intervals.sort(key=lambda x: (x.start, x.end))
#
# 6. Python 排序是稳定的。
#    - 排序依据相同的元素，保持它们原来的相对顺序。
#
#
# 五、lambda 基础
#
# lambda 参数: 返回的表达式
#
# lambda meeting: meeting.start
#
# 等价于：
#
# def get_start(meeting):
#     return meeting.start
# 因此下面两种排序等价：
# intervals.sort(key=lambda meeting: meeting.start)
# intervals.sort(key=get_start)
#
# 注意：
# - meeting 是自定义参数名，也可以写成 x。
# - lambda 不需要写 return。
# - key 接收函数，让排序过程对每个元素调用它。
#
#
# 六、sort 与 sorted 的区别
#
# nums.sort()
# - 修改原列表。
# - 返回 None。
# - 是列表的方法。
#
# result = sorted(nums)
# - 不修改原列表。
# - 返回新的已排序列表。
# - 可以接收列表、元组等可迭代对象。
#
# 两者都支持 key 和 reverse。
#
# 如果不想修改原来的会议顺序：
# ordered = sorted(intervals, key=lambda meeting: meeting.start)
#
#
# 七、复杂度与易错点
#
# 时间复杂度：O(n log n)。
# - 排序 O(n log n)，扫描 O(n)。
#
# 额外空间复杂度：O(n)。
# - Python 的列表排序最坏需要 O(n) 辅助空间。
# - 原地修改列表，不代表额外空间一定为 O(1)。
#
# 易错点：
# - 先排序，再比较相邻会议。
# - 冲突条件用 <，不能用 <=。
# - 从 i = 1 开始，才能正确比较前一场会议。
# - 按实际元素类型选择 .start / .end 或 [0] / [1]。