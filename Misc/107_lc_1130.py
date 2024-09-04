'''
1130. Minimum Cost Tree From Leaf Values
'''
from typing import List
# brute force greedy
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        '''
        it makes sense to use the largest number present in arr
        at the topmost level instead of using it at a lowermost level
        this is because if we use that val at lower level then res calculation 
        ie..., leftMax * rightMax will be higher for lower level non-leaf nodes
        '''
        n = len(arr)
        res = 0
        while (n > 1):
            minValIndex = arr.index(min(arr))
            if 0 < minValIndex < n-1: res += arr[minValIndex] * min(arr[minValIndex-1], arr[minValIndex+1])
            else: res += arr[minValIndex] * (arr[minValIndex-1] if minValIndex==n-1 else arr[minValIndex+1])
            arr.pop(minValIndex)
            n-=1
        
        return res
    

# Monotonic decreasing stack
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        '''
        it makes sense to use the largest number present in arr
        at the topmost level instead of using it at a lowermost level
        this is because if we use that val at lower level then res calculation 
        ie..., leftMax * rightMax will be higher for lower level non-leaf nodes
        '''
        n = len(arr)
        res = 0
        st = [100]
        for num in arr:
            while st and st[-1] <= num:
                popValue = st.pop()
                if st:
                    res += popValue * min(num, st[-1])
            st.append(num)
        
        while len(st) > 2:
            res += st.pop() * st[-1]
        
        return res