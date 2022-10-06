from collections import defaultdict
from sortedcontainers import SortedList

class TimeMap:

    """
        Problem: https://leetcode.com/problems/time-based-key-value-store/submissions/
        Comments: 
            - Initial Thoughts:  Dictionary of sorted (timestamps, val) tuples
    """
    
    def __init__(self):
        self.tm = defaultdict(lambda: SortedList())

    # All the timestamps timestamp of set are strictly increasing
    def set(self, key: str, value: str, timestamp: int) -> None:
        idx = self.tm[key].add((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        idx = self.tm[key].bisect_right((timestamp, "{")) - 1
        if idx >= 0:
            return self.tm[key][idx][1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)