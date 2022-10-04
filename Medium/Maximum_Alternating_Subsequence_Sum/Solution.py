class Solution:
    
    """
        Problem: https://leetcode.com/problems/maximum-alternating-subsequence-sum/
        Comments:
            - Initial Thoughts:
                - Is Iterative DP a possible solution?
                    - Given the MAS of a subsequence, the new MAS is either to 
                        - 'replace' the last element
                        - 'add' two elements
                        - not quite covering all cases here mayber
                    - Keep track of last 'unadded' element to the right of the last added element
                        - Will never add an element before the last added element because it will flip the signs,
                            resulting in a net negative up to the point your new number is added
                        - [a,c,b,d,e], new number f:
                        - f - (b - d + e) + g v/s f - (some val < e)
                            - (f - e) - (b-d) v/s f - (some val < e)
                            - (f - e) < f - (some val < e), and (b-d) > 0
                
    """
    
    def maxAlternatingSum_2(self, nums: list[int]) -> int:
        altsum = nums[0]
        
        for i in range(1, len(nums)):
            altsum += max(0, nums[i] - nums[i-1])
        
        return altsum
    
    def maxAlternatingSum(self, nums: list[int]) -> int:
        altsum = nums[0]
        prev = nums[0]
        
        for i in range(1, len(nums)):
            curr = nums[i]
            if curr > prev:
                altsum += (curr - prev)
            prev = curr
        
        return altsum