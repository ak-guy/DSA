class Solution:
    def getAtmostKUniqueCharSubstring(self, s, k):
        alpha = [
            0 for i in range(26)
        ]  # this will be the count of char occurrence in given string
        n = len(s)
        unique_chars = 0
        res = 0
        last = 0
        """Our sliding window can have atmost k unique chars if it exeeceds k then we will move left
           till the number of unique chars is <= k
        """
        for ind in range(n):
            alpha[ord(s[ind]) - 97] += 1
            if alpha[ord(s[ind]) - 97] == 1:
                unique_chars += 1

            while unique_chars > k:
                alpha[ord(s[last]) - 97] -= 1
                if alpha[ord(s[last]) - 97] == 0:
                    unique_chars -= 1
                last += 1

            res += (
                ind - last + 1
            )  # this is used to count number of substring having s[ind] in it
        return res

    def substrCount(self, s, k):
        """to get substrings with k unique chars we can find all substring with atmost k chars and
        substract it with count of all substring with k-1 chars
        """
        return self.getAtmostKUniqueCharSubstring(
            s, k
        ) - self.getAtmostKUniqueCharSubstring(s, k - 1)


"""
s = "abcd"
res = 0
for i in range(len(s)):
    res += i+1
print(res)
"""
