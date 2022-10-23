from sortedcontainers import SortedList

class Solution:
    
    """
        Problem: https://leetcode.com/contest/biweekly-contest-40/problems/minimum-number-of-removals-to-make-mountain-array/
        Comments:
            - Initial Thoughts: (LIS courtesy of se7enn)
                - Main two LIS (longest increasing subsequence)
                    - One from start gonig forward
                    - One from end going backwards
                - Make each index a peak
                    - Operations = (i - flis[i-1]) + ((n-i) - blis[i+1])
    """
    
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        n = len(nums)
        
        flis = [0 for _ in range(n)]
        blis = [0 for _ in range(n)]
        
        sl = SortedList()
        for i in range(n):
            curr = nums[i]
            index = sl.bisect_left(curr)
            if index < len(sl):
                sl.pop(index)
            sl.add(curr)
            flis[i] = (len(sl), sl[-1])
        
        sl = SortedList()
        for i in range(1,n+1):
            curr = nums[-i]
            index = sl.bisect_left(curr)
            if index < len(sl):
                sl.pop(index)
            sl.add(curr)
            blis[-i] = (len(sl), sl[-1])
            
        # print(flis)
        # print(blis)
            
        start = 1
        while nums[start] <= nums[start-1]:
            start += 1
        end = n-1
        while nums[end-1] <= nums[end]:
            end -= 1
            
        mv = 10 ** 6
        for i in range(start, end):
            soln = (i - flis[i-1][0]) + ((n-i-1) - blis[i+1][0])
            if nums[i] <= flis[i-1][1] and nums[i] <= blis[i+1][1]:
                soln += 1
                if flis[i-1][1] == blis[i+1][1]:
                    soln += 1
            elif flis[i-1][1] == nums[i] or nums[i] == blis[i+1][1]:
                soln += 1
            # print(soln)
            mv = min(mv, soln)
            
        return mv