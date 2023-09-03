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