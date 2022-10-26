class Solution:
    
    """
        Problem:
        Comments:
            - Inital Thoughts: O(n * k) solution: keep a seen set of sum % k
                - k can be a massive number (2 ^ 31)
                - Can better be done?
                - Idea: Immediately mod all elements by k
                    - if len(n) > k**2, answer is true
                - Post implementation: Read better... has to be contiguous
            - Idea: O(n^2) brute force solution
                - Expensive part of this solution is upkeep of complements set
                    - Keep an extra number to represent current offset from when number was originally added
                        - Pair with prefix sum?
                    
    """
    
    def brute_force_soln(self, nums, k):
        curr = set()
        
        for i in nums:
            next_set = set()
            i %= k
            if (k-i)%k in curr:
                return True
            
            next_set.add(i)
            for j in curr:
                next_set.add((i+j)%k)
            curr = next_set
            # print(curr)
            
        return False
        
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        
        seen = set()
        cs = 0
        prev = -1
        for i in nums:
            if i%k == 0:
                if prev == 0:
                    return True
                else:
                    prev = 0
                    continue
            
            cs = (cs + i) % k
            if cs == 0 or cs in seen:
                return True
            seen.add(cs)
            prev = i
            
        return False
