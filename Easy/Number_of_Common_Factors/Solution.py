class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-313/problems/number-of-common-factors/
    """
    
    def commonFactors(self, a: int, b: int) -> int:
        bound = min(a,b)
        
        cf = [1]
        for i in range(2, bound+1):
            if  a%i == 0 and b%i == 0:
                cf.append(i)
                
        return len(cf)
        