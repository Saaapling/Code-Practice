class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-312/problems/longest-subarray-with-maximum-bitwise-and/
    """

    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0
        max_val = 0
        
        curr = 0
        for i in nums:
            if i > max_val:
                curr = 1
                max_len = 1
                max_val = i
            elif i == max_val:
                curr += 1
            else:
                curr = 0
                
            if curr > max_len:
                max_len = curr
                
        return max_len