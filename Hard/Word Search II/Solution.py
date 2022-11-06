class Solution:
    
    """
        Problem: https://leetcode.com/problems/word-search-ii/
    """
    
    def brute_force(self, board, words):
        m = len(board)
        n = len(board[0])
        wm = set(words)
        
        seen = [[False for _ in range(n)] for _ in range(m)]
        def dfs(i,j,curr):
            nonlocal m
            nonlocal n
            
            seen[i][j] = True
            curr += board[i][j]
            if curr in wm:
                wm.remove(curr)
            
            if len(curr) == 10:
                seen[i][j] = False
                return
            
            if i < m-1 and not seen[i+1][j]:
                dfs(i+1,j,curr)
            if j < n-1 and not seen[i][j+1]:
                dfs(i,j+1,curr)
                
            if i > 0 and not seen[i-1][j]:
                dfs(i-1,j,curr)
            if j > 0 and not seen[i][j-1]:
                dfs(i,j-1,curr)
            
            seen[i][j] = False
            return
        
        for i in range(m):
            for j in range(n):
                dfs(i,j,"")
        
        return set(words) - wm
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        return self.brute_force(board, words)