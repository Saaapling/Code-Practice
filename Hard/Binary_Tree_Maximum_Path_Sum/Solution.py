from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    
    
    """
        Problem: https://leetcode.com/problems/binary-tree-maximum-path-sum/
        Comments: 
            Initial Thoughts: Recursive Aux Call
    """

    def maxSumAux(self, root):
        if not root:
            return 0
                
        left = self.maxSumAux(root.left)
        right = self.maxSumAux(root.right)
        
        max_sum = max(root.val, root.val + max(0, left) + max(0, right))
        if max_sum > self.max:
            self.max = max_sum
        
        return max(0, max(root.val, root.val + max(left, right)))    
    
    def maxSumAux_original(self, root):
        max_sum = root.val
        max_path = root.val
        
        if root.left:
            left = self.maxSumAux(root.left)
        else:
            left = 0
            
        if root.right:
            right = self.maxSumAux(root.right)
        else:
            right = 0
        
        
        total = left + right + max_sum
        left_sum = left + max_sum
        right_sum = right + max_sum
        max_sum = max([max_sum, left_sum, right_sum, total])
        if max_sum > self.max:
            self.max = max_sum
        
        max_path = max(max_path, max_path + max(left, right))
        return max(0, max_path)
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = -1001
        self.maxSumAux(root)
        return self.max