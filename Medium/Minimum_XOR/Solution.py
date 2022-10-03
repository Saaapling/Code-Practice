class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-313/problems/minimize-xor/
        Comments:
            - Zero out num1's bit by largest to smallest first
            - Add remaining bits in smallest positions possible
    """
    
    def minimizeXor(self, num1: int, num2: int) -> int:
        a = list(bin(num1)[2:])
        b = list(bin(num2)[2:])
        
        result_arr = [False for i in range(max(len(a), len(b)))]
        a_bits = a.count('1')
        b_bits = b.count('1')
        for i in range(len(a)):
            if b_bits == 0:
                break
            if a[i] == '1':
                b_bits -= 1
                result_arr[len(a) - i - 1] = True
            
        index = 0
        while b_bits > 0:
            if not result_arr[index]:
                result_arr[index] = True
                b_bits -= 1
            index += 1
                
        x = 0
        for i in range(len(result_arr)):
            if result_arr[i]:
                x += 2 ** i
                
        return x