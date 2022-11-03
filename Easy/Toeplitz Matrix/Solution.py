class Solution:
    
    """
        Problem: https://leetcode.com/problems/toeplitz-matrix/
    """
    
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
                
                
        return True