class Solution:
    
    def countTime(self, time: str) -> int:
        tot = 0
        
        # Hours
        if time[0] == "?":
            if time[1] == "?":
                tot = 24
            elif ord(time[1]) <= ord("3"):
                tot = 3
            else:
                tot = 2
        elif time[1] == "?":
            if ord(time[0]) <= ord ("1"):
                tot = 10
            else:
                tot = 4
        
        # print(tot)
                
        # Minutes
        mult = 1
        if time[3] == "?":
            if time[4] == "?":
                mult = 60
            else:
                mult = 6
        elif time[4] == "?":
            mult = 10
        
#         print(mult)
#         print()
            
        if tot > 0:
            return tot * mult
        else:
            return mult