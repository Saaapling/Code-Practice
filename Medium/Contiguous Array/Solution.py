from collections import defaultdict

class Solution:
    
    """
        Problem: https://leetcode.com/problems/contiguous-array/submissions/
    """
    
    def findMaxLength(self, nums: List[int]) -> int:
        vc = defaultdict(int)
        vc[0] = -1
        
        curr = 0
        mv = 0
        for idx, i in enumerate(nums):
            if i == 0:
                curr -= 1
            else:
                curr += 1
                
            if curr in vc:
                mv = max(mv, idx - vc[curr])
            else:
                vc[curr] = idx
                
        return mv