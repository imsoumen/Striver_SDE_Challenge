from math import *
from collections import *
from sys import *
from os import *

def LongestSubsetWithZeroSum(arr):

    # Write your Code here.
    # Return an integer denoting the answer.

    presum = OrderedDict()

    sum = 0
    maxLen = 0
    n = len(arr)

    for i in range(n):
        sum += arr[i]

        if (arr[i] == 0 and maxLen == 0):
            maxLen = 1
        if sum == 0:
            maxLen = i + 1

        if (sum in presum):
            maxLen = max(maxLen, i - presum.get(sum))

        else:
            presum[sum] = i

    return maxLen
