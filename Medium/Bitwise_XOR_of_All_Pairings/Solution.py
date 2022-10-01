class Solution:
    
    """
        Problem: https://leetcode.com/contest/biweekly-contest-88/problems/bitwise-xor-of-all-pairings/
        nums1 = [2,1,3], nums2 = [10,2,5,0]
        [2,2,0,0] len(3)
        [1,2,1,1], len(4)
        [(2 * (4-1)) + 1, (2 * (4-2)) + 2, 3, 3]
        [7,6,3,3]
        
        [(1 * )]
        
        [7,6,3,3]
        Comments:
            - There is a simplier math based solution (found by Erik)
            - Final XOR of bc_3, group numbers (x_i) together, pairs cancel out
                - # of x_i is based on the length/parity of other list
                - XOR all elements with parity 1
    """
    
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        max_val = max(max(nums1), max(nums2))
        max_len = len(bin(max_val)) - 2
        bc_1 = [0 for i in range(max_len)]
        bc_2 = [0 for i in range(max_len)]
        # This array is not needed, but included for debugging + visual clarity
        bc_3 = [0 for i in range(max_len)]

        for x in nums1:
            bc = list(bin(x)[2:])
            n = len(bc)
            for i in range(n):
                bc_1[n-i-1] += int(bc[i])
                
        for x in nums2:
            bc = list(bin(x)[2:])
            n = len(bc)
            for i in range(n):
                bc_2[n-i-1] += int(bc[i])
                
        n1l = len(nums1)
        n2l = len(nums2)
        val = 0
        for i in range(max_len):
            bc_3[i] = bc_1[i] * (n2l - bc_2[i]) + bc_2[i] * (n1l - bc_1[i])
            if bc_3[i] % 2 == 1:
                val += 2**i
        
        # print(bc_1)
        # print(bc_2)
        # print(bc_3)
        
        return val