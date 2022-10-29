#!/bin/python3

import math
import os
import random
import re
import sys

"""
    Problem: https://www.hackerrank.com/challenges/torque-and-development/problem?isFullScreen=true
    Comments:
        - Create connected components, 1 library for each cc, (n-1) roads for each CC
"""

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Edge Case
    if c_road >= c_lib:
        return n * c_lib
    
    adj_lst = [[] for _ in range(n+1)]
    
    for i,j in cities:
        adj_lst[i].append(j)
        adj_lst[j].append(i)
        
    # print(adj_lst)
    
    seen = [False for _ in range(n+1)]
    seen[0] = True
    
    tot = 0
    curr = 0
    for curr in range(n+1):
        if seen[curr]:
            continue
        
        # Add city to new CC
        tot += c_lib
        seen[curr] = True
        stack = [curr]
        while stack:
            nv = stack.pop()
            for i in adj_lst[nv]:
                if not seen[i]:
                    seen[i] = True
                    stack.append(i)
                    tot += c_road
        # print(curr)
        # print(tot)
                    
    return tot

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
