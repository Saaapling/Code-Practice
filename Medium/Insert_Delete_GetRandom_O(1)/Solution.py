class RandomizedSet:

    """
        Problem: https://leetcode.com/problems/insert-delete-getrandom-o1/
    """
    
    def __init__(self):
        self.values = set()
        
        self.map = {}
        self.arr = []
        self.n = 0
        

    def insert(self, val: int) -> bool:
        if val in self.values:
            return False
        
        self.values.add(val)
        
        self.map[val] = self.n
        self.arr.append(val)
        self.n += 1
        return True

    def remove(self, val: int) -> bool:
        if not val in self.values:
            return False
        
        self.values.remove(val)
        
        index = self.map[val]
        if index == len(self.arr) - 1:
            self.arr.pop() 
        else:
            i_val = self.arr.pop() 
            self.arr[index] = i_val
            self.map[i_val] = index
        
        del self.map[val]
        self.n -= 1
        
        return True

    def getRandom(self) -> int:
        index = random.randint(0, self.n - 1)
        return self.arr[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()