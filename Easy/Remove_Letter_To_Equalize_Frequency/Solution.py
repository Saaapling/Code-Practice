from collections import defaultdict
import math
from tkinter import Y

class Solution:
    
    """
        Problem: https://leetcode.com/contest/biweekly-contest-88/problems/remove-letter-to-equalize-frequency/
    """
    
    def equalFrequency(self, word: str) -> bool:
        lc = defaultdict(lambda: 0)
        
        for ch in word:
            lc[ch] += 1
            
        x = list(lc.values())
        print(x)

        for ch in lc:
            lc[ch] -= 1
            y = set(list(lc.values()))
            y.discard(0)
            if len(y) == 1:
                return True
            lc[ch] += 1

        return False
        
test = Solution()
result = test.equalFrequency("cbccca")
print(result)