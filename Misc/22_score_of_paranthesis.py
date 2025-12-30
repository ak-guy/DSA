class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = []
        st.append(0)
        for char in s:
            if (
                char == "("
            ):  # new parent so adding zero value to the stack, later we will use this value to add to its older parent
                st.append(0)
            else:
                sub_expression_val = (
                    2 * st.pop()
                )  # getting the value of current parent (while popping it)
                val = max(
                    sub_expression_val, 1
                )  # taking max of current parent value and 1, then we will add it to older parent

                st[-1] += val  # adding it to older parent

        return st[-1]
