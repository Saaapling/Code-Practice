class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-314/problems/paths-in-matrix-whose-sum-is-divisible-by-k/
    """

    def numberOfPaths(self, grid: list[list[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        M = 10 ** 9 + 7
        dp = {}
        dp[(m-1,n-1,(k - grid[m-1][n-1]) % k)] = 1
        def aux(i, j, curr):
            if (i,j,curr) in dp:
                return dp[(i,j,curr)]
            
            tot = 0
            if i < m-1:
                tot += aux(i+1, j, (curr + grid[i][j]) % k)
            if j < n-1:
                tot += aux(i, j+1, (curr + grid[i][j]) % k)
            
            dp[(i,j,curr)] = tot % M
            # print(dp)
            return tot
        
        ans = aux(0,0,0)
        return ans % M