class Solution:
    
    """
        Problem: https://leetcode.com/problems/image-overlap/
        Comments:
            - Brute force: Check every single configuration O(n^2*n^2) -> O(n^4)
                - Would actually work because n <= 30
                - Simplification: O(n^3) through bit comparison
                    - Collapse each row down to a bitfield
                        - Comparing rows goes from O(n) to O(1)
                    - Shifting array left and right becomes left/right shifting
    """
    
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        
        bf1 = [0 for _ in range(n)]
        bf2 = [0 for _ in range(n)]
        
        for i in range(n):
            bf1[i] = int("".join(map(str, img1[i])), 2)
            bf2[i] = int("".join(map(str, img2[i])), 2)
            
        mv = 0
        for i in range(n):
            for j in range(n):
                # Right Shift (Down)
                tot = 0
                for k in range(n-i):
                    res = (bf1[k] >> j) & bf2[k+i]
                    tot += res.bit_count()
                mv = max(mv, tot)
                
                # Left Shift (Down)
                tot = 0
                for k in range(n-i):
                    res = (bf1[k] << j) & bf2[k+i]
                    tot += res.bit_count()
                mv = max(mv, tot)
                
                # Right Shift (Up)
                tot = 0
                for k in range(n-i):
                    res = (bf1[k+i] >> j) & bf2[k]
                    tot += res.bit_count()
                mv = max(mv, tot)
                
                # Left Shift (Up)
                tot = 0
                for k in range(n-i):
                    res = (bf1[k+i] << j) & bf2[k]
                    tot += res.bit_count()
                mv = max(mv, tot)
                
        return mv