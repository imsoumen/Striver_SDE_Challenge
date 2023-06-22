from math import *
from collections import *
from sys import *
from os import *

def lengthOfLongestConsecutiveSequence(arr,n):

   arr.sort()
   ans, count = 0, 0
   
   for i in range(n):
        if (i > 0 and  (arr[i] == arr[i - 1] + 1)):
            count += 1
        elif (i > 0 and  arr[i] == arr[i - 1]):
                continue
        else:
            count = 1
        ans = max(ans,count)
        
   return ans
