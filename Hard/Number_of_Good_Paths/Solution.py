from collections import defaultdict, deque

class Solution:

    """
        Problem: https://leetcode.com/contest/weekly-contest-312/problems/number-of-good-paths/
        Comments:
            - Attempted techniques: Adjacency list, Connected Components, Union Find
            - Initial Solution provided by Erik
    """


    # Uses adjacency lists, then iterates max-to-min while removing edges
    def numberOfGoodPaths_TLE(self, vals: list[int], edges: list[list[int]]) -> int:
        n = len(vals)
        adjLst = [set() for _ in range(n)] #map idx to ngbring idxs
        v2i = {}
        fq = {}
        for i, v in enumerate(vals):
            fq[v] = fq.get(v, 0) + 1
            if v in v2i:
                v2i[v].append(i)
            else:
                v2i[v] = [i]
        for x, y in edges:
            adjLst[x].add(y)
            adjLst[y].add(x)
        ccs = set()
        ct = 0
        for v in sorted(set(vals), reverse=True):
            if fq[v] >= 2:
                for i in v2i[v]:
                    if i not in ccs:
                        ccs.add(i)
                        cc = 0
                        bfs = deque([i]) #value or idx???
                        seen = set([i])
                        while bfs:
                            cur = bfs.popleft()
                            if vals[cur] == vals[i]:
                                cc += 1
                                ccs.add(cur)
                            for ngbr in adjLst[cur]: #
                                if vals[ngbr] <= vals[i] and ngbr not in seen:
                                    bfs.append(ngbr)
                                    seen.add(ngbr)
                        ct += (cc * (cc-1)) // 2 
                    for ngbr in adjLst[i]:
                        adjLst[ngbr].remove(i) 
                    adjLst[i] = set()
        return ct + len(vals)


    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:
        n = len(vals)

        adjLst = [set() for _ in range(n)] #map idx to ngbring idxs
        for x, y in edges:
            if vals[x] >= vals[y]:
                adjLst[x].add(y)
            if vals[x] <= vals[y]:
                adjLst[y].add(x)

        v2i = defaultdict(lambda:[])
        for i, v in enumerate(vals):
            v2i[v].append(i)

        union_find_arr = list(range(n))
        def traverse(a):
            while union_find_arr[a] != a:
                a = union_find_arr[a]
            return a

        def compare(a, b):
            idx_a = traverse(a)
            idx_b = traverse(b)
            val_a = vals[idx_a]
            val_b = vals[idx_b]

            if val_a < val_b:
                union_find_arr[idx_b] = idx_a
            elif val_a > val_b:
                union_find_arr[idx_a] = idx_b
            else:
                if idx_a < idx_b:
                    union_find_arr[idx_b] = idx_a
                else:
                    union_find_arr[idx_a] = idx_b

        total = 0
        for v in sorted(set(vals)):
            for i in v2i[v]:
                for ngbr in adjLst[i]:
                    compare(i, ngbr)
   
            end_idx = defaultdict(lambda:0)
            for i in v2i[v]:
                end_idx[traverse(i)] += 1

            for idx in end_idx:
                cc_count = end_idx[idx]
                total += (cc_count * (cc_count-1)) // 2

        return total + len(vals)

test = Solution()
vals = [2,5,5,1,5,2,3,5,1,5]
edges = [[0,1],[2,1],[3,2],[3,4],[3,5],[5,6],[1,7],[8,4],[9,7]]
result = test.numberOfGoodPaths(vals, edges)
print(result)