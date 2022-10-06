from collections import defaultdict, OrderedDict

class LFUCache:
    
    """
        Problem: https://leetcode.com/problems/lfu-cache/
        Comments:
            - Initial Thoughts:
                - Have to keep track of both LRU (least recently used), and a use-counter
                    - use-counter never decrements
                - Potentially have two data-structures, one for use-counter, one for LRU
                - LinkedList Solution + Counter Dict
                    - Keep track of:
                        - Previous
                        - Next
                        - counter
                    - Dictionary points to first value in cache of 'counter' uses
                    - For both get and put, remove the key (if exists for put), then re-insert after
                    - Not sure how to translate this solution into the OrderedDict data structure
                        - https://docs.python.org/3/library/collections.html#collections.OrderedDict
                - Potential OrderedDict Solution:
                    - Regular Dict of (key, val)
                    - DefaultDict of OrderedDicts for counter
                    - Same of idea of removing the key for both get's and put's
                    - Keep track of least frequently used
                        - Important: When an element is removed, a new element is added
                        - Adding a new element not in cache:
                            - LFU = 1
                        - Get/update existing item
                            - perform remove and add
                            - if no more elements in LFU-list for counter, LFU += 1
                
    """

    def __init__(self, capacity: int):
        self.n = capacity
        self.cache = {}
        self.u_cache = {}
        self.lfu_dict = defaultdict(lambda: OrderedDict())
        self.lfuc = 0
        

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        
        self.put(key, self.cache[key])
        return self.cache[key]
                

    def put(self, key: int, value: int) -> None:
        # Edge case
        if self.n == 0:
            return
        
        if key in self.cache:
            self.cache[key] = value
            uc = self.u_cache[key]
            self.u_cache[key] += 1
            self.lfu_dict[uc].move_to_end(key)
            self.lfu_dict[uc].popitem()
            self.lfu_dict[uc+1][key] = value
            if uc == self.lfuc and len(self.lfu_dict[self.lfuc]) == 0:
                self.lfuc += 1
        else:            
            if len(self.cache) == self.n:
                old_key, _ = self.lfu_dict[self.lfuc].popitem(last=False)
                del self.cache[old_key]
                del self.u_cache[old_key]

            self.cache[key] = value
            self.u_cache[key] = 1
            self.lfu_dict[1][key] = value
            self.lfuc = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)