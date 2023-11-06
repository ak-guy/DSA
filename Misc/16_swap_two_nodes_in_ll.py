# # Method - 1 (Brute Force)
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        len_ll = 1
        while curr:
            curr = curr.next
            len_ll += 1
        
        curr = head
        traversed_len = 0
        while curr:
            traversed_len += 1
            if traversed_len == k:
                node1 = curr
            if traversed_len == len_ll - k:
                node2 = curr
            curr = curr.next
        
        node1.val, node2.val = node2.val, node1.val
        return head
    

# # Method - 2 (Optimized Approach)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr1, curr2 = head, head

        # making sure curr1 points to first node
        for i in range(1, k):
            curr1 = curr1.next

        # making sure curr2 points to second node
        last = curr1
        while last.next:
            last = last.next
            curr2 = curr2.next
        
        curr1.val, curr2.val = curr2.val, curr1.val
        return head