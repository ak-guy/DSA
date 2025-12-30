"""
1079. Letter Tile Possibilities
"""


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = {}
        for char in tiles:
            counter[char] = 1 + counter.get(char, 0)

        def backtrack(counter, perm):
            nonlocal res
            if perm != "":
                res += 1
            for char in counter:
                if counter[char] > 0:
                    counter[char] -= 1
                    backtrack(counter, perm + char)
                    counter[char] += 1

        res = 0
        backtrack(counter, "")
        return res


"""
        take ex = AAB
        
                      a2b1
                [A]         [B]
               a1b1             a2
          [AA]     [AB]         [BA]
          b1         a1         a1
        [AAB]        [ABA]      [BAA]
        Nu            Nu        Nu
"""
