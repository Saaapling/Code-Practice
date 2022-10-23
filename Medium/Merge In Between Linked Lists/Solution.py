# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    """
        Problem: https://leetcode.com/contest/biweekly-contest-40/problems/merge-in-between-linked-lists/
    """
    
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev = list1
        idx = 0
        while idx < a - 1:
            prev = prev.next
            idx += 1
            
        nextnode = prev
        while idx < b + 1:
            nextnode = nextnode.next
            idx += 1
            
        prev.next = list2
        curr = list2
        while curr.next:
            curr = curr.next
        curr.next = nextnode
        
        return list1