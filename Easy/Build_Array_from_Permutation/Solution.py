class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-248/problems/build-array-from-permutation/
        Naive: Traversal
    """
    
    def buildArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i, j in enumerate(nums):
            result[i] = nums[nums[i]]
            
        return result
        