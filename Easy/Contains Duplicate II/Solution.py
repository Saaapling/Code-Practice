from collections import defaultdict
from collections import OrderedDict

class Solution:
    
    """
        Problem: https://leetcode.com/problems/contains-duplicate-ii/submissions/
        Comments:
            - Initial Thoughts: maintain a set or dict
                - Ordered Dict handles this problem perfectly
    """
    
    def ordered_dict_soln(self, nums, k):
        n = len(nums)
        seen = OrderedDict()
        
        for i in range(min(k, n)):
            if nums[i] in seen:
                return True
            seen[nums[i]] = True
            
        for i in range(k, n):
            if nums[i] in seen:
                return True
            seen[nums[i]] = True
            seen.popitem(last=False)
        
        return False
            
    def dict_soln(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        seen = defaultdict(lambda: False)
        
        for i in range(min(k, n)):
            if seen[nums[i]]:
                return True
            seen[nums[i]] = True
            
        for i in range(k, n):
            if seen[nums[i]]:
                return True
            seen[nums[i]] = True
            seen[nums[i-k]] = False
            
        return False
    
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        return self.ordered_dict_soln(nums, k)