class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-313/problems/maximum-sum-of-an-hourglass/
        Comments:
            - The idea is that you want to perserve information going from one cell to the next
            - Brute force looks like it will pass (150^2 * 7)
    """
    
    def maxSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        
        mv = 0
        for i in range(1,n-1):
            for j in range(1,m-1):
                total = grid[i][j]
                for k in range(-1,2):
                    total += grid[i-1][j-k] + grid[i+1][j+k]
                
                # print(total)
                if total > mv:
                    mv = total
                    
        return mv