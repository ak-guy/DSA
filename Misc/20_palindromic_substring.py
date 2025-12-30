# Brute force (checking each substring if it is palidrome or not)
class Solution:
    def checkPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def countSubstrings(self, s: str) -> int:
        s_len = len(s)
        palindrome_substring_count = 0
        for r in range(s_len):
            for c in range(r, s_len):
                if self.checkPalindrome(s[r : c + 1]):
                    palindrome_substring_count += 1

        return palindrome_substring_count


# Optimized Approach (Expand from middle approach)
class Solution:
    def helper(self, s: str, i: int, j: int) -> int:
        """
        Parameters :
        i, int -> left index
        j, int -> right index
        """
        number_of_palindrome = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            number_of_palindrome += 1
            i -= 1
            j += 1

        return number_of_palindrome

    def countSubstrings(self, s: str) -> int:
        """
        Algo: we will iterate over all chars of s, and assume it to be center of the palidromic string
              then we expand to both sides and check if the resultant string is still a palindrom
              now here can be two case, one -> odd length palindromic substring
              and two -> even length palindromic substring
              so while calculating total number of palindromic substring we will consider both cases
        """
        res = 0
        for ind in range(len(s)):
            res += self.helper(s, ind, ind) + self.helper(s, ind, ind + 1)

        return res
