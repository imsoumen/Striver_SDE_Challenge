from math import *
from collections import *
from sys import *
from os import *

def missingAndRepeating(arr, n):
    # Write your code here
    countNumbers = [0] * n

    for i in range(n):
        countNumbers[arr[i] - 1] = countNumbers[arr[i] - 1] + 1

    m = -1
    r = -1

    for i in range(n):
        if(countNumbers[i] == 0):
            m = i + 1

        if(countNumbers[i] == 2):
            r = i + 1

    ans = m, r

    return ans
