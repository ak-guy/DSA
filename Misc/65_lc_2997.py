from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total_xor = 0
        for num in nums:
            total_xor ^= num
            
        bit_repr_of_total_xor = bin(total_xor)[2:]
        bit_repr_of_k = bin(k)[2:]
        n = len(bit_repr_of_total_xor)
        m = len(bit_repr_of_k)

        if n > m:
            bit_repr_of_k = '0' * (n - m) + bit_repr_of_k
        elif n < m:
            bit_repr_of_total_xor = '0' * (m - n) + bit_repr_of_total_xor
            
        res = 0
        for i in range(len(bit_repr_of_total_xor)):
            if bit_repr_of_total_xor[i] != bit_repr_of_k[i]:
                res += 1

        return res