class Solution:
    
    """
        Problem: https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/
        Comments: 
            - Seperate states by operators (& and |)
            - Keep track of cumulative state up to new operator
                - Recurse down parenthesis?
                - Split by operator
            - Keep track of current minimum to flip operation
            - Ex: (1&0)&0&(1&0)
                - change 2nd '&' to '|', change last '0' to '1'
            - Ex: (1&0)&0
            - Post Initial Submission:
                - Method works, but is too slow (TLE)
                - Need a better way than iterating down the entire thing to find the closing parenthesis
                    - Can find all matching parenthesis in 1 iteration, and then cache the results
                - Method no longer TLE's with the improved caching solution
            - Better solution: https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/discuss/1267304/Python-Recursion-dfs-solution-explained
                - Much cleaner dp than what I have in my own solution
                - Similar concept of using recusion to go downward
                    - Visualizes the expression as a tree, with the operands as parent nodes, and the 'booleans' as leaves
                    - Instead of direct iterative, just calculates left and right
                        - Which is still the same as iterative depending on how you choose 'left' and 'right'
    """
       
    def aux(self, expression, start, end):
        min_swap = 10**9
        n = len(expression)
        
        i = start
        operand = 0 #0: '|', 1: '&'
        curr = 0
        first = True
        while i < end:
            if expression[i] == '(':
                swap_count, new = self.aux(expression, i+1, self.d[i])
                i = self.d[i]
            else:
                new = int(expression[i])
                swap_count = 1
                
            # print("Curr: " + str(curr))
            # print("Operand: " + str(operand))
            # print("New: " + str(new))
            if first:
                first = False
                curr = new
                min_swap = swap_count
            else:
                if operand == 0:
                    if curr == 1:
                        # Change '|' to '&'
                        swaps = 1
                        if new == 1:
                            swaps += swap_count 
                        min_swap = min(min_swap + 1, swaps)    
                    else:
                        if new == 1:
                            swaps = 1
                            curr = 1
                        else:
                            swaps = swap_count
                        min_swap = min(min_swap, swaps)    
                else:
                    if curr == 1:
                        if new == 1:
                            swaps = swap_count
                        else:
                            swaps = 1
                            curr = 0
                        min_swap = min(min_swap, swaps)
                    else:
                        # Change '&' to '|'
                        swaps = 1
                        if new == 0:
                            swaps += swap_count
                        min_swap = min(min_swap + 1, swaps) 
            
            #     print("Swaps: " + str(swaps))
            # print("Minimum: " + str(min_swap))
            i += 1
            if i >= end:
                break
            
            if expression[i] == '|':
                operand = 0
            else:
                operand = 1
            i += 1
        
        return min_swap, curr
    
    def minOperationsToFlip(self, expression: str) -> int:
        # Not my own code
        def corr(s):
            stack, d = [], {}
            for i, elem in enumerate(s):
                if elem == "(":
                    stack.append(i)
                elif elem == ")":
                    last = stack.pop()
                    d[last] = i
            return d
    
        self.d = corr(expression)
        min_swap, _ = self.aux(expression, 0, len(expression))
        return min_swap