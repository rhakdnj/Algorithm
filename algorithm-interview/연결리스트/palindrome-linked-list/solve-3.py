from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow, fast = head
        # to make rev-linked-list using runner
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        # check is it palindrome?
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        # if it is palindrome, rev is None and slow is None, so return not rev is True
        return not rev