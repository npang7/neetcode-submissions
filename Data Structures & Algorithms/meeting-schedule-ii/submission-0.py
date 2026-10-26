"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda meeting: meeting.start)
        #最小堆保证： rooms[0]是最小值
        rooms = [] #最小堆：一间已分配房间里，最后一场会议的结束时间

        for meeting in intervals:
            # 最早空出的房间可以复用，端点相等也可以
            if rooms and rooms[0] <= meeting.start:
                heapq.heappop(rooms)

            # 安排当前会议，更新这个房间的结束时间
            heapq.heappush(rooms, meeting.end)

        return len(rooms)