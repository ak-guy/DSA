class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n = len(nums1)
        m = len(nums2)

        if n>m:
            return self.findMedianSortedArrays(nums2, nums1)

        left_arr_length = (n + m + 1) // 2 # length of left part of array after merging two sorted arrays

        # search range (no of elements we need to pick)
        l, r = 0, n
        while l <= r:
            mid_arr1 = (l+r) // 2
            mid_arr2 = left_arr_length - mid_arr1

            l1,r1, l2,r2 = float('-inf'),float('inf'), float('-inf'),float('inf')
            