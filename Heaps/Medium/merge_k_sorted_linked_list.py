# # Method - 1 (Merging two sorted list at a time but one by one)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge2Lists(self, l1, l2):
        dummy = ListNode()
        newHead = dummy

        while l1 and l2:
            if l1.val > l2.val:
                newHead.next = l2
                l2 = l2.next
            else:
                newHead.next = l1
                l1 = l1.next
            newHead = newHead.next

        if l1:
            newHead.next = l1
        if l2:
            newHead.next = l2

        return dummy.next

    def mergeKLists(self, arr):
        K = len(arr)
        if not arr or K == 0:
            return None
        if K == 1:
            return arr[0]

        first_list = arr[0]
        for i in range(K - 1):
            second_list = arr[i + 1]

            first_list = self.merge2Lists(first_list, second_list)
        """
        arr = [node1, node2, node3, node4]
        after first iteration -> first_list = [node12]
        after second iteration -> first_list = [node123]
        after third iteration -> first_list = [node1234]
        then we return first_list
        """
        return first_list


# # Method - 2 (Merging two sorted list at a time and storing the newHead in newlist)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge2Lists(self, l1, l2):
        dummy = ListNode()
        newHead = dummy

        while l1 and l2:
            if l1.val > l2.val:
                newHead.next = l2
                l2 = l2.next
            else:
                newHead.next = l1
                l1 = l1.next
            newHead = newHead.next

        if l1:
            newHead.next = l1
        if l2:
            newHead.next = l2

        return dummy.next

    def mergeKLists(self, lists):
        if not lists:
            return None

        while len(lists) > 1:
            newList = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                newList.append(self.merge2Lists(l1, l2))
            lists = newList
        """
        arr = [node1, node2, node3, node4, node5]
        after complete iteration over lists with length 5 -> newlist = [node12, node34, node5] = lists
        after complete iteration over lists with length 3 -> newlist = [node1234, node5] = lists
        after complete iteration over lists with length 2 -> newList = [node12345] = lists
        then we return lists[0]
        """
        return lists[0]


# # Method - 3 (Using Heaps)
import heapq
from typing import List, Optional


class Solution:
    """
    idea is to use heap to get the minimum of all the ListNode.val, once we push one node in heap we will
    also move the pointer
    """

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hq = []
        n = len(lists)
        dummy = ListNode()
        curr = dummy
        for i in range(n):
            if lists[i]:
                heapq.heappush(hq, (lists[i].val, i))
                lists[i] = lists[i].next

        while hq:
            value, i = heapq.heappop(hq)
            curr.next = ListNode(value)
            curr = curr.next
            if lists[i]:
                heapq.heappush(hq, (lists[i].val, i))
                lists[i] = lists[i].next

        return dummy.next
