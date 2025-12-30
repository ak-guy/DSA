class Solution:
    def countSquares(self, mat) -> int:
        n = len(mat)
        m = len(mat[0])
        res = 0
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 1 and r > 0 and c > 0:
                    mat[r][c] += min(mat[r][c - 1], mat[r - 1][c - 1], mat[r - 1][c])
                res += mat[r][c]

        return res
