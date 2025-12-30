"""
1552. Magnetic Force Between Two Balls
"""

from typing import List


class Solution:
    def getBool(self, position: List[int], m: int, mag_force: int) -> int:
        last_pos = position[0]
        m -= 1
        for pos in position:
            if pos - last_pos >= mag_force:
                last_pos = pos
                m -= 1

        return m <= 0

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        start = 1
        end = position[-1] - position[0]
        res = 0
        while start <= end:
            possible_min_magnetic_force = (start + end) // 2
            if self.getBool(position, m, possible_min_magnetic_force):
                res = max(res, possible_min_magnetic_force)
                start = possible_min_magnetic_force + 1
            else:
                end = possible_min_magnetic_force - 1

        return res
