class Solution:
    '''
    make a stack, traverse in reverse, will store res in stack, if alnum append in stack,
    else if operator is encountered then st.append(str(first+second+operator))
    atlast return st.pop()
    '''
    def preToPost(self, pre_exp):
        st = []
        n = len(pre_exp)
        for i in range(n-1, -1, -1):
            if pre_exp[i].isalnum():
                st.append(pre_exp[i])
            else:
                res = str(st.pop() + st.pop() + pre_exp[i])
                st.append(res)
        
        return st.pop()