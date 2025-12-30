# # GFG Problem
class Solution:
    def reverseWords(self, s):
        arr = list(s.split("."))
        for i in range(len(arr)):
            curr = arr[i]
            arr[i] = curr[::-1]

        return ".".join(arr)
