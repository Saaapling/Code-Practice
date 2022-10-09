class Solution:
    
    """
        Problem: https://leetcode.com/contest/weekly-contest-314/problems/find-the-original-array-of-prefix-xor/
    """

    def findArray(self, pref: list[int]) -> list[int]:
        n = len(pref)
        rs = [0 for _ in range(n)]
        rs[0] = pref[0]
        
        for i in range(1, n):
            rs[i] = pref[i-1] ^ pref[i]

        return rs