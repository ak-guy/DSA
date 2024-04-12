from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        current_traversing_node = dummy
        
        for i in range(left-1):
            current_traversing_node = current_traversing_node.next
        
        node_just_before_left = current_traversing_node
        node_at_left_position = node_just_before_left.next
        current_traversing_node = current_traversing_node.next
        prev = None

        for i in range(right - left + 1):
            next_node = current_traversing_node.next
            current_traversing_node.next = prev
            prev = current_traversing_node
            current_traversing_node = next_node

        node_just_before_left.next = prev
        node_at_left_position.next = current_traversing_node
        return dummy.next