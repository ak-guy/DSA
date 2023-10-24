# # Method - 1 (Brute Force)
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        res = 0
        ptr1, ptr2 = 0, len(arr)-1
        while ptr1 < ptr2:
            res = max(res, arr[ptr1] + arr[ptr2])
            ptr1 += 1
            ptr2 -= 1
        
        return res
    
# # Method - 2 (Using Fast Pointer)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = 0
        
        # get middle node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse after middle pointer
        curr, prev = slow, None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # prev will point to last node
        while prev:
            res = max(res, prev.val + head.val)
            prev = prev.next
            head = head.next
        
        return res