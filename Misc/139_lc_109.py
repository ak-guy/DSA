'''
109. Convert Sorted List to Binary Search Tree
'''

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Method 1 : Converting Linked List to array then converting that sorted arr to BST 
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        totalNode = len(arr)
        
        def constructBST(s, e, arr):
            root = None
            if s <= e:
                mid = (s+e) // 2
                root = TreeNode(arr[mid])
                root.left = constructBST(s, mid-1, arr)
                root.right = constructBST(mid+1, e, arr)
            return root

        return constructBST(0, len(arr)-1, arr)
    

# Method - 2 : Directly converting Linked List to BST
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def constructBST(head, tail):
            root = None
            if head != tail:
                slow, fast = head, head
                while fast!=tail and fast.next!=tail:
                    slow = slow.next
                    fast = fast.next.next

                root = TreeNode(slow.val)
                root.left = constructBST(head, slow)
                root.right = constructBST(slow.next, tail)
            return root

        return constructBST(head, None)