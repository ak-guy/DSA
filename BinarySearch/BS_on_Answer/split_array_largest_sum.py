class Solution:
    def getPossibility(self, arr, search_summ, k, n):
        rem_search_summ = search_summ
        for i in range(n):
            if arr[i] <= rem_search_summ:
                rem_search_summ -= arr[i]
            else:
                k -= 1
                rem_search_summ = search_summ
                rem_search_summ -= arr[i]

        return k >= 1

    def splitArray(self, nums, k: int) -> int:
        l, r = max(nums), sum(nums)
        res = 10000000000
        n = len(nums)

        while l <= r:
            mid = (l + r) // 2
            cond = self.getPossibility(
                nums, mid, k, n
            )  # assuming this is the max sum we want array to have

            if cond:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res
