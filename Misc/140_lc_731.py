'''
731. My Calendar II
'''

class MyCalendarTwo:

    def __init__(self):
        self.events = []
        self.overlappingEvent = [] # will only contain overlapping part of two intervals

    def overlapExists(self, overlapping_event, start, end):
        return max(overlapping_event[0], start) < min(overlapping_event[1], end)

    def getOverlappingEvent(self, overlapping_event, start, end):
        return [max(overlapping_event[0], start), min(overlapping_event[1], end)]

    def book(self, start: int, end: int) -> bool:
        for overlapping_event in self.overlappingEvent:
            if self.overlapExists(overlapping_event, start, end):
                return False
        
        for event in self.events:
            if self.overlapExists(event, start, end):
                self.overlappingEvent.append(self.getOverlappingEvent(event, start, end))

        self.events.append([start, end])
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)