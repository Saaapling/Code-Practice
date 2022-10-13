class Solution:
    
    """
        Problem: https://leetcode.com/problems/increasing-triplet-subsequence/
        Comments:
            - Brute Force: n^2
                - Probably too slow
            - Idea: Greedily maintain best 3
                - Ex: [2,1,5,0,4,6]
                    - [2] -> [1] -> [1,5] -> [0,5] -> [0,4] -> [0,4,6]
                - Ex: [0,6,5,1,1,2]
                - No need for binary search because n = 2
                    - Just maintaining 2 numbers is good enough
    """
    
    def increasingTriplet(self, nums: list[int]) -> bool:
        i = nums[0]
        j = 2 ** 31
        
        def aux(k):
            nonlocal i
            nonlocal j
            
            if k > j:
                return True
            
            if k < i:
                i = k
            elif k < j and k > i:
                j = k
            
            return False
        
        for k in range(1, len(nums)):
            if aux(nums[k]):
                return True
        
        return False