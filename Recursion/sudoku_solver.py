board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

def is_valid(board, r, c, i):
    for j in range(9):
        if board[r][j] == str(i): # for row condition
            return False
        if board[j][c] == str(i): # for col condition
            return False
        if board[3 * (r // 3) + (j // 3)][3 * (c // 3) + (j % 3)] == str(i): # for sub-matrix condition
            return False
    return True

def solveSudoku(board):
    # running loop for every element of matrix
    for r in range(9):
        for c in range(9):

            # only if the value at board[r][c] is not determined we will proceed
            if board[r][c] == ".":
                for i in range(1, 10):
                    # some black_box function which tells us whether we can put number i at board[r][c] position
                    if is_valid(board, r, c, i):
                        board[r][c] = str(i)

                        # if we found a solution we return true else we backtrack...or in other words we make board[r][c] = '.'
                        if solveSudoku(board) == True:
                            return True
                        else:
                            board[r][c] = '.'
                # we will return false if we tried all (1 -> 10) numbers and none of it results in satisfying all three sudoku condition
                return False

    return True

solveSudoku(board=board)

print(*board)