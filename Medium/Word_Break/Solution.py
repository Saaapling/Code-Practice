from collections import defaultdict

class wordTree:

    def __init__(self, character, valid):
        self.value = character
        # Rather than having each node have 26 garrunteed children, possibly better to use a dict
        self.children = {}
        self.valid_word = valid

    def add_word(self, word):
        curr = self
        for i in word:
            if not i in curr.children:
                curr.children[i] = wordTree(i, False)
            curr = curr.children[i]

        curr.valid_word = True
        return

    def fetch(self, pattern):
        words = []
        curr = self
        for i, letter in enumerate(pattern):
            if not letter in curr.children:
                return words
            curr = curr.children[letter]
            if curr.valid_word:
                words.append(pattern[0:i+1])

        return words

class Solution:

    """
        Problem: https://leetcode.com/problems/word-break/
        Time Taken: 45 min + 45min (Read explanation + memoization) + 10 min (dp implementation)
        Comments: 
            - Naive Solution: Left-to-right Taversal, match words if applicable
                - Runs into the problem with sequences being parts of multiple words (cat, cats, catty, cater)
                - Match word, recursively call if false, don't match the word
                    - Potentially super super expensive
                - Could arrange the word dict into a tree
                - Post submission: Too slow, even with the tree
                    - The tree implementation is somewhat wasted/uneeded
                    - Add memoization to remove repetitive checks
            - DP Solution:
                - Explanation provided in soluton: https://leetcode.com/problems/word-break/solution/
            - Trie Solution:
                - https://leetcode.com/problems/word-break/discuss/870187/Python-trie-solution
    """ 

    def word_dict_tree_traversal_aux(self, s, tree, index, cache):
        if len(s) == 0:
            return True

        if not cache[index]:
            return False

        valid_words = tree.fetch(s)
        for word in valid_words:
            if (self.word_dict_tree_traversal_aux(s[len(word):], tree, index+len(word), cache)):
                return True

        cache[index] = False
        return False

    def word_dict_tree_traversal(self, s, wordDict):
        tree = wordTree(None, False)
        for word in wordDict:
            tree.add_word(word)

        cache = [True] * len(s)
        return self.word_dict_tree_traversal_aux(s, tree, 0, cache)

    def dp_solution(self, s, wordDict):
        words = set(wordDict)
        dp_arr = [False] * (len(s) + 1)
        dp_arr[0] = True
        for i in range(1,len(s) + 1):
            for j in range(i):
                if dp_arr[j] and s[j:i] in words:
                    dp_arr[i] = True

        return dp_arr[i]

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        return self.dp_solution(s, wordDict)


test = Solution()
wordDict = ["leet", "code"]
s = "leetcode"
result = test.wordBreak(s, wordDict)
print(result)