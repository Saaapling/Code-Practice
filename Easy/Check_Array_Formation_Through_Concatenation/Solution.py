class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-213/problems/check-array-formation-through-concatenation/
        Time Taken: 15 min
        Comments: 
            - The inner for loop is actually inefficient
                - Array slicing is expensive O(n) where n is size
                - The actual comparison is still O(length)
                - Better to iterate from 0 to length, and manually check in a nested loop
    """
    
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        p_dict = {}
        for i in range(len(pieces)):
            p_dict[pieces[i][0]] = i
            
        i = 0
        while i < len(arr):
            start = arr[i]
            if start not in p_dict:
                return False
            num_list = pieces[p_dict[start]]
            length = len(num_list)
            if arr[i:i+length] == num_list:
                i += length
            else:
                return False        
        
        return True