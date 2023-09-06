class Solution:
    def postToPre(self, post_exp):
        st = []
        for char in post_exp:
            if char.isalnum():
                st.append(char)
            else:
                first = st.pop()
                second = st.pop()
                res = str(char + second + first)
                st.append(res)
        
        return st.pop()