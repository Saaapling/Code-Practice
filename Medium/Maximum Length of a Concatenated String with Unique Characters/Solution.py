class Solution:
    
    """
        Problem: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
        Comments:
            - Initial Ideas: Brute force
                - The constraints are tiny (n=16) that brute force will work
                - 2^16 total possible combinations
                    - Probably n*2 work using dp?
    """
    
    def dp_solution(self, arr):
        dp = []
        seen = set()
        
        for i in arr:
            if not len(set(i)) == len(i):
                continue
            for j in dp:
                if len(j.intersection(set(i))) == 0:
                    union = j.union(set(i))
                    if not str(union) in seen:
                        dp.append(union)
                        seen.add(str(union))
            if not str(set(i)) in seen:
                dp.append(set(i))
                seen.add(str(set(i)))
            # print(dp)

        mv = 0
        for j in dp:

            mv = max(mv, len(j))
        return mv
    
    def maxLength(self, arr: List[str]) -> int:
        return self.dp_solution(arr)