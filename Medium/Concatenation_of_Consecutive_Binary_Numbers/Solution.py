import math

class Solution:

    """
        Problem: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/submissions/
        Time Taken: 7 min
    """

    def concatenatedBinary_shortened(self, n)
        M = 10**9 + 7
        dp = 1

        for i in range(2, n+1):
            dp = ((dp << (math.floor(math.log2(i)) + 1)) + i) % M

        return dp

    def concatenatedBinary(self, n: int) -> int:
        M = 10**9 + 7
        dp = 1

        for i in range(2, n+1):
            dp <<= (math.floor(math.log2(i)) + 1)
            dp %= M
            dp = (dp + i) % M

        return dp
        

test = Solution()
input = 10 ** 5
result = test.concatenatedBinary(input)
print(result)