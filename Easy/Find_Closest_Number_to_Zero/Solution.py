class Solution:
    
    """
        Problem: https://leetcode.com/contest/biweekly-contest-76/problems/find-closest-number-to-zero/
    """
    
    def findClosestNumber(self, nums: list[int]) -> int:
        val = nums[0]
        
        for i in range(1, len(nums)):
            nval = nums[i]
            if abs(nval) < abs(val):
                val = nval
            elif abs(nval) == abs(val):
                if val < 0 and nval > 0:
                    val = nval
                    
        return val