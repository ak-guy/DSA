from typing import List
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n = len(board)
        m = len(board[0])
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        if board[click[0]][click[1]] == 'E':
            visited = set()

            def f(r, c, board):
                # base condition
                if (r, c) in visited or r<0 or c<0 or r>=n or c>=m or board[r][c] != 'E':
                    return
                
                mine_count = 0
                # eight surrounding blocks
                coordinates = [[-1,-1], [-1,0], [-1,1],
                                [0,-1], [0,1],
                                [1,-1], [1, 0], [1, 1]]

                for coordinate in coordinates:
                    row = r+coordinate[0]
                    col = c+coordinate[1]
                    if not (row<0 or row>=n or col<0 or col>=m) and board[row][col] == 'M':
                        mine_count += 1
                
                if mine_count:
                    # if we get some mines around (r,c) then no need to check surrounding blocks(hence no recursion req)
                    board[r][c] = str(mine_count)
                    visited.add((r,c))
                else:
                    board[r][c] = 'B'
                    visited.add((r,c))
                    # making recursive call on all 8 surrounding blocks
                    for coordinate in coordinates:
                        row = r+coordinate[0]
                        col = c+coordinate[1]
                        f(row, col, board)

            f(click[0], click[1], board)
            return board
