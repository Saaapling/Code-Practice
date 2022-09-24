class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-213/problems/count-sorted-vowel-strings/
        Time Taken: 7 min
    """
    
    def countVowelStrings(self, n: int) -> int:
        
        dp = [1] * 5
        dp[1] = n
        
        for i in range(2, n+1):
            dp[4] += i + dp[2] + dp[3]
            dp[3] += i + dp[2]
            dp[2] += i

        return sum(dp)