# # similar to sum of subarray minimum

from typing import List
class Solution:
    '''
    this problem is similar to sum of subarray minimum, only difference is here we also have
    to find sum of subarray maximum that we can easily do with monotonic dec stack
    '''
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        ple = [i+1 for i in range(n)]
        nle = [n-i for i in range(n)]

        st = []
        for i in range(n):
            while st and st[-1][0] >= arr[i]: # monotonic inc stack
                st.pop()
            
            if st:
                ple[i] = i - st[-1][1]
            st.append([arr[i],i])
        
        st = []
        for i in range(n-1, -1, -1):
            while st and st[-1][0] > arr[i]: # monotonic inc stack
                st.pop()
            
            if st:
                nle[i] = st[-1][1] - i
            st.append([arr[i],i])

        res = 0
        for i in range(n):
            res += (ple[i] * nle[i] * arr[i])
            
        return res
    
    def sumSubarrayMaxs(self, arr: List[int]) -> int:
        n = len(arr)
        pge = [i+1 for i in range(n)] # distance bw current index and previous greater element
        nge = [n-i for i in range(n)] # distance bw next greater element and current index

        st = []
        for i in range(n):
            while st and st[-1][0] <= arr[i]: # monotonic dec stack
                st.pop()
            
            if st:
                pge[i] = i - st[-1][1]
            st.append([arr[i],i])
        
        st = []
        for i in range(n-1, -1, -1):
            while st and st[-1][0] < arr[i]: # monotonic dec stack
                st.pop()
            
            if st:
                nge[i] = st[-1][1] - i
            st.append([arr[i],i])
        
        res = 0
        for i in range(n):
            res += (pge[i] * nge[i] * arr[i])
            
        return res

    def subArrayRanges(self, nums: List[int]) -> int:
        return self.sumSubarrayMaxs(nums) - self.sumSubarrayMins(nums)