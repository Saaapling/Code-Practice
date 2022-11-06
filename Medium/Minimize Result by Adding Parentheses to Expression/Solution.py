class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-288/problems/minimize-result-by-adding-parentheses-to-expression/
    """
    
    def minimizeResult(self, expression: str) -> str:
        a,b = expression.split('+')

        mv = int(a) + int(b)
        ans = "(" + expression + ")"
        n = len(a)
        m = len(b)
        for i in range(n):
            if i == 0:
                l = 1
                sl = "("
            else:
                l = int(a[:i])
                sl = a[:i] + "("
            lm = int(a[i:n])
            sl += a[i:n]
            
            for j in range(1, m+1):
                rm = int(b[:j])
                sr = b[:j] + ")"
                if j == m:
                    r = 1
                else:
                    r = int(b[j:m])
                    sr += b[j:m]
                    
                if mv > l * (lm + rm) * r:
                    mv = l * (lm + rm) * r
                    ans = sl + '+' + sr
                
        return ans
    
