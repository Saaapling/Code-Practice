class Solution:
    
    """
        Problem: https://leetcode.com/problems/minimum-window-substring/
        Comments: 
            - Thoughts: Iterate though entire string, checking every possible configuration
                - Use a is_valid() function when encountering a char in 't', calculate string len if valid
    """
    
    def minWindow(self, s: str, t: str) -> str:
        