class Solution:
    
    """
        Problem: https://leetcode.com/problems/daily-temperatures/
        Initial Thoughts:
            - Could sort the list (nope, not a fan)
            - Monotonically decreasing stack of tuples (temperature, index)
    """
    
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        
        stack = []
        result = [0 for _ in range(n)]
        for i in range(n):
            curr = temperatures[i]
            while stack and stack[-1][0] < curr:
                _, idx = stack.pop()
                result[idx] = i - idx
            stack.append((curr, i))
                
        return result