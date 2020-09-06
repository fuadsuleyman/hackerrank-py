# Task Link https://www.hackerrank.com/challenges/python-sort-sort/problem

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    nm = input().split()
    # print(nm)
    n = int(nm[0])
    # print(f'n= {n}')

    m = int(nm[1])
    # print(f'm= {m}')

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    # print(arr)


    k = int(input())

    arr.sort(key = lambda x: x[k])

    for line in arr:
        print(*line)
    
