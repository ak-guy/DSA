# Two pointer
class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                if l < r - 1 and s[l + 1] == s[r]:
                    l += 1
                elif r > l + 1 and s[r - 1] == s[l]:
                    r -= 1
                else:
                    l += 1
                    r -= 1
            else:
                break

        return abs(r - l + 1)
