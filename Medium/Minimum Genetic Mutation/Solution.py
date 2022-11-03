import copy

class Solution:
    
    """
        Problem: https://leetcode.com/problems/minimum-genetic-mutation/
        Comments: https://leetcode.com/problems/minimum-genetic-mutation/
            - Low contraints (n=10), (m=8)
            - Recursive solution: n! * m
                - Kind of bad, but at the same time should work with these constraints
                - Cannot just do greedy selection
                    - 'AA' -> 'CC', bank = ['CC', 'BC', 'BB', 'AB'], answer = 4 [AB -> BB -> BC -> CC]
                    - 'AA' -> 'CC', bank = ['CC', 'CB', 'BB', 'AB'], answer = 3 [AB -> CB -> CC]
                - Not truely n! (can eliminate all elements at current step from bank)
                    - If two elements are both 1 step away, cannot go from 1 ele to the other ele in one step
                    - No need to do two steps, because then it would be not optimal
                - Optimization, hash the string to reduce string comparison to O(1)?
                    - Bit representation?
    """
    
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def comp(a, b):
            diff = 0
            for i in range(8):
                if a[i] != b[i]:
                    diff += 1
                    
            if diff == 1:
                return True
            return False
        
        def aux(start, curr, bank):
            if curr == start:
                return 0
            
            found = []
            nbank = copy.deepcopy(bank)
            for i in bank:
                if comp(curr, i):
                    found.append(i)
                    nbank.remove(i)
            
            mv = 10*10
            for i in found:
                mv = min(mv, 1 + aux(start, i, nbank))
                
            return mv
            
        if not end in bank:
            return -1
        if not start in bank:
            bank.append(start)
            
        ans = aux(start, end, bank)
        if ans > 10:
            return -1
        return ans