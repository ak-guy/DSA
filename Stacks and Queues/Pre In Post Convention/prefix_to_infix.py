class Solution:
    def preToInfix(self, pre_exp):
        st = []
        
        for char in range(len(pre_exp)-1, -1, -1):
            if pre_exp[char].isalnum():
                st.append(pre_exp[char])
            else:
                res = str('(' + st.pop() + pre_exp[char] + st.pop() + ')')
                st.append(res)
        
        final = st.pop()
        return final