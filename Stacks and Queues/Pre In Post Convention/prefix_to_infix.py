class Solution:
    def preToInfix(self, pre_exp):
        st = []
        
        for char in range(len(pre_exp)-1, -1, -1):
            if pre_exp[char].isalnum():
                st.append(pre_exp[char])
            else:
                first = st.pop()
                second = st.pop()
                res = str('(' + first + pre_exp[char] + second + ')')
                st.append(res)
        
        final = st.pop()
        return final