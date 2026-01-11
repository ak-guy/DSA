"""
3315. Construct the Minimum Bitwise Array II



"""

class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [-1 for _ in range(n)]

        for i in range(n):
            num = bin(nums[i])
            for j in range(len(num)):
                if num[j] == '1':
                    temp_num = num[:j]+'0'+num[j+1:]
                    int_num = int(temp_num,2)
                    if int_num | (int_num+1) == nums[i]:
                        result[i] = int_num
                        break

        return result
