# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

# Input: n = 1
# Output: [["Q"]]


def isSafe(row, col, board):

    ## horizontal
    for j in range(len(board)):
        if (board[row][j] == 'Q'):
            return False
    
    ## vertical
    for i in range(len(board)):
        if (board[i][col] == 'Q'):
            return False
    
    # ## left diagonal
    # for i in range(len(board)):
    #     if (i == col) & (board[i][col]=='Q'):
    #         return False

    # upper left
    r = row
    c = col
    while (c>=0) & (r>=0):
        if board[r][c] == 'Q':
            return False
        r-=1
        c-=1
        
    
    ## upper right diagonal
    r = row
    c = col
    while (c<len(board)) & (r>=0):
        if board[r][c] == 'Q':
            return False
        r-=1
        c+=1

    ## lower left diagonal
    r = row
    c = col
    while (c>=0) & (r<len(board)):
        if board[r][c] == 'Q':
            return False
        r+=1
        c-=1

    ## lower right diagonal
    r = row
    c = col
    while (c<len(board)) & (r<len(board)):
        if board[r][c] == 'Q':
            return False
        r+=1
        c+=1
    
    return True
    

def saveBoard(board, allBoard):
    row = ""
    newBoard = []

    for i in range(len(board)):
        row = ""
        for j in range(len(board)):
            if board[i][j] == 'Q':
                row += 'Q'
            else:
                row += '.'
        newBoard.append(row)
    allBoard.append(newBoard)


def helper(board, allBoard, col):
    if col == n:
        saveBoard(board, allBoard)
        return

    for row in range(len(board)):
        if isSafe(row, col, board):
            board[row][col] = 'Q'
            helper(board, allBoard, col+1)
            board[row][col] = '.'


def solveNQueens(n):
    allBoard = [] #['.'*n]*n
    # board =  ['.'*n]*n #[['']*n]*n

    # allBoard = [["."] * n for _ in range(n)]
    board = [["."] * n for _ in range(n)]

    helper(board, allBoard, col=0)
    return allBoard

if __name__ == "__main__":
    n = 5
    print(solveNQueens(n))