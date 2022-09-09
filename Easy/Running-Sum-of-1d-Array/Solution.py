class Solution:

    """
        Problem: https://leetcode.com/problems/running-sum-of-1d-array/
        Time Taken: 2 minutes
    """

    def naive_solution(self, nums):
        result = []
        sum = 0
        for x in nums:
            sum += x
            result.append(sum)
        return result

    def runningSum(self, nums: list[int]) -> list[int]:
        return self.naive_solution(nums)


test = Solution()
result = test.runningSum([1,2,3,4])
print(result)