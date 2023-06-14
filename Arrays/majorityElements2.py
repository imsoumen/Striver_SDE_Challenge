from math import *
from collections import *
from sys import *
from os import *

def majorityElementII(arr):
	# Write your code here.
	freq = {}
	N = len(arr)
	ans = []
	for i in range(N):
		if arr[i] in freq:
			freq[arr[i]] += 1
		else:
			freq[arr[i]] = 1
	
	
	for item in freq:
		if freq[item] > N//3:
			ans.append(item)

	return ans
