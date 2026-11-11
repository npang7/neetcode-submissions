"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = []
        end_times = []
        intervals.sort(key=lambda interval: interval.start)

        for interval in intervals:
            if not rooms or interval.start < end_times[0]: #要新房间
                rooms.append(interval)
                heapq.heappush(end_times,interval.end)
            else: #
                heapq.heappop(end_times)
                heapq.heappush(end_times,interval.end)
        return len(rooms)
