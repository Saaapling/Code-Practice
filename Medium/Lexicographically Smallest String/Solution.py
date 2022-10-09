from functools import cmp_to_key

class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-314/problems/using-a-robot-to-print-the-lexicographically-smallest-string/
        Comments:
            - Smallest letter ALWAYS comes first
            - From there, recurse?
            - Base implemenation is expensive with searches O(n^2)
                 - Sort list while tracking original index
                 - Iterate down sorted list, until reach original last index
                 - O (nlog(n))
            - Potential Idea: O(n)
                - Build string greedily, when new smaller char, add everything up to min to t:
                - "aabcesadbc"
                - answer: "aaaabcdsecb"
                - "aabces" -> REVERSE
                - "aaasecb"
                - Should work, but this contest doesn't demand O(n)
    """
    
    def robotWithString(self, s: str) -> str:
        n = len(s)
        tup_arr = [(0,0) for _ in range(n)]
        
        for i in range(n):
            tup_arr[i] = (s[i], i)
            
        def compare(a, b):
            if a[0] < b[0]:
                return -1
            elif a[0] == b[0]:
                return a[1] - b[1]
            else:
                return 1
            
        tup_arr.sort(key=cmp_to_key(compare))
        # print(tup_arr)
        
        ans = [0 for _ in range(n)]
        last = -1
        i = 0
        start = 0
        end = n-1
        while last < n-1:
            char, idx = tup_arr[i]
            i += 1
            # print("Index: " + str(idx))
            if idx < last:
                continue
                
            # Pop smaller chars from end of string
            while end < n-1:
                if ans[end+1] <= char:
                    ans[start] = ans[end+1]
                    start += 1
                    end += 1
                else:
                    break
                
            # Add char to start of string, update last
            ans[start] = char
            start += 1
            
            # Add inbetween-ers to end of string
            for j in range(last + 1, idx):
                ans[end] = s[j]
                end -= 1
                
            last = idx
            # print(last)

        # print(ans)
        return "".join(ans)