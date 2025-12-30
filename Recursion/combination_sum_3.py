from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(recursion_depth, possible_res, curr_sum):
            if curr_sum > n:
                return

            if curr_sum == n and len(possible_res) == k:
                self.res.append(possible_res.copy())
                return

            for ind in range(recursion_depth, 10):
                if ind > n:
                    break

                curr_sum += ind
                possible_res.append(ind)
                backtrack(ind + 1, possible_res, curr_sum)

                curr_sum -= ind
                possible_res.pop()

        backtrack(1, [], 0)
        return self.res
