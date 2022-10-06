class Solution:
    
    """
        Problem: https://leetcode.com/problems/minimum-height-trees/description/
        Comments: 
            - Initial Thoughts: 
                - DFS as a possible technique
                    - Brute force DFS's down each starting node
                    - Keep track of sub-minimums as you DFS, and only retry those with <= minimum
                - Is there a way to do this while only traversing each edge once?
                    - DFS once, keep greedy minimum (not accounting for other sub-paths)
                    - DFS again, with updated values from other subpaths
                    - This doesn't really work. Would need to DFS again with each recursive call
            - Post submission thoughts:
                - Brute force failed, as expected, used the given solution
                - An important idea is that there are maximum of 2 nodes with minimum height
                    - Was able to figure this out, but did not know what to do from it
                - Trim leaf nodes until you reach the center
    """
    
    def brute_force_dfs(self, n: int, edges: list[list[int]]) -> list[int]:
        h = [0 for _ in range(n)]
        
        # Adjacency List
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
            
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
            
        # print(adj_list)
        def dfs(i, d):
            seen[i] = True
            
            max_edge = 0
            for ngbr in adj_list[i]:
                if not seen[ngbr]:
                    max_edge = max(max_edge, dfs(ngbr, d+1))

            h[i] = max(h[i], max(d, max_edge))
            return 1 + max_edge
            
        for i in range(n):
            seen = [False for _ in range(n)]
            dfs(i, 0)

        min_h = min(h)
        result = []
        for i in range(n):
            if min_h == h[i]:
                result.append(i)
        
        return result
        
    
    def provided_leaf_trim_solution(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        # Build the graph with the adjacency list
        adj_list = [set() for i in range(n)]
        for start, end in edges:
            adj_list[start].add(end)
            adj_list[end].add(start)

        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(adj_list[i]) == 1:
                leaves.append(i)

        # Trim the leaves until reaching the centroids
        remaining = n
        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = []
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                # the only neighbor left for the leaf node
                ngbr = adj_list[leaf].pop()
                # remove the only edge left
                adj_list[ngbr].remove(leaf)
                if len(adj_list[ngbr]) == 1:
                    new_leaves.append(ngbr)

            # prepare for the next round
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph
        return leaves
    
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        return self.provided_leaf_trim_solution(n, edges)