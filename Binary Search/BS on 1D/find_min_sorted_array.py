'''
in this problem we cannot just eliminate some portion of array and then reach the res
we need to keep a variable in which we will store the result
facts:
1. at any point if we found out arr[l] <= arr[r] then res will be min(res, arr[l])
2. if above cond does not satisfy then that means array is not in sorted order
3. now since array is not in sorted order then if arr[l] <= arr[m] then it would mean smallest elem is in right half
'''
# solution 1
arr = [4,5,6,7,0,1,2]
n = len(arr)
def find_min(arr, n):
    l, r = 0, n-1
    res = 1e10
    while l <= r:
        m = (l + r) // 2
        if arr[l] <= arr[r]:
            return min(res, arr[l])
        
        res = min(res, arr[m])
        if arr[m] >= arr[l]:
            l = m+1
        else:
            r = m-1
    return res

print(find_min(arr, n))


'''
to find minimum, firstly one condition should always satisfy that arr[m] <= left_to_mid and arr[m] <= right_to_mid
if this condition does not satisfy then we can check if arr[m] <= arr[r] then move r=m-1 else move l=m+1
'''
# solution 2
from typing import List
class Solution:
    def findMin(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, n-1

        while l <= r:
            m = (l + r) // 2
            left_to_mid = arr[m-1] if m>0 else -5001
            right_to_mid = arr[m+1] if m<n-1 else 5001

            if arr[m] <= left_to_mid and arr[m] <= right_to_mid: # 10, 0, 4
                return arr[m]
            elif arr[r] >= arr[m]: # here we cannot use arr[l] >= arr[m] condition because in already sorted array this condition will never be true so we would end up moving l to m+1 take example of [4,5,6,7,0,1,2]
                r = m-1
            else:
                l = m+1
            
        return arr[l]