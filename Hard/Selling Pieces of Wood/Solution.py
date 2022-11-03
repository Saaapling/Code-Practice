class Solution:
    
    """
        Problem: https://leetcode.com/problems/selling-pieces-of-wood/
        Comments:
            - Initial Thoughts:
                - We know its a DP question (Given)
                - Potential States: length and width?
                    - Base Case: All 0's
                    - For a new state, follow this loops
                        - For each possible peice:
                            - Fit the peice in the bottom right corner (and cut the board to make it as such)
                            - Cutting a peice off creates up to three new peices
                                - Sum the peice price, and the three dp peices together
                            - Important: you don't have to make both cuts simulataneously
                - Optimization: Instead of iterating down peices at every step, make peices a base case
                    - Instead of cutting based on peices, instead, make all possible horizontal and vertical cuts
                    - m*n states
                    - For previous TLE implementations, with worse case (1x1 peice), runtime was at least m*n anyways (m*n*k with k = len(peices))

            - Post Submission Thoughts: Giga-hard problem. Fun though
    """
    
    def iterative_dp_tle(self, m, n, prices):
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                best = 0
                for h, w, p in prices:
                    # Check if the peice fits
                    if h <= i and w <= j:
                        # Vertical cut first:
                        v_cut = p
                        v_cut += dp[i][j-w]
                        v_cut += dp[i-h][w]
                        
                        # Horizontal cut first:
                        h_cut = p
                        h_cut += dp[i-h][j]
                        h_cut += dp[h][j-w]
                        
                        best = max(best, v_cut)
                        best = max(best, h_cut)

                dp[i][j] = best
                
        # for lst in dp:
        #     print(lst)
                
        return dp[m][n]
        
    def recursive_dp_tle(self, m, n, prices):
        dp = {}
        def aux(m, n):
            if (m,n) in dp:
                return dp[(m,n)]
            
            nonlocal prices
            best = 0
            for h, w, p in prices:
                # Check if the peice fits
                if h <= m and w <= n:
                    # Vertical cut first:
                    v_cut = p
                    v_cut += aux(m, n-w)
                    v_cut += aux(m-h, w)

                    # Horizontal cut first:
                    h_cut = p
                    h_cut += aux(m-h, n)
                    h_cut += aux(h, n-w)

                    best = max(best, v_cut)
                    best = max(best, h_cut)
                    
            dp[(m,n)] = best
            return best
            
        return aux(m,n)
        
        
    def recursive_dp_cleaned_tle(self, m, n, prices):
        # Base Case
        if len(prices) == 1:
            h,w,p = prices[0]
            x = n // w
            y = m // h
            return x * y * p
        
        dp = {}
        base = {}
        
        mh = 10**10
        mw = 10**10
        for h,w,p in prices:
            base[(h,w)] = p
            mh = min(mh, h)
            mw = min(mw, w)
            
        for i in range(mh):
            for j in range(mw):
                dp[(i,j)] = 0
                
        def aux(m,n):
            if (m,n) in dp:
                return dp[(m,n)]
            
            best = base.get((m,n), 0)
            for i in range(1, (m+2)//2):
                best = max(best, aux(i,n) + aux(m-i,n))
            for i in range(1, (n+2)//2):
                best = max(best, aux(m,i) + aux(m,n-i))
            
            dp[(m,n)] = best
            return dp[(m,n)]

        ans = aux(m,n)
        return ans
        
    # Iterative dp, finally doesn't TLE
    def sellingWood(self, m: int, n: int, prices: list[list[int]]) -> int:
        dp = {}
        
        dp[(1,1)] = 0
        for h,w,p in prices:
            dp[(h,w)] = p
                            
        for i in range(m+1):
            for j in range(n+1):
                best = dp.get((i,j), 0)
                for x in range(1, (i//2) + 1):
                    best = max(best, dp[(x,j)] + dp[(i-x,j)])
                for x in range(1, (j//2) + 1):
                    best = max(best, dp[(i,x)] + dp[(i,j-x)])
                    
                dp[(i,j)] = best
                
        # print(dp)
        return dp[(m,n)]