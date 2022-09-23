class Solution:

    """
        Problem: https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/
        Time Taken:
        Comments: 
            - Initial Solution: Has to be some form of DP
                - dp_array[n][m]
                - dp[i][j] where (i < k) = 0
                - dp[i][j] where (m < k) = 0
                - dp[k][k] = 1
                - dp[1][m] = m (if k = 1)
    """

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        return

test = Solution()
n = 2
m = 3
k = 1
result = test.numOfArrays(n,m,k)
print(result)