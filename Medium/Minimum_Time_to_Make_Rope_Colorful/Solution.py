class Solution:
    
    """
        Problem: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
        Comments:
            - Initial Thoughts: Greedily remove balloons
    """
    
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        
        prev = 0
        for i in range(1, len(colors)):
            if colors[prev] == colors[i]:
                if neededTime[prev] > neededTime[i]:
                    total += neededTime[i]
                else:
                    total += neededTime[prev]
                    prev = i
            else:
                prev = i
                        
        return total