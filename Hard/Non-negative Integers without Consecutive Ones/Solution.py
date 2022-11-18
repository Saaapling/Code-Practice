class Solution:
    
    """
        Problem: https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/
        Comments:
            - DP solution
                - State: Length (power of two)
                - Tracks: Count ending with 1?
            - Traverse twice, first time for max power of 2, second time for remaining elements
    """
    
    
    def findIntegers(self, n: int) -> int:
       # Edge Cases
        if n == 0:
            return 1
        elif n == 1:
            return 2
        
        power = int(math.log(n,2))
        
        dp = [0 for _ in range(power + 1)]
        dp[0] = 1
        dp[1] = 1
        ps = [1,2]
        for i in range(2,power+1):
            dp[i] = ps[i-2]
            ps.append(ps[-1] + dp[i])
            
        tot = ps[-1]
        n -= 2**power
        while n > 0:
            if n >= 2**(power-1):
                n = 2**(power-1) - 1
            else:
                power = int(math.log(n,2))
                tot += ps[power]
                n -= 2**power
            
        # print(dp)
        # print(ps)
        return tot + 1