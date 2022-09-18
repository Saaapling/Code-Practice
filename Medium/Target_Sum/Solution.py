from collections import defaultdict

class Solution:

    """
        Problem: https://leetcode.com/problems/target-sum/
        Time Taken: 5 min (implementation, thought about the problem away from PC)
        Comments: 
            - Naive Solution: Keep dict of (sum, count) [Is this dp?]
            - Post Submission: Both runtime and memory are supposedly very good for this solution
    """

    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp_arr = defaultdict(lambda: 0)
        dp_arr[0] = 1

        for x in nums:
            result_arr = defaultdict(lambda: 0)
            for i in dp_arr:
                result_arr[i + x] += dp_arr[i]
                result_arr[i - x] += dp_arr[i]
            dp_arr = result_arr
            print(dp_arr)

        return dp_arr[target]

test = Solution()
nums = [1]
target = 1
result = test.findTargetSumWays(nums, target)
print(result)