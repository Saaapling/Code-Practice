from sortedcontainers import SortedList

class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-195/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
        Comments:
    """

    def numSubseq(self, nums: List[int], target: int) -> int:
        M = 10 ** 9 + 7    
        nums.sort()
        
        mv = nums[0]
        if mv * 2 > target:
            return 0
        
        n = len(nums)
        l = 0
        for i in range(n):
            if nums[i] + mv > target:
                break
        r = i
        
        cache = {}
        def aux(n):
            x = 1
            cache[0] = 1
            for i in range(1, n+1):
                x = (x*2) % M
                cache[i] = x            
        
        aux(r + 1)
        tot = cache[r+1] - 1
        while l <= r:
            while l <= r and nums[l] + nums[r] <= target:
                l += 1
            
            while l <= r and nums[l] + nums[r] > target:
                tot -= cache[r-l]
                r -= 1

        return tot % M