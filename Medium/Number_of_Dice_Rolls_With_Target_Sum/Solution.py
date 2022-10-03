class Solution:
    
    """
        Problem: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
        Comments:
            - Initials Thoughts: DP Solution
                - States: n, k, (target?)
                    - if n*k < target, answer = 0
                - Ex: n=2, k=6, target = 7
                    - [0, 0, 0, 0, 0, 0]
                    - [0, 0, 0, 2, 2, 2]
                    - Total is 6
                - Ex: n=5, k=6, target = 15
                    - [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
                    - [0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2]
                    - [0, 0, 0, 0, 1, ]
                    - []
                    - []
                - dp[i][j] = dp[i][j-1] + dp[]
                - dp[i][j][k] = dp[i-1][1:j][k-j]
                    - How to generate the first base case?
"""
    
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        M  = 10 ** 9 + 7
        dp = [[-1 for _ in range(target + 1)] for _ in range(n + 1)]
        # print(dp_arr)
        
        for i in range(1, target + 1):
            if i > k:
                break
            dp[1][i] = 1

        def aux(n, t):
            if n == 0 or t < 0:
                return 0
            
            if dp[n][t] != -1:
                return dp[n][t]
            
            if n * k < t:
                dp[n][t] = 0
                return 0
            
            tot = 0
            for i in range(1, k+1):
                val = aux(n-1, t-i)
                tot += val
            
            dp[n][t] = tot % M
            return dp[n][t]

        val = aux(n,target)
        return val