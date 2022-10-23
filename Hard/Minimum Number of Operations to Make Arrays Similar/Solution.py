class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-316/problems/minimum-number-of-operations-to-make-arrays-similar/
        Comments:
            - Is sorting O(nlog(n)) too slow?
            - Answer: No its not :)
     """
    
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        even_nums = []
        odd_nums = []
        even_targets = []
        odd_targets = []
        
        n = len(nums)
        for i in range(n):
            if nums[i] % 2 == 0:
                even_nums.append(nums[i])
            else:
                odd_nums.append(nums[i])
            
            if target[i] % 2 == 0:
                even_targets.append(target[i])
            else:
                odd_targets.append(target[i])
                
        even_nums.sort()
        even_targets.sort()
        odd_nums.sort()
        odd_targets.sort()
        
        # print(even_nums)
        # print(even_targets)
        
        total = 0
        if even_nums:
            m = len(even_nums)
            for i in range(m):
                total += abs(even_nums[i] - even_targets[i])
                
        if even_nums:
            m = len(odd_nums)
            for i in range(m):
                total += abs(odd_nums[i] - odd_targets[i])
                
        return total // 4
        