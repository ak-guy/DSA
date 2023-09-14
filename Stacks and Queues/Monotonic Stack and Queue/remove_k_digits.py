class Solution:
    def removeKdigits(self, S, K):
        st = []
        for i in range(len(S)):
            while st and int(st[-1]) > int(S[i]) and K > 0:
                st.pop()
                K -= 1
            st.append(S[i])
            
        while K:
            st.pop()
            K -= 1
            
        return int("".join(st))