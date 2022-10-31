class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-317/problems/minimum-addition-to-make-integer-beautiful/
        Comments: DP?
    """
    
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def get_sum(x):
            tot = 0
            for i in str(x):
                tot += int(i)
            return tot
        
        power = 1
        curr = n
        while get_sum(curr) > target:
            curr += 10**power - curr % 10**power
            power += 1
            
        return curr - n