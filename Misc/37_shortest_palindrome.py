# # Brute Force TC -> O(N^2) gives TLE
from __future__ import annotations


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1 or n == 2 and s[0] == s[1]:
            return s

        new_s = '$'*(n-1) + s
        starting_index = (n-2) + (n//2 + 1) if n % 2 else (n-2) + (n//2)
        print(new_s, starting_index)
        res = ''
        is_already_palindrome = False
        for ind in range(starting_index, n-2, -1):
            odd_res = ''
            left_ind = ind-1
            right_ind = ind+1
            while right_ind < len(new_s):
                if new_s[left_ind] != new_s[right_ind] and new_s[left_ind] == '$':
                    odd_res += new_s[right_ind]
                elif new_s[left_ind] != new_s[right_ind] and new_s[left_ind] != '$':
                    break
                elif new_s[left_ind] == new_s[right_ind] and right_ind == 2*n-2:
                    is_already_palindrome = True
                    break
                left_ind -= 1
                right_ind += 1

            if is_already_palindrome:
                break

            even_res = ''
            if new_s[ind] == new_s[ind+1]:
                left_ind = ind-1
                right_ind = ind+2
                while right_ind < len(new_s):
                    if new_s[left_ind] != new_s[right_ind] and new_s[left_ind] == '$':
                        even_res += new_s[right_ind]
                    elif new_s[left_ind] != new_s[right_ind] and new_s[left_ind] != '$':
                        break
                    elif new_s[left_ind] == new_s[right_ind] and right_ind == 2*n-2 and left_ind < n:
                        is_already_palindrome = True
                        break
                    left_ind -= 1
                    right_ind += 1

            if is_already_palindrome:
                break
            print(
                f'for index {ind}, odd_res = {odd_res} and even_res = {even_res}')
            if odd_res == '' and even_res == '':
                continue
            elif odd_res != '' and even_res == '':
                res = odd_res if res == '' or (
                    res != '' and len(res) > len(odd_res)) else res
            elif even_res != '' and odd_res == '':
                res = even_res if res == '' or (
                    res != '' and len(res) > len(even_res)) else res
            else:
                if len(odd_res) > len(even_res):
                    res = even_res if res == '' or (
                        res != '' and len(res) > len(even_res)) else res
                else:
                    res = odd_res if res == '' or (
                        res != '' and len(res) > len(odd_res)) else res
            print(f'final res is {res}')
        return res[::-1] + s
