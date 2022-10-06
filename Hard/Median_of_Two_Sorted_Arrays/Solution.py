class Solution:
    
    """
        Problem: https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/
        Comments:
            - Initial Thoughts: Binary Search?
                - Take median of both lists, BST the smaller of the two against the other
                - After first BS, you have minimum min(m/2,n/2) smaller items, maximum min(m,n) smaller items
                    - will NOT have passed median
                - For future BS, take median of remaining list
            - Given lists of size m, n,
                - median is (m+n)/2
                
                
            - [1,2,3,4,5]
            - [6,7,8,9,10,11,12,13,14,15]
            - median is 8
            - before first bs:
                - [1,2,3,4,5]
                - [6,7,8,9,10,11,12,13]
            - after first bs:
                - confirmed: [1,2,3]
                - remaining: [4,5]
                -            [6,7,8,9,10]
            - after second bs:
                - confirmed: [1,2,3,4]
                - remaining: [5]
                -            [6,7,8,9]

        Post-Submission Comments: The solution works, buts its somewhat needlessly complicated
            - Even cleaned solution isn't much better :/
    """
    
    def findMedianSortedArrays_cleaned(self, nums1: list[int], nums2: list[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        remaining = (m + n) // 2
        
        def bs(lst, val, left, right):
            idx = (left + right) // 2
            while lst[idx] != val and left <= right:
                if lst[idx] > val:
                    right = idx - 1
                else:
                    left = idx + 1
                idx = (left + right) // 2

            if lst[idx] == val and left <= right:
                idx -= 1

            return idx
        
        idx_1 = 0
        idx_2 = 0
        idx_1r = min(m-1, remaining - 1)
        idx_2r = min(n-1, remaining - 1)
        while remaining > 0 and idx_1 < m and idx_2 < n:      
            x = idx_1 + (idx_1r - idx_1) // 2
            y = idx_2 + (idx_2r - idx_2) // 2
            if nums1[x] < nums2[y]:
                idx = bs(nums2, nums1[x], idx_2, idx_2r)
                remaining -= (x - idx_1) + 1
                remaining -= (idx - idx_2) + 1
                idx_1 = x + 1
                idx_2 = idx + 1
            else:
                idx = bs(nums1,  nums2[y], idx_1, idx_1r)
                remaining -= (y - idx_2) + 1
                remaining -= (idx - idx_1) + 1
                idx_1 = idx + 1
                idx_2 = y + 1
            idx_1r = min(idx_1r, idx_1 + remaining - 1)
            idx_2r = min(idx_2r, idx_2 + remaining - 1)

        def get(lst, idx):
            if idx < len(lst):
                return lst[idx]
            return 10 ** 7
        
        if remaining == 0:
            a = get(nums1, idx_1)
            b = get(nums2, idx_2)
            if (m + n) % 2 == 1:
                return min(a, b)
            else:
                c = min(nums1[x], nums2[y])
                return (c + min(a,b)) / 2
        else:
            if idx_1 == m:
                if (m + n) % 2 == 1:
                    return nums2[idx_2r+1]
                else:
                    return (nums2[idx_2r] + nums2[idx_2r + 1]) / 2
            else:
                if (m + n) % 2 == 1:
                    return nums1[idx_1r+1]
                else:
                    return (nums1[idx_1r] + nums1[idx_1r + 1]) / 2

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        m_idx = (m + n) // 2
        
        def bs(lst, val, left, right):
            idx = (left + right) // 2
            
            while lst[idx] != val and left <= right:
                if lst[idx] > val:
                    right = idx - 1
                else:
                    left = idx + 1
                    
                idx = (left + right) // 2

            if lst[idx] == val and left <= right:
                idx -= 1

            return idx
        
        c_idx = 0
        idx_1 = 0
        idx_2 = 0
        idx_1r = min(m-1, m_idx)
        idx_2r = min(n-1, m_idx)
        while c_idx < m_idx and idx_1 < m and idx_2 < n:      
            x = idx_1 + max(0, (idx_1r - idx_1) // 2 - 1)
            y = idx_2 + max(0, (idx_2r - idx_2) // 2 - 1)
            c = min(nums1[x], nums2[y])
            if nums1[x] < nums2[y]:
                idx = bs(nums2, nums1[x], idx_2, idx_2r)
                c_idx += (x - idx_1) + 1
                c_idx += (idx - idx_2) + 1
                idx_1 = x + 1
                idx_2 = idx + 1
            else:
                idx = bs(nums1,  nums2[y], idx_1, idx_1r)
                c_idx += (y - idx_2) + 1
                c_idx += (idx - idx_1) + 1
                idx_1 = idx + 1
                idx_2 = y + 1
            idx_1r = min(idx_1r, idx_1 + m_idx - c_idx)
            idx_2r = min(idx_2r, idx_2 + m_idx - c_idx)

        def get(lst, idx):
            if idx < len(lst):
                return lst[idx]
            return 10 ** 7
        
        if c_idx == m_idx:
            a = get(nums1, idx_1)
            b = get(nums2, idx_2)
            if (m + n) % 2 == 1:
                return min(a, b)
            else:
                return (c + min(a,b)) / 2
        else:
            if idx_1 == m:
                if (m + n) % 2 == 1:
                    return nums2[idx_2r]
                else:
                    return (nums2[idx_2r] + nums2[idx_2r - 1]) / 2
            else:
                if (m + n) % 2 == 1:
                    return nums1[idx_1r]
                else:
                    return (nums1[idx_1r] + nums1[idx_1r - 1]) / 2

test = Solution()
list_a = []
list_b = [1,2,3,4,5]
result = test.findMedianSortedArrays_cleaned(list_a, list_b)
print(result)