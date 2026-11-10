"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_time = sorted(i.start for i in intervals)
        end_time = sorted(i.end for i in intervals)
        max_rooms = 0
        s = 0
        e = 0
        rooms = 0
        while s < len(start_time) and e < len(end_time):
            if (start_time[s] < end_time[e]):
                rooms += 1
                s += 1
            else:
                rooms -= 1
                e += 1
            if (rooms < 0):
                rooms = 0
            if (rooms > max_rooms):
                max_rooms = rooms
        
        return max_rooms
