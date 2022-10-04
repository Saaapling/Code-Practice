class Solution:
    
    """
        Problem: https://leetcode.com/problems/coin-change-ii/
        Comments: 
            Initial Thoughts: DP Solution
                - Very Similiar to this previous problem: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
                - dp[i][j] represents number of ways to reach amount 'i' with the smallest 'j' coins
                - Inductive reasoning is a little bit tricky, but could also be just tired when solving this problem

    """
    
    def change(self, amount: int, coins: list[int]) -> int:
        coins.sort()
        n = len(coins)
        dp = [[-1 for _ in range(n)] for _ in range(amount+1)]
        
        for i in range(n):
            dp[0] = [1 for i in range(n)]
        
        def aux(amt, max_i):           
            if dp[amt][max_i] != -1:
                return dp[amt][max_i]
            
            tot = 0
            for i in range(max_i + 1):
                if coins[i] <= amt:
                    tot += aux(amt-coins[i], i)
            
            dp[amt][max_i] = tot
            return dp[amt][max_i]
        
        for i in range(n):
            aux(amount, i)
        # print(dp)
        
        return dp[amount][n-1]