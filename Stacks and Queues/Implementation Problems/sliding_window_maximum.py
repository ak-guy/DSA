from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        res = []
        d = deque() # we will store ind here, also it will be monotonic dec deque

        # for first k elements
        for i in range(k):
            while d and arr[d[-1]] <= arr[i]:
                d.pop()
            d.append(i)
        res.append(arr[d[0]])
        print(d)

        # for remaining (n - k) elements
        for i in range(k, n):
            while d and arr[d[-1]] <= arr[i]:
                d.pop()
            
            while d and i - d[0] >= k:
                d.popleft()
            
            d.append(i)
            res.append(arr[d[0]])
        
        return res


# # stack implementation but it wont work 
from collections import deque
class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        res = []
        st = [] # (index, element)

        # for first k elements
        for i in range(k):
            if st and st[-1][1] > arr[i]:
                continue

            while st and st[-1][1] <= arr[i]:
                st.pop()
            
            st.append([i, arr[i]])
        res.append(st[-1][1])

        # for remaining (n - k) elements
        for i in range(k, n):
            flag = False
            if st and st[-1][1] > arr[i]:
                flag = True

            while st and st[-1][1] <= arr[i]:
                st.pop()
            
            while st and i - st[-1][0] >= k:
                st.pop()

            if not flag or not st:
                st.append([i, arr[i]])
            res.append(st[-1][1])
        
        return res