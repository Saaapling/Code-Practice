class Solution:
    
    """
        Problem: https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
        Comments: 
            - Initial Thoughts: Maintain a stack
                - Count unaddressed right brackets
                - "[][]][[]][]["
    """
    
    def minSwaps(self, s: str) -> int:
        ub = 0
        
        lb = 0
        for ch in s:
            if ch == "[":
                lb += 1
            else:
                if lb > 0:
                    lb -= 1
                else:
                    ub += 1
        
        return (ub // 2) + (ub % 2)