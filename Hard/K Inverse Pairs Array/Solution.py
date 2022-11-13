class Solution:
    
    """
        Problem: https://leetcode.com/problems/k-inverse-pairs-array/
        Comments:
            - DP solution
                - Two possible states: n, k | up to O(n*k) -> O(n^2)
                - Base Case:
                    - dp[i][0] = 1
                    - dp[i][1] = i-1
                    - dp[i][j] = 0 when i <= j
                - dp[i][j] = dp[i-1][j] + dp[i-1][j-1] + dp[i-1][j-2] + ...  
                    - For new element K = i:
                        - Appending K to end keeps inverse pairs the same
                        - Adding K to the 2nd to last element creates 1 new inversions
                        - Adding K to the 3rd to last element creates 2 new inversions
                    - Optimization: Prefix sum
    """
    
    def non_ps_soln(self, n, k):
        M = 10 ** 9 + 7
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        
        # Base Case
        for i in range(1,n+1):
            dp[i][0] = 1
            ps[i][0] = i
        
        for i in range(2,n+1):
            for j in range(1, k+1):
                tot = 0
                for x in range(max(0, j-i+1), j+1):
                    tot += dp[i-1][x]
                    
                dp[i][j] = tot % M

        return dp[n][k]
    
    def dp_soln_with_extra_vars(self, n, k):
        M = 10 ** 9 + 7
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        ps = [[0 for _ in range(k+1)] for _ in range(n+1)]
        
        # Base Case
        for i in range(1,n+1):
            dp[i][0] = 1
            ps[i][0] = 1

        for i in range(1,n+1):
            for j in range(1, k+1):
                tot = ps[i-1][j]
                if j-i >= 0:
                    tot -= ps[i-1][j-i]
                    
                dp[i][j] = tot % M
                ps[i][j] = (ps[i][j-1] + dp[i][j]) % M

        # print(dp)
        
        return dp[n][k]
    
    def kInversePairs(self, n: int, k: int) -> int:
        # Edge Case:
        if k == 0:
            return 1
        
        M = 10 ** 9 + 7
        ps = [[0 for _ in range(k+1)] for _ in range(n+1)]
        
        # Base Case
        for i in range(1,n+1):
            ps[i][0] = 1

        for i in range(1,n+1):
            for j in range(1, k+1):
                tot = ps[i-1][j]
                if j-i >= 0:
                    tot -= ps[i-1][j-i]
                ps[i][j] = (ps[i][j-1] + tot) % M
        
        return (ps[n][k] - ps[n][k-1]) % M