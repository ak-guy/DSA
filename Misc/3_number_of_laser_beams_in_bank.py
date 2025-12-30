# # Method - 1
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev_count = 0
        for ind in range(len(bank)):
            count_1 = bank[ind].count("1")
            res += prev_count * count_1
            prev_count = prev_count if count_1 == 0 else count_1

        return res
