import math

class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-248/problems/eliminate-maximum-number-of-monsters/
        Naive: Traversal
            - Can compute turns to reach city
    """
    
    
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        turns = [0] * len(dist)
        for i in range(0, len(dist)):
            turns[i] = math.ceil(dist[i] / speed[i])
                
        turns.sort()
        shots = 0
        while len(turns) > 0 and shots < turns.pop(0):
            shots += 1
            
        return shots