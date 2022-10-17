class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-315/problems/count-subarrays-with-fixed-bounds/
        Comments:
            - Optimistic Traversal Keeping track of starts
                - Fails when you encountre min/max multiple times
    """
    
    def optimistic_traversal(self, nums, minK, maxK):
        n = len(nums)
        lf = False
        hf = False
        
        left = 0
        pot = 0
        tot = 0
        for i in range(n):
            curr = nums[i]
            if curr == minK:
                lf = True
                if hf:
                    tot += pot
                    pot = 0
                else:
                    pot = i - left
            
            if curr == maxK:
                hf = True
                if lf:
                    tot += pot
                    pot = 0
                else:
                    pot = i - left
                    
            if curr < minK:
                lf = False
                hf = False
                left = i+1
            
            if curr > maxK:
                lf = False
                hf = False
                left = i+1
                
            if lf and hf:
                tot += 1
                left = i+1
                
            print(lf)
            print(hf)
            print(pot)
            print(tot)
            print()
                
        return tot 
    
    def countSubarrays(self, nums: list[int], l: int, h: int) -> int:
        n = len(nums)
        
        lidx = -1
        lf = False
        hidx = -1
        hf = False
        start = 0
        tot = 0
        for i in range(n):
            curr = nums[i]

            if curr < l or curr > h:
                lf = False
                hf = False
                start = i+1
                continue
                
            if curr == l:
                lf = True
                lidx = i

            if curr == h:
                hf = True
                hidx = i

            if lf and hf:
                tot += 1 + min(lidx, hidx) - start
                
            # print(tot)
                
        return tot 
