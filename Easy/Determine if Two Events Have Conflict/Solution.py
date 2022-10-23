class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-316/problems/determine-if-two-events-have-conflict/
    """
    
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def cvi(time):
            mins = 0
            mins += 600 * int(time[0])
            mins += 60 * int(time[1])
            mins += int(time[3:5])
            return mins
        
        a = cvi(event1[0])
        b = cvi(event1[1])
        c = cvi(event2[0])
        d = cvi(event2[1])
        # print(a)
        # print(b)
        
        return (b >= c and d >= a)