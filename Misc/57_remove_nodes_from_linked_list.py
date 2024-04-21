from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# method 1: using stack and creating a new linked list based on values present in stack
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