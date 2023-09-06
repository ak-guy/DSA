class Solution:
    def postToInfix(self, postfix):
        st = []
        for char in postfix:
            if char.isalnum():
                st.append(char)
            else:
                first = st.pop()
                second = st.pop()
                res = str('(' + second + char + first + ')')
                st.append(res)
        
        return st.pop()