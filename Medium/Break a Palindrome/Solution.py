class Solution:
    
    """
        Problem: https://leetcode.com/problems/break-a-palindrome/
        Comments:
            - Initial Thoughts:
                - Replace first non-'a'
                    - What if this creates a palindrome in itself?
    """
    
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        
        # Base Case
        if n == 1:
            return ""
        
        non_a = 0
        idx = 0
        for i in range(n):
            if palindrome[i] != 'a':
                non_a += 1
                if non_a == 1:
                    idx = i
                else:
                    break
                
        if non_a < 2:
            return palindrome[:-1] + "b"
        else:
            return palindrome[:idx] + "a" + palindrome[idx+1:]