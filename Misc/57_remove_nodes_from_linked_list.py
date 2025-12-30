from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Method 1: using stack and creating a new linked list based on values present in stack
class Solution1:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st = []
        curr = head
        while curr:
            while st and st[-1] < curr.val:
                st.pop()
            st.append(curr.val)
            curr = curr.next

        # print(st)
        dummy = ListNode(0)
        res_node = ListNode(0, dummy)
        for i in range(len(st)):
            create_node = ListNode(st[i])
            dummy.next = create_node
            dummy = create_node

        return res_node.next.next


# Method - 2: traversing in reversed ll
class Solution2:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        # reversing
        curr = head
        prev = None
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next

        # prev will now be pointing at tail of the original ll
        newHead = prev
        temp_prev = prev
        max_val = prev.val
        prev = prev.next
        while prev:
            while prev and max_val > prev.val:
                temp_prev.next = prev.next
                prev = prev.next

            if not prev:
                break

            max_val = max(max_val, prev.val)
            temp_prev = prev
            prev = prev.next

        # again reverse
        prev = None
        while newHead:
            temp_next = newHead.next
            newHead.next = prev
            prev = newHead
            newHead = temp_next

        return prev
