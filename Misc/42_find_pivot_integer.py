class Solution:
    def helper(self, mid, n):
        left_sum = mid * (1 + mid) // 2
        right_sum = (n-mid+1) * (mid + n) // 2
        if left_sum == right_sum:
            return 1
        if left_sum > right_sum:
            return 0
        if left_sum < right_sum:
            return 2

    def pivotInteger(self, n: int) -> int:
        start, end = 1, n
        while start <= end:
            mid = (start + end) // 2
            ''' 0 -> need to check in left of mid
                1 -> found res
                2 -> need to check in right of mid 
            '''
            value = self.helper(mid, n)
            # print(f"search space = {start} to {end} with mid = {mid}")
            # print(f"value = {value}")
            if value == 1:
                return mid
            elif value == 2:
                start = mid + 1
            else:
                end = mid - 1
        
        return -1
