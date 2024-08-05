'''
1850. Minimum Adjacent Swaps to Reach the Kth Smallest Number
'''

from typing import List
class Solution:
    def getNextPermutation(self, num_list: List[int]) -> str:
        n = len(num_list)
        swap_point = None
        for i in range(n-2, -1, -1):
            if num_list[i] < num_list[i+1]:
                swap_point = i
                break

        # if no next greater permutation exist then we return empty string, but in problem statement it is mentioned that there will always be a next greater permutation, so we can ignore below condition
        if swap_point is None: return ''

        for i in range(n-1, swap_point, -1):
            if num_list[i] > num_list[swap_point]:
                num_list[i], num_list[swap_point] = num_list[swap_point], num_list[i]
                break

        start_ind = swap_point+1
        end_ind = n-1
        while start_ind < end_ind:
            num_list[start_ind], num_list[end_ind] = num_list[end_ind], num_list[start_ind]
            start_ind += 1
            end_ind -= 1 
        
        return num_list

    def getMinSwaps(self, num: str, k: int) -> int:
        num = [int(char) for char in num]
        org_num = num.copy()

        while k:
            num = self.getNextPermutation(num)
            k -= 1
        
        # count mismatch values in num and res
        res = 0
        for ind_org_num in range(len(org_num)):
            ind_num = ind_org_num
            while org_num[ind_org_num] != num[ind_num]:
                ind_num += 1
            
            while ind_num > ind_org_num:
                num[ind_num-1], num[ind_num] = num[ind_num], num[ind_num-1]
                ind_num -= 1
                res += 1
        
        return res
