class Solution:
    def getBool(self, arr, num, m, k):
        n = len(arr)
        rem = k
        for i in range(n):
            if arr[i] <= num:
                rem -= 1
            else: # it breaks the adjancent rule, so we will reset 'rem'
                rem = k

            if rem == 0 and m != 0:
                rem = k
                m -= 1
        return m==0

    def minDays(self, bd, m: int, k: int) -> int:
        l, r = min(bd), max(bd)
        res = 10000000009 # needed to exceed 10**9 limit
        while l<=r:
            mid = (l+r) // 2
            cond = self.getBool(bd, mid, m, k)
            if cond: # we got mid value where we can make 'm' bouquets using 'k' adjacent flowers
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res if res != 10000000009 else -1