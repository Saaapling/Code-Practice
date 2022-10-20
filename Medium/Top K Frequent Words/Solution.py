from sortedcontainers import SortedList
from collections import defaultdict
import functools

class Solution:
    
    """
        Problem: https://leetcode.com/problems/top-k-frequent-words/
        Comments:
            - Initial Thoughts: Easy nlog(n) solution by sorting the, then maintaining a heap
            - Improved Solution: nlog(k) by keeping a sorted list of the best 'k' words
    """
    
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wfreq = defaultdict(lambda: 0)
        k_largest = defaultdict(lambda: False)
        
        def compare(x, y):
            if x[0] == y[0]:
                if x[1] > y[1]:
                    return -1
                elif x[1] < y[1]:
                    return 1
                else:
                    return 0
            else:
                return x[0] - y[0]
        soln = SortedList(key=functools.cmp_to_key(compare))

        for x in words:
            if k_largest[x]:
                soln.remove((wfreq[x], x))
            
            wfreq[x] += 1
            if len(soln) < k:
                soln.add((wfreq[x], x))
                k_largest[x] = True
            else:
                if compare((wfreq[x], x), soln[0]) > 0:
                    f,w = soln.pop(0)
                    k_largest[w] = False
                    soln.add((wfreq[x], x))
                    k_largest[x] = True
                    
            # print(soln)
                    
        result = []
        idx = k-1
        while idx >= 0:
            freq = soln[idx][0]
            start = soln.bisect_left((freq, "{"))
            while idx >= start:
                result.append(soln[idx][1])
                idx -= 1
            
        return result