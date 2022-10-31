# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-317/problems/height-of-binary-tree-after-subtree-removal-queries/
        
        # Backtracking (TLE)
        def get_height(x):
            diff = height[x]
            cv = x
            cn = v2n[cv]
            cp = parent[cv]
            while cp:
                cp = v2n[cp]

                left = 0
                right = 0
                if cp.left:
                    left = height[cp.left.val]
                    if cp.left.val == cv:
                        left -= diff
                    
                if cp.right:
                    right = height[cp.right.val]
                    if cp.right.val == cv:
                        right -= diff
                        
                # No affect on max height
                diff = height[cp.val] - max(left,right) - 1
                if diff == 0:
                    return height[root.val] - 1
                
                cv = cp.val
                cn = v2n[cv]
                cp = parent[cv]
                    
            return height[root.val] - diff - 1
        
        
        m = len(queries)
        ans = [-1 for _ in range(m)]
        for i in range(m):
            ans[i] = get_height(queries[i])
            
        return ans
    """
    
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        parent = {}
        height = {} 
        v2n = {}
        
        # Initial DFS
        def init_dfs(node):
            v2n[node.val] = node
            
            left = 0
            right = 0
            if node.right:
                parent[node.right.val] = node.val
                init_dfs(node.right)
                right = height[node.right.val]
            if node.left:
                parent[node.left.val] = node.val
                init_dfs(node.left)
                left = height[node.left.val]
            
            height[node.val] = 1 + max(left,right)
            
        parent[root.val] = None
        init_dfs(root)

        
        diff = {}
        def set_0_dfs(node, val = 0):
            if node == None:
                return
            
            diff[node.val] = val
            set_0_dfs(node.right)
            set_0_dfs(node.left)
            
        def sec_dfs(node,mv,h=1):    
            # print(mv)
            left = 0
            right = 0
            if node.right:
                right = height[node.right.val]
            if node.left:
                left = height[node.left.val]
                
            if left == right:
                set_0_dfs(node.right)
                set_0_dfs(node.left)
            elif left > right:
                x = left - right
                if height[root.val] - x > mv:
                    diff[node.left.val] = x
                else:
                    diff[node.left.val] = height[root.val] - mv
                mv = max(mv, right+h)
                sec_dfs(node.left, mv, h+1)
                
                set_0_dfs(node.right)
            else:                
                x = right - left
                if height[root.val] - x > mv:
                    diff[node.right.val] = x
                else:
                    diff[node.right.val] = height[root.val] - mv
                mv = max(mv, left+h)
                sec_dfs(node.right, mv, h+1)
                
                set_0_dfs(node.left)
                
        sec_dfs(root, 0)
        # print(diff)
                
        m = len(queries)
        ans = [-1 for _ in range(m)]
        root_height = height[root.val] - 1
        for i in range(m):
            ans[i] = root_height - diff[queries[i]]
            
        return ans
