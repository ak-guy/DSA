"""
1833. Maximum Ice Cream Bars
"""

from typing import List


class Solution:
    def countSort(self, arr: List[int], n: int) -> List[int]:
        max_val = max(arr)
        count_arr = [0 for _ in range(max_val + 1)]
        for ind in range(n):
            count_arr[arr[ind]] += 1
        sorted_arr = []
        for ind, val in enumerate(count_arr):
            while count_arr[ind] > 0:
                sorted_arr.append(ind)
                count_arr[ind] -= 1
        return sorted_arr

    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = len(costs)
        sorted_arr = self.countSort(costs, n)
        curr_ind = 0
        res = 0
        while curr_ind < n and coins >= sorted_arr[curr_ind]:
            coins -= sorted_arr[curr_ind]
            curr_ind += 1
            res += 1
        return res
