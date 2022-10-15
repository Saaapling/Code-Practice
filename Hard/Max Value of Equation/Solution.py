import heapq
from collections import deque

class Solution:
    
    """
        Problem: https://leetcode.com/problems/max-value-of-equation/
        Comments:
            - Ex: [(1,3),(2,2),(3,1),(4,3)] k = 2
                - heap: [(1,4)]?
                    - [(1,5),(2,3)]
                    - [(1,6), (2,3), (3, 2)]
            - Ex: [(1:3),(2:1),(3,4),(4,1)] k =3
                - max = 7 (1,4), not 6 (3,4)
                
            - Thoughts: Use a heap with values: (index, 'supposed value')
                - where the 'supposed value' is y + (n - idx - 1)
                - this is the value of the last element would see from the first element (if its a valid pair)
                - remove elements from heap when no longer valid
                
            - Optimal Solution: Use a monotonic queue to get O(n) runtime
                - Key thought: new 'larger' elements are *always* better than previous 'smaller' elements
                    if we iterate from smallest to largest index
    """
    
    
    def monotonic_queue_soln(self, points, k):
        n = len(points)
        mq = deque()
        
        mv = -1 * 10 ** 9
        for x, y in points:
            while mq and x - mq[0][1] > k:
                mq.popleft()
                
            if mq:
                mv = max(mv, x+y+mq[0][0]-n)
                
            while mq and y+n-x >= mq[-1][0]:
                mq.pop()
                
            mq.append((y+n-x, x))
            # print(mq)
            # print(mv)
            
        return mv
    
    def heap_soln(self, points: list[list[int]], k: int) -> int:
        n = len(points)
        heap = []
        
        mv = -1 * 10 ** 9
        for x, y in points:
            while heap and x - heap[0][1] > k:
                heapq.heappop(heap)
                
            if heap:
                if y + (-1 * heap[0][0]) - (n - heap[0][1] - 1) + (x - heap[0][1]) > mv:
                    mv = y + (-1 * heap[0][0]) - (n - heap[0][1] - 1) + (x - heap[0][1])
                
            
            heapq.heappush(heap, (-1 * (y + (n - x - 1)), x))
            # print(heap)
        
        return mv
    
    def findMaxValueOfEquation(self, points: list[list[int]], k: int) -> int:
        return self.monotonic_queue_soln(points, k)