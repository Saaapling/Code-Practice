import heapq
class Solution:
    
    """
        Problem: https://leetcode.com/problems/candy/
        Comments: 
            - Initial Thoughts: Greedy?
                - Runs into an issue where child 1 doesn't neccessarily start with 1 candy
                - How do you what to assign w/o knowing the right neighbor
                    - Ex: [1,2,3,4,1,4,3,2,1]
            - Start with minimum value?
            - Ex: [4,3,1,6,3,9,1,2,3]
                - Sol: [3,2,1,2,1,2,1,2,3] ?
                - Total = 17
            - Heap Solution: O(nlogn)
                - Populate starting from minimum element
                - Element candies = 1 + max(neighbor)
                - Post Submission Comments: O(nlog(n)) is a valid solution
            - Greedy (O(n)) Solution: Single pass through with backlog counter:
                - [4,3,1,6,3,9,1,2,7,5,4,3]
                    - Sol: [3,2,1,2,1,2,1,2,4,3,2,1]
                    - num = 4, curr = 1, ctr = 1
                    - num = 3, curr = 1, ctr = 2
                    - num = 1, curr = 1, ctr = 3
                    - num = 6, curr = 2, ctr = 0
                    - num = 3, curr = 1, ctr = 1
                    - num = 9, curr = 2, ctr = 0
                    - num = 1, curr = 1, ctr = 1
                    - num = 2, curr = 2, ctr = 0
                    - num = 7, curr = 3, ctr = -1
                    - num = 5, curr = 2, ctr = 0
                    - num = 4, curr = 1, ctr = 1
                    - num = 3, curr = 1, ctr = 2
                - Not entirely sure how to make this work
            - Greedy: Pass through array twice, forward and backwards
                - Take max of the two
                
    """
    
    def sorting_soln(self, ratings: list[int]) -> int:
        n = len(ratings)
        soln = [0 for _ in range(n)]
        
        heap = [(ratings[i], i) for i in range(n)]
        heapq.heapify(heap)
        while heap:
            _, idx = heapq.heappop(heap)
            left = 0
            right = 0
            if idx > 0 and ratings[idx-1] < ratings[idx]:
                left = soln[idx-1]
            if idx < n-1 and ratings[idx+1] < ratings[idx]:
                right = soln[idx+1]

            soln[idx] = 1 + max(left, right)

        return sum(soln)
    
    def greedy_double_iteration(self, ratings):
        n = len(ratings)
        forward = [0 for _ in range(n)]
        backward = [0 for _ in range(n)]
        
        forward[0] = 1
        prev = ratings[0]
        for i in range(1, n):
            if ratings[i] > prev:
                forward[i] = forward[i-1] + 1
            else:
                forward[i] = 1
            prev = ratings[i]
        
        backward[-1] = 1
        prev = ratings[-1]
        for i in range(2, n+1):
            if ratings[-i] > prev:
                backward[-i] = backward[-i+1] + 1
            else:
                backward[-i] = 1
            prev = ratings[-i]
        
        soln = [0 for _ in range(n)]
        for i in range(n):
            soln[i] = max(forward[i], backward[i])
            
        # print(soln)
        return sum(soln)
    
    def candy(self, ratings: list[int]) -> int:
        return self.greedy_double_iteration(ratings)