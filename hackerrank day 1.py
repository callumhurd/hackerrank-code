##1) Given an array of integers, calculate the ratios of its elements that are
# positive, negative, and zero. Print the decimal value of each fraction on
# a new line with  places after the decimal.

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos=0
    neg=0
    zero=0
    for i in range(n):
        if arr[i]>0:
            pos += 1
        if arr[i]<0:
            neg += 1
        if arr[i]==0:
            zero += 1
        
    print(round(pos/n,6))
    print(round(neg/n,6))
    print(round(zero/n,6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
    
#2) print the largest sum and smallest sum of 4 of 5 numbers

def minmax(arr):
    maxvalue=max(arr)
    minvalue=min(arr)
    arr.remove(maxvalue)
    arr.remove(minvalue)
    print(arr+minvalue)
    print(arr+maxvalue)
    
arr=[1,2,3,4,5]

minmax(arr)

#3) convert digital time to military time

def timeConversion(s):
    if s[:2]=='12' and s[8]=='A':
        return '00'+s[2:-2]
    if s[:2]=='12' and s[8]=='P':
        return s[:-2]
    if s =='12:00:00PM':
        return '12:00:00'
    if s[8]=='A' :
        return s[:-2]
    if s[8]=='P' :
        endstring=s[2:]
        number= int(s[:2])
        newnumber=number+12
        rtrnval=str(newnumber)+str(endstring)
        return rtrnval[:-2]
    
print(timeConversion("12:45:54PM"))
print(timeConversion("01:12:01PM"))


#4) find the lonely integer in a list

def lonelyinteger(a):
    for i in range(len(a)):
        count=a.count(a[i])
        if count == 1 :
            return a[i]

#5) compute the difference od the diagonals of matrices

def diagonalDifference(arr):
    maindiag=[]
    offdiag=[]
    for i in range(n):
        maindiag.append(arr[i][i])
    for i in range(n):
        offdiag.append(arr[n-i-1][i])
    return abs(sum(maindiag)-sum(offdiag))