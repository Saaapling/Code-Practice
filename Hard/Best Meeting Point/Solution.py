from collections import defaultdict

class Solution:
    
    """
        Problem: https://leetcode.com/problems/best-meeting-point/
        Comments:
            - Initial Thoughts:
                - Seperate x/y axis, solve seperatly
                - Treat row/col as weighted sum
    """
    
    def minTotalDistance(self, grid: list[list[int]]) -> int:
        rw = defaultdict(lambda: 0)
        cw = defaultdict(lambda: 0)
        
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rw[i] += 1
                    cw[j] += 1
                    
        # print(rw)
        # print(cw)
                    
        # Could be improved with a sorted set of keys, but m,n small (<= 200)
        def aux(x):
            l = min(x)
            r = max(x)
            
            tot = 0
            while l < r:
                if x[l] > x[r]:
                    r -= 1
                    x[r] += x[r+1]
                    tot += x[r+1]
                else:
                    l += 1
                    x[l] += x[l-1]
                    tot += x[l-1]
            return tot
        
        return aux(rw) + aux(cw)