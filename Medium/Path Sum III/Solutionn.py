from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    """
        Problem: https://leetcode.com/problems/path-sum-iii/?envType=study-plan&id=level-3
        Comments: 
            - Store x
            - search for (x-k)
    """
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ps = defaultdict(lambda: 0)
        ps[0] = 1
        
        count = 0
        def aux(node, prev):
            if not node:
                return
            
            nonlocal count
            curr = prev + node.val
            count += ps[curr-targetSum]
            ps[curr] += 1

            aux(node.left, curr)
            aux(node.right, curr)
            
            ps[prev + node.val] -= 1
            
        aux(root, 0)
        return count