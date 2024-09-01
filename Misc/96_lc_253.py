'''

253. Meeting Rooms II (Premium)

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

Example 1:
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2


Example 2:
Input: [[7,10],[2,4]]
Output: 1


Constraints:
    1 <= intervals.length <= 10^4
    0 <= start[i] < end[i] <= 10^6

'''

arr = [(1, 3), (2, 5), (4, 6)]

def solve(arr):
    events = []
    for i in range(len(arr)):
        events.append((arr[i][0], "start"))
        events.append((arr[i][1]+1, "end"))
        
    events.sort(key=lambda e: (e[0], e[1] == "start"))
    
    roomCount = 0
    currentRoomCount = 0

    for event in events:
        if event[1] == "start":
            currentRoomCount += 1
            roomCount = max(roomCount, currentRoomCount)
        else:
            currentRoomCount -= 1
    
    return roomCount

print(solve(arr))