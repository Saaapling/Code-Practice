class Solution:
    
    """
        Problem: https://leetcode.com/contest/biweekly-contest-90/problems/odd-string-difference/
    """

    def oddString(self, words: list[str]) -> str:
        n = len(words[0])
        m = len(words)
        
        da = []
        for i in range(1,n):
            da.append(ord(words[0][i]) - ord(words[0][i-1]))
        
        # print(da)
        
        first = True
        second = []
        sidx = -1
        for i in range(1,m):
            curr = []
            for j in range(1,n):
                curr.append(ord(words[i][j]) - ord(words[i][j-1]))
            for j in range(0,n-1):
                if da[j] != curr[j]:
                    if first:
                        second = curr
                        sidx = i
                        break
                    else:
                        if second:
                            return words[0]
                        else:
                            return words[i]
            if first:
                first = False
            
            if second and i > 1:
                return words[sidx]
                        