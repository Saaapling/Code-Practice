class Seg_Tree:

    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n*2)

    def find_max(self, low, high): # Inclusive
        low += self.n
        high += self.n

        max_val = 0
        while low < high:
            if low % 2 == 1: # low & 1 also works
                max_val = max(max_val, self.tree[low])
                low += 1
            if high % 2 == 0:
                max_val = max(max_val, self.tree[high])
                high -= 1

            low = low >> 1
            high = high >> 1

        if low == high:
            max_val = max(max_val, self.tree[low])

        return max_val

    def update(self, index, value):
        index += self.n
        self.tree[index] = value
        while index >> 1 > 0:
            index = index >> 1
            self.tree[index] = max(self.tree[index << 1], self.tree[(index << 1) + 1])

class Solution:

    """
        Problem: https://leetcode.com/problems/longest-increasing-subsequence-ii/
        Time Taken: 30 min (first soltion) + 45 min (brainstorming) + infinity
        Comments: This is probably a dynamic programming problem
            - Idea: (Starting from the end) subsequence of x equals [DOESN'T WORK]
                - subsequence of x[1:] if x[0] < first number in that subsequence
                - x[0] + subsequence of x[1:] otherwise
                - Multiple subsequences may have the same length, return all of them?
                    - Return the one with the largest start 
                    - With smaller starts, is functionally equivalent

            - Idea: (Starting from end), keep track of largest subsequence that includes
                    current index. Find largest subsequence at end
                - Loop through already completed subsequences, and add current index into
                    existing sequence, or create new sequence if current index is too large
                - Because sequence is gated by current index (new smallest), all possible
                    subsequences of same length are functionally equivalent
                - Time complexity: should be O(n^2)
                - Result 1: Solution timed out
                    - Only keep the 'best' substring of length n for each n
                    - Possible keep only the 'best' substring with starting index
                    - Result 2: Due to a variety of edge cases, this solution is not much better
                        - More importantly, it doesn't 'truly' lower the time complexity, which is the
                            crux of the issue

        Solution: Dynamic Programming with a Segment Tree
            Comments: This solution is the same as the 'failed' forward implementation, except it
                improves upon the search through the dp_results array through the use of a segment-tree
            Time-Complexity: O(nlog(n)
            Documentation: https://leetcode.com/problems/longest-increasing-subsequence-ii/discuss/2560085/Python-Explanation-with-pictures-Segment-Tree
                           https://codeforces.com/blog/entry/18051
            Implementation Time: 
    """

    def find_optimal_subsequence(self, x, k, subsequences):
        max = 1
        curr_sequence = [x]
        for sequence in subsequences:
            if x < sequence[0] and x >= sequence[0] - k and len(sequence) + 1 > max:
                max = len(sequence) + 1
                curr_sequence = [x] + sequence

        i = 0
        while i < len(subsequences):
            if subsequences[i][0] == x or subsequences[i][0] == x + 1:
                subsequences.pop(i)
            else:
                i += 1

        subsequences.append(curr_sequence)

        print(subsequences)

    def backtracking_method(self, nums, k):
        subsequences = []

        for i in range(len(nums) - 1, -1, -1):
            self.find_optimal_subsequence(nums[i], k, subsequences)

        return max(len(x) for x in subsequences)

    def forwardtracking_method(self, nums, k):
        solution_arr = {nums[0]: 1}

        for x in nums:
            max_len = 1
            if x in solution_arr:
                max_len = solution_arr[x]
            for i in range(x - k, x):
                if i in solution_arr and solution_arr[i] >= max_len:
                    max_len = solution_arr[i] + 1
            
            solution_arr[x] = max_len
            # print(solution_arr)

        return max(x for x in solution_arr.values())

    def forward_with_segtree(self, nums, k):
        solution_tree = Seg_Tree(max(nums) + 1)

        for x in nums:
            max_subseq = 1 + solution_tree.find_max(max(0, x - k), x - 1)
            solution_tree.update(x, max_subseq)

        return solution_tree.find_max(0, max(nums))

    def lengthOfLIS(self, nums: list[int], k: int) -> int:
        return self.forward_with_segtree(nums, k)


test = Solution()
input = [4,2,1,4,3,4,5,8,15]
input = list(range(1, 100000))
k = 3
result = test.forwardtracking_method(input, k)
print(result)