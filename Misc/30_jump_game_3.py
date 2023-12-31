from __future__ import annotations

from typing import List


class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        if arr[start] == 0:
            return True
        n = len(arr)

        st = []
        st.append([arr[start], start])
        arr[start] *= -1

        while st:
            jump_value, ind = st.pop()
            if jump_value == 0:
                return True
            left_jump = ind - jump_value
            right_jump = ind + jump_value

            if left_jump >= 0 and arr[left_jump] >= 0:
                st.append([arr[left_jump], left_jump])
                arr[left_jump] *= -1
            if right_jump < n and arr[right_jump] >= 0:
                st.append([arr[right_jump], right_jump])
                arr[right_jump] *= -1

        return False
