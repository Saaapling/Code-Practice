class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-288/problems/largest-number-after-digit-swaps-by-parity/
    """
    
    def largestInteger(self, num: int) -> int:
        odds = []
        evens = []
        
        num = str(num)
        n = len(num)
        for i in range(n):
            x = int(num[i])
            if x % 2 == 1:
                odds.append(x)
            else:
                evens.append(x)
                
        odds.sort(reverse=True)
        evens.sort(reverse=True)
        
        ans = 0
        oidx = 0
        eidx = 0
        for i in range(n):
            x = int(num[i])
            if x % 2 == 1:
                ans = ans*10 + odds[oidx]
                oidx += 1
            else:
                ans = ans*10 + evens[eidx]
                eidx += 1
        
        return ans