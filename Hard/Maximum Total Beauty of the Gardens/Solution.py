from collections import defaultdict

class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-288/problems/maximum-total-beauty-of-the-gardens/
        Comments:
            - Leave 1 plot unfinished if partial >= full
                - Maximize flowers in this plot
            - Always start planting from highest count?
                - Does not work
                - [0,0,0], flowers = 10, target = 5, full = 4, partial = 3
                    - [3,3,3] -> 9
                    - [5,5,0] -> 8
                    - [5,2,2] -> 10
            - Idea: sorted deque, compare val-increase for inc left (++ partial) to filling right (++ full)
                - What about partial k's?
                - [0,0,0,0], flowers = 12, target = 5, full = 4, partial = 3
                    - [5,5,0,0] -> 8
                        - [5,2,2,2] -> 10
                    - [3,3,3,3] -> 9
                    - left = (4,3) vs right (5,4)
                        -> [5,1,1,1]
                        -> left = (3,3) vs right (4,4)
                            - [5,2,2,2] vs [5,5,1,1] -> 10 vs 11
                            - If equal, take bigger value?
                                - if remaining flowers > 2*min, take min. Else, take max
                    - if flowers = 15:
                        - Optimal = [5,5,2,2] -> 14
                            - [5,3,3,3] -> 13
                        - By formula:
                            - [5,0,0,0]
                            - [5,1,1,1]
                            - [5,5,1,1]
                                - left = (2,3) vs right (4,4)
                            - [5,5,2,2]
                - Scenario: full once or inc twice, full > partial
                    - [0,0,0], target = 5, flowers = 6, full = 5, partial = 3
                    - (3,3) vs (5,5)
                        - [5,0,0] vs [2,2,2]
                        
            - Dicussion Page Idea: 
                - Start by maximizing the incomplete garden
                - Decrease incompelete garden by 1, compare the score loss to  increase from full gardens
    """
    
    def failed_iterative(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        x = flowers
        x.sort()
                
        l = 0
        r = len(x) - 1
        
        # Remove already full gardens
        tot = 0
        while r > l and x[r] >= target:
            r -= 1
            tot += full
        
        # Maximize partial gardens
        tot += partial * x[l]
        k = newFlowers
        cost = []
        count = x[l]
        size = 0
        while count < target - 1:
            while l <= r and x[l] == count:
                size += 1
                l += 1
            if size > k:
                break
                
            k -= size
            cost.append(size)
            count += 1
            tot += partial
                
        cost = cost[::-1]
        # print(cost)
        # print(tot)
        # print()
        
        # Fill gardens with remaining k
        while r > 0 and k > (target - x[r]):
            k -= (target - x[r])
            tot += full
            r -= 1
                
        # Create new gardens at the expense of reducing partial gardens
        l = min(l,r)
        for i in cost:
            temp = k + i
            count -= 1
            curr = 0
            while r > 0 and temp >= (target - x[r]):
                temp -= (target - x[r])
                curr += full
                if r == l :
                    l -= 1
                    temp += count - x[r]
                r -= 1
            
            if partial <= curr:
                tot += curr
                tot -= partial
                k = temp
            else:
                count += 1
                break
            
        # If all gardens can be filled, check if its better to leave the last garden as partial
        if r == 0 and k > (target - x[r]):
            if full > (partial * (target - 1)):
                tot += full
                tot -= (partial * (target - 1))
        else:
            # Split the remaining k amongst the remaining incomplete gardens
            print(tot)
            print(k)
            print(l)
            tot += (k // (l+1)) * partial
        
        return tot
    
    
    def guided_soln(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        x = []
        for i in range(len(flowers)):
            x.append(min(target, flowers[i]))
        x.sort()      
        
        # Edge Cases
        if min(x) >= target:
            return full * len(x)
        if newFlowers >= target * len(x) - sum(x):
            return full * (len(x) - 1) + max(full, partial * (target - 1))
          

        # Build cost array
        cost = [0]
        for i in range(1, len(x)):
            cost.append(cost[i-1] + i * (x[i] - x[i-1]))
            
            
        # Remove already full gardens
        n = len(x)
        r = n - 1
        while x[r] >= target:
            r -= 1
            
        # Fill remaining gardens one at a time
        k = newFlowers
        mv = 0
        while k > 0:
            idx = min(r, bisect_right(cost, k) - 1)
            mp = x[idx] + (k - cost[idx]) // (idx + 1)
            mv = max(mv, mp * partial + full * (n - r - 1))
            k -= (target - x[r])
            r -= 1
        
        return mv
    
    def disc_soln(self, A: List[int], new: int, t: int, full: int, part: int) -> int:
        A = [min(t, a) for a in A]
        A.sort()
		
		# Two edge cases
        if min(A) == t: return full * len(A)
        if new >= t * len(A) - sum(A):
            print(full*len(A) - full)
            print(part*(t-1))
            return max(full*len(A), full*(len(A)-1) + part*(t-1))
        
		# Build the array `cost`.
        cost = [0]
        for i in range(1, len(A)):
            pre = cost[-1]
            cost.append(pre + i * (A[i] - A[i - 1]))

		# Since there might be some gardens having `target` flowers already, we will skip them.
        j = len(A) - 1
        while A[j] == t:
            j -= 1
        
		# Start the iteration
        ans = 0
        while new >= 0:
		
			# idx stands for the first `j` gardens, notice a edge case might happen.
            idx = min(j, bisect_right(cost, new) - 1)
			
			# bar is the current minimum flower in the incomplete garden
            bar = A[idx] + (new - cost[idx]) // (idx + 1)
			
            ans = max(ans, bar * part + full *(len(A) - j - 1))
            
			# Now we would like to complete garden j, thus deduct the cost for garden j 
			# from new and move on to the previous(next) incomplete garden!
            new -= (t - A[j])
            j -= 1
                        
        return ans
    
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        return self.guided_soln(flowers, newFlowers, target, full, partial)