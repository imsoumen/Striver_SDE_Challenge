from os import *
from sys import *
from collections import *
from math import *

def nextPermutation(permutation, n):
    # Write your code here.
    # Return a list.

    for i in range(n - 2, -1, -1):

        if permutation[i] < permutation[i + 1]:
            index = n - 1
            for j in range(i + 1, n):
                if permutation[j] < permutation[i]:
                    index = j - 1
                    break

            permutation[i], permutation[index] = permutation[index], permutation[i]

            for j in range(((n - i) // 2)):
                permutation[i + 1 + j], permutation[n - 1 - j] = permutation[n - 1 - j], permutation[i + 1 + j]

            return permutation

    permutation = [i for i in range(1, n + 1)]

    return permutation
