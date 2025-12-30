from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        def backtrack(recursion_depth, subset):
            # print(f'recursion_depth = {recursion_depth}, and subset = {subset}')
            if recursion_depth == n:
                self.res.append(subset.copy())
                return

            # `all subsets that include nums[recursion_depth]
            subset.append(nums[recursion_depth])
            backtrack(recursion_depth + 1, subset)
            subset.pop()

            # all subsets that dont include nums[recursion_depth]
            while (
                recursion_depth < n - 1
                and nums[recursion_depth] == nums[recursion_depth + 1]
            ):
                recursion_depth += 1
            backtrack(recursion_depth + 1, subset)

        backtrack(0, [])
        return self.res


# obj = Solution()
# obj.subsets(nums=[1,2,2])
