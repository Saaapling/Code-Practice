class Solution:
    
    """
        Problem: https://leetcode.com/problems/substring-with-largest-variance/
        Comments:
            - Brute Force: Check every possible substring O(n^2)
                - Use a freq-map to make each check O(1)
                    - Adding and removing elements might actually make checks O(log(n))
                    - Can use either a segtree (n=26) or a sortedlist with insert/removal (n=26)
                    - Way too slow with log(n) check -> O(n^2 * log(n))
            - Had to use hints:
                - Relevant Hint 1: Think about how to solve the problem if the string had only two distinct characters.
                    - Replace char's with 1, -1, find max subarray (Hint 2, but I was able to figure this out)
                - Relevant Hint 2: Think about how to solve the problem if the string had only two distinct characters.
                    - Take set(string), consider what happens if each ele of this set was the 'maximum' element in substring
                - Proposed Complexity: O(26 * 25 * n) -> O(n)
    """
            
    def largestVariance(self, s: str) -> int:
        chars = set(s)
        # Edge case    
        if len(chars) == 1:
            return 0
        
        ans = 0
        chars = list(chars)
        for a in chars:
            for b in chars:
                if a == b:
                    continue
                    
                mv = 0
                curr = 0
                other = False
                for c in s:
                    if c == a:
                        curr += 1
                    elif c == b:
                        curr -= 1
                        other = True
                    else:
                        continue
                        
                    if other:
                        mv = max(mv, curr)
                    else:
                        mv = max(mv, curr-1)
                        
                    if curr < 0:
                        curr = 0
                        other = False

                ans = max(ans, mv)
            
        return ans