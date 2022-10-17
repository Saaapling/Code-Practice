import math
class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-315/problems/largest-positive-integer-that-exists-with-its-negative/
    """
    
    def findMaxK(self, nums: List[int]) -> int:
        vals = set()
        
        mv = -1
        for i in nums:
            if abs(i) > mv and -1 * i in vals:
                mv = abs(i)
            vals.add(i)
        
        return mv