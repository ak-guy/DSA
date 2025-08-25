'''
3143. Maximum Points Inside the Square
'''

'''
Your solution for the LeetCode problem "3143. Maximum Points Inside the Square" 
attempts to determine the maximum number of points that can be enclosed in a 
square based on categorizing points by characters in the string s. It iterates 
through each point, calculating a size metric as the maximum absolute coordinate 
value for that point, and uses a dictionary to map each character in s to a 
corresponding size. As it processes the points, it updates a max_range value to 
track the minimum size constraints encountered across characters. Finally, it 
counts how many character mappings have sizes less than this max_range to determine 
the number of points that can fit inside the square. The approach leverages grouping 
points by character and comparing their size constraints to identify the maximum 
feasible square that includes the relevant points.
'''

from typing import List


class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        max_range = 1_000_000_007
        char_to_len_map = {}
        for i in range(len(s)):
            size = max(abs(points[i][0]), abs(points[i][1]))

            if s[i] not in char_to_len_map:
                char_to_len_map[s[i]] = size
            elif char_to_len_map[s[i]] < size:
                max_range = min(max_range, size)
            else:
                max_range = min(max_range, char_to_len_map[s[i]])
                char_to_len_map[s[i]] = size
        
        result = 0
        for val in char_to_len_map.values():
            if val < max_range:
                result += 1
        return result
