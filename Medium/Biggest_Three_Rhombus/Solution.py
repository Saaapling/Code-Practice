import math

class Solution:

    """
        Problem: https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/
        Time Taken: 75 min
        Comments: The formula / thought process was correct, the implementation was a disaster
            - Tried 'optimizing' by checking only the 3 largest perimeter squares (this is wrong)
            - Tried exiting out of the for 'k' loop early (under the above assumpting that bigger perimeter = bigger sum), this is wrong
            - Confused the formula to calculate the sum, double counting certain numbers, then tried removing 'left_sum', this is - obviously - wrong
            - Pepega brain
    """

    def check_sum(self, value):
        if value in self.sums:
            return

        if value < self.sums[2]:
            return
        
        if value < self.sums[1]:
            self.sums[2] = value
            return
        
        if value < self.sums[0]:
            self.sums[2] = self.sums[1]
            self.sums[1] = value
            return

        self.sums[2] = self.sums[1]
        self.sums[1] = self.sums[0]
        self.sums[0] = value
        return

    def getBiggestThree(self, grid: list[list[int]]) -> list[int]:
        self.sums = [0, 0, 0]

        m = len(grid[0])
        n = len(grid)
        left_sum = [[0]*m for i in range(n)]
        right_sum = [[0]*m for i in range(n)]

        for i in range(m):
            left_sum[0][i] = grid[0][i]
            right_sum[0][i] = grid[0][i]

        for i in range(n):
            right_sum[i][0] = grid[i][0]
            left_sum[i][m-1] = grid[i][m-1]

        for i in range(1, n):
            for j in range(1, m):
                right_sum[i][j] = grid[i][j] + right_sum[i-1][j-1]
                left_sum[i][j-1] = grid[i][j-1] + left_sum[i-1][j]
        
        for i in range(0, n):
            for j in range(0, m):
                max_width = min(m-j-1, j)
                max_height = math.floor((n-i-1)/2)
                max_len = min(max_width, max_height)

                for k in range(max_len, 0, -1):
                    sum = right_sum[i+k][j+k]
                    if (i > 0):
                        sum -= right_sum[i-1][j-1]
                    sum += right_sum[i+2*k][j]
                    if (j - k > 0):
                        sum -= right_sum[i+k-1][j-k-1]

                    sum += left_sum[i+k-1][j-k+1] - left_sum[i][j]
                    sum += left_sum[i+2*k-1][j+1] - left_sum[i+k][j+k]

                    self.check_sum(sum)
                    print(sum)

                self.check_sum(grid[i][j])

        while 0 in self.sums:
            self.sums.remove(0)

        return self.sums

test = Solution()
input = [[4,5,3],[1,1,2],[1,3,4]]
result = test.getBiggestThree(input)
print(result)