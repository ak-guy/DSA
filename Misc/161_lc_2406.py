"""
2406. Divide Intervals Into Minimum Number of Groups

This solution calculates the minimum number of groups required by treating the problem as finding the maximum number of
overlapping intervals at any single point in time. It uses a min-heap to store and sort all interval boundaries
(start and end points) as discrete events; start points are flagged with 0 to increment a counter, while end points are
flagged with 1 to decrement it. By processing these events in chronological order, the algorithm tracks a running count of
"active" intervals, where the peak value of this counter represents the maximum overlap and thus the minimum number of
groups needed to ensure no two intervals in the same group overlap.
"""

import heapq


class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        hq = []
        for interval in intervals:
            heapq.heappush(hq, (interval[0], 0))
            heapq.heappush(hq, (interval[1], 1))

        res = 0
        curr_max = 0
        while hq:
            _, interval_flag = heapq.heappop(hq)
            if interval_flag == 0:
                curr_max += 1
            else:
                curr_max -= 1
            res = max(res, curr_max)

        return res
