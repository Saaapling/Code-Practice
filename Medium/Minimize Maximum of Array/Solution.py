import math
class Solution:
    
    """
        Problem: https://leetcode.com/contest/biweekly-contest-89/problems/minimize-maximum-of-array/
    """

    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        mv = nums[0]
        
        tot = mv
        for i in range(1, n):
            curr = nums[i]
            tot += curr
            if curr > mv:
                mv = max(mv, math.ceil(tot / (i + 1)))
                
        return mv
