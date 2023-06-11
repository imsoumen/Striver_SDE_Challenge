from os import *
from sys import *
from collections import *
from math import *
from itertools import permutations

def permutations(lst, i, j, ans):
    if (i >= j):
        permStr = ""

        for k in range(len(lst)):
            permStr += (lst[k])  

        ans.append(permStr)
        return

    for k in range(i,j+1):
        lst[i], lst[k] = lst[k], lst[i]
        permutations(lst, i + 1, j, ans)
        lst[i], lst[k] = lst[k], lst[i]
    

def findPermutations(s):
    ans = []
    lst = list(s)
    permutations(lst, 0, len(lst) - 1, ans)
    return ans