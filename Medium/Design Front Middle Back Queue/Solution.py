# Definition for doubly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class FrontMiddleBackQueue:

    """
        Problem: https://leetcode.com/contest/biweekly-contest-40/problems/design-front-middle-back-queue/
        Comments: Solution is not clean at all
            - In future, could consider moving the list manipulations into the ListNode itself (better encapsulation)
    """
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.mid = None
        self.n = 0
        return

    def pushFront(self, val: int) -> None:
        nn = ListNode(val, self.head)
        self.n += 1
        
        if self.n == 1:
            self.head = nn
            self.tail = nn
            self.mid = nn
            return
        
        self.head.prev = nn
        self.head = nn
            
        if self.n % 2 == 0:
            if self.mid.prev:
                self.mid = self.mid.prev
            else:
                self.mid = nn
        
    def pushMiddle(self, val: int) -> None:
        self.n += 1
        
        if self.mid == None:
            nn = ListNode(val)
            self.head = nn
            self.tail = nn
            self.mid = nn
            return
            
        if self.n % 2 == 1:
            nn = ListNode(val, self.mid.next, self.mid)
            if self.mid.next:
                self.mid.next.prev = nn
            self.mid.next = nn
        else:
            nn = ListNode(val, self.mid, self.mid.prev)
            if self.mid.prev:
                self.mid.prev.next = nn
            self.mid.prev = nn
            if self.n == 2:
                self.head = nn
        self.mid = nn

    def pushBack(self, val: int) -> None:
        nn = ListNode(val, None, self.tail)
        self.n += 1
        
        if self.n == 1:
            self.head = nn
            self.tail = nn
            self.mid = nn
            return
        
        self.tail.next = nn
        self.tail = nn
        
        if self.n % 2 == 1:
            self.mid = self.mid.next

    def popFront(self) -> int:
        if self.n == 0:
            return -1
        
        ans = self.head.val
        self.head = self.head.next
        self.n -= 1
       
        if self.n == 0:
            self.tail = None
            self.mid = None
            return ans

        if self.n % 2 == 1:
            self.mid = self.mid.next
        return ans

    def popMiddle(self) -> int:
        if self.n == 0:
            return -1
        
        ans = self.mid.val
        self.n -= 1
        
        if self.n == 0:
            self.head = None
            self.tail = None
            self.mid = None
        elif self.n == 1:
            self.head = self.head.next
            self.mid  = self.mid.next
        else:
            self.mid.prev.next = self.mid.next
            self.mid.next.prev = self.mid.prev
            if self.n % 2 == 1:
                self.mid = self.mid.next
            else:
                self.mid = self.mid.prev
                
        return ans

    def popBack(self) -> int:
        if self.n == 0:
            return -1
        
        ans = self.tail.val
        self.tail = self.tail.prev
        self.n -= 1
        
        if self.n == 0:
            self.head = None
            self.mid = None
            return ans
        
        if self.n % 2 == 0:
            self.mid = self.mid.prev
        return ans


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()