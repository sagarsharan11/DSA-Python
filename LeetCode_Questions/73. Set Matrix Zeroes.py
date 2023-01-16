# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

### Brute Force Approach
# def setZeroes(matrix):
#     org_idx = []
#     nRows = len(matrix)
#     nCols = len(matrix[0])
#     for i in range(nRows):
#         for j in range(nCols):
#             if matrix[i][j] == 0:
#                  org_idx.append((i,j))

#     for row, col in org_idx:
#         ## changing col values
#         for j in range(nCols):
#             matrix[row][j] = 0
#         ## changing row values
#         for i in range(nRows):
#             matrix[i][col] = 0

#     return matrix

## TIME COMPLEXITY | O(m*n) m=no of rows, n=no of cols
## SPACE COMPLEXITY | O(m+n)

## Major Challenge is getting space complexity to O(1) - Modify the matrix InPlace

## --------------------------------------------------------------------------------------------

#### Working on more optimal approach
def setZeroes(matrix):
    isCol = False
    nRows = len(matrix)
    nCols = len(matrix[0])
    for i in range(nRows):
        if matrix[i][0] == 0:
            isCol = True
        for j in range(1, nCols):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, nRows):
        for j in range(1, nCols):
            if not matrix[i][0] or not matrix[0][j]:
                matrix[i][j] = 0

    if matrix[0][0] == 0:
        for j in range(nCols):
            matrix[0][j] = 0

        # See if the first column needs to be set to zero as well        
        if isCol:
            for i in range(nRows):
                matrix[i][0] = 0

    return matrix
## TIME COMPLEXITY | O(m*n) m=no of rows, n=no of cols
## SPACE COMPLEXITY | O(1)


if __name__ == '__main__':
    matrix  = [[1,1,1],[1,0,1],[1,1,1]]
    print(setZeroes(matrix))

    matrix  = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print(setZeroes(matrix))