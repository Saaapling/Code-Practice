class Solution:
    
    """
        Problem: https://leetcode.com/contest/biweekly-contest-40/problems/maximum-repeating-substring/
        Comments:
            - Wasn't able to find optimal solution, used naive O(mn) time solution
            - Optimal Algorithm: Knuth-Morris-Pratt (KMP)
                - https://www.youtube.com/watch?v=V5-7GzOfADQ
                - https://towardsdatascience.com/pattern-search-with-the-knuth-morris-pratt-kmp-algorithm-8562407dba5b
                - Algorithm needs to be adapted to allow for repeats, for sake of time, I chose dumbest method
    """
    
    def incorrect_greedy(self, sequence, word):
        m = len(word)
        slen = 0
        
        idx = 0
        mv = 0
        for char in sequence:
            if char == word[idx]:
                idx = (idx + 1) % m
                if idx == 0:
                    slen += 1
                mv = max(mv, slen)
            else:
                idx = 0
                slen = 0
                
        return mv
    
    def brute_force(self, sequence, word):
        
        def aux(seq, word, start):
            m = len(word)
            slen = 0

            idx = 0
            for i in range(start, len(seq)):
                char = seq[i]
                if char == word[idx]:
                    idx = (idx + 1) % m
                    if idx == 0:
                        slen += 1
                else:
                    return slen
            return slen
        
        mv = 0
        for i in range(len(sequence)):
            length = aux(sequence, word, i)
            mv = max(mv, length)
            
        return mv
    
    def kmp_soln(self, seq, word):
        m = len(word)
        lps = [0 for _ in word]
        
        idx = 0
        for i in range(1, m):
            if word[i] == word[idx]:
                idx += 1
                lps[i] = idx
            else:
                while idx > 0 and word[i] != word[idx]:
                    idx = lps[idx - 1]
                    
        # print(lps)
    
        idx = 0
        match = []
        for i in range(len(seq)):
            char = seq[i]
            while idx > 0 and char != word[idx]:
                idx = lps[idx - 1]
                slen = 0
            
            if char == word[idx]:
                idx += 1
                if idx == m:
                    match.append(i)
                    idx = lps[idx - 1]
                    
        # print(match)

        mv = 0
        mset = set(match)
        for i in range(len(match)):
            slen = 0
            idx = match[i]
            while idx in mset:
                mset.remove(idx)
                slen += 1
                idx += m
            mv = max(mv, slen)
                
        return mv
    
    def maxRepeating(self, sequence: str, word: str) -> int:
        return self.kmp_soln(sequence, word)
            