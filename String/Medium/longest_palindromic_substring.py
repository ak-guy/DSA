class Solution:
    def longestPalindrome(self, S):
        temp = S[0]
        n = len(S)
        
        # assuming odd length palindromic substring
        max_len = 0
        for i in range(n):
            left = i
            right = i
            while left>=0 and right<n:
                if S[left] == S[right]:
                    if right - left + 1 > max_len:
                        max_len = right-left+1
                        temp = S[left:right+1]
                    left -= 1
                    right += 1
                else:
                    break
        
        # assuming even length palindromic substring
        temp1 = S[0]
        max_len = 0
        for i in range(1,n):
            left = i-1
            right = i
            while left>=0 and right<n:
                if S[left] == S[right]:
                    if right - left + 1 > max_len:
                        max_len = right-left+1
                        temp1 = S[left:right+1]
                    left -= 1
                    right += 1
                else:
                    break
        
        return temp if len(temp)>len(temp1) else temp1
    

# # better implementation
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        new_length = 0
        
        # expanding outwards
        
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if new_length < r - l + 1:
                    res = s[l : r + 1]
                    new_length = r - l + 1
                l -= 1
                r += 1
            
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if new_length < r - l + 1:
                    res = s[l : r + 1]
                    new_length = r - l + 1
                l -= 1
                r += 1
        
        return res
    

# expand from the middle technique
class Solution:
    def getLongestPalindrome(self, s: str, starting_index: int, is_odd: bool, string_length: int):
        ind_1 = starting_index-1
        ind_2 = starting_index+1 if is_odd else starting_index+2
        
        if not is_odd and s[starting_index] != s[starting_index+1]:
            return '', 0

        largest_palindrome_length = 1 if is_odd else 2
        while ind_1 >= 0 and ind_2 <= string_length-1:
            if s[ind_1] != s[ind_2]:
                break
            largest_palindrome_length += 2
            ind_1 -= 1
            ind_2 += 1

        return s[ind_1+1:ind_1+largest_palindrome_length+1], largest_palindrome_length

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ''
        largest_palindrome_length = 0
        for i in range(n):
            # odd length palindrome
            res, res_length = self.getLongestPalindrome(s, starting_index=i, is_odd=True, string_length=n)
            if res_length > largest_palindrome_length:
                largest_palindrome_length = res_length
                ans = res

            # skip checking even length palindromic substring if we reach (n-1)th index
            if i == n-1:
                continue

            # even length palindrome
            res, res_length = self.getLongestPalindrome(s, starting_index=i, is_odd=False, string_length=n)
            if res_length > largest_palindrome_length:
                largest_palindrome_length = res_length
                ans = res

        return ans