class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        removed = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < prev_end: # 有重叠，
                # 删除一个，保留结束更早的区间
                removed += 1
                prev_end = min(prev_end, end)
            else:
                # 没有重叠，保留当前区间
                prev_end = end

        return removed