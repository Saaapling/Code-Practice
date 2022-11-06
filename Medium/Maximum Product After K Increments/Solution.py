from collections import defaultdict
from collections import deque

class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-288/problems/maximum-product-after-k-increments/
        Comments:
            - Is it true to always inc smallest num?
                - a * b * c, a < b < c
                - inc a -> (a*b*c) + (b+c)
                - inc b -> (a*b*c) + (a+c)
                - inc c -> (a*b*c) + (a+b)
                - Always inc smallest, bc sum of rem elements is largest
            - Implemenation: 
                - Min heap, element, tuple?
                    - Sorted array, (element, count)
                - O(nlog(n))
    """
    
    def maximumProduct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        M = 10**9 + 7
        
        vc = defaultdict(lambda: 0)
        for i in nums:
            vc[i] += 1
            
        x = []
        for i in vc:
            x.append((i, vc[i]))
        x.sort()
        x.append((10**7, 0))
        x = deque(x)
        # print(x)
        
        i = 0
        while k > 0:
            curr = x.popleft()
            np = x.popleft()
            
            diff = (np[0] - curr[0]) * curr[1]
            if diff <= k:
                x.appendleft((np[0], np[1] + curr[1]))
                k -= diff
            else:
                ## k = 5, (2,3) -> k = 2, (3,3) -> k=0 (3,1), (4,2)
                x.appendleft(np)
                if k >= curr[1]:
                    nvl = curr[0] + (k // curr[1])
                    x.appendleft((nvl + 1, k % curr[1]))
                    x.appendleft((nvl, curr[1] - (k % curr[1])))
                else:
                    x.appendleft((curr[0] + 1, k % curr[1]))
                    x.appendleft((curr[0], curr[1] - (k % curr[1])))
                k = 0
        
        # print(x)
        ans = 1
        for val, count in x:
            ans = (ans * (val ** count)) % M
        return ans 