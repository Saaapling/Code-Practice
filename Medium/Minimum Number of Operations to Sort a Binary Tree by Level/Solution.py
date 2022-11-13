from collections import defaultdict
from sortedcontainers import SortedList

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-319/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/
        Comments:
            - Seperate problems by level
            - For each level, compile numbers, sort to get intended order, then do connected components to count swaps (bin-search)
                - Get levels arrays through dfs
    """
    
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(lambda: [])
        
        def dfs(node, level):
            levels[level].append(node.val)
            
            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)
                
        dfs(root, 0)
        
        tot = 0
        for arr in levels.values():
            x = SortedList(arr)
            
            n = len(arr)
            for i in range(n):
                while arr[i] != x[i]:
                    tot += 1
                    idx = x.bisect_left(arr[i])
                    temp = arr[i]
                    arr[i] = arr[idx]
                    arr[idx] = temp
            # print(arr)
            
        return tot
