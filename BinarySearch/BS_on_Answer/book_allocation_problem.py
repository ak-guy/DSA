class Solution:
    def getPossibiliy(self, arr, min_pages, n, no_of_students):
        rem_pages = min_pages
        for i in range(n):
            if arr[i] <= rem_pages:
                rem_pages -= arr[i]
            else:
                rem_pages = min_pages
                rem_pages -= arr[i]
                no_of_students -= 1

        return no_of_students >= 1

    def findPages(self, arr, n, m):
        if n < m:
            return -1

        l = max(arr)
        r = sum(arr)
        res = 1000000

        while l <= r:
            mid = (
                l + r
            ) // 2  # assuming this is the max page that can be allocated to one student
            cond = self.getPossibiliy(arr, mid, n, m)

            if cond:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res
