import heapq
class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-318/problems/total-cost-to-hire-k-workers/
    """
    
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        
        l = 0
        lheap = []
        r = n-1
        rheap = []
        
        # Need base case where candidates > n
        seen = set()
        for i in range(candidates):
            if not l in seen:
                heapq.heappush(lheap, (costs[l], l))
                seen.add(l)
                
            if not r in seen:
                heapq.heappush(rheap, (costs[r], r))
                seen.add(r)
                
            l = min(l+1, n-1)
            r = max(r-1, 0)
            
        # print(lheap)
        # print(rheap)
            
        tot = 0
        i = 0
        while i < k and lheap and rheap:               
            left = lheap[0]
            right = rheap[0]
            
            if left[0] <= right[0]:
                tot += left[0]
                heapq.heappop(lheap)
                if not l in seen:
                    heapq.heappush(lheap, (costs[l], l))
                    seen.add(l)
                l = min(l+1, n-1)
            else:
                tot += right[0]
                seen.add(right[1])
                heapq.heappop(rheap)
                if not r in seen:
                    heapq.heappush(rheap, (costs[r], r))
                    seen.add(r)
                r = max(r-1, 0)
            
            i += 1
            # print(tot)
            # print(lheap)
            # print(rheap)
            # print()

        while i < k:
            if lheap:
                tot += heapq.heappop(lheap)[0]
                i += 1
            else:
                tot += heapq.heappop(rheap)[0]
                i += 1
        return tot