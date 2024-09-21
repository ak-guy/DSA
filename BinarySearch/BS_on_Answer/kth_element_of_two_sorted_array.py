class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        if n > m:
            return self.kthElement(arr2, arr1, m, n, k)
        
        # search space (we can pick 0 to all elements present in arr1 for the left part of combined array)
        l = max(0,k-m) # this is the minimum no of elements we can pick from shorter array
        r = min(k,n) # this is the maximum no of elements we can pick from shorter array
        
        while l<=r:
            mid_arr1 = (l+r) // 2
            mid_arr2 = k - mid_arr1
            
            l1,r1, l2,r2 = float('-inf'),float('inf'), float('-inf'),float('inf')
            if mid_arr1 > 0:
                l1 = arr1[mid_arr1 - 1]
            if mid_arr1 < n:
                r1 = arr1[mid_arr1]
            if mid_arr2 > 0:
                l2 = arr2[mid_arr2 - 1]
            if mid_arr2 < m:
                r2 = arr2[mid_arr2]
            
            if l1 <= r2 and l2 <= r1: # we found answer
                return max(l1, l2)
                
            elif l1 > r2: # this condition means there is bigger element present in left part of combined array
                r = mid_arr1 - 1

            else:
                l = mid_arr1 + 1