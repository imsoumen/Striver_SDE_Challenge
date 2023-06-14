def searchMatrix(mat: [[int]], target: int) -> bool:
    # Write your code here.
    m = len(mat)
    n = len(mat[0])

    i, j = 0, n-1

    while i < m and j >= 0:
        if target == mat[i][j]:
            return True
        elif target > mat[i][j]:
            i += 1
        else:
            j -= 1
    
    return False

