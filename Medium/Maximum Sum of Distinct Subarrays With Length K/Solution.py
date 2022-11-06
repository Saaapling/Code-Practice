class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-318/problems/maximum-sum-of-distinct-subarrays-with-length-k/
    """
    
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        mv = 0
        n = len(nums)
        
        seen = set()
        i = 0
        l = 0
        ps = 0
        while i < n:
            x = nums[i]
            if i-l >= k:
                seen.remove(nums[l])
                ps -= nums[l]
                l += 1
                
            while x in seen:
                seen.remove(nums[l])
                ps -= nums[l]
                l += 1
                
            seen.add(x)
            ps += x
            if len(seen) == k:
                mv = max(mv, ps)
            
            i += 1
                
        return mv