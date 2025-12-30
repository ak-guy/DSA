# # Brute Force
class Solution:  # TC -> O(N*queries) and SC -> O(queries)
    """
    no use of stack is required, just run normal loop
    """

    def count_NGEs(self, N, arr, queries, indices):
        ans = [0 for i in range(queries)]
        for i in range(queries):
            ind = indices[i]
            res = 0
            for j in range(ind + 1, N):
                if arr[j] > arr[ind]:
                    res += 1
            ans[i] = res

        return ans
