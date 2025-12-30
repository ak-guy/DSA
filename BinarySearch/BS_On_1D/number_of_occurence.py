"""
same logic as first and last occurence of element
"""


class Solution:
    def count(self, arr, n, target):
        left = 0
        right = n - 1
        start = -1
        while left <= right:
            mid = (left + right) // 2
            if target == arr[mid]:
                start = mid
                right = mid - 1
            elif target > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1

        # to find ending index
        left = 0
        right = n - 1
        end = -1
        while left <= right:
            mid = (left + right) // 2
            if target == arr[mid]:
                end = mid
                left = mid + 1
            elif target > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return end - start + 1 if end != -1 and start != -1 else 0
