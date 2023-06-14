from os import *
from sys import *
from collections import *
from math import *

def pairSum(arr, s):
    # Write your code here.
    n = len(arr)
    ans = []

    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] == s):
                pair = [-1 for i in range(2)]
                
                pair[0] = arr[i]
                pair[1] = arr[j]
                ans.append(pair)

    res = [[-1 for j in range(2)] for i in range(len(ans))]

    for i in range(len(ans)):
        a = ans[i][0]
        b = ans[i][1]

        res[i][0] = min(a, b)
        res[i][1] = max(a, b)

    res = sorted(res, key=lambda x: x[0])

    return res
