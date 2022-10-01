from sortedcontainers import SortedList

class Solution:
    
    """
        Problem: https://leetcode.com/problems/longest-increasing-subsequence/
        Comments:
            - Initial Thoughs: DP with O(N^2)
            - Optimal Solutions:
                - Binary Search Method
                - Segment Tree Method
    """
    
    def slow_dp_solution(self, nums):
        n = len(nums)
        dp_arr = [1] * n
        
        for i in range(1, n):
            curr = nums[i]
            max_len = 0
            for j in range(0, i):
                if nums[j] < curr:
                    if dp_arr[j] > max_len:
                        max_len = dp_arr[j]
            dp_arr[i] = max_len + 1

        return max(dp_arr)

    def binary_search_solution(self, nums):
        n = len(nums)
        bis_lis = SortedList()
        bis_lis.add(nums[0])
        
        for i in range(1, n):
            curr = nums[i]
            index = bis_lis.bisect_left(curr)
            if index < len(bis_lis):
                bis_lis.pop(index)
            bis_lis.add(curr)

        return len(bis_lis)

    def binary_search_solution_cleaned(self, nums):
        bis_lis = SortedList()
        
        for i in nums:
            index = bis_lis.bisect_left(i)
            if index < len(bis_lis):
                bis_lis.pop(index)
            bis_lis.add(i)

        return len(bis_lis)

    def lengthOfLIS(self, nums: list[int]) -> int:
        return self.binary_search_solution_cleaned(nums)

test = Solution()
input = [7,7,7,7,7,7,7]
result = test.lengthOfLIS(input)
print(result)