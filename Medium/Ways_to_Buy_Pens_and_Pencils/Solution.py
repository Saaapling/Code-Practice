class Solution:
    
    """
        Problem: https://leetcode.com/contest/biweekly-contest-76/problems/number-of-ways-to-buy-pens-and-pencils/
        Comments:
            Initial Thoughts: DP
                - Ex: Store answer at dp
                    - dp[0-4] = 1
                    - dp[5-9] = 2
                    - dp[10] = (1 + dp[0]) + (1 + dp[5]) = 2 + 2 = 4
                    - dp[15] = (1 + dp[5]) + (1 + dp[10]) = 3 + 5 = 8
                    - dp[20] = (1 + dp[10]) + (1 + dp[15]) = 5 + 9 = 13
                    - This method is flawed
                - Ex: Dp[val] spends all of val
                    - dp[0-4] = 0
                    - dp[5] = 1
                    - dp[6-9] = 0
                    - dp[10] = (1:bc) + dp[5] = 2
                    - dp[11-14] = 0
                    - dp[15] = dp[5] + dp[10] = 3 (should be 2)
                    - dp[20] = dp[10] + dp[15] = 2 + 3 = 5 (should be 3)
                - Ex: Backtracking with seen-arr?
                - Ex: Follow the example.... buy 0-n pens, check pencils
                    - Wow...
                    
    """
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        tot = 0
        for i in range(0, (total // cost1) + 1):
            rem = total - (cost1 * i)
            tot += 1 + rem // cost2
            # print(tot)
            
        return tot