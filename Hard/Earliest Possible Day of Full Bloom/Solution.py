class Solution:
    
    """
        Problem: https://leetcode.com/problems/earliest-possible-day-of-full-bloom/
        Comments
            - If plant time > grow time, min time should plant plant-time + minimum grow time
            - If grow time > plant time, plant in reverse growth order?
                [3 3 3 2 2 1]
            - Current idea is O(nlogn) due to sorting, possible to reduce to O(n)?
                - [(1,5), (1,5),(1,5)] -> 3(planting) + 5(growing)
                - [(1,5), (1,2)] -> 2(planting) + 4(growing)
    """
    
    def earliestFullBloom(self, plantTime: list[int], growTime: list[int]) -> int:       
        n = len(plantTime)
        x = []
        for i in range(n):
            x.append((growTime[i],i))
        x.sort(reverse = True)
        # print(x)
        
        rem = 0
        tot = 0
        for i in range(n):
            idx = x[i][1]
            tot += plantTime[idx]
            rem = max(growTime[idx], rem - plantTime[idx])
        tot += rem
        
        return tot