# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    """
        Problem: https://leetcode.com/problems/count-complete-tree-nodes/
        Comments:
            - Goal: Find where on the bottom rung that the tree ends
                - Traversing down the tree costs log(n)
                - Using binary search to find element is log(n/2)
                    -> Overal its log(n)^2
    """
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        tot = 0
        curr = root
        level = 0
        while curr:
            tot += 2 ** level
            curr = curr.right
            level += 1

        l = 0
        r = tot
        def traverse(x):
            x += tot + 1
            nodes = []
            while x > 1:
                nodes.append(x%2)
                x >>= 1
            nodes = nodes[::-1]
            curr = root
            for i in range(len(nodes)):
                if nodes[i]:
                    curr = curr.right
                else:
                    curr = curr.left
            
            if curr == None:
                return -1
            else:
                return 1

        found = -1
        while l <= r:
            m = (l+r) // 2
            if traverse(m) > 0:
                found = m
                l = m+1
            else:
                r = m-1

        # print(tot)
        # print(found)
                
        return tot + found + 1