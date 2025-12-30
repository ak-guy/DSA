from typing import List


class Solution:
    """
    Iteration 1:
        5 ^ y = 2
        => y = 2 ^ 5 = 7

    Iteration 2:
        2 ^ y = 0
        => y = 2

    Iteration 3:
        0 ^ y = 3
        => y = 3

    Iteration 4:
        3 ^ y = 1
        => y = 2

    pref = [5, 2, 0, 3, 1]
    res = [5, 7, 2, 3, 2]
    """

    def findArray(self, pref: List[int]) -> List[int]:
        temp = pref[0]
        for i in range(1, len(pref)):
            actual_pref_i = pref[i]
            pref[i] ^= temp
            temp = actual_pref_i

        return pref
