#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
import heapq

"""
    Problem: 
    Comments:
        - Idea 1: Djikstra's on each node (query) + caching
            - O(V * Djikstras) -> O(V * (E + VlogV)) -> O(VE + V^2log(V))
                - Worse case E = V^2, O(V^3)
            - Minor improvements by caching partial results (Build multiple djikstra's simultaneous)
        - Idea 2: Build minimum path as graph is constructed
            - O(V^2 * E) potentially
            - Adding an edge can change up to 'V' shortest paths
                - By using a 'Djikstra-like' algorithm, should not product errors
                - Ex: 2->[1,4], 1->[4], new edge 3->2
                - Update path from 2->3
                    - Update all nodes that can get to 2 with node 2's minimum edges
                    - Up to V nodes will have V paths changed
            - With worse case, its worse than Djikstras
"""

# Djikstra's algorithm
def get_distance(x, y, adj_list, weight_list, cache):
    if x == y:
        return 0
    
    if x in cache:
        if y in cache[x]:
            return cache[x][y]
        else:
            return -1
    
    mp = {}
    vheap = [(0, x)]
    seen = [False for _ in range(len(adj_list) + 1)]
    while vheap:
        plen, cnode = heapq.heappop(vheap)
        if seen[cnode]:
            continue
        seen[cnode] = True
        mp[cnode] = plen
        
        for ngbr in adj_list[cnode]:
            if seen[ngbr]:
                continue
            
            cp_weight = plen + weight_list[cnode][ngbr]
            heapq.heappush(vheap, (cp_weight, ngbr))

    cache[x] = mp
    if y in cache[x]:
        return cache[x][y]
    else:
        return -1

if __name__ == '__main__':
    nodes, edges = map(int, input().rstrip().split())
        
    adj_list = [set() for _ in range(nodes + 1)]
    weight_list = [[0 for _ in range(nodes + 1)] for _ in range(nodes + 1)]
    for i in range(edges):
        f, t, w = map(int, input().rstrip().split())
        if t not in adj_list[f]:
            adj_list[f].add(t)
        weight_list[f][t] = w

    q = int(input().strip())

    cache = {}
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        x = int(first_multiple_input[0])
        y = int(first_multiple_input[1])
        
        print(get_distance(x,y, adj_list, weight_list, cache))