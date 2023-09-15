'''
taking inspiration from largest rectangle in histogram
'''
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

    def maximalRectangle(self, M: List[List[str]]) -> int:
        n = len(M)
        m = len(M[0])
        h = [0 for i in range(m)]
        res = 0
        for r in range(n):
            for c in range(m):
                if M[r][c] == '1':
                    h[c] += 1
                else:
                    h[c] = 0
                        
            res = max(res, self.largestRectangleArea(h))
        
        return res