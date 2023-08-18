class Solution:
    def findMedianSortedArrays(self, arr1, arr2) -> float:
        n = len(arr1)
        m = len(arr2)

        if n>m:
            return self.findMedianSortedArrays(arr2, arr1)

        left_arr_length = (n + m + 1) // 2 # length of left part of array after merging two sorted arrays

        # search range (no of elements we need to pick from smaller array)
        l, r = 0, n
        while l <= r:
            mid_arr1 = (l+r) // 2 # no of elements picking from arr1
            mid_arr2 = left_arr_length - mid_arr1 # no of elements picking from arr2

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
                if (n+m) % 2 == 0: # if total combined array's length is even
                    return (float(max(l1, l2)) + float(min(r1, r2)))/2.0
                else: # if total combined array's length is odd
                    return float(max(l1, l2))
                
            elif l1 > r2: # this condition means there is bigger element present in left part of combined array
                r = mid_arr1 - 1

            else:
                l = mid_arr1 + 1