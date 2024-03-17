'''
Algo -> we will maintain start_val and end_val which will be the new modified interval that we
        we will be pushing to the result
'''
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start_val = newInterval[0]
        end_val = newInterval[1]

        res = []

        for ind, interval in enumerate(intervals):
            if end_val < interval[0]: # meaning no need to check further we have successfully merged newInterval in intervals
                res.append([start_val, end_val])
                res += intervals[ind:]
                return res
            elif start_val > interval[1]: # newInterval does not exist in current interval
                res.append(interval)
            else: # we will modify our interval
                start_val = min(start_val, interval[0])
                end_val = max(end_val, interval[1])
        
        res.append([start_val, end_val])
        return res