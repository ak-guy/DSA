import heapq, collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hq = []  # will store frequency of elements (using it as a max_heap)
        dq = collections.deque()  # will store -> count_available, what_time_it_is_available : its structure will be such that dq[0][1] < dq[1][1]

        time = 0
        dic = {}
        for i in range(len(tasks)):
            if tasks[i] not in dic:
                dic[tasks[i]] = 1
            else:
                dic[tasks[i]] += 1

        for val in dic.values():
            heapq.heappush(hq, -val)

        while hq or dq:
            time += 1
            if hq:
                value = (
                    1 + heapq.heappop(hq)
                )  # will pop from heap, but will push this value back to heap 'what_time_it_is_available' == time
                if value:  # will add in dq only if value is less than 0
                    dq.append([value, time + n])
            if dq and dq[0][1] == time:
                count_available, what_time_it_is_available = dq.popleft()
                heapq.heappush(hq, count_available)

        return time
