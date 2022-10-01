import heapq

class Solution:
    
    """
        Problem: https://leetcode.com/problems/the-skyline-problem/
        Comments:
            - Initial thoughts: Stacks and Heaps
                - One Heap for building height
                - Stack for start/ends of buildings (no longer keep ends)
                    - No longer need a stack, since its already sorted
                - Potential Issue: heap removal is O(n) to find the target to remove, log(n) for the actual removal
                    - Fix: why remove if not head?
                    - Check head, remove if no longer relevant
                - Steps: 
                    - Get next element from array
                    - Peek heap head, fill in skylines_result with value
                        - Pop element from heap if building ends and repeat
                    - Add building to heap
    """
    
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        # Initial States
        height_heap = []
        skylines = [[0,0]]

        def construct_skyline(x, height):
            nonlocal skylines
            prev = skylines[-1]
            if height != prev[1]:
                skylines.append([x, height])
        
        x = 0
        for i in range(len(buildings)):
            curr = buildings[i]
            while x < curr[0]:
                # print(curr[0])
                # print(x)
                # print(height_heap)
                if height_heap:
                    height, end = height_heap[0]
                    if end <= x:
                        heapq.heappop(height_heap)
                        continue
                        
                    if end >= curr[0]:
                        construct_skyline(x, height * -1)
                        x = curr[0]
                    else:
                        construct_skyline(x, height * -1)
                        x = end
                        heapq.heappop(height_heap)
                else:
                    construct_skyline(x, 0)
                    x = curr[0]
                
            heapq.heappush(height_heap, (curr[2] * -1, curr[1]))
            
        # Sort out remaining buildings
        while height_heap:
            height, end = height_heap[0]
            if end > x:
                construct_skyline(x, height * -1)
                x = end

            heapq.heappop(height_heap)
        
        # Add the last element and remove the first element
        skylines.append([x, 0])
        skylines.pop(0)

        return skylines

test = Solution()
buildings = [[4,9,10],[4,9,15],[4,9,12],[10,12,10],[10,12,8]]
result = test.getSkyline(buildings)
print(result)