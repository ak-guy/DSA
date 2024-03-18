'''
Sort then apply use Greedy Approach
'''
from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = 1
        if len(points) == 1:
            return res

        points.sort()
        start = points[0][1]
        for ind in range(1, len(points)):
            # print(f'start at ind {ind} = {start}')
            if start < points[ind][0]:
                # print(f'increasing res at {ind}')
                res += 1
                start = points[ind][1]
            else:
                start = min(start, points[ind][1])

        return res