from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    # Write your code here.
    sp = prices[0]
    profit_max = 0
    n = len(prices)
    
    for i in range(1, n):

        if prices[i] < sp:
            sp = prices[i]

        elif prices[i]-sp > profit_max:
            profit_max = prices[i] - sp
        
    
    return profit_max
