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