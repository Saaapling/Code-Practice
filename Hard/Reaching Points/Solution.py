class Solution:
    
    """
        Problem: https://leetcode.com/problems/reaching-points/
        Comments:
            - Idea: Backtracking, only the larger element can decrease
    """
    
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            
            if tx > ty:
                tx -= ty * max(1, ((tx - sx) // ty))
            else:
                ty -= tx * max(1, ((ty - sy) // tx))
            # print(str(tx) + ", " + str(ty))
                
        return False