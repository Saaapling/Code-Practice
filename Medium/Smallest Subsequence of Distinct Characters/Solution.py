class Solution:
    
    """
        Problem: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
        Initial Thoughts:
            - Treat the input as a stack, and keep track of letter positions (doesn't quite work)
            - String as a linked list, replace existing if next is smaller (i think this works, but not implementing)
                - Not implementing bc this is a monotonic stack problem
            - Monotonically decreasing stack?
                - Solution: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/discuss/308210/JavaC%2B%2BPython-Stack-Solution-O(N)
            - Post Submission comments: This was a really really hard question - could not solve it
    """
    
    # Not fully original
    def smallestSubsequence(self, s: str) -> str:
        last = {char:i for i,char in enumerate(s)}
        print(last)
        
        stack = []
        # Relies on characters being displaced by better characters with the
        # knowledge that the same character WILL appear again later
        for i, char in enumerate(s):
            if char in stack:
                continue
            while stack and char < stack[-1] and i < last[stack[-1]]:
                stack.pop()
            stack.append(char)
                
        return "".join(stack)