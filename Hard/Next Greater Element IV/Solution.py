from sortedcontainers import SortedList

class Solution:
    
    """
        Problem: https://leetcode.com/contest/biweekly-contest-90/problems/next-greater-element-iv/
    """
    
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sl = SortedList()
        
        ret = [-1 for _ in range(n)]
        for i in range(n):
            idx = sl.bisect_left((nums[i],0,0))
            j = 0
            # print(idx)
            # print(sl)
            while j < idx:
                if sl[j][2] == 1:
                    ret[sl[j][1]] = nums[i]
                    del sl[j]
                    idx -= 1
                    continue
                sl.add((sl[j][0],sl[j][1],1))
                del sl[j]
                j += 1
            # print(ret)
                
            sl.add((nums[i],i,0))

        return ret