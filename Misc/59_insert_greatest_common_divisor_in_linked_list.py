from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getGCD(self, val1, val2):
        while val2:
            val1, val2 = val2, val1 % val2
        return abs(val1)

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        curr_node = head
        next_node = curr_node.next

        while curr_node and next_node:
            new_node = ListNode(self.getGCD(curr_node.val, next_node.val), next_node)
            curr_node.next = new_node

            curr_node = next_node
            next_node = next_node.next
        
        return head