from collections import defaultdict
class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-195/problems/check-if-array-pairs-are-divisible-by-k/
    """
    
    def canArrange(self, arr: List[int], k: int) -> bool:
        c = defaultdict(lambda: 0)
        
        for x in arr:
            x = x % k
            
            
            if c[x] > 0:
                c[x] -= 1
            else:
                c[(k-x) % k] += 1
            
        
        for key in c:
            if c[key] > 0:
                return False
            
        return True