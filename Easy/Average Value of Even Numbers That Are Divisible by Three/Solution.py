class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-317/problems/average-value-of-even-numbers-that-are-divisible-by-three/
    """
    
    def averageValue(self, nums: List[int]) -> int:
        count = 0
        tot = 0
        for i in nums:
            if i%3 == 0 and i%2 == 0:
                tot += i
                count += 1
                
        if count == 0:
            return 0
        
        return tot // count