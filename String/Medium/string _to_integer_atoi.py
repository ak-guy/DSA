class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(" ")
        res = ""

        if not s:
            return 0
        
        negative_flag = False
        if s[0] == '-':
            negative_flag = True
        
        start = 0
        if s[0] == '-' or s[0] == '+':
            start = 1

        for ind in range(start, len(s)):
            if s[ind].isdigit():
                res += s[ind]
            else:
                break
                
        if res:
            if negative_flag and -1 * int(res) <  -2147483648:
                return -2147483648
            elif negative_flag and -1 * int(res) >= -2147483648:
                return -1 * int(res)
            elif int(res) > 2147483647:
                return 2147483647
            else:
                return int(res)
        else:
            return 0