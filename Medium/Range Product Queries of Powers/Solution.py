from collections import deque

class Solution:
    
    """
        Problem: https://leetcode.com/contest/biweekly-contest-89/problems/range-product-queries-of-powers/
    """
    
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        M = 10 ** 9 + 7
        power = deque()
        
        i = 0
        while 2 ** i < n:
            i += 1
            
        # Create powers
        while n != 0:
            if 2 ** i <= n:
                n -= 2 ** i
                power.appendleft(2 ** i)
            i -= 1
            
        result = [0 for _ in range(len(queries))]
        # Might be a fast way but this will do
        for k,(l,r) in enumerate(queries):
            tot = 1
            for i in range(l, r+1):
                tot *= power[i] 
                tot %= M
            result[k] = tot
            
        return result