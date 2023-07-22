class Solution:
    def compare(self, arr1, arr2):
        if len(arr1) - len(arr2) != 1: # if diff in length is exact 1 then only we will check further
            return False
        i, j = 0, 0 # i to traverse arr1 and j for arr2
        while i<len(arr1) :
            if j<len(arr2) and arr1[i] == arr2[j]:
                i+=1
                j+=1
            else:
                i+=1
        if i==len(arr1) and j==len(arr2):
            return True
        return False

    def longestStrChain(self, words) -> int:
        n = len(words)
        words = sorted(words, key=lambda x: len(x))
        dp = [1 for x in range(n)] # to store what max length can be acheived till that index
        count = 1
        for curr in range(n):
            for prev in range(0, curr):
                if self.compare(words[curr], words[prev]) and dp[curr] < 1 + dp[prev]:
                    dp[curr] = 1+dp[prev]
            
            count = max(count, dp[curr])

        return count