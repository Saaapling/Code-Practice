class SegmentTree:
    
    def __init__(self, n):
        self.n = n
        self.tree = [0 for _ in range(n*2)]

    def add(self, idx, val):
        idx += self.n
        self.tree[idx] = val
        
        while idx >> 1 > 0:
            idx >>= 1
            self.tree[idx] = max(self.tree[idx], val)
            
    def get(self, right):
        left = self.n
        right += self.n
        
        mv = 0
        while left <= right:
            if left % 2 == 1:
                mv = max(mv, self.tree[left])
                left += 1
            if right % 2 == 0:
                mv = max(mv, self.tree[right])
                right -= 1
            left >>= 1
            right >>= 1
            
        return mv
        
class Solution:
    
    """
        Problem:
        Comments:
            - Initial Thoughts:
                - DP (Given)
                - Store sorted lists?
                - Ex: [2, 100], [90, 101], [101,102],[10,20], [21,31], [32,42]
                    - Sorted: [2, 100], [10,20], [21,31], [32,42], [90, 101], [101,102]
                    - Best: [10,20], [21,31], [32,42], [90, 101]
                - Brute Force?: Sort List, then maintain all possible chains of pairs
    """
    
    
    def seg_tree_nlogn(self, pairs):
        seg_tree = SegmentTree(3000)
        
        pairs.sort()
        for pair in pairs:
            best = seg_tree.get(pair[0] + 1500 - 1)
            seg_tree.add(pair[1] + 1500, best + 1)
                        
        # Does seg_tree.tree[1] work??
        return seg_tree.tree[1]
    
    def brute_force_n_squared(self, pairs):
        pairs.sort()
        
        pc = []
        for pair in pairs:
            best = 1
            for i in range(len(pc)):
                if pair[0] > pc[i][0]:
                    best = pc[i][1] + 1
            pc.append((pair[1], best))
            
        best = 0
        for i in range(len(pc)):
            best = max(best, pc[i][1])
            
        return best
    
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        return self.seg_tree_nlogn(pairs)
