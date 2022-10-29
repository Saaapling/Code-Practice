from collections import defaultdict
class Solution:
    
    def destroyTargets(self, nums: List[int], space: int) -> int:
        mp = defaultdict(lambda:[0,-1 * 10**10])
        n = len(nums)
        
        for i in range(n):
            rem = nums[i] % space
            mp[rem][1] = max(mp[rem][1], nums[i] * -1)
            mp[rem][0] += 1
            
        x = list(mp.values())
        x.sort(reverse=True)
        # print(x)
            
        return x[0][1] * -1