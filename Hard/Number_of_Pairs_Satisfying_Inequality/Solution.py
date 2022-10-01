from sortedcontainers import SortedList

class SegmentTree:
    
    def __init__(self, n):
        self.n = n
        self.tree = [0 for i in range(n * 2)]
    
    def find_sum(self, low, high): # Inclusive
        low += self.n + 1
        high += self.n + 1

        sum = 0
        while low < high:
            if low % 2 == 1: # low & 1 also works
                sum += self.tree[low]
                low += 1
            if high % 2 == 0:
                sum += self.tree[high]
                high -= 1

            low = low >> 1
            high = high >> 1

        if low == high:
            sum += self.tree[low]
        
        return sum
    
    def add(self, x):
        index = x + self.n + 1
        self.tree[index] += 1
        while index >> 1 > 0:
            index >>= 1
            self.tree[index] += 1

class Solution:
    
    """
        Problem: https://leetcode.com/contest/biweekly-contest-88/problems/number-of-pairs-satisfying-inequality/
        Comments:
            - Brute Force Solution: For each new pair (num1, num2), check all prevous elements
                - O(n^2)
                
            - Check is: nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff
                - Equivalent to: 0 <= nums1[j] + nums2[i] - (nums1[i] + nums2[j]) + diff 
                - Equivalent to: 0 <= (nums1[j] - nums2[j]) + (nums2[i] - nums1[i]) + diff
                - Equivalent to: 0 <= (nums1[j] - nums2[j]) + (nums2[i] - nums1[i] + diff)
                - Equivalent to: nums1[i] - nums2[i] - diff <= nums1[j] - nums2[j]
                - Keep track of arr[i] = nums1[i] - nums2[i] - diff
                    - Keep freq_arr = arr[i]
                    - Solution 1: Segment Tree
                        - Can leverage offset to create seg_tree, works because bounds are relatively small (10^5)
                        - Solution works, but likely not optimal
                            - Runs into space problems for bigger testcases
                            - More complex than needed
                    - Solution 2: Binary Search
                        - Keep track of arr[i] in sorted list
                        - Binary Search to find # of index smaller
    """
    
    def binary_search_soltion(self, nums1, nums2, diff):
        total = 0
        
        sl = SortedList()
        
        n = len(nums1)
        for i in range(n):
            search = nums1[i] - nums2[i]
            val = search - diff
            total += sl.bisect_right(search)
            sl.add(val)
        
        return total
    
    def seg_tree_solution(self, nums1, nums2, diff):
        seg_tree = SegmentTree(10 ** 5)
        
        n = len(nums1)
        offset = 5 * (10 ** 4)
        
        total = 0
        for i in range(n):
            index = nums1[i] - nums2[i] - diff + offset
            total += seg_tree.find_sum(0, nums1[i] - nums2[i] + offset)
            seg_tree.add(index)
            # print(index)
            # print(total)
            
        return total
    
    def numberOfPairs(self, nums1: list[int], nums2: list[int], diff: int) -> int:           
        return self.binary_search_soltion(nums1, nums2, diff)