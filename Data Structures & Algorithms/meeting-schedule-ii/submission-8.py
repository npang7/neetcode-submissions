"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for meeting in intervals:
            events.append((meeting.start, 1))
            events.append((meeting.end, -1))
        
        events.sort()

        current = 0
        max_rooms = 0
        for time, change in events:
            current += change
            max_rooms = max(max_rooms, current)
            
        return max_rooms

