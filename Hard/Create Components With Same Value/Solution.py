from copy import deepcopy
from collections import defaultdict

class Solution:
    
    """
        Problem: https://leetcode.com/contest/biweekly-contest-89/problems/create-components-with-same-value/
        Comments: 
            - Initial Thoughts:
                - Techniques Considered: Union-Find, DFS/BFS, DP?
    """
    
    def factorize(self, n, nodes, mv):
        rs = []
        
        i = 2
        while i <= n ** 0.5:
            if i > nodes:
                i += 1
                break
            if n / i < mv:
                i += 1
                continue
                
            if n % i == 0:
                if i >= mv:
                    rs.append(i)
                rs.append(n//i)
            i += 1
        
        rs.sort()
        return rs
    
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        # Base Case (Because factorize won't catch this)
        if len(set(nums)) == 1:
            return len(edges)
        
        
        n = len(nums)
        tot = 0
        for i in nums:
            tot += i
        
        factors = self.factorize(tot, n, max(nums))
        # print(factors)

        adj_list = [set() for _ in range(n)]
        for x,y in edges:
                adj_list[x].add(y)
                adj_list[y].add(x)
                
        def aux(val):
            nonlocal adj_list
            nonlocal nums
            
            ccval = [i for i in nums]
            seen = [False for _ in nums]
            ngbrs = [len(adj_list[i]) for i in range(len(adj_list))]
            
            deleted = 0
            stack = []
            for node in range(len(adj_list)):
                if ngbrs[node] == 1:
                    stack.append(node)
            
            while stack:
                node = stack.pop()
                seen[node] = True
                if ngbrs[node] != 1:
                    continue
                
                for ngbr in adj_list[node]:
                    if not seen[ngbr]:
                        break

                if ccval[node] < val:
                    ccval[ngbr] += ccval[node]
                    if ccval[ngbr] > val:
                        return -1
                    ccval[node] = 0
                else:
                    deleted += 1

                ngbrs[node] -= 1
                ngbrs[ngbr] -= 1
                if ngbrs[ngbr] == 1:
                    stack.append(ngbr)
              
            # Emergency Check to make sure all elements are valid, but this check is not needed because the
                # if ccval[ngbr] > val check already handles this
            # for i in ccval:
            #     if i != 0 and i != val:
            #         return -1
                
            return deleted
        
        # Could use binary-search to speed this up
        for val in factors:
            deleted = aux(val)
            if deleted > -1:
                return deleted
            
        return 0
                
            
        