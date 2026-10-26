"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
#给我这道题的知识点以及sort基础知识笔记，以及这道题目所属的数据结构或者用到的关键词：比如：interval、sort、greedy、1-D dp等等
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda meeting: meeting.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True