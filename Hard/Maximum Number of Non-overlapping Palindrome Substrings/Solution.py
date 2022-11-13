from sortedcontainers import SortedList

class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-319/problems/maximum-number-of-non-overlapping-palindrome-substrings/
        Comments:
            - Problem can be split into two parts:
                - Find palindromes
                    - Brute Force: O(n^3) too slow
                    - DP O(n^2)
                        - Had to look this up: https://leetcode.com/problems/palindromic-substrings/solution/
                - Select optimal sequences (Knapsack problem)
    """
    
    def knap_sack_calc(self, s, k):
        n = len(s)
        if k == 1:
            return n
        
        # Edge Cases
        if len(set(s)) == 1:
            return n // k
        
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            
        palins = []
        for i in range(1,n):
            if s[i-1] == s[i]:
                dp[i-1][i] = True
                if k <= 2:
                    palins.append((i-1, i))

        for i in range(2, n):
            for j in range(i, n):
                start = j-i
                if dp[start+1][j-1] and s[start] == s[j]:
                    dp[start][j] = True
                    if k <= i+1:
                        palins.append((start, j))
                        
        palins = SortedList(palins)
        
        # Edge case
        if len(palins) == 0:
            return 0
        
        kp = {}
        n = len(palins)
        def knapsack(idx):
            if idx >= n:
                return 0
            
            if idx in kp:
                return kp[idx]
            
            end = palins[idx][1]
            nidx = palins.bisect_left((end+1, 0))
            ret = max(1 + knapsack(nidx), knapsack(idx + 1))

            kp[idx] = ret
            return ret
            
        return knapsack(0)
    
    def greedy_calc(self, s, k):
        n = len(s)
        if k == 1:
            return n

        
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            
        palins = []
        for i in range(1,n):
            if s[i-1] == s[i]:
                dp[i-1][i] = True
                if k <= 2:
                    palins.append((i, i-1))

        for i in range(2, n):
            for j in range(i, n):
                start = j-i
                if dp[start+1][j-1] and s[start] == s[j]:
                    dp[start][j] = True
                    if k <= i+1:
                        palins.append((j, start))
                        
        palins = SortedList(palins)
        
        # Edge case
        if len(palins) == 0:
            return 0
        
        idx = -1
        n = len(palins)
        tot = 0
        ev = 0
        while idx < n:
            idx += 1
            while palins[idx][0] <= ev:
                if idx >= n:
                    return tot
                idx += 1
                
            tot += 1
            ev = palins[idx][0]
            
        return tot
    
    def maxPalindromes(self, s: str, k: int) -> int:
        return self.greedy_calc(s,k)
        