class Solution:
    """
    point to note is that only negative can destroy positive if magnitude of negative is greater or
    equal to magnitude of positive
    """

    def asteroidCollision(self, n, arr):
        st = []
        for i in range(n):
            flag = False
            while (
                st and arr[i] < 0 and st[-1] > 0
            ):  # checking whether we have to pop or not
                if (
                    abs(arr[i]) > st[-1]
                ):  # this is the case that incoming asteroid will destroy other asteroid
                    st.pop()
                elif (
                    abs(arr[i]) == st[-1]
                ):  # this is the case that same weight asteroid collides
                    st.pop()
                    flag = True
                    break
                else:  # no need to add in stack as this -ve asteroid will be destroyed
                    flag = True
                    break
            if not flag:
                st.append(arr[i])

        return st
