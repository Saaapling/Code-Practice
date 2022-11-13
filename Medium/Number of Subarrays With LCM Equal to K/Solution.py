class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-319/problems/number-of-subarrays-with-lcm-equal-to-k/
        Comments:
            - Brute Force: O(n^2 * (n?))
    """
    
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        tot = 0
        for i in range(n):
            curr = 1
            for j in range(i,n):
                curr = math.lcm(curr, nums[j])
                if curr == k:
                    tot += 1
        
        return tot