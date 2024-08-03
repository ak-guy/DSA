'''
1310. XOR Queries of a Subarray
'''

from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre_comp_xor = [arr[0]]
        for i in range(1,len(arr)):
            pre_comp_xor.append(pre_comp_xor[i-1] ^ arr[i])
        
        res = []
        for query in queries:
            prev = 0 if query[0] == 0 else pre_comp_xor[query[0]-1]
            res.append(prev ^ pre_comp_xor[query[1]])

        return res
