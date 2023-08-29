class Solution:
    def convertRoman(self, n):
        mapping = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]
        res = ""
        for i in range(13):
            if n >= mapping[i][1]:
                res += (mapping[i][0] * (n // mapping[i][1]))
                n -= (mapping[i][1] * (n // mapping[i][1]))
            
        return res
                   