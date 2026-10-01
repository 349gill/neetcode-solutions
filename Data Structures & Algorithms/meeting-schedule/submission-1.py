"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        meetings = []

        for meeting in intervals:
            # Create a start-time to duration mapping
            #   e.g. 0: 30, 5: 5, 15: 5
            #   for (0, 30), (5, 10), (15, 20)
            meetings.append((meeting.start, meeting.end - meeting.start))
        
        # Sort by start-times
        meetings.sort(key=lambda meeting: meeting[0])

        i = 0
        while i < len(meetings) - 1:
            # Check whether next meeting starts before the previous one ends
            if meetings[i + 1][0] < meetings[i][0] + meetings[i][1]:
                return False

            i += 1

        return True