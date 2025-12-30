"""
apply BS on range(1 to sum(arr)) get mid value then check if we can ship that amount under d days
if True then search for lesser value else check for greater
"""


class Solution:
    def getPossibility(self, w, mid, d, n):
        rem_days = mid
        d -= 1
        for i in range(n):
            if mid < w[i]:
                return False

            if w[i] <= rem_days:
                rem_days -= w[i]
            else:
                d -= 1
                rem_days = mid - w[i]

        return d >= 0

    def shipWithinDays(self, w, d: int) -> int:
        l, r = 1, sum(w)
        res = r
        n = len(w)
        while l <= r:
            mid = (l + r) // 2
            cond = self.getPossibility(w, mid, d, n)
            # print(cond, mid)
            if cond:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res
