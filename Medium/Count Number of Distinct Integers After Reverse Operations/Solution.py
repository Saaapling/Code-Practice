class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-315/problems/count-number-of-distinct-integers-after-reverse-operations/
    """
    
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            curr = nums[i]
            nums.append(int(str(curr)[::-1]))
            
        return len(set(nums))
        