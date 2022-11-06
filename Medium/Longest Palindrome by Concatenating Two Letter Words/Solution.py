from collections import defaultdict
class Solution:
    
    """
        Problem: https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
    """
    
    def longestPalindrome(self, words: List[str]) -> int:
        pairs = defaultdict(lambda: 0)
        
        tot = 0
        solo = 0
        for i in words:
            x = False
            if i[0] == i[1]:
                solo += 1
                x = True
            
            if pairs[i[::-1]] > 0:
                pairs[i[::-1]] -= 1
                if x:
                    solo -= 2
                tot += 4
            else:
                pairs[i] += 1
                
        if solo > 0:
            tot += 2
            
        return tot