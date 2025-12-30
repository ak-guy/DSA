"""
suppose nums = [5,4,3,2,1]
then modified_nums = [5,4,3,2,1,5,4,3,2,1]
now if we find NGE of modified_nums and take only first 5 elements then we will get result
but we dont need to append nums again, we can mimic that by traversing from 2*n - 1 to 0 index and take
current_value as nums[i%n]
"""

from typing import List


class Solution:
    def nextGreaterElements(self, nums2: List[int]) -> List[int]:
        n = len(nums2)
        nums1 = [-1 for i in range(n)]
        st = []  # this will be our monotonically increasing stack, st[-1] < st[-2]

        for i in range(2 * len(nums2) - 1, -1, -1):
            val = nums2[i % n]
            while st and st[-1] <= val:
                st.pop()

            if st:
                res = st.pop()
                nums1[i % n] = res
                st.append(res)

            st.append(val)

        return nums1
