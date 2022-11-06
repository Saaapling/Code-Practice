class Solution:
    
    """
        Problem:https://leetcode.com/problems/reverse-vowels-of-a-string/
        Comments: 
    """
    
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        s = list(s)
        
        vowels = []
        for i in s:
            if i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                vowels.append(i)
                
        idx = 0
        for j, i in enumerate(s):
            if i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                s[j] = vowels[~idx]
                idx += 1
                
        return "".join(s)