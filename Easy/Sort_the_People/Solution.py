class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-312/problems/sort-the-people/
    """

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heap = []
        h2n = {}
        
        for i in range(len(names)):
            height = heights[i]
            heapq.heappush(heap, -1 * height)
            h2n[height] = names[i]
            
        result = []
        while len(heap) > 0:
            height = heapq.heappop(heap) * -1
            result.append(h2n[height])
            
        return result