from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        dummy = ListNode(-1, head)
        curr1 = dummy
        curr2 = dummy
        traversed_length = 0
        while curr1 and curr1.next:
            # print(f"curr1_val = {curr1.val}, curr2_val = {curr2.val}, traversed_length = {traversed_length}") # debug
            while curr2 and curr2.next and traversed_length < k:
                curr2 = curr2.next
                traversed_length += 1
            # print(f"curr1_val = {curr1.val}, curr2_val = {curr2.val}, traversed_length = {traversed_length}") # debug
            if traversed_length != k:
                break

            temp_curr = curr1
            save_next = curr1.next
            curr1 = curr1.next
            prev = None

            for i in range(k-1):
                temp = curr1.next
                curr1.next = prev
                prev = curr1
                curr1 = temp
            
            temp_curr.next.next = curr1.next
            curr1.next = prev
            temp_curr.next = curr1
            curr1 = curr2 = save_next

            traversed_length = 0
            # print(f"curr1_val = {curr1.val}, curr2_val = {curr2.val}, traversed_length = {traversed_length}") # debug
            # print(self.print_ll(dummy.next)) # debug
        return dummy.next