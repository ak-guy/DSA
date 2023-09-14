# # Method - 1 (inspired by sum of subarray minimum)
from typing import List
class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        n = len(arr)
        ple = [i+1 for i in range(n)] # previous less element
        nle = [n-i for i in range(n)] # next less element
        
        st = []
        for i in range(n):
            while st and st[-1][0] >= arr[i]:
                st.pop()
            if st:
                ple[i] = i - st[-1][1]
            st.append([arr[i], i])
        
        st = []
        for i in range(n-1, -1, -1):
            while st and st[-1][0] >= arr[i]:
                st.pop()
            if st:
                nle[i] = st[-1][1] - i
            st.append([arr[i], i])
        
        res = 0
        for i in range(n):
            res = max(res, arr[i] * (ple[i] + nle[i] - 1))
        
        return res

# # Method - 2 (do this when it naturally comes to you)
