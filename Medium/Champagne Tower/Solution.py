class Solution:
    
    """
        Problem: https://leetcode.com/problems/champagne-tower/
    """
    
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        curr = [poured]
        
        n = 1
        for i in range(query_row):
            nr = [0 for _ in range(n+1)]
            for j in range(n):
                x = max(0, (curr[j]-1)/2)
                if x > 0:
                    nr[j] += x
                    nr[j+1] += x
                    
            curr = nr
            n += 1
            
        return min(1, curr[query_glass])