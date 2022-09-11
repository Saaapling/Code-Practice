from collections import defaultdict

class Solution:

    """
        Problem: https://leetcode.com/problems/largest-component-size-by-common-factor/
        Time Taken: Unsure, multiple starts and stops
        Comments: The common_factor_grouping_method works (I think), but takes too long. Time complexity is O(n*n*sqrt(n))
            or worse for worst case [n * distinct_groups(n) * factors(sqrt(n))] on top of (potentially expensive) set operations.
        Optimal Method: Union-Find (https://www.delftstack.com/howto/python/union-find-in-python/)
            Implementaton Time: 55 minutes
            Complexity: O(n*sqrt(n))
            Comments: This solution avoids having to loop through the list of factor groups
    """

    def get_prime_factors(self, n):
        i = 2
        prime_factors = set()
        while i * i <= n:
            if n % i == 0:
                prime_factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            prime_factors.add(n)
        return prime_factors

    def common_factor_grouping_method(self, nums):
        prime_groups = []
        connected_nodes = []

        for number in nums:
            prime_factors = self.get_prime_factors(number)

            index = 0
            found = False
            target_index = 0

            # Find if this number belongs to an existing group
            while index < len(prime_groups) and not found:
                if not prime_factors.isdisjoint(prime_groups[index]):
                    prime_groups[index] = prime_groups[index].union(prime_factors)
                    connected_nodes[index] += 1
                    target_index = index
                    index += 1
                    found = True
                    break
                index += 1

            if found:
                # Consolidate the groups
                while index < len(prime_groups):
                    if not prime_factors.isdisjoint(prime_groups[index]):
                        prime_groups[target_index] = prime_groups[target_index].union(prime_groups[index])
                        connected_nodes[target_index] += connected_nodes[index]
                        del prime_groups[index]
                        del connected_nodes[index]
                    else:
                        index += 1
            else:
                # Create a new group
                prime_groups.append(prime_factors)
                connected_nodes.append(1)

            # print(prime_groups)
            # print(connected_nodes)

        return max(connected_nodes)

    # Because the default has parent_b point to parent_a, it could be nice to generally have the larger 
    # node (index) point to the smaller one or vice versa, but this is an aesthetic choice for this problem
    def union(self, node_a, node_b, tree, rank):
        parent_a = self.find(node_a, tree)
        parent_b = self.find(node_b, tree)
        if parent_a != parent_b:
            if rank[parent_a] > rank[parent_b]:
                tree[parent_b] = parent_a
            elif rank[parent_a] < rank[parent_b]:
                tree[parent_a] = parent_b
            else:
                tree[parent_b] = parent_a
                rank[parent_a] += 1

        return

    # Returns the highest parent
    def find(self, node, tree):
        while tree[node] != node:
            if tree[node] == -1:
                return node
            node = tree[node]
        return node

    def union_find_method(self, nums):
        # An array structure can represent a tree here because node in this tree only have 1 or less directed edge (1 parent)
        # Thus, the array index denotes the node, and the value denotes its parent. Nodes without parents can point to themselves
        tree = defaultdict(lambda:-1)
        rank = defaultdict(lambda:0)

        # Construct the tree
        for node in nums:
            n = node
            i = 2
            while i * i <= n:
                if n % i == 0:
                    self.union(i, node, tree, rank)
                    while n % i == 0:
                        n //= i
                i += 1
            if n > 1:
                self.union(n, node, tree, rank)

        # Traverse the tree, counting the number of elements in each disjoint set
        count = defaultdict(lambda: 0)
        max = 0
        for node in nums:
            parent = self.find(node, tree)
            count[parent] += 1
            if count[parent] > max:
                max += 1

        return max

    def largestComponentSize(self, nums: list[int]) -> int:
        return self.union_find_method(nums)

test = Solution()
input = [83,99,39,11,19,30,31]
print(test.largestComponentSize(input))
