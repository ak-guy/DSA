"""
986. Interval List Intersections
"""

from typing import List


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        starting_index_fl1 = 0
        starting_index_fl2 = 0
        n1 = len(firstList)
        n2 = len(secondList)
        res = []

        while starting_index_fl1 < n1 and starting_index_fl2 < n2:
            firstList_start, firstList_end = firstList[starting_index_fl1]
            secondList_start, secondList_end = secondList[starting_index_fl2]

            possible_x = max(firstList_start, secondList_start)
            possible_y = min(firstList_end, secondList_end)

            # case of intersection
            if possible_x <= possible_y:
                res.append([possible_x, possible_y])

            # no need to handle case of no intersection bcz in that we just need to move pointer that is handled down

            if firstList_end > secondList_end:
                starting_index_fl2 += 1
            else:
                starting_index_fl1 += 1

        return res
