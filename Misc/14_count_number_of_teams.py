"""
think of algo in this way
if we run a loop over all elements, then for every element how can we decide the
number of teams it can form if we keep that element in middle (x, rating[i], y)
"""

from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        teams_asc = teams_desc = 0
        for i, v in enumerate(rating):
            left_lower_count = 0
            left_greater_count = 0
            right_lower_count = 0
            right_greater_count = 0

            for j in rating[:i]:
                if v > j:
                    left_lower_count += 1
                else:
                    left_greater_count += 1

            for k in rating[i + 1 :]:
                if v > k:
                    right_lower_count += 1
                else:
                    right_greater_count += 1

            # keeping rating[i] in the middle of three elements [x, rating[i], y] how many teams exists =>
            teams_asc += left_lower_count * right_greater_count
            teams_desc += left_greater_count * right_lower_count

        return teams_asc + teams_desc
