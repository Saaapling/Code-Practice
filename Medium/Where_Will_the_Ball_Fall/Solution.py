class Solution:
    
    """
        Problem: https://leetcode.com/problems/where-will-the-ball-fall/
        Comments: 
            Initial Thoughts: DP
                - O(m * n)
    """
    
    def findBall(self, grid: list[list[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        
        # Edge case
        if n == 1:
            return [-1]
        
        dp = [[-2 for _ in range(n)] for _ in range(m)]
        
        # First element in last row
        if grid[m-1][0] == 1 and grid[m-1][0] == 1:
            dp[m-1][0] = 1
        else:
            dp[m-1][0] = -1
        
        # Elements in the middle
        for j in range(1, n-1):
            curr = grid[m-1][j]
            if grid[m-1][j] == grid[m-1][j+curr]:
                dp[m-1][j] = j + curr
            else:
                dp[m-1][j] = -1
                
        # Last element in last row
        if grid[m-1][-1] == -1 and grid[m-1][-2] == -1:
            dp[m-1][-1] = n-2
        else:
            dp[m-1][-1] = -1
            
        # print(dp)
        
        def aux(i, j):
            if j < 0 or j >= n:
                return -1
            
            if dp[i][j] != -2:
                return dp[i][j]
            
            val = 0
            if grid[i][j] == 1:
                if j == n-1 or grid[i][j+1] == -1:
                    val = -1
                else:
                    val = aux(i+1, j+1)
            else:
                if j == 0 or grid[i][j-1] == 1:
                    val = -1
                else:
                    val = aux(i+1, j-1)
                    
            dp[i][j] = val
            return val
        
        result = [0 for _ in range(n)]
        for j in range(n):
            result[j] = aux(0, j)
            
        # print(dp)
        return result