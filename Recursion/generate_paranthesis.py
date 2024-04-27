from typing import List

# using recursion
class Solution:
    def __init__(self):
        self.res = []

    def generateParenthesis(self, n: int) -> List[str]:
        def recursion(left_count, right_count, val):
            # base condition
            if left_count == right_count == n:
                self.res.append(val)
            
            if left_count < n:
                recursion(left_count + 1, right_count, val + '(')
            
            if left_count > right_count:
                recursion(left_count, right_count + 1, val + ')')
            
        recursion(0, 0, '')

        return self.res
    

# using backtrack
class Solution:
    def __init__(self):
        self.res = []
        self.stack = []

    def generateParenthesis(self, n: int) -> List[str]:
        def recursion(left_count, right_count):
            if left_count == right_count == n:
                resultant_string = "".join(self.stack)
                self.res.append(resultant_string)
                return
            
            if left_count < n:
                self.stack.append('(')
                recursion(left_count + 1, right_count)
                self.stack.pop()
            
            if left_count > right_count:
                self.stack.append(')')
                recursion(left_count, right_count + 1)
                self.stack.pop()
            
        recursion(0, 0)

        return self.res