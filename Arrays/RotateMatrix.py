from math import *
from collections import *
from sys import *
from os import *

def rotate(mat, rowStart, colStart, rowEnd, colEnd):

    if(rowStart >= rowEnd or colStart >= colEnd):
        return

    if (rowStart >= rowEnd - 1 or colStart >= colEnd - 1):
        return

    previous = mat[rowStart + 1][colStart]
    current = previous

    for i in range(colStart, colEnd):

        current = mat[rowStart][i]
        mat[rowStart][i] = previous
        previous = current

    rowStart += 1

    for i in range(rowStart, rowEnd):

        current = mat[i][colEnd-1]
        mat[i][colEnd-1] = previous
        previous = current

    colEnd -= 1

    if (rowStart < rowEnd):
        for i in range(colEnd - 1, colStart - 1, -1):

            current = mat[rowEnd-1][i]
            mat[rowEnd-1][i] = previous
            previous = current

    rowEnd -= 1

    if (colStart < colEnd):
        for i in range(rowEnd-1, rowStart-1, -1):

            current = mat[i][colStart]
            mat[i][colStart] = previous
            previous = current

    colStart += 1

    rotate(mat, rowStart, colStart, rowEnd, colEnd)

def rotateMatrix(mat, n, m):

    # Write your code here
    rotate(mat, 0, 0, n, m)
 
