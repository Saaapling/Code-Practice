class Solution:
    
    """
        Problem: https://leetcode.com/problems/stone-game-vii/
        Time Taken: ~15 + 30 min (initial recursive + optimization)
        Comments: Even the optimal solution sometimes TLEs, but when it finishes successfully, it is better than 80% of python
            - Leetcode's submission for this one seems to just be wierd
    """

    def stoneGameVII_recursive(self, stones: list[int]) -> int:
        dp = {}
        
        def aux(l, r): #p1 score, p2 score
            if l == r-1:
                return max(stones[l], stones[r])
            
            if (l,r) in dp:  #0,4
                return dp[(l,r)]

            full_sum = sum(stones[l:r+1])
            return max(full_sum - stones[l] - aux(l+1,r), full_sum - stones[r] - aux(l,r-1))
            
            
        ans = aux(0, len(stones)-1)
        return ans

    def stoneGameVII_self_defined_query(self, stones: list[int]) -> int:
        dp = [[0 for _ in range(len(stones))] for _ in range(len(stones))]
        prefix_sum = [0] * len(stones)
        
        prefix_sum[0] = stones[0]
        for i in range(1, len(stones)):
            prefix_sum[i] = prefix_sum[i-1] + stones[i]
        
        for i in range(0, len(stones) - 1):
            dp[i][i+1] = max(stones[i], stones[i+1])
            
        def query(l, r):
            if l == 0:
                return prefix_sum[r]
            return prefix_sum[r] - prefix_sum[l-1]
            
        for d in range(2, len(stones)): # interval size
            for s in range(0, len(stones) - d): # starting index
                left = query(s+1,s+d) - dp[s+1][s+d]
                right = query(s,s+d-1) - dp[s][s+d-1]
                
                dp[s][s+d] = max(left, right)

                
        return dp[0][len(stones)-1]

    def stoneGameVII(self, stones: list[int]) -> int:
        n = len(stones)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        prefix_sum = [0] * n
        prefix_sum[0] = stones[0]           
        
        for i in range(0, n - 1):
            dp[i][i+1] = max(stones[i], stones[i+1])
            prefix_sum[i+1] = prefix_sum[i] + stones[i+1]
            
        for d in range(2, n): # interval size
            for s in range(0, n - d): # starting index
                left = prefix_sum[s+d] - prefix_sum[s] - dp[s+1][s+d]
                right = prefix_sum[s+d-1] - dp[s][s+d-1]
                if s > 0:
                    right -= prefix_sum[s-1]
                    
                dp[s][s+d] = max(left, right)

                
        return dp[0][n-1]
