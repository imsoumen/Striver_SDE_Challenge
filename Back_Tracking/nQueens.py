def isSafe(board, row, col, n):
    i = row - 1
    while i >= 0:
        if board[i][col] == 1:
            return False
        i = i - 1
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j - 1

    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j + 1

    return True

def solve(row, n, board):
    if row == n:
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
        print()
        return

    for col in range(n):
        if isSafe(board, row, col, n,):
            board[row][col] = 1
            solve(row + 1, n, board)
            board[row][col] = 0
    return

def solveNQueens(n):
    board = [[0 for i in range(n)] for j in range(n)]
    solve(0, n, board)
    return board[n:]
