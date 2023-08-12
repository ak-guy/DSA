import math
class Solution:
    def getPossibility(self, nums, divisor, th):
        total = 0
        for i in range(len(nums)):
            if total > th:
                return False
            total += math.ceil(nums[i] / divisor)
        
        return total <= th

    def smallestDivisor(self, nums, th: int) -> int:
        l, r = 1, max(nums)
        res = r
        while l <= r:
            mid = (l+r) // 2
            cond = self.getPossibility(nums, mid, th)

            if cond:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res