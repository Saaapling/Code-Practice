from collections import defaultdict
class Solution:
    
    """
        Problem: https://leetcode.com/problems/count-number-of-nice-subarrays/
        Comments:
            - Some form of prefix-sum/count
                - Together with a hash map?
    """
    
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oc = defaultdict(int)
        oc[0] = -1
        
        mv = 0
        count = 0
        for idx, i in enumerate(nums):
            if i % 2 == 1:
                count += 1
                oc[count] = idx
                
        # Edge Case
        if count < k:
            return 0
                
        n = len(nums)
        oc[count+1] = n
        tot = 0
        for i in range(k, count+1):
            left = oc[i-k+1] - oc[i-k]
            right = oc[i+1] - oc[i]
            tot += left * right
            
        return tot