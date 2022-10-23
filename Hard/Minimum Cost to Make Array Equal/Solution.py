from collections import defaultdict

class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-316/problems/minimum-cost-to-make-array-equal/
        Comments:
            - Initial Thoughts:
                - Combine -> compare min/max -> combine
    """
    
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        n = len(nums)
        
        cs = defaultdict(lambda: 0)
        for i in range(n):
            cs[nums[i]] += cost[i]
        
        vals = list(set(nums))
        vals.sort()
        left = 0
        right = len(vals)-1
        tot = 0
        while left < right:
            lc = cs[vals[left]]
            hc = cs[vals[right]]
            if lc <= hc:
                left += 1
                nv = vals[left]
                steps = nv - vals[left-1]
                cs[nv] += lc
                tot += lc * steps
            else:
                right -= 1
                nv = vals[right]
                steps = vals[right+1] - nv
                cs[nv] += hc
                tot += hc * steps
                
        return tot