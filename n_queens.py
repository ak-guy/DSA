n = 5
col = set()
posDiag = set()
negDiag = set()
res = []
board = [["."] * n for i in range(n)]
# print(board)

def backtrack(r, curr):
    if r == n:
        curr = ["".join(row) for row in board]
        res.append(curr.copy())
        return

    for c in range(n):
        if c in col or r+c in posDiag or r-c in negDiag:
            continue

        col.add(c)
        posDiag.add(r+c)
        negDiag.add(r-c)
        board[r][c] = 'Q'
        backtrack(r+1, curr)

        col.remove(c)
        posDiag.remove(r+c)
        negDiag.remove(r-c)
        board[r][c] = '.'
    
    return

    
backtrack(0, [])
print(res)