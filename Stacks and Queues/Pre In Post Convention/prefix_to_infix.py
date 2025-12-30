class Solution:
    """
    make a stack, traverse in reverse, will store res in stack so final ans will be st.pop()
    if we encounter alnum then directly append it to stack
    else if operator is encountered then st.append(str(  '(' +first+operator+second+ ')'  ))
    """

    def preToInfix(self, pre_exp):
        st = []
        for char in range(len(pre_exp) - 1, -1, -1):
            if pre_exp[char].isalnum():
                st.append(pre_exp[char])
            else:
                first = st.pop()
                second = st.pop()
                res = str("(" + first + pre_exp[char] + second + ")")
                st.append(res)

        final = st.pop()
        return final
