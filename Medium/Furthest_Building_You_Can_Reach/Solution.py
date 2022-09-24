import heapq

class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-213/problems/furthest-building-you-can-reach/
        Time Taken: ~20 min
        Comments: 
            - DP is a possible solution, but potentially too slow (3 state variables, worse case n^3)
    """
    
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        heap = []
        
        for i in range(0, len(heights) - 1):
            diff = heights[i+1] - heights[i]
            
            if diff <= 0:
                continue
            
            heapq.heappush(heap, diff * -1)
            if diff > bricks:
                if ladders > 0:
                    if len(heap) > 0:
                        bricks += (-1 * heapq.heappop(heap)) - diff
                        ladders -= 1
                else:
                    return i
            else:
                bricks -= diff
                

        return len(heights) - 1
        