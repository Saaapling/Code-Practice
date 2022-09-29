import heapq
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    
    """
        Problem: https://leetcode.com/problems/rotate-list/
        Comments:
            - Initial Thoughts: Modulo, Traverse, Split/Merge
    """
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # Check for empty list
        if not head:
            return None
        
        tail = head
        n = 1
        while tail.next:
            n += 1
            tail = tail.next
            
        k %= n
        # If non looping is needed, return the original list (needed for when length is 1)
        if k == 0:
            return head
        
        cur = head
        for i in range(1, n-k):
            cur = cur.next
            
            
        temp = cur.next
        # print(temp)
        cur.next = None
        tail.next = head
        # print(temp)

        return temp