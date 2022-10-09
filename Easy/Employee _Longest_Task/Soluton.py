class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-314/problems/the-employee-that-worked-on-the-longest-task/
    """
    
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        tl = [0 for _ in range(n)]
        
        prev = 0
        for task in logs:
            time = task[1] - prev
            tl[task[0]] = max(tl[task[0]], time)
            prev = task[1]
                                    
        idx = 0
        mv = 0
        for i in range(n):
            if tl[i] > mv:
                idx = i
                mv = tl[i]
                
        return idx