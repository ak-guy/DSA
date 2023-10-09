class Solution:
    '''
    make a stack, traverse in **forward**, will store res in stack, if alnum append in stack,
    else if operator is encountered then st.append(str(operator+second+first))
    atlast return st.pop()
    '''
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