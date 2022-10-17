class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-315/problems/sum-of-number-and-its-reverse/
        Comments:
            - Must be some formula:
                - x = abcd + dcba
                - One numer has to at least >= num // 2
    """
    
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num == 0:
            return True
        
        # Do the dumb way
        for i in range(num//2, num):
            if i + int(str(i)[::-1]) == num:
                return True
            
        return False
