from collections import defaultdict

class Solution:
    
    """
        Problem: https://leetcode.com/problems/maximum-score-of-a-node-sequence/
        Comments:
            - Initial Thoughts:
                - DFS + prefix sum + seen array
                    - Think this doesn't really work
                - Directed graph, point from low -> high, keep arr of max pre_sum up to 4
                    - Doesn't work, directing graph causes issues when a larger val is the start of sequence
                - Discard edges (doesn't matter order of discard), maintain seq_maximum up to 4
                    - Going to attempt this
                - Build max len(2), then 3, then 4?
            - Post Submission:
                - Optimal solution is O(Edges)
                - Look at the middle two nodes of the sequence, then find the maximum two non-duplicate edges nodes
                    - Can keep an adj_lst of just the 3 largest neighbors as an optimization
                - https://leetcode.com/problems/maximum-score-of-a-node-sequence/discuss/1953669/Python-Explanation-with-pictures-top-3-neighbors.
    """
    
    def maximumScore(self, scores: list[int], edges: list[list[int]]) -> int:
        n = len(scores)
        adj_lst = defaultdict(lambda: set())
        
        for lst in edges:
            adj_lst[lst[0]].add(lst[1])
            adj_lst[lst[1]].add(lst[0])

        v_arr = [[0 for _ in range(4)] for _ in range(n)]
        s_arr = [[set() for _ in range(4)] for _ in range(n)]

        for i in range(n):           
            v_arr[i][0] = scores[i]
            s_arr[i][0] = {i}
        
        def propogate(i):
            
            for ngbr in adj_lst[i]:
                if ngbr > i:
                    break
                    
                # print(str(i) + ": " + str(ngbr))
                # 4 node sequences:
                if len(s_arr[i][0].union(s_arr[ngbr][2])) == 4:
                    if v_arr[ngbr][3] < v_arr[ngbr][2] + scores[i]:
                        v_arr[ngbr][3] = v_arr[ngbr][2] + scores[i]
                        s_arr[ngbr][3] = s_arr[ngbr][2].union({i})
                if len(s_arr[i][1].union(s_arr[ngbr][1])) == 4:
                    if v_arr[ngbr][3] < v_arr[ngbr][1] + v_arr[i][1]:
                        v_arr[ngbr][3] = v_arr[ngbr][1] + v_arr[i][1]
                        s_arr[ngbr][3] = s_arr[ngbr][1].union(s_arr[i][1])
                if len(s_arr[i][2].union(s_arr[ngbr][0])) == 4:
                    if v_arr[ngbr][3] < v_arr[ngbr][0] + v_arr[i][2]:
                        v_arr[ngbr][3] = v_arr[ngbr][0] + v_arr[i][2]
                        s_arr[ngbr][3] = s_arr[ngbr][0].union(s_arr[i][2])               
                        
                # 3 node sequences
                if v_arr[ngbr][2] == 0:
                    v_arr[ngbr][2] = v_arr[i][2]
                    s_arr[ngbr][2] = s_arr[i][2].union({})
                    propogate(ngbr)
                else:
                    if len(s_arr[i][0].union(s_arr[ngbr][1])) == 3:
                        if v_arr[ngbr][2] < v_arr[ngbr][1] + scores[i]:
                            v_arr[ngbr][2] = v_arr[ngbr][1] + scores[i]
                            s_arr[ngbr][2] = s_arr[ngbr][1].union({i})
                            propogate(ngbr)
                    if len(s_arr[i][1].union(s_arr[ngbr][0])) == 3:
                        if v_arr[ngbr][2] < v_arr[ngbr][0] + v_arr[i][1]:
                            v_arr[ngbr][2] = v_arr[ngbr][0] + v_arr[i][1]
                            s_arr[ngbr][2] = s_arr[ngbr][0].union(s_arr[i][1])
                            propogate(ngbr)
                
                
                # 2 node sequence
                if v_arr[ngbr][1] < scores[i]:
                    v_arr[ngbr][1] = v_arr[ngbr][0] + scores[i]
                    s_arr[ngbr][1] = s_arr[ngbr][0].union({i})
                    propogate(ngbr)
        
        for i in range(n):
            propogate(i)
            for ngbr in adj_lst[i]:
                if ngbr < i:
                    continue
                
                # 4 node sequences:
                if len(s_arr[i][0].union(s_arr[ngbr][2])) == 4:
                    if v_arr[ngbr][3] < v_arr[ngbr][2] + scores[i]:
                        v_arr[ngbr][3] = v_arr[ngbr][2] + scores[i]
                        s_arr[ngbr][3] = s_arr[ngbr][2].union({i})
                if len(s_arr[i][1].union(s_arr[ngbr][1])) == 4:
                    if v_arr[ngbr][3] < v_arr[ngbr][1] + v_arr[i][1]:
                        v_arr[ngbr][3] = v_arr[ngbr][1] + v_arr[i][1]
                        s_arr[ngbr][3] = s_arr[ngbr][1].union(s_arr[i][1])
                if len(s_arr[i][2].union(s_arr[ngbr][0])) == 4:
                    if v_arr[ngbr][3] < v_arr[ngbr][0] + v_arr[i][2]:
                        v_arr[ngbr][3] = v_arr[ngbr][0] + v_arr[i][2]
                        s_arr[ngbr][3] = s_arr[ngbr][0].union(s_arr[i][2])               
                        
                # 3 node sequences
                if len(s_arr[i][0].union(s_arr[ngbr][1])) == 3:
                    if v_arr[ngbr][2] < v_arr[ngbr][1] + scores[i]:
                        v_arr[ngbr][2] = v_arr[ngbr][1] + scores[i]
                        s_arr[ngbr][2] = s_arr[ngbr][1].union({i})
                if len(s_arr[i][1].union(s_arr[ngbr][0])) == 3:
                    if v_arr[ngbr][2] < v_arr[ngbr][0] + v_arr[i][1]:
                        v_arr[ngbr][2] = v_arr[ngbr][0] + v_arr[i][1]
                        s_arr[ngbr][2] = s_arr[ngbr][0].union(s_arr[i][1])
                
                
                # 2 node sequence
                if v_arr[ngbr][1] < scores[i]:
                    v_arr[ngbr][1] = v_arr[ngbr][0] + scores[i]
                    s_arr[ngbr][1] = s_arr[ngbr][0].union({i})
                
                
            # print(i)
            # for i in range(n):
            #     print(str(i) + ": " + str(v_arr[i]))
            # print()

                               
        ms = -1
        for node in range(n):
            if v_arr[node][3] > 0:
                ms = max(ms, v_arr[node][3])
            
        return ms
