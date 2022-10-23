from math import gcd
class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-316/problems/number-of-subarrays-with-gcd-equal-to-k/
        Comments:
            - Ended up doing brute force O(n^2)
            - Better solution: https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/discuss/2734123/O(N*logN)-and-O(N*N)-Solutions
    """
    
    def incorrect_factoring(self, nums):
        total = 0

        start = 0
        right = -1
        for idx, i in enumerate(nums):
            if i % k == 0:
                if i == k:
                    right = idx
                if right >= 0:
                    total += right-start+1
            else:
                start = idx + 1
                right = -1
                
            # print("Total: " + str(total))
                                
        return total
    
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        total = 0

        start = 0
        for idx, curr in enumerate(nums):
            if curr % k == 0:
                for i in range(start, idx+1):
                    # print(nums[i:idx+1])
                    if gcd(*nums[i:idx+1]) == k:
                        total += 1
            else:
                start = idx + 1
            # print(total)
                                
        return total