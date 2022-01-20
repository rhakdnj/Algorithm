from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, li1: Optional[ListNode], li2: Optional[ListNode]) -> Optional[ListNode]:
        if (not li1) or (li2 and li1.val > li2.val):
            li1, li2 = li2, li1
        if li1:
            li1.next = self.mergeTwoLists(li1.next, li2)
        return li1


if __name__ == "__main__":
    solution = Solution()
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    print(solution.mergeTwoLists(l1, l2))