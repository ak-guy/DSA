class Solution:
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