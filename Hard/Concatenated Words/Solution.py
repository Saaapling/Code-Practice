class Solution:
    
    """
        Problem: https://leetcode.com/problems/concatenated-words/
        Comments:
            - Idea: Sort input words by length (smaller words cannot be made up of larger words)
            - Given: Use some form of Trie
    """
    
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = list(map(lambda x:(len(x), x), words))
        words.sort()
        words = list(map(lambda x:x[1], words))
        print(words)
        
        trie = {"end":False}
        
        def is_concat(x):
            if len(x) == 0:
                return True
            
            curr = trie
            for i in range(len(x)):
                ch = x[i]
                if not ch in curr:
                    return False
                curr = curr[ch]
                if curr["end"]:
                    if is_concat(x[i+1:]):
                        return True
                    
            return False
        
        def add_word(x):
            curr = trie
            for ch in x:
                if not ch in curr:
                    curr[ch] = {"end": False}
                curr = curr[ch]
            curr["end"] = True
        
        ans = []
        for word in words:
            if is_concat(word):
                ans.append(word)
            else:
                add_word(word)
            
        # print(trie)
        return ans