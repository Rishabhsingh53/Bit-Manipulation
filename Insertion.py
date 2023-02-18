"""
You are given two 32 bit numbers N and M and two bit position i and j. Write i method to insert M into N such that M starts with at bit j and
ends at bit i. You can assume that the bits j through i have enough sapce to fit all of M. 
N = 10000000000
M = 10011
i = 2 
j = 6
N = 10001001100
"""

""" 
Algorithm
Create a MASK with the first B - A + 1 bits set.
Shift   MASK by A bits to left.
Negate the MASK and take bitwise and with X to clear all set bits of X from B to A.
Shift Y by A bits and take its bitwise or with X. We finally return X.
"""

def solution(n,m,i, j):
    
    mask = ( (1 << (j - i + 1 )) - 1 ) << i 
    n = n & ~mask 
    m = m << i 
    return n | m
    
n , m , i , j = map(int, input().split())
print(solution(n, m, i , j))