# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    """
        Problem: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
        Comments: 
            - Keep two points: 1 prior to current middle, and last
            - When reach end, delete current middle
    """
    
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        parent = None
        curr = head
        
        n = 0
        while curr:
            curr = curr.next
            n += 1
            if n%2 == 0:
                if parent:
                    parent = parent.next
                else:
                    parent = head
        
        if parent:
            parent.next = parent.next.next
            return head
        else:
            return None