from collections import OrderedDict

class LRUCache:
    
    """
        Problem: https://leetcode.com/problems/lru-cache/
        Comments: https://leetcode.com/problems/lru-cache/
            - Initial Thoughts:
                - Keeping the cache as an array is expensive O(n) puts
                - Doubly linked list alongside hashmap of key
                    - Python has this built in: OrderedDict
                    - https://docs.python.org/3/library/collections.html#collections.OrderedDict
    """

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.n = capacity

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if not key in self.cache and len(self.cache) == self.n:
            self.cache.popitem(last=False)

        self.cache[key] = value
        self.cache.move_to_end(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)