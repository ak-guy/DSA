# Brute Force (doing exactly as told in question)
from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        m = len(popped)
        push_st = []
        counter_pop = 0

        # TC -> O(n+m) ~ O(n)
        for val in pushed:
            push_st.append(val)
            while counter_pop < m and push_st and push_st[-1] == popped[counter_pop]:
                push_st.pop()
                counter_pop += 1

        return len(push_st) == 0
    

# Space optimized (utilizing pushed array as a stack)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        m = len(popped)
        
        push_pointer, pop_pointer = 0, 0

        for val in pushed:
            pushed[push_pointer] = val
            while push_pointer >= 0 and pushed[push_pointer] == popped[pop_pointer]:
                push_pointer -= 1
                pop_pointer += 1

            push_pointer += 1
        
        return push_pointer == 0