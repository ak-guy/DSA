"""
1061. Lexicographically Smallest Equivalent String
"""


class Solution:
    def __init__(self):
        self.parent = {}

    def find(self, x: str):
        # base case where we have not encountered x
        if not self.parent.get(x):
            self.parent[x] = x
            return self.parent[x]

        # if x's parent is x
        if self.parent[x] == x:
            return self.parent[x]

        self.parent[x] = self.find(self.parent[x])  # path compression

        return self.parent[x]

    def union(self, x: str, y: str):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX > rootY:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        for i in range(n):
            self.union(s1[i], s2[i])

        res = ""
        for char in baseStr:
            res += self.find(char)

        return res
