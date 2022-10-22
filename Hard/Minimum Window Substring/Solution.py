from collections import defaultdict
from collections import deque

class Solution:
    
    """
        Problem: https://leetcode.com/problems/minimum-window-substring/
        Comments: 
            - Thoughts: Iterate though entire string, checking every possible configuration
                - Use a is_valid() function when encountering a char in 't', calculate string len if valid
            - Post Submission Comments: O(n + m?)
                - Iterates through 't': O(m)
                - Iterates through 's': O(n) base
                    - Calls is_valid for each character: (1)
                        - Adds and removes from deques, which is O(1)
    """
    
    def minWindow(self, s: str, t: str) -> str:
        rem = defaultdict(lambda: 0)
        pos = {}
        for char in t:
            rem[char] += 1
            pos[char] = deque()
            
        char_pos = deque()
        seen = set()
        left = len(t)
        def is_valid(x, idx):
            nonlocal left
            
            if not x in rem:
                return 10 ** 6
            
            pos[x].append(idx)
            char_pos.append(idx)
            if rem[x] == 0:
                old = pos[x].popleft()
                seen.add(old)
                while char_pos[0] in seen:
                    seen.remove(char_pos[0])
                    char_pos.popleft()
            else:
                rem[x] -= 1
                left -= 1
            
            if left == 0:
                return char_pos[-1] - char_pos[0] + 1
            
            return 10 ** 6
        
        mv = 10 ** 6
        ans = [-1,-1]
        for i, char in enumerate(s):
            substr_len = is_valid(char, i)
            if substr_len < mv:
                mv = substr_len
                ans = [char_pos[0], char_pos[-1]]
 
        if ans[0] == -1:
            return ""
        else:
            return s[ans[0]:ans[1]+1]