class Solution:
    
    """
        Problem: https://leetcode.com/problems/maximum-subarray/
        Comments:
            Initial Thoughts: 
                - Optimal Algorithm: Kadane's (Given, but don't know what it is prior to solving)
                    - https://www.interviewbit.com/blog/maximum-subarray-sum/#:~:text=Kadane's%20Algorithm%20is%20an%20iterative,ending%20at%20the%20previous%20position.
                - Prefix Sum + Minimum-Val Array
    """
    
    def maxSubArray(self, nums: list[int]) -> int:      
        n = len(nums)
        
        p_sum = nums[0]
        min_val = min(0, nums[0])
        max_val = nums[0]
        for i in range(1, n):
            p_sum += nums[i]
            max_val = max(max_val, p_sum - min_val)
            min_val = min(min_val, p_sum)
        
        return max_val