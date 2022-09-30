import math
from collections import defaultdict

class Solution:
    
    """
        Problem: https://leetcode.com/problems/group-anagrams/
        Comments:
            - Initial Thoughts: Prime-Multiplication Hashing?
    """
    
    def check(self, n):
        for i in range(3, math.floor(n ** 0.5)+1, 2):
            if n % i == 0:
                return False
        
        return True
    
    def get_primes(self):
        count = 0
        l2p = {'a': 2}
        letters = list("abcdefghijklmnopqrstuvwxyz")
        
        curr = 3
        while count < 25:
            if self.check(curr):
                count += 1
                l2p[letters[count]] = curr
            curr += 2
    
        return l2p
    

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        l2p = self.get_primes()
        M = 10**9 + 7

        str_hash = defaultdict(lambda:[])
        def calculate(word):
            nonlocal l2p
            hash = 1
            for letter in list(word):
                hash *= l2p[letter]
            return hash

        for word in strs:
            str_hash[calculate(word)].append(word)

        return list(str_hash.values())

test = Solution()
strs = ["a"]
result = test.groupAnagrams(strs)
print(result)