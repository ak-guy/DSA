from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        actual_head = head
        total_nodes = 0
        dummy_head = head

        while dummy_head:
            total_nodes += 1
            dummy_head = dummy_head.next
        
        greater_length_parts = total_nodes % k
        res = []
        while head:
            for _ in range(k):
                to_run = total_nodes // k if greater_length_parts <= 0 \
                         else total_nodes // k + 1
                
                new_dummy_head = ListNode(0)
                temp_head = new_dummy_head
                for j in range(to_run):
                    new_dummy_head.next = ListNode(head.val, None)
                    new_dummy_head = new_dummy_head.next
                    head = head.next

                res.append(temp_head.next)
                greater_length_parts -= 1

        return res if actual_head else [None for _ in range(k)]