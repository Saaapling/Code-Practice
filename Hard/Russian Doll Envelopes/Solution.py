from sortedcontainers import SortedList

class Seg_Tree:
    
    def __init__(self, n):
        self.tree = [0 for _ in range(2*n)]
        self.n = n
        
    def add(self, idx, val):
        idx += self.n
        while idx > 0:
            self.tree[idx] = max(self.tree[idx], val)
            idx >>= 1
            
    def get(self, l, r):
        l += self.n
        r += self.n
        
        mv = 0
        while l <= r:
            if l % 2 == 1:
                mv = max(mv, self.tree[l])
                l += 1
            if r % 2 == 0:
                mv = max(mv, self.tree[r])
                r -= 1
            
            l >>= 1
            r >>= 1
        
        return mv
        
class Solution:
    
    """
        Problem: https://leetcode.com/problems/russian-doll-envelopes/
        Comments: 
            - Probably some sort of double sort by height and width (heap)
            - Can dp be used? (m*n = 10^10)
                - But only 10^5 possble states if each state is an envelope
                    - But if index matters, extra 10^5
                - Use pointers on a sorted list
            - Prayge segment tree????
    """
    
    def n_sqrd_soln(self, envelopes):
        n = len(envelopes)
        envelopes.sort()
        
        chain = [1 for _ in range(n)]
        for i in range(n):
            curr = envelopes[~i]
            mv = 1
            for j in range(i):
                pros = envelopes[~j]
                if curr[0] < pros[0] and curr[1] < pros[1]:
                    mv = max(mv, 1 + chain[~j])
            chain[~i] = mv
        
        return max(chain)
    
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        for i in range(len(envelopes)):
            envelopes[i][1] *= -1
        envelopes.sort()
        for i in range(len(envelopes)):
            envelopes[i][1] *= -1
        # print(envelopes)
        
        segtree = Seg_Tree(10**6)
        sl = SortedList()
        sl.add(0)
        for i in range(n):
            curr = envelopes[~i]
            mv = 1
            
            if curr[1] < sl[-1]:
                r = sl[-1]
                l = sl[sl.bisect_right(curr[1])]
                mv += segtree.get(l, r)
                
            sl.add(curr[1])
            segtree.add(curr[1], mv)
            # print(mv)
                        
        return segtree.get(0, 10**5)