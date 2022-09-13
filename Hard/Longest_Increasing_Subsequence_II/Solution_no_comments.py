# See other file for comments
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

    def forward_with_segtree(self, nums, k):
        solution_tree = Seg_Tree(max(nums) + 1)

        for x in nums:
            max_subseq = 1 + solution_tree.find_max(max(0, x - k), x - 1)
            solution_tree.update(x, max_subseq)

        return solution_tree.find_max(0, max(nums))

    def lengthOfLIS(self, nums: list[int], k: int) -> int:
        return self.forward_with_segtree(nums, k)


test = Solution()
input = [7,4,5,1,8,12,4,7]
# input = list(range(1, 100000))
k = 5
result = test.lengthOfLIS(input, k)
print(result)