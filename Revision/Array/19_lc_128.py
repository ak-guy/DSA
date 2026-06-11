'''
128. Longest Consecutive Sequence

Intuition: The intuition behind this solution relies on finding the anchor points of consecutive 
number sequences and building them out in reverse to measure their lengths efficiently. By dumping 
all the numbers into a hash set, you can check for the existence of any value in instant ($O(1)$) 
time. Instead of mindlessly counting streaks from every single number in the set, the algorithm 
optimizes the process by identifying the "rightmost peak" of a sequence—a number that has no 
immediate successor (num + 1 not in unique_elem). Once it identifies one of these boundary peaks, 
it deploys a downward probe (temp_num = num - 1) to march backward, counting how many consecutive 
smaller numbers exist in that specific chain. This strategy guarantees that the inner while loop 
only triggers exactly once per consecutive sequence rather than at every single element, ensuring 
a highly efficient linear scan that catches the maximum sequence length (res) without redundant 
calculations.
'''

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        unique_elem = set(nums)
        res = 0

        for num in unique_elem:
            if num+1 not in unique_elem:
                temp_res = 1
                temp_num = num-1
                while temp_num in unique_elem:
                    temp_res += 1
                    temp_num -= 1
                
                res = max(res, temp_res)
        
        return res
