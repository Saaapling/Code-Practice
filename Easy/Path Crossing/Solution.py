class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-195/problems/path-crossing/
    """
    def isPathCrossing(self, path: str) -> bool:
        curr = (0,0)
        seen = set()
        seen.add((0,0))
        
        for ch in path:
            if ch == 'N':
                 curr = (curr[0], curr[1] + 1)
            elif ch == 'S':
                 curr = (curr[0], curr[1] - 1)
            elif ch == 'E':
                 curr = (curr[0] + 1, curr[1])
            else:
                 curr = (curr[0] - 1, curr[1])
                 
            if curr in seen:
                 return True
            
            seen.add(curr)
                 
        return False