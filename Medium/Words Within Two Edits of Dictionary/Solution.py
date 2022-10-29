class Solution:
    
    """
        Problem: https://leetcode.com/contest/biweekly-contest-90/problems/words-within-two-edits-of-dictionary/
        Comments:
            - Can use a trie
            - Could use brute force (10^2 * 10^2 * 10^2)
    """
    
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n = len(dictionary[0])
        
        ret = []
        for i in range(len(queries)):
            word = queries[i]
            for j in range(len(dictionary)):
                dictw = dictionary[j]
                count = 0
                for k in range(n):
                    if word[k] != dictw[k]:
                        count += 1
                        
                if count <= 2:
                    ret.append(word)
                    break
                    
        return ret
        