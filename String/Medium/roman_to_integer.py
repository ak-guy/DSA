class Solution:
    def romanToDecimal(self, S):
        res = 0
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        S = S.replace("IV", "IIII").replace("IX", "VIIII")
        S = S.replace("XL", "XXXX").replace("XC", "LXXXX")
        S = S.replace("CD", "CCCC").replace("CM", "DCCCC")

        for char in S:
            res += mapping[char]

        return res
