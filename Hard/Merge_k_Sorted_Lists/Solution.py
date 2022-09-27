# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    """
        Problem: https://leetcode.com/problems/merge-k-sorted-lists/?envType=study-plan&id=level-3
        Time Taken: Start (5:45)
        Comments:
            - Initial Thoughs: Min-Heap while keeping track list_index (tuple?)
    """
    
    
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        head = None
        tail = None

        filler = 0
        for head_node in lists:
            if head_node:
                heap.append((head_node.val, filler, head_node))
                filler+=1
                
        # print(heap)
        heapq.heapify(heap)
        
        # Edge Case of if the heap is empty:
        if not heap:
            return None
        
        # Set initial node
        v, _, cur = heapq.heappop(heap)
        head = cur
        tail = head
        if cur.next:
            heapq.heappush(heap, (cur.next.val, filler, cur.next))
            filler+=1
        
        # Continually add and remove from the heap and add to the linkedlist
        while heap:
            v, _, cur = heapq.heappop(heap)
            if cur.next:
                heapq.heappush(heap, (cur.next.val, filler, cur.next))
                filler+=1
            tail.next = cur
            tail = tail.next
            
        tail.next = None
        
        return head