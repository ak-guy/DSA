'''
3488. Closest Equal Element Queries
'''

'''
Your solution for LeetCode problem 3488, "Closest Equal Element Queries," 
works by first mapping each unique value in the input array to a sorted 
list of its indices. For each query index, you identify the value at that 
position and retrieve its indices list from the map. Then, using a binary 
search, you find the closest position to the query index in that list. 
You calculate the shortest distance to the nearest equal element by checking
the difference to neighbors in the indices list, carefully handling edge 
cases when the query index is at the boundaries or singular in the list. 
Finally, you return the minimum distance found or -1 if no other equal 
element exists. This approach efficiently leverages binary search on the 
preprocessed index lists to answer each query in logarithmic time relative 
to the number of occurrences of that value.
'''

from collections import defaultdict
from typing import List


class Solution:
    def do_binary_search(self, query: int, index_list: list[int]):
        start, end = 0, len(index_list)-1
        while start <= end:
            mid = (start + end) // 2
            if index_list[mid] == query:
                return mid
            elif index_list[mid] > query:
                end = mid-1
            else:
                start = mid+1
        return start
            
    def get_shortest_distance(self, query: int, index_list: list[int], arr: list[int]) -> int:
        if len(index_list) == 1:
            return -1
        n = len(arr)
        ind = self.do_binary_search(query, index_list)

        left_closest_distance = index_list[ind] - index_list[ind-1] if ind-1>=0 else index_list[ind] + (n-index_list[-1])
        right_closest_distance = index_list[ind+1] - index_list[ind] if ind+1<len(index_list) else index_list[0]+1 + (n-query-1)
        
        return min(left_closest_distance, right_closest_distance)

    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        val_to_ind_map = defaultdict(list)
        for ind in range(len(nums)):
            val_to_ind_map[nums[ind]].append(ind)
        
        result = []
        for query in queries:
            val = nums[query]
            index_list = val_to_ind_map[val]
            distance = self.get_shortest_distance(query, index_list, nums)
            result.append(distance)
        
        return result
