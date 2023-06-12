from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit

class Solution:
    def __init__ (self, start, end):
        self.start = start
        self.end = end

def mergeIntervals(intervals):
    # Write your code here.
    N = len(intervals)
    ans = []
    for i in range(N):
        start = intervals[i].start
        end = intervals[i].end

        if (len(ans) == 0 or start > ans[len(ans) - 1].end):
            ans.append(intervals[i])

        else:
            ans[len(ans)-1].end = max(ans[len(ans)-1].end, end)
    return ans
    

n = int(input())
arr1 = list(map(int, stdin.readline().strip().split(" ")))
arr2 = list(map(int, stdin.readline().strip().split(" ")))
arr1.sort()
arr2.sort()
intervals = []
for i in range(n):
    a = Solution(arr1[i], arr2[i])
    intervals.append(a)

res = mergeIntervals(intervals)

for i in range(len(res)):
    print(res[i].start, res[i].end)
