from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        '''
        think of array as [-1] + arr + [-1]
        '''
        n = len(arr)
        mod = 1000000007
        ple = [i+1 for i in range(n)] # distance bw current index and previous less element
        nle = [n-i for i in range(n)] # distance bw next less element and current index

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
        
        '''
        suppose for arr [2,9,7,8,3,4,6,1], we have to count how many subarray are there with minimum element
        as 3. so previous less element is 2(with distance 4) and next less element is 1(with distance 3)
        then total number of such subarray will be 4 * 3 and total contribution to result will be (4 * 3 * 3)
        '''
        res = 0
        for i in range(n):
            res += ((ple[i] * nle[i] * arr[i]) % mod)
            
        return res % mod