import heapq
from typing import List
class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        modified_nums = [[value, index] for index, value in enumerate(nums)]
        heapq.heapify(modified_nums)
        total_sum = sum(nums)
        visited = set()
        res = []

        for query in queries:
            if total_sum == 0:
                res.append(0)
                continue
            ind = query[0]
            val = query[1]
            if ind not in visited:
                total_sum -= nums[ind]
            visited.add(ind)

            while val and len(modified_nums) > 0:
                value, index = heapq.heappop(modified_nums)
                # print(f'for query = {query}, poping = {value} {index} from heap')
                if index not in visited:
                    total_sum -= nums[index]
                    val -= 1
                visited.add(index)
                
            # print(visited)
            res.append(total_sum)
        return res