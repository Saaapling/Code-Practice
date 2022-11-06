class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-318/problems/apply-operations-to-an-array/
    """
    
    def applyOperations(self, nums: List[int]) -> List[int]:
        zeros = 0
        vals = []
        
        n = len(nums)
        i = 0
        while i < n-1:
            if nums[i] == 0:
                zeros += 1
                i += 1
                continue
            
            if nums[i] == nums[i+1]:
                vals.append(nums[i] * 2)
                zeros += 1
                i += 2
            else:
                vals.append(nums[i])
                i += 1
                
        if i == n-1:
            vals.append(nums[i])

        for i in range(zeros):
            vals.append(0)
            
        return vals