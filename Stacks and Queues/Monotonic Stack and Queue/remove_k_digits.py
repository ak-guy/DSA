class Solution:
    """
    take example of '123456789' we have to remove 3 digits which one should we remove -> 789
    take example of '987654321' we have to remove 3 digits which one should we remove -> 987
    so we need to maintain a monotonic inc stack and and whenever we find a number that is
    smaller than st[-1] we will pop that number
    """

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
